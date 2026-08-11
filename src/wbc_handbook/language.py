"""Chinese-first writing checks and a canonical bilingual robotics glossary."""

from __future__ import annotations

import re
from typing import Any, Iterable, List, Optional, Sequence, Tuple


_CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
_BILINGUAL_TERM_RE = re.compile(
    r"[\u3400-\u4dbf\u4e00-\u9fff].{0,50}[（(][A-Za-z][^）)]{1,100}[）)]"
)


# The first item is the canonical Chinese-first display string.  Aliases are
# matched against the reviewed card plus its source-level technical context.
BILINGUAL_TECHNICAL_GLOSSARY: Sequence[Tuple[str, Sequence[str]]] = (
    ("全身控制（Whole-Body Control, WBC）", ("WBC", "whole-body control", "whole body control", "全身控制")),
    ("二次规划（Quadratic Programming, QP）", ("QP", "quadratic programming", "二次规划")),
    ("模型预测控制（Model Predictive Control, MPC）", ("MPC", "model predictive control", "模型预测控制")),
    ("逆运动学（Inverse Kinematics, IK）", ("IK", "inverse kinematics", "逆运动学")),
    ("强化学习（Reinforcement Learning, RL）", (" RL ", "RL-based", "reinforcement learning", "强化学习")),
    ("仿真到现实（Simulation-to-Real, Sim2Real）", ("sim-to-real", "sim2real", "仿真到现实", "仿真实机")),
    ("仿真到仿真（Simulation-to-Simulation, Sim2Sim）", ("sim-to-sim", "sim2sim", "仿真到仿真")),
    ("域随机化（Domain Randomization, DR）", ("domain randomization", "domain ran", "域随机化")),
    ("课程学习（Curriculum Learning）", ("curriculum", "课程学习", "课程训练")),
    ("状态估计（State Estimation）", ("state estimation", "状态估计", "基座状态")),
    ("惯性测量单元（Inertial Measurement Unit, IMU）", ("IMU", "inertial measurement", "惯性测量")),
    ("激光雷达（Light Detection and Ranging, LiDAR）", ("LiDAR", "lidar", "激光雷达")),
    ("同时定位与建图（Simultaneous Localization and Mapping, SLAM）", ("SLAM", "定位与建图")),
    ("准直接驱动（Quasi-Direct Drive, QDD）", ("QDD", "quasi-direct drive", "准直接驱动")),
    ("机器人操作系统 2（Robot Operating System 2, ROS 2）", ("ROS2", "ROS 2", "robot operating system")),
    ("数据分发服务（Data Distribution Service, DDS）", ("DDS", "data distribution service", "数据分发服务")),
    ("服务质量（Quality of Service, QoS）", ("QoS", "quality of service", "服务质量")),
    ("统一机器人描述格式（Unified Robot Description Format, URDF）", ("URDF", "robot description format")),
    ("机器人模型格式（MuJoCo Modeling Format, MJCF）", ("MJCF",)),
    ("开放神经网络交换格式（Open Neural Network Exchange, ONNX）", ("ONNX",)),
    ("统一计算设备架构（Compute Unified Device Architecture, CUDA）", ("CUDA",)),
    ("图形处理器（Graphics Processing Unit, GPU）", ("GPU", "显卡", "显存")),
    ("每秒帧数（Frames Per Second, FPS）", ("FPS", "帧率")),
    ("应用程序接口（Application Programming Interface, API）", ("API", "接口")),
    ("软件开发工具包（Software Development Kit, SDK）", ("SDK", "固件")),
    ("比例-微分控制（Proportional-Derivative Control, PD Control）", (" PD ", "PD control", "PD 控制", "kp", "kd")),
    ("执行器（Actuator）", ("actuator", "执行器", "电机")),
    ("关节力矩（Joint Torque）", ("torque", "力矩", "扭矩")),
    ("接触约束（Contact Constraint）", ("contact", "接触约束", "足底接触")),
    ("动作重定向（Motion Retargeting）", ("retarget", "动作重定向", "重定向")),
    ("动作跟踪（Motion Tracking）", ("motion tracking", "动作跟踪", "运动跟踪")),
    ("全身遥操作（Whole-Body Teleoperation）", ("teleoperation", "teleop", "遥操作", "遥操")),
    ("端到端时延（End-to-End Latency）", ("latency", "时延", "延迟")),
    ("时延抖动（Latency Jitter）", ("jitter", "抖动")),
    ("质心（Center of Mass, CoM）", ("COM", "center of mass", "质心", "重心")),
    ("有效载荷（Payload）", ("payload", "载荷", "负载")),
    ("系统辨识（System Identification）", ("system identification", "系统辨识")),
    ("模型式强化学习（Model-Based Reinforcement Learning, MBRL）", ("MBRL", "model-based reinforcement")),
    ("典型相关分析（Canonical Correlation Analysis, CCA）", ("CCA", "典型相关分析")),
    ("门控循环单元（Gated Recurrent Unit, GRU）", ("GRU", "gated recurrent")),
    ("共享内存（Shared Memory）", ("shared memory", "共享内存")),
    ("零拷贝（Zero-Copy）", ("zero-copy", "zero copy", "零拷贝")),
    ("时间戳同步（Timestamp Synchronization）", ("timestamp", "时间戳", "时间同步")),
    ("重力补偿（Gravity Compensation）", ("gravity compensation", "重力补偿")),
    ("反向驱动性（Backdrivability）", ("backdrivability", "backdrivable", "反向驱动", "反驱")),
    ("热漂移（Thermal Drift）", ("thermal drift", "热漂移", "温漂", "过热")),
    ("力控带宽（Force-Control Bandwidth）", ("force-control bandwidth", "力控带宽")),
    ("求解器（Solver）", ("solver", "求解器")),
    ("动力学（Dynamics）", ("dynamics", "动力学")),
    ("大规模并行仿真（Massively Parallel Simulation）", ("parallel simulation", "并行仿真", "并行训练", "num_envs")),
    ("安全急停（Emergency Stop, E-Stop）", ("e-stop", "emergency stop", "急停", "断电")),
)


def cjk_character_count(value: Any) -> int:
    """Return the number of CJK ideographs in a value."""

    return len(_CJK_RE.findall(str(value)))


def chinese_first_error(question: Any, answer: Any) -> Optional[str]:
    """Return a stable error when a Q&A card is not substantively Chinese-first."""

    question_count = cjk_character_count(question)
    answer_count = cjk_character_count(answer)
    if question_count < 5:
        return "question_zh must contain at least 5 Chinese characters"
    if answer_count < 20:
        return "answer_zh must contain at least 20 Chinese characters"
    return None


def is_bilingual_technical_term(value: Any) -> bool:
    """Return whether a term follows the Chinese（English）display convention."""

    return bool(_BILINGUAL_TERM_RE.fullmatch(str(value).strip()))


def normalize_bilingual_terms(value: Any, name: str = "bilingual_terms") -> List[str]:
    """Validate and deduplicate explicit Chinese-first bilingual terms."""

    if not isinstance(value, list) or not value:
        raise ValueError(f"{name} must be a non-empty list")
    if len(value) > 12:
        raise ValueError(f"{name} exceeds the 12-term limit")
    terms: List[str] = []
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            raise ValueError(f"{name}[{index}] must be a non-empty string")
        term = item.strip()
        if len(term) > 140:
            raise ValueError(f"{name}[{index}] exceeds 140 characters")
        if not is_bilingual_technical_term(term):
            raise ValueError(
                f"{name}[{index}] must use the Chinese（English）format"
            )
        if term not in terms:
            terms.append(term)
    return terms


def infer_bilingual_terms(text: Any, limit: int = 6) -> List[str]:
    """Infer canonical bilingual display terms from reviewed technical context."""

    haystack = f" {str(text)} "
    folded = haystack.casefold()
    terms: List[str] = []
    for canonical, aliases in BILINGUAL_TECHNICAL_GLOSSARY:
        matched = False
        for alias in aliases:
            if alias.isascii():
                matched = alias.casefold() in folded
            else:
                matched = alias in haystack
            if matched:
                break
        if matched:
            terms.append(canonical)
            if len(terms) >= limit:
                break
    return terms


def bilingual_terms_text(terms: Iterable[str]) -> str:
    """Render terms as a stable Chinese enumeration."""

    return "；".join(terms)
