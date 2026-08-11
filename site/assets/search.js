(function () {
  "use strict";

  const MAX_RESULTS = 20;
  const FIELD_WEIGHTS = Object.freeze({
    title: 5,
    aliases: 4,
    keywords: 3,
    summary: 1,
    search_text: 1,
  });
  const TOKEN_RE = /[\u3400-\u4dbf\u4e00-\u9fff]|[0-9a-zA-ZÀ-ž._+-]+/gu;
  const LATIN_TERM_RE = /[a-z][a-z0-9._+-]{3,}/g;

  const input = document.getElementById("problem-search");
  const resultsElement = document.getElementById("search-results");
  const statusElement = document.getElementById("search-status");

  let index = null;
  let items = [];
  let itemsById = new Map();
  let latinDictionary = [];
  let searchLexicon = [];
  let activeIndex = -1;
  let composing = false;
  let lastResults = [];

  function normalize(value) {
    return String(value || "")
      .normalize("NFKC")
      .toLocaleLowerCase("en-US")
      .replace(/[^0-9a-z\u3400-\u4dbf\u4e00-\u9fff.+_-]+/g, " ")
      .trim()
      .replace(/\s+/g, " ");
  }

  function encode(value) {
    return normalize(value).match(TOKEN_RE) || [];
  }

  function asSearchText(value) {
    return Array.isArray(value) ? value.join(" ") : String(value || "");
  }

  function createIndex(records) {
    const documentIndex = new window.FlexSearch.Document({
      tokenize: "forward",
      encode,
      cache: 100,
      document: {
        id: "id",
        index: ["title", "aliases", "keywords", "summary", "search_text"],
        store: ["id", "title", "summary", "keywords", "aliases", "url"],
      },
    });
    for (const record of records) {
      documentIndex.add(record);
    }
    return documentIndex;
  }

  function buildLatinDictionary(records) {
    const terms = new Set();
    for (const record of records) {
      const text = normalize([
        ...(record.aliases || []),
        ...(record.keywords || []),
      ].join(" "));
      for (const match of text.match(LATIN_TERM_RE) || []) {
        terms.add(match);
      }
    }
    return Array.from(terms).sort();
  }

  function buildSearchLexicon(records) {
    const terms = new Set();
    for (const record of records) {
      for (const value of [...(record.aliases || []), ...(record.keywords || [])]) {
        const term = normalize(value);
        const cjkLength = (term.match(/[\u3400-\u4dbf\u4e00-\u9fff]/g) || []).length;
        if (cjkLength >= 2 || /^[a-z0-9][a-z0-9._+ -]+$/.test(term)) {
          terms.add(term);
        }
      }
    }
    return Array.from(terms).sort((left, right) =>
      right.length - left.length || left.localeCompare(right, "zh-CN")
    );
  }

  function queryConcepts(query) {
    let remaining = ` ${normalize(query)} `;
    const concepts = [];
    for (const term of searchLexicon) {
      const position = remaining.indexOf(term);
      if (position < 0) continue;
      concepts.push(term);
      remaining = `${remaining.slice(0, position)} ${remaining.slice(position + term.length)}`;
      remaining = remaining.replace(/\s+/g, " ");
    }
    return concepts;
  }

  function editDistanceAtMostOne(left, right) {
    if (left === right) return true;
    if (Math.abs(left.length - right.length) > 1) return false;
    let i = 0;
    let j = 0;
    let edits = 0;
    while (i < left.length && j < right.length) {
      if (left[i] === right[j]) {
        i += 1;
        j += 1;
        continue;
      }
      edits += 1;
      if (edits > 1) return false;
      if (left.length > right.length) i += 1;
      else if (right.length > left.length) j += 1;
      else {
        i += 1;
        j += 1;
      }
    }
    if (i < left.length || j < right.length) edits += 1;
    return edits <= 1;
  }

  function correctedQuery(query) {
    const parts = normalize(query).split(" ");
    let changed = false;
    const corrected = parts.map((part) => {
      if (!/^[a-z][a-z0-9._+-]{3,}$/.test(part)) return part;
      const candidate = latinDictionary.find((term) =>
        editDistanceAtMostOne(part, term)
      );
      if (candidate && candidate !== part) {
        changed = true;
        return candidate;
      }
      return part;
    });
    return changed ? corrected.join(" ") : query;
  }

  function fieldText(record, field) {
    return normalize(asSearchText(record[field]));
  }

  function searchCore(query) {
    if (!index || !normalize(query)) return [];
    const rawGroups = index.search(query, {
      enrich: true,
      suggest: false,
      limit: 80,
    });
    const scores = new Map();
    const normalizedQuery = normalize(query);
    const compactQuery = normalizedQuery.replace(/\s+/g, "");
    const concepts = queryConcepts(query);
    for (const group of rawGroups) {
      const field = group.field;
      const weight = FIELD_WEIGHTS[field] || 1;
      const hits = group.result || [];
      hits.forEach((hit, rank) => {
        const id = String(hit.id === undefined ? hit : hit.id);
        const record = itemsById.get(id);
        if (!record) return;
        const previous = scores.get(id) || 0;
        let score = weight * 100 - rank;
        if (fieldText(record, field).includes(normalizedQuery)) {
          score += weight * 35;
        }
        if (normalize(record.title) === normalizedQuery) {
          score += 300;
        }
        scores.set(id, previous + score);
      });
    }
    return Array.from(scores.entries())
      .map(([id, score]) => {
        const record = itemsById.get(id);
        const fields = Object.keys(FIELD_WEIGHTS).map((field) => ({
          field,
          text: fieldText(record, field),
        }));
        const conceptMatches = concepts.filter((concept) =>
          fields.some(({ text }) => text.includes(concept))
        );
        if (concepts.length && conceptMatches.length !== concepts.length) return null;
        for (const { field, text } of fields) {
          const weight = FIELD_WEIGHTS[field];
          if (text.replace(/\s+/g, "").includes(compactQuery)) score += weight * 80;
          for (const concept of conceptMatches) {
            if (text.includes(concept)) score += weight * 18;
          }
        }
        return { record, score };
      })
      .filter(Boolean)
      .sort((left, right) =>
        right.score - left.score ||
        left.record.title.localeCompare(right.record.title, "zh-CN") ||
        left.record.id.localeCompare(right.record.id)
      );
  }

  function runSearch(query) {
    let results = searchCore(query);
    let effectiveQuery = query;
    if (!results.length) {
      const corrected = correctedQuery(query);
      if (corrected !== query) {
        results = searchCore(corrected);
        effectiveQuery = corrected;
      }
    }
    return { results, effectiveQuery };
  }

  function clearChildren(element) {
    while (element.firstChild) element.removeChild(element.firstChild);
  }

  function appendHighlightedText(container, text, query) {
    const source = String(text || "");
    const needle = String(query || "").trim();
    if (!needle) {
      container.textContent = source;
      return;
    }
    const foldedSource = source.normalize("NFKC").toLocaleLowerCase("en-US");
    const foldedNeedle = needle.normalize("NFKC").toLocaleLowerCase("en-US");
    let cursor = 0;
    let matchIndex = foldedSource.indexOf(foldedNeedle);
    if (matchIndex < 0) {
      container.textContent = source;
      return;
    }
    while (matchIndex >= 0) {
      if (matchIndex > cursor) {
        container.appendChild(document.createTextNode(source.slice(cursor, matchIndex)));
      }
      const mark = document.createElement("mark");
      mark.textContent = source.slice(matchIndex, matchIndex + needle.length);
      container.appendChild(mark);
      cursor = matchIndex + needle.length;
      matchIndex = foldedSource.indexOf(foldedNeedle, cursor);
    }
    if (cursor < source.length) {
      container.appendChild(document.createTextNode(source.slice(cursor)));
    }
  }

  function matchingTerms(record, query, effectiveQuery) {
    const normalizedQueries = [normalize(query), normalize(effectiveQuery)].filter(Boolean);
    const matches = [];
    for (const value of [...(record.keywords || []), ...(record.aliases || [])]) {
      const normalizedValue = normalize(value);
      if (normalizedQueries.some((item) =>
        normalizedValue.includes(item) || item.includes(normalizedValue)
      )) {
        matches.push(value);
      }
      if (matches.length >= 3) break;
    }
    return matches.length ? matches : [effectiveQuery];
  }

  function setActiveResult(nextIndex, shouldScroll) {
    const links = Array.from(resultsElement.querySelectorAll(".result-link"));
    if (!links.length) {
      activeIndex = -1;
      input.setAttribute("aria-activedescendant", "");
      return;
    }
    activeIndex = Math.max(-1, Math.min(nextIndex, links.length - 1));
    links.forEach((link, indexValue) => {
      const selected = indexValue === activeIndex;
      link.setAttribute("aria-selected", selected ? "true" : "false");
      if (selected && shouldScroll) link.scrollIntoView({ block: "nearest" });
    });
    input.setAttribute(
      "aria-activedescendant",
      activeIndex >= 0 ? links[activeIndex].id : ""
    );
  }

  function hideResults() {
    clearChildren(resultsElement);
    resultsElement.hidden = true;
    input.setAttribute("aria-expanded", "false");
    input.setAttribute("aria-activedescendant", "");
    activeIndex = -1;
    lastResults = [];
  }

  function updateQueryUrl(query) {
    const url = new URL(window.location.href);
    if (query.trim()) url.searchParams.set("q", query.trim());
    else url.searchParams.delete("q");
    window.history.replaceState(null, "", url);
  }

  function renderResults(query) {
    const normalizedQuery = normalize(query);
    updateQueryUrl(query);
    if (!normalizedQuery) {
      hideResults();
      statusElement.textContent = "";
      return;
    }

    const searchStarted = performance.now();
    const outcome = runSearch(query);
    statusElement.dataset.searchMs = (performance.now() - searchStarted).toFixed(3);
    lastResults = outcome.results;
    clearChildren(resultsElement);
    activeIndex = -1;
    if (!outcome.results.length) {
      resultsElement.hidden = true;
      input.setAttribute("aria-expanded", "false");
      statusElement.textContent = "没有找到匹配问题，尝试换一种症状描述或英文术语。";
      return;
    }

    const shown = outcome.results.slice(0, MAX_RESULTS);
    const fragment = document.createDocumentFragment();
    shown.forEach(({ record }, resultIndex) => {
      const item = document.createElement("li");
      item.className = "result-card";
      const link = document.createElement("a");
      link.className = "result-link";
      link.id = `search-result-${resultIndex}`;
      link.href = record.url;
      link.setAttribute("role", "option");
      link.setAttribute("aria-selected", "false");

      const title = document.createElement("div");
      title.className = "result-title";
      appendHighlightedText(title, record.title, query);

      const summary = document.createElement("div");
      summary.className = "result-summary";
      appendHighlightedText(summary, record.summary, query);

      const footer = document.createElement("div");
      footer.className = "result-footer";
      const match = document.createElement("span");
      match.className = "result-match";
      match.textContent = `匹配：${matchingTerms(record, query, outcome.effectiveQuery).join(" · ")}`;
      const more = document.createElement("span");
      more.className = "result-more";
      more.textContent = "查看完整经验 →";
      footer.append(match, more);
      link.append(title, summary, footer);
      link.addEventListener("mouseenter", () => setActiveResult(resultIndex, false));
      item.appendChild(link);
      fragment.appendChild(item);
    });
    resultsElement.appendChild(fragment);
    resultsElement.hidden = false;
    input.setAttribute("aria-expanded", "true");
    statusElement.textContent = outcome.results.length > MAX_RESULTS
      ? `共 ${outcome.results.length} 条匹配，显示前 ${MAX_RESULTS} 条；继续输入可缩小范围。`
      : `共 ${outcome.results.length} 条匹配。`;
  }

  function onKeyDown(event) {
    if (composing || event.isComposing) return;
    const shownCount = Math.min(lastResults.length, MAX_RESULTS);
    if (event.key === "ArrowDown" && shownCount) {
      event.preventDefault();
      setActiveResult(activeIndex + 1 >= shownCount ? 0 : activeIndex + 1, true);
    } else if (event.key === "ArrowUp" && shownCount) {
      event.preventDefault();
      setActiveResult(activeIndex <= 0 ? shownCount - 1 : activeIndex - 1, true);
    } else if (event.key === "Enter" && activeIndex >= 0) {
      event.preventDefault();
      const link = document.getElementById(`search-result-${activeIndex}`);
      if (link) window.location.assign(link.href);
    } else if (event.key === "Escape") {
      event.preventDefault();
      input.value = "";
      renderResults("");
    }
  }

  async function initialize() {
    try {
      const response = await fetch("./search-index.json", { cache: "no-cache" });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const payload = await response.json();
      if (payload.schema_version !== 1 || !Array.isArray(payload.items)) {
        throw new Error("unsupported search index schema");
      }
      items = payload.items;
      itemsById = new Map(items.map((item) => [String(item.id), item]));
      latinDictionary = buildLatinDictionary(items);
      searchLexicon = buildSearchLexicon(items);
      index = createIndex(items);
      input.disabled = false;
      input.setAttribute("aria-busy", "false");
      statusElement.textContent = "";
      const query = new URL(window.location.href).searchParams.get("q") || "";
      if (query) {
        input.value = query;
        renderResults(query);
      }
      input.focus({ preventScroll: true });
    } catch (error) {
      input.setAttribute("aria-busy", "false");
      statusElement.textContent = "搜索索引加载失败，请刷新页面后重试。";
      console.error("WBC search initialization failed", error);
    }
  }

  input.addEventListener("compositionstart", () => { composing = true; });
  input.addEventListener("compositionend", () => {
    composing = false;
    renderResults(input.value);
  });
  input.addEventListener("input", () => {
    if (!composing) renderResults(input.value);
  });
  input.addEventListener("keydown", onKeyDown);

  window.__WBC_SEARCH_BENCHMARK__ = function (queries, iterations) {
    const samples = [];
    const selectedQueries = Array.isArray(queries) ? queries : [];
    const loops = Math.max(1, Number(iterations) || 20);
    for (let loop = 0; loop < loops; loop += 1) {
      for (const query of selectedQueries) {
        const started = performance.now();
        runSearch(query);
        samples.push(performance.now() - started);
      }
    }
    samples.sort((left, right) => left - right);
    const p95Index = Math.max(0, Math.ceil(samples.length * 0.95) - 1);
    return {
      samples: samples.length,
      p95_ms: samples[p95Index] || 0,
      max_ms: samples[samples.length - 1] || 0,
    };
  };

  initialize();
})();
