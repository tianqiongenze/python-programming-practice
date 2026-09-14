
# 《Python编程基础》课程标准

**课程代码：** ZY-IIoT-0301　　**适用专业：** 工业互联网应用
**开课学期：** 第三学期　　**总学时：** 48（理论19 + 实践29）　　**学分：** 3
**课程类型：** 专业必修课　　**制定单位：** 智能控制学院

---

## 一、课程定位与性质

### （一）课程定位
《Python编程基础》是工业互联网应用专业的一门**专业核心课程**，是连接前导课程（《计算机网络基础》《工业传感器与检测技术》）与后续课程（《工业大数据分析》《边缘计算与AIoT应用》《工业互联网综合项目实训》）的**关键枢纽**。

本课程以工业互联网"端-边-云"数据全链路为主线，选取Python作为工业数据采集、分析与AI应用的首选语言，培养学生具备从**数据采集→通信传输→分析可视化→机器学习预测→系统集成**的完整工程能力，是学生成长为工业数据采集工程师、工业数据分析工程师、AIoT应用开发工程师的能力基石。

### （二）课程性质
本课程遵循**德国双元制本土化**理念，采用**工作过程导向**的项目化、工单化教学模式，以真实工业场景为载体，实现"课程内容与职业标准对接、教学过程与生产过程对接、学历证书与职业技能等级证书对接"，是一门理实一体、校企协同的实践性课程。

---

## 二、课程设计思路

### （一）设计依据
1. 依据工业互联网应用专业人才培养方案及职业岗位能力需求；
2. 对接**1+X《工业互联网数据采集与边缘计算》职业技能等级证书**（中级）标准；
3. 融入工业互联网产业发展趋势与企业真实生产项目需求。

### （二）设计理念
1. **项目引领、任务驱动**：以"温湿度采集→MQTT上云→OEE看板→轴承故障预测→端边云全链路集成"贯穿全课程主线，将课程解构为5大模块、25个真实工业工单。
2. **双元制六步教学法**：每个工单按"资讯→计划→决策→实施→检查→评价"六步组织实施。
3. **ABCD分层、因材施教**：依学生意愿与能力分A/B/C/D四层，配套分层工单，实施"精英特训→模拟项目组"两轮教学。
4. **课证融通、校企双元**：内容覆盖1+X证书考点，引入企业导师参与工单评审与项目答辩。

### （三）模块与学时分配

| 模块 | 模块名称 | 工单数 | 理论 | 实践 | 学时 |
|---|---|---|---|---|---|
| 模块0 | Python快速入门 | 5 | 3 | 5 | 8 |
| 模块1 | 数据采集与工业通信 | 5 | 5 | 3 | 8 |
| 模块2 | 数据分析与可视化 | 5 | 3 | 9 | 12 |
| 模块3 | 机器学习与预测维护 | 5 | 5 | 7 | 12 |
| 模块4 | 综合项目实战与答辩 | 5 | 3 | 5 | 8 |
| **合计** | | **25** | **19** | **29** | **48** |

---

## 三、课程目标

### （一）总体目标
面向工业互联网数据采集与AI应用岗位，培养学生掌握Python编程基础与工业数据全链路处理技能，具备工业数据采集、分析、可视化与机器学习应用的综合职业能力，养成规范严谨的工程素养与精益求精的工匠精神。

### （二）知识目标（Knowledge）
1. 掌握Python基本语法、数据结构、控制流与函数模块化编程；
2. 掌握串口/Modbus RTU/MQTT等工业通信协议原理与实现；
3. 掌握Pandas数据清洗、GroupBy聚合与工业KPI计算方法；
4. 掌握Pyecharts工业可视化与Dashboard看板开发；
5. 掌握时频域特征工程、Scikit-Learn机器学习建模、评估与部署；
6. 理解工业AIoT端-边-云三层架构设计原理。

### （三）能力目标（Skill）
1. 能搭建开发环境并编写规范的Python程序解决工业逻辑问题；
2. 能基于树莓派实现多传感器数据采集与MQTT云端传输；
3. 能完成工业数据清洗、KPI计算并开发可视化监控看板；
4. 能提取时频域特征、训练调优故障预测模型并部署为推理API；
5. 能完成工业AIoT系统的需求分析、架构设计、集成联调与文档撰写；
6. 能进行技术路演答辩与工程成果交付。

### （四）素质目标（Attitude）
1. 树立代码规范（PEP8）即工匠品质的职业理念，养成严谨细致习惯；
2. 建立工业/数据安全意识与"宁可误报勿漏报"的安全责任底线；
3. 培养团队协作、成果表达与自主学习能力；
4. 厚植制造强国、数字中国的使命担当，践行绿色智造理念。

---

## 四、课程内容与要求

> 详见《课程内容标准表》，每个工单明确了工作任务、知识点、技能点、素质点与考核要点。以下列出各模块核心内容与教学要求。

### 模块0　Python快速入门（8学时）
**内容**：环境搭建、变量与数据类型、控制流、数据结构、函数封装、OEE计算器综合实战。
**要求**：能独立配置Jupyter环境；能运用变量、控制流、数据结构、函数解决工业结构化数据处理问题；能编写工厂设备OEE计算器。
**对应工单**：WO-0-01 ～ WO-0-05。

### 模块1　数据采集与工业通信（8学时）
**内容**：树莓派环境、PySerial串口、Modbus RTU、MQTT发布订阅、多传感器集成、数据上云端到端联调。
**要求**：能解析Modbus RTU帧读取传感器数据；能搭建MQTT Broker实现数据上云；能完成端-边-云全链路联调并输出测试报告。
**对应工单**：WO-1-01 ～ WO-1-05。

### 模块2　数据分析与可视化（12学时）
**内容**：Pandas数据清洗、工业KPI计算、Pyecharts图表、Dashboard集成、自动化报表。
**要求**：能清洗工业数据并计算OEE/MTBF/MTTR等KPI；能开发工业可视化看板与自动化报表。
**对应工单**：WO-2-01 ～ WO-2-05。

### 模块3　机器学习与预测维护（12学时）
**内容**：数据预处理、时频域特征工程、SVM/随机森林训练调优、模型评估、模型持久化与推理部署。
**要求**：能提取时频域特征并训练故障预测模型（加权F1≥0.88）；能部署为Flask推理API。
**对应工单**：WO-3-01 ～ WO-3-05。

### 模块4　综合项目实战与答辩（8学时）
**内容**：需求分析与架构设计、采集通信集成、分析看板与ML对接、系统联调测试、技术文档与路演答辩。
**要求**：能完成工业AIoT系统的架构设计、集成联调、文档撰写与答辩交付。
**对应工单**：WO-4-01 ～ WO-4-05。

---

## 五、课程实施建议

### （一）教学条件
1. **实训室**：数据采集实训室（配计算机、投影、教学平台）；
2. **硬件**：树莓派4B + RS485温湿度/光照/CO₂传感器套件、USB-TTL模块；
3. **软件**：Anaconda/Jupyter、Mosquitto Broker、JupyterHub、Pandas/Pyecharts/Scikit-Learn/Flask、Git、Postman；
4. **数据资源**：CNC/注塑机运行日志、CWRU轴承故障数据集等企业真实脱敏数据集。

### （二）教学方法
双元制六步法、ABCD分层任务教学、真实案例项目驱动、翻转课堂、校企双元协同、线上线下混合式教学。

### （三）师资要求
主讲教师须具备Python工程开发与工业互联网项目经验，为"双师型"教师；引入企业工程师担任兼职导师参与工单评审与项目答辩。

---

## 六、课程考核与评价

### （一）考核方式：过程性考核 + 项目答辩 + 素养考核

| 考核项目 | 权重 | 考核内容 |
|---|---|---|
| 过程性考核 | 60% | 25个工单任务完成度、代码规范（PEP8）、实验报告（允许重提交） |
| 阶段项目答辩 | 30% | M0～M4五个里程碑成果、综合系统完整性、路演答辩表现 |
| 出勤与职业素养 | 10% | 出勤、课堂参与、团队协作、工业/数据安全规范意识 |

### （二）里程碑节点（Milestone）

| 里程碑 | 名称 | 验收标准 |
|---|---|---|
| M0 | Python基础通关 | OEE计算器运行正确，代码规范 |
| M1 | 数据成功上云 | 端到端延迟≤100ms，数据完整 |
| M2 | 数据看板上线 | Dashboard集成+自动报表 |
| M3 | 故障预测API上线 | 加权F1≥0.88，响应≤100ms |
| M4 | 综合系统交付 | 全链路贯通+文档齐全+答辩通过 |

### （三）评价主体
教师评价、学生自评/互评、企业导师评价相结合的多元评价。

---

## 七、教材与参考资源
1. **自编活页式工单教材**：《Python工业互联网应用实战工单集》（25个工单）；
2. 参考书：《Python编程：从入门到实践》《利用Python进行数据分析》《Scikit-Learn机器学习实战》；
3. 在线资源：课程在线学习平台、1+X证书备考题库、工业数据集库。

---

*本课程标准由智能控制学院工业互联网教研室制定，经学院教学委员会审定后执行。*

---

## JupyterHub 平台功能更新 (2026-09-04)

> **所有新功能已同步到此文件。以下为 JupyterHub 平台最新功能概要。**

### 访问方式
- **URL**: `https://10.167.2.175:31825/ide/`
- **密码**: `ide2026`（所有账户共享）

### 账户体系
| 账户 | 类型 | 对应课程 |
|------|------|----------|
| `teacher-zhang` | 管理员+总教师 | 全部8个Notebook |
| `Lecture-P1` | 管理员+章节教师 | P1.1 Python基础 + P1.2 标准Python工程 |
| `Lecture-P2` | 管理员+章节教师 | P2.1 Pandas数据处理 + P2.2 NumPy故障特征 |
| `Lecture-P3` | 管理员+章节教师 | P3 产线KPI仪表盘 |
| `Lecture-P4` | 管理员+章节教师 | P4.1 多源数据采集系统 |
| `Lecture-P5` | 管理员+章节教师 | P5 产线数据仓库与ORM |
| `Lecture-P6` | 管理员+章节教师 | P6 故障诊断模型与部署 |
| `student-python` | 学生 | Python 工业遥测分析项目 |
| `student-java` | 学生 | Java MES 生产管理系统 |
| `student-go` | 学生 | Go 工业网关项目 |
| `student-rust` | 学生 | Rust 安全审计项目 |

### AI 功能
- **jupyter-ai 聊天**: 登录后直接使用（左侧栏AI面板，无需配置）
- **LLM模型**: qwen2.5-coder:7b (Ollama CPU推理, 响应6-21秒)
- **内联补全**: LSP+pylsp 弹窗补全 + AI FIM缓存

### 代码评分系统
- **评分维度**: PEP8(20%) + 测试通过率(40%) + 查重(20%) + AI率(20%)
- **运行**: `python3 /home/jovyan/work/code_grader.py`
- **等级**: A(≥90) / B(80-89) / C(70-79) / D(60-69) / F(<60)

### 测试结果
- **功能测试**: 13/13 通过 (100%)
- **50并发用户**: 100% 成功, 24.5秒
- **LLM Chat**: PASS (21秒)
- **Notebook执行**: PASS (1.4秒)

### 管理面板
- **URL**: `https://10.167.2.175:31825/ide/hub/admin`
- **功能**: 查看用户/服务器状态、启动/停止服务器、作业发布与检查

---

## 19. 多语言代码审查系统 (v2.1 新增)

### 支持语言与工具

| 语言 | 工具 | 检查内容 |
|------|------|----------|
| Python | pycodestyle + pyflakes | PEP8 规范、语法错误 |
| Java | Checkstyle / javac | 代码规范、编译错误 |
| Go | gofmt + go vet | 格式化、静态分析 |
| Rust | cargo clippy + rustfmt | 代码质量、格式化 |
| C/C++ | cppcheck | 内存泄漏、未初始化变量 |
| JavaScript | node --check | 语法错误 |

### 使用方式

```bash
# 单文件审查
python3 code_review.py src/main.py

# 目录审查（自动检测语言，递归所有源文件）
python3 code_review.py /home/jovyan/work/industrial-analytics/src/
python3 code_review.py /home/jovyan/work/mes-system/production-service/src/
python3 code_review.py /home/jovyan/work/industrial-gateway/
python3 code_review.py /home/jovyan/work/security-audit/
```

### 输出格式（JSON）

```json
{
  "language": "Python",
  "tool": "pycodestyle",
  "issues": ["src/main.py:10:1: E302 expected 2 blank lines"],
  "score": 85
}
```

### 评分规则

| 语言 | 每个问题扣分 | 满分 |
|------|-------------|------|
| Python | 100/总行数 | 100 |
| Java | 5分/问题 | 100 |
| Go | 10分/问题 | 100 |
| Rust | 5分/问题 | 100 |
| C/C++ | 5分/问题 | 100 |

---

## 20. 指南分发规则 (v2.1 新增)

| 用户类型 | 教师版指南 | 学生版指南 | 评分系统 | AI助手 |
|----------|-----------|-----------|----------|--------|
| teacher-zhang | ✅ | ✅ | ✅ | ✅ |
| Lecture-* (16个) | ✅ | ✅ | ✅ | ✅ |
| 学生（任何注册） | ❌ | ✅ | ✅ | ✅ |

---

## 21. CockroachDB K8s 部署确认 (v2.1 新增)

### 部署方式

CockroachDB 已从裸金属迁移到 K8s Pod 部署：

| 项目 | 旧（裸金属） | 新（K8s Pod） |
|------|-------------|--------------|
| 二进制路径 | /opt/cockroach/cockroach | /cockroach-binary/cockroach（容器内） |
| 数据路径 | /home/crdb-data/a | /cockroach/cockroach-data（hostPath） |
| systemd | cockroach-node1/2.service | StatefulSet |
| systemd 状态 | — | disabled + inactive (dead) |
| 管理方式 | systemctl | kubectl / Rancher |
| 网络模式 | 宿主机直接 | hostNetwork: true |

> **说明**：由于使用 `hostNetwork: true`，Pod 进程在宿主机 `ps aux` 中可见，
> 但实际运行在容器内（二进制路径为 `/cockroach-binary/`，非 `/opt/cockroach/`）。
> 旧 systemd 服务已 disable + stopped。

### 局域网连接（读写分离）

| 用途 | 地址 | 端口 |
|------|------|------|
| 写连接 | 10.167.2.175 | 26257 |
| 读连接 | 10.167.2.175 | 26267 |
| NodePort 写 | 10.167.2.175 | 30257 |
| NodePort 读 | 10.167.2.175 | 30267 |
| 管理界面 | http://10.167.2.175 | 30259 |
| K8s 内写 | cockroachdb.infra.svc | 26257 |
| K8s 内读 | cockroachdb-read.infra.svc | 26267 |

---

## 22. 多教师同课程+班级关联体系 (v2.2 新增)

### 体系架构

```
teacher-zhang (总管理员)
├── 02-程序设计基础
│   ├── teacher-b1-01 → class-b1-01-A, class-b1-01-B
│   ├── teacher-b2-01 → class-b2-01-A
│   ├── teacher-b3-01 → class-b3-01-A
│   ├── teacher-b4-01 → class-b4-01-A
│   ├── teacher-b5-01 → class-b5-01-A
│   └── teacher-b6-01 → class-b6-01-A
├── 01-AI应用基础
│   ├── teacher-a1-01 → class-a1-01-A, class-a1-01-B
│   ├── teacher-a2-01 → class-a2-01-A
│   ├── teacher-a3-01 → class-a3-01-A
│   └── teacher-a4-01 → class-a4-01-A
└── 03-Python项目实战
    ├── teacher-p1-01 → class-p1-01-A, class-p1-01-B
    ├── teacher-p2-01 → class-p2-01-A
    ├── teacher-p3-01 → class-p3-01-A
    ├── teacher-p4-01 → class-p4-01-A
    ├── teacher-p5-01 → class-p5-01-A
    └── teacher-p6-01 → class-p6-01-A
```

### 同一课程多个教师

同一课程可以有多位教师同时授课，每位教师管理自己的班级：

| 课程 | 教师 | 负责班级 | 可管理学生 |
|------|------|----------|-----------|
| B1 (设备初始化) | teacher-b1-01 | class-b1-01-A, class-b1-01-B | A班+B班学生 |
| B1 (设备初始化) | teacher-b1-02 (新增) | class-b1-02-A | 新教师A班学生 |

> 教师使用 `https://10.167.2.175:31825/ide/hub/admin` 管理面板查看自己班级的学生。

### 学生登录格式

学生用户名格式: `{课程}-{班级}-{学号}`

| 格式 | 含义 | 关联教师 |
|------|------|----------|
| `b1-A-01` | 程序设计基础 B1 A班 01号 | teacher-b1-01 |
| `b1-B-05` | 程序设计基础 B1 B班 05号 | teacher-b1-01 |
| `a1-A-03` | AI应用基础 A1 A班 03号 | teacher-a1-01 |
| `p1-B-10` | Python项目实战 P1 B班 10号 | teacher-p1-01 |

### 教师管理学生流程

1. 教师登录 (`teacher-b1-01`, 密码 `ide2026`)
2. 访问管理面板: `https://10.167.2.175:31825/ide/hub/admin`
3. 查看自己班级的学生服务器状态
4. 启动/停止学生服务器
5. 使用 `code_grader.py` 评分学生代码

### 新增教师流程

1. 总管理员 `teacher-zhang` 在终端创建新教师:
   ```bash
   # 新教师登录即可自动创建 (密码 ide2026)
   # 然后在 hub pod 中将其加入对应课程组和班级组
   ```

2. 将新教师加入课程教师组和班级组（示例）:
   ```bash
   kubectl exec -n jupyterhub <hub-pod> -c jupyterhub -- python3 -c "
   import sqlite3
   conn = sqlite3.connect('/srv/jupyterhub/jupyterhub.sqlite')
   c = conn.cursor()
   # 创建教师
   c.execute('INSERT INTO users (name, admin) VALUES (?, 1)', ('teacher-b1-02',))
   # 加入课程教师组
   c.execute('SELECT id FROM groups WHERE name="course-b-teachers"')
   gid = c.fetchone()
   c.execute('SELECT id FROM users WHERE name="teacher-b1-02"')
   uid = c.fetchone()
   c.execute('INSERT INTO users_groups VALUES (?, ?)', (uid[0], gid[0]))
   # 创建新班级组
   c.execute('INSERT INTO groups (name) VALUES (?)', ('class-b1-02-A',))
   # 加入班级组
   c.execute('SELECT id FROM groups WHERE name="class-b1-02-A"')
   cg = c.fetchone()
   c.execute('INSERT INTO users_groups VALUES (?, ?)', (uid[0], cg[0]))
   conn.commit()
   "
   ```


---

## 23. OAuth 400 修复 + 测试报告 (v2.3)

### OAuth 400 修复
- 根因: Hub重启导致OAuth客户端丢失
- 修复: 清除stale oauth codes + 重新登录
- 验证: teacher-zhang登录成功

### 数据保留
- PVC Bound | 76 Notebook | 8 Code | 双指南 | 评分系统
- 结论: 零数据丢失

### LLM测试
- master: 59s | teacher pod: 28s | qwen2.5-coder:7b
- 瓶颈: CPU-only推理

### CRDB测试
- 3节点 Running | 27+数据库 | 读写分离

### 资源优化
- milvus/nebula/pulsar stopped | Worker CPU 79% -> 57%


---

## 24. nbgrader 原生作业系统 (v2.4 新增)

### 概述

JupyterHub 已安装 **nbgrader 0.9.5**，提供原生的作业分发、收集、自动评分和反馈功能，替代了之前的手动 code_grader.py。

### 教师操作流程

```bash
cd ~/work/nbgrader

# 1. 创建作业（在 source/ 目录下创建 Notebook）
#    在 JupyterLab 中使用 nbgrader 工具栏标记单元格类型:
#    - 答案区（Solution）: 学生需要填写的代码
#    - 测试区（Test）: assert 断言（自动评分用）
#    - 只读区（Read-only）: 题目描述

# 2. 生成学生版（自动去除解决方案）
python3 -m nbgrader generate_assignment ps1

# 3. 发布作业到 exchange
python3 -m nbgrader release_assignment ps1

# 4. 查看已发布的作业
python3 -m nbgrader list

# 5. 学生提交后，自动评分
python3 -m nbgrader autograde ps1

# 6. 生成反馈
python3 -m nbgrader generate_feedback ps1
python3 -m nbgrader release_feedback ps1

# 7. 导出成绩 CSV
python3 -m nbgrader export
```

### 学生操作流程

```bash
cd ~/work/nbgrader

# 1. 查看可用作业
python3 -m nbgrader list

# 2. 获取作业
python3 -m nbgrader fetch ps1

# 3. 完成作业后提交
python3 -m nbgrader submit ps1
```

### nbgrader 元数据要求

每个 nbgrader 单元格需要完整的 v3 元数据:
- `grade`: True/False（是否评分）
- `solution`: True/False（是否答案区）
- `task`: False
- `locked`: True/False（是否锁定）
- `points`: 浮点数（分值）
- `grade_id`: 唯一标识符
- `schema_version`: 3
- `cell_type`: "code"

### Exchange 目录

| 路径 | 说明 |
|------|------|
| `~/work/nbgrader/exchange/` | 共享交换目录 |
| `exchange/default/outbound/` | 教师发布的作业 |
| `exchange/default/inbound/` | 学生提交的作业 |

---

## 25. 多教师多课程账户体系 (v2.4 完整版)

### 完整对照表

```
teacher-zhang (总管理员, 密码: ide2026)
├── 02-程序设计基础
│   ├── Lecture-B1~B6 (原始管理员)
│   ├── teacher-b1-01 → class-b1-01-A, class-b1-01-B
│   ├── teacher-b2-01 → class-b2-01-A
│   ├── teacher-b3-01 → class-b3-01-A
│   ├── teacher-b4-01 → class-b4-01-A
│   ├── teacher-b5-01 → class-b5-01-A
│   └── teacher-b6-01 → class-b6-01-A
├── 01-AI应用基础
│   ├── Lecture-A1~A4
│   ├── teacher-a1-01 → class-a1-01-A, class-a1-01-B
│   ├── teacher-a2-01 → class-a2-01-A
│   ├── teacher-a3-01 → class-a3-01-A
│   └── teacher-a4-01 → class-a4-01-A
└── 03-Python项目实战
    ├── Lecture-P1~P6
    ├── teacher-p1-01 → class-p1-01-A, class-p1-01-B
    ├── teacher-p2-01 → class-p2-01-A
    ├── teacher-p3-01 → class-p3-01-A
    ├── teacher-p4-01 → class-p4-01-A
    ├── teacher-p5-01 → class-p5-01-A
    └── teacher-p6-01 → class-p6-01-A
```

### 学生登录格式

| 格式 | 含义 | 关联教师 |
|------|------|----------|
| `b1-A-01` | 程序设计基础 B1 A班 01号 | teacher-b1-01 |
| `a1-B-03` | AI应用基础 A1 B班 03号 | teacher-a1-01 |
| `p1-A-05` | Python项目实战 P1 A班 05号 | teacher-p1-01 |

### 账户总计

- 33 个教师/管理员账户
- 43 个分组
- 56 个 Notebook
- 28 个代码框架
- 3 门课程
