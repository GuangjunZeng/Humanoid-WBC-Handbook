# 论文关键图资产

本目录只保留深读正文实际引用的关键图所在页，不保存整篇 PDF。每篇论文的 `manifest.json` 记录固定版本 PDF、页码、Figure/Table 定位、中文图注与 SHA-256。

图像均来自对应论文，仅用于评论、教学与技术分析；版权和许可不归本项目 Apache-2.0 许可覆盖。转载、商用或二次分发前，请核对论文出版方与作者的原始条款。

重建与校验：

```bash
python3 scripts/extract_key_figures.py
python3 scripts/extract_key_figures.py --check
```

PDF 只下载到已忽略的 `var/papers/` 目录；页码规格在 `research/key-figures.json`。
