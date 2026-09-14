
# 《Python工业互联网应用实战工单集》
## ——工业互联网应用专业活页式工单教材

**主编：** 宫宇伟　　**适用课程：** Python编程基础　　**工单总数：** 25个

---

### 【工单使用说明】

本工单集配合《Python编程基础》课程使用，共25个工单，对应五大模块。每个工单采用**双元制六步法**结构组织：**① 任务资讯 → ② 任务计划 → ③ 方案决策 → ④ 任务实施 → ⑤ 检查验收 → ⑥ 评价反思**。工单实行**ABCD分层任务**：A层（拓展挑战，含异常处理与优化）、B层（核心任务）、C层（模板填空）、D层（跟练操作），学生按分层完成并提交交付物。

---
---

# 模块0　Python快速入门

---

## 工单 WO-0-01　《零基础第一行代码》

**建议学时：** 2　　**难度：** ★☆☆☆☆　　**对应里程碑：** M0

### ① 任务资讯
| 项目 | 内容 |
|---|---|
| **任务场景** | 某智能工厂需要新入职工程师快速搭建Python开发环境，作为工业数据处理的第一步。你需要配置好开发环境并运行第一个程序，验证工具链可用。 |
| **任务目标** | 完成Anaconda与Jupyter Notebook安装配置，运行首个Python程序。 |
| **知识点** | Anaconda发行版、Jupyter Notebook交互式环境、print()、变量、type()、Python在工业AIoT中的地位 |
| **技能点** | 环境安装、Jupyter基本操作、运行代码单元 |
| **素质点** | 破除零基础心理壁垒，建立编程自信 |

### ② 任务计划
1. 下载并安装Anaconda发行版；
2. 启动Jupyter Notebook，创建新的.ipynb文件；
3. 编写并运行print、四则运算、变量赋值、类型查看代码。

### ③ 方案决策
- **环境选型**：为什么选Anaconda而非纯Python？（内置科学计算库、环境管理便捷）
- **IDE选型**：Jupyter交互式"输入即见结果"适合初学者调试。

### ④ 任务实施（分层任务）
```python
# 【D层/C层】跟练基础代码
print("Hello, Industrial IoT!")
print(3 + 5, 10 * 2, 100 / 7)

# 【B层】变量与类型
device_id = "CNC-001"      # 字符串
temperature = 65.5          # 浮点数
is_running = True           # 布尔
print(device_id, type(device_id))
print(temperature, type(temperature))

# 【A层拓展】用f-string格式化输出设备状态
print(f"设备{device_id}当前温度{temperature}℃, 运行状态: {is_running}")
```

### ⑤ 检查验收
| 检查项 | 标准 | 自检 |
|---|---|---|
| 环境安装 | Anaconda/Jupyter正常启动 | □ |
| 代码运行 | 无报错，输出正确 | □ |
| 类型查看 | 正确识别str/float/bool | □ |
| 代码规范 | 变量命名有意义 | □ |

### ⑥ 评价反思
- **交付物**：Jupyter笔记本文件（.ipynb）+ 环境配置截图
- **反思**：安装过程遇到的问题及解决方法？_______________

---

## 工单 WO-0-02　《变量、数据类型与控制流实战》

**建议学时：** 2　　**难度：** ★★☆☆☆

### ① 任务资讯
| 项目 | 内容 |
|---|---|
| **任务场景** | 工厂需要一个程序，根据设备温度自动判断设备处于"正常/预警/故障"三种状态，辅助巡检员快速决策。 |
| **任务目标** | 运用变量、数据类型、运算符与条件分支实现设备状态判断。 |
| **知识点** | int/float/str/bool、运算符、f-string、if/elif/else、比较与逻辑运算符 |
| **技能点** | 条件分支编写、多条件判断 |
| **素质点** | 树立"一次做对"的严谨习惯 |

### ② 任务计划
1. 定义设备ID、温度、运行状态变量；
2. 设定阈值（正常<70℃，预警70-85℃，故障>85℃）；
3. 用if/elif/else输出状态。

### ③ 方案决策
- 阈值边界如何处理（>= 还是 >）？工业上通常预警区间取闭区间。
- 是否需要考虑温度为负值等异常输入？

### ④ 任务实施（分层任务）
```python
# 【B层核心任务】
device_id = "CNC-001"
temperature = 78.5

if temperature > 85:
    status = "故障"
elif temperature >= 70:
    status = "预警"
else:
    status = "正常"
print(f"设备{device_id} 温度{temperature}℃ → 状态: {status}")

# 【A层拓展】增加输入校验与湿度联合判断
def check_device(device_id, temp, humidity):
    if temp < -20 or temp > 200:
        return f"{device_id}: 传感器异常(温度越界)"
    if temp > 85 or humidity > 90:
        return f"{device_id}: 故障"
    elif temp >= 70:
        return f"{device_id}: 预警"
    return f"{device_id}: 正常"

print(check_device("CNC-002", 78.5, 65))
```

### ⑤ 检查验收
| 检查项 | 标准 | 自检 |
|---|---|---|
| 三种状态 | 边界值判断正确 | □ |
| 输出格式 | f-string规范 | □ |
| A层异常处理 | 越界能识别 | □ |

### ⑥ 评价反思
- **交付物**：设备状态判断脚本（.py）+ 运行结果截图
- **反思**：边界值（如70℃、85℃）应归入哪一档？为什么？

---

## 工单 WO-0-03　《内置数据结构：组织工业数据》

**建议学时：** 1　　**难度：** ★★☆☆☆

### ① 任务资讯
| 项目 | 内容 |
|---|---|
| **任务场景** | 车间有多台设备，每台设备有ID、类型、温度、状态等属性，需用合适的数据结构组织这批结构化数据并进行批量处理。 |
| **知识点** | list、dict、tuple特性与适用场景、增删改查、for/while循环、range、break/continue、推导式 |
| **技能点** | 数据结构选择与操作、循环批处理、推导式 |
| **素质点** | 工作过程导向的数据组织思维 |

### ② 任务计划
1. 用list存储设备列表，dict存储单设备属性，tuple存储不可变传感器配置；
2. 用for循环遍历批量处理；
3. 用推导式筛选高温设备。

### ③ 方案决策
- 何时用list（有序可变）、dict（键值映射）、tuple（不可变配置）？
- 嵌套字典如何安全访问避免KeyError？（使用.get()）

### ④ 任务实施（分层任务）
```python
# 【B层】设备数据组织
devices = [
    {"id": "CNC-001", "type": "机床", "temp": 65.5, "status": "正常"},
    {"id": "CNC-002", "type": "机床", "temp": 88.0, "status": "故障"},
    {"id": "INJ-001", "type": "注塑机", "temp": 72.3, "status": "预警"},
]
sensor_config = ("Modbus", 9600, 8, 1)  # 不可变配置

for d in devices:
    print(f"{d['id']}: {d.get('temp')}℃ - {d['status']}")

# 【A层拓展】推导式筛选高温设备(>70℃)
high_temp = [d["id"] for d in devices if d["temp"] > 70]
print("高温设备:", high_temp)
```

### ⑤ 检查验收
| 检查项 | 标准 | 自检 |
|---|---|---|
| 数据结构选择 | 合理使用list/dict/tuple | □ |
| 循环遍历 | 输出完整无遗漏 | □ |
| 推导式 | 筛选结果正确 | □ |

### ⑥ 评价反思
- **交付物**：数据结构操作脚本（.py）
- **反思**：传感器配置为何用tuple而非list？

---

## 工单 WO-0-04　《函数封装与模块化编程》

**建议学时：** 1　　**难度：** ★★★☆☆

### ① 任务资讯
| 项目 | 内容 |
|---|---|
| **任务场景** | 设备状态判断逻辑在多处重复使用，需将其封装为可复用函数，并整理为独立模块供其他脚本导入调用。 |
| **知识点** | 函数定义、参数、返回值、默认参数、模块导入、代码复用 |
| **技能点** | 函数封装、模块化拆分、import调用 |
| **素质点** | 模块化工程思维 |

### ② 任务计划
1. 将状态判断封装为check_status(temp, threshold=70)；
2. 将格式化输出封装为format_report(data)；
3. 保存为device_utils.py模块并在主脚本导入。

### ③ 方案决策
- 函数拆分粒度如何把握？（单一职责原则）
- 哪些参数应设默认值？

### ④ 任务实施（分层任务）
```python
# device_utils.py 【B层】
def check_status(temp, warn=70, fault=85):
    if temp > fault:
        return "故障"
    elif temp >= warn:
        return "预警"
    return "正常"

def format_report(device_id, temp):
    return f"[报告] 设备{device_id} 温度{temp}℃ 状态:{check_status(temp)}"

# main.py 【A层】导入调用
from device_utils import check_status, format_report
print(format_report("CNC-001", 78.5))
```

### ⑤ 检查验收
| 检查项 | 标准 | 自检 |
|---|---|---|
| 函数定义 | 参数返回值正确 | □ |
| 模块导入 | 成功import调用 | □ |
| 默认参数 | 阈值可配置 | □ |

### ⑥ 评价反思
- **交付物**：函数模块（device_utils.py）+ 调用测试脚本
- **反思**：封装函数带来了哪些好处？

---

## 工单 WO-0-05　《综合实战：工厂设备OEE计算器》

**建议学时：** 2　　**难度：** ★★★☆☆　　**里程碑：** M0验收

### ① 任务资讯
| 项目 | 内容 |
|---|---|
| **任务场景** | 精益生产要求量化设备综合效率（OEE）。你需开发一个OEE计算器，输入可用性、性能、质量数据，计算并分级评价多台设备的OEE。 |
| **知识点** | OEE=可用性A×性能P×质量Q、输入验证、边界处理、函数综合应用 |
| **技能点** | 综合编程、批量数据处理、异常处理 |
| **素质点** | 精益生产、精益求精工匠精神 |

### ② 任务计划
1. 编写calculate_oee(a, p, q)函数；
2. 对多设备测试数据集批量计算；
3. 按世界级基准（OEE≥85%优秀）分级。

### ③ 方案决策
- 如何处理除零、比率>1等异常输入？
- OEE分级标准如何设定？（≥85%优秀，60-85%良好，<60%待改进）

### ④ 任务实施（分层任务）
```python
def calculate_oee(availability, performance, quality):
    # 【A层】输入验证
    for v in (availability, performance, quality):
        if not (0 <= v <= 1):
            raise ValueError("比率须在0-1之间")
    oee = availability * performance * quality
    if oee >= 0.85:
        level = "世界级"
    elif oee >= 0.60:
        level = "良好"
    else:
        level = "待改进"
    return round(oee * 100, 2), level

data = [
    {"id": "CNC-001", "A": 0.90, "P": 0.95, "Q": 0.99},
    {"id": "INJ-001", "A": 0.80, "P": 0.85, "Q": 0.92},
]
for d in data:
    oee, level = calculate_oee(d["A"], d["P"], d["Q"])
    print(f"{d['id']}: OEE={oee}% ({level})")
```

### ⑤ 检查验收
| 检查项 | 标准 | 自检 |
|---|---|---|
| OEE公式 | 计算正确 | □ |
| 批量处理 | 多设备遍历 | □ |
| 异常处理 | 越界能捕获 | □ |
| 分级 | 阈值判断正确 | □ |

### ⑥ 评价反思
- **交付物**：OEE计算脚本 + 多设备测试数据集 + 运行结果截图 + Jupyter学习笔记本（里程碑M0）
- **反思**：OEE提升对绿色低碳制造有何意义？

---
---

# 模块1　数据采集与工业通信

---

## 工单 WO-1-01　《边缘节点搭建与串口通信》

**建议学时：** 2　　**难度：** ★★★☆☆

### ① 任务资讯
| 项目 | 内容 |
|---|---|
| **任务场景** | 工厂需在产线部署边缘采集节点。你需将树莓派配置为边缘计算节点，并通过串口与外部设备实现双向通信。 |
| **知识点** | OSI模型、工业现场总线层次、树莓派OS烧录、SSH/VNC、PySerial串口参数（波特率/数据位/停止位/校验位） |
| **技能点** | 树莓派配置、串口通信编程 |
| **素质点** | IT与OT融合的工业互联网使命，电气安全规范 |

### ② 任务计划
1. 烧录RaspberryPi OS，配置SSH/VNC远程连接；
2. 搭建Python环境，安装pyserial；
3. 通过USB-TTL实现PC↔树莓派双向收发。

### ③ 方案决策
- 波特率、数据位、停止位如何与对端匹配？不匹配会怎样？
- 串口设备号（/dev/ttyUSB0）如何识别？

### ④ 任务实施（分层任务）
```python
import serial

# 【B层】打开串口
ser = serial.Serial(
    port='/dev/ttyUSB0', baudrate=9600,
    bytesize=8, stopbits=1, parity='N', timeout=1
)
# 发送
ser.write(b'Hello Device\n')
# 接收
data = ser.readline()
print("收到:", data.decode('utf-8', errors='ignore'))
ser.close()
```

### ⑤ 检查验收
| 检查项 | 标准 | 自检 |
|---|---|---|
| 树莓派 | SSH/VNC可连接 | □ |
| 串口参数 | 双方一致 | □ |
| 双向通信 | 收发正常 | □ |

### ⑥ 评价反思
- **交付物**：串口通信脚本 + 通信验证截图
- **反思**：接线前为何要断电、防静电？

---

## 工单 WO-1-02　《Modbus RTU协议解析与温湿度采集》

**建议学时：** 2　　**难度：** ★★★★☆

### ① 任务资讯
| 项目 | 内容 |
|---|---|
| **任务场景** | 产线部署了RS485温湿度传感器（SHT20），需通过Modbus RTU协议读取其寄存器并转换为温度、湿度物理量。 |
| **知识点** | Modbus RTU帧结构（从机地址/功能码/寄存器地址/CRC）、FC03读保持寄存器、大端序解析 |
| **技能点** | Modbus帧构建与解析、物理量换算 |
| **素质点** | 严谨的协议规范意识 |

### ② 任务计划
1. 构建FC03读保持寄存器请求帧；
2. 接收并解析响应帧（大端序）；
3. 将原始值换算为温度℃/湿度%RH。

### ③ 方案决策
- 使用原生struct手动解析还是minimalmodbus库？
- CRC校验如何验证数据完整性？

### ④ 任务实施（分层任务）
```python
# 【B层】使用minimalmodbus
import minimalmodbus

instr = minimalmodbus.Instrument('/dev/ttyUSB0', 1)  # 从机地址1
instr.serial.baudrate = 9600

# FC03读保持寄存器: 温度寄存器0x0001, 湿度0x0002
temp = instr.read_register(1, 1, functioncode=3)  # 1位小数
humidity = instr.read_register(2, 1, functioncode=3)
print(f"温度: {temp}℃, 湿度: {humidity}%RH")

# 【A层拓展】手动CRC校验与大端解析(struct)
```

### ⑤ 检查验收
| 检查项 | 标准 | 自检 |
|---|---|---|
| 请求帧 | 功能码/地址正确 | □ |
| 响应解析 | 大端序换算正确 | □ |
| 物理量 | 温湿度合理 | □ |

### ⑥ 评价反思
- **交付物**：Modbus采集脚本 + 数据解析日志
- **反思**：为何工业寄存器多采用大端序？

---

## 工单 WO-1-03　《MQTT Broker搭建与发布订阅》

**建议学时：** 2　　**难度：** ★★★☆☆

### ① 任务资讯
| 项目 | 内容 |
|---|---|
| **任务场景** | 采集到的数据需上传云端。你需搭建MQTT消息中间件，设计规范的Topic并实现设备数据的发布与订阅。 |
| **知识点** | 发布/订阅模型、QoS 0/1/2、Topic分层设计、通配符（+/#）、遗嘱消息LWT |
| **技能点** | Mosquitto部署、paho-mqtt发布订阅编程 |
| **素质点** | 工业数据安全意识（认证、加密） |

### ② 任务计划
1. 树莓派部署Mosquitto Broker；
2. 设计Topic：`factory/workshop1/CNC-001/temperature`；
3. 用paho-mqtt编写发布端与订阅端，验证QoS1。

### ③ 方案决策
- QoS等级选型：温度数据用QoS1（至少一次）保证可靠。
- 生产环境是否需启用TLS+用户名密码？（是，端口8883）

### ④ 任务实施（分层任务）
```python
# publisher.py 【B层】
import paho.mqtt.client as mqtt
import json, time

client = mqtt.Client("sensor_pub")
client.connect("localhost", 1883)
payload = json.dumps({"device": "CNC-001", "temp": 65.5,
                      "timestamp": time.time()})
client.publish("factory/workshop1/CNC-001/temperature", payload, qos=1)

# subscriber.py 【A层】通配符订阅+遗嘱消息
def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")
sub = mqtt.Client("monitor")
sub.on_message = on_message
sub.connect("localhost", 1883)
sub.subscribe("factory/+/+/temperature", qos=1)
sub.loop_forever()
```

### ⑤ 检查验收
| 检查项 | 标准 | 自检 |
|---|---|---|
| Broker | Mosquitto运行 | □ |
| 发布订阅 | 消息互通 | □ |
| Topic设计 | 分层规范 | □ |
| QoS1 | 可靠投递 | □ |

### ⑥ 评价反思
- **交付物**：MQTT发布/订阅脚本 + Broker配置截图
- **反思**：为何生产环境禁止匿名连接？

---

## 工单 WO-1-04　《多传感器数据采集脚本集成》

**建议学时：** 2　　**难度：** ★★★★☆

### ① 任务资讯
| 项目 | 内容 |
|---|---|
| **任务场景** | 现场有温湿度、光照、CO₂多个传感器，需将采集、解析、发布整合为统一脚本，并用多线程提高采集效率。 |
| **知识点** | 模块整合、多线程threading、JSON Payload规范（含timestamp）、轮询采集 |
| **技能点** | 多模块集成、多线程并行 |
| **素质点** | 统一数据规范的工程习惯 |

### ② 任务计划
1. 整合PySerial+Modbus+MQTT三模块；
2. 多传感器轮询采集；
3. 多线程并行采集与发布。

### ③ 方案决策
- 单线程轮询 vs 多线程并行的效率差异？
- JSON Payload字段如何标准化？

### ④ 任务实施（分层任务）
```python
import threading, json, time
import paho.mqtt.client as mqtt

client = mqtt.Client("multi_collector")
client.connect("localhost", 1883)

def collect_publish(sensor_name, topic, read_func):
    while True:
        value = read_func()  # 读取传感器
        payload = json.dumps({
            "sensor": sensor_name, "value": value,
            "timestamp": time.time()
        })
        client.publish(topic, payload, qos=1)
        time.sleep(1)

# 【A层】多线程启动多传感器
sensors = [
    ("temp", "factory/w1/temp", lambda: 65.5),
    ("light", "factory/w1/light", lambda: 800),
    ("co2", "factory/w1/co2", lambda: 420),
]
for name, topic, func in sensors:
    threading.Thread(target=collect_publish,
                     args=(name, topic, func), daemon=True).start()
```

### ⑤ 检查验收
| 检查项 | 标准 | 自检 |
|---|---|---|
| 三模块集成 | 数据管道通畅 | □ |
| 多传感器 | 全部采集 | □ |
| 多线程 | 并行发布 | □ |
| JSON规范 | 含timestamp | □ |

### ⑥ 评价反思
- **交付物**：集成采集脚本 + 多传感器数据日志
- **反思**：多线程采集需注意哪些资源竞争问题？

---

## 工单 WO-1-05　《数据上云与端到端通信联调》

**建议学时：** 2　　**难度：** ★★★★☆　　**里程碑：** M1

### ① 任务资讯
| 项目 | 内容 |
|---|---|
| **任务场景** | 完成从传感器到云端的全链路打通，实现工业级健壮性（断线重连、超时处理），并验证延迟与完整性。 |
| **知识点** | 端-边-云数据流、断线重连（reconnect_delay）、超时重试、数据校验 |
| **技能点** | 全链路联调、健壮性编程、性能优化 |
| **素质点** | 系统集成与全链路质量意识 |

### ② 任务计划
1. 联调：传感器→树莓派→采集脚本→MQTT Broker→监控终端；
2. 实现断线重连与超时重试；
3. 验证延迟≤100ms，编写端到端测试报告。

### ③ 方案决策
- 如何将5传感器轮询由500ms优化至100ms内？（多线程并行）
- 断线后如何自动恢复？

### ④ 任务实施（分层任务）
```python
import paho.mqtt.client as mqtt

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("意外断开,尝试重连...")
        while True:
            try:
                client.reconnect()
                break
            except:
                time.sleep(2)

client = mqtt.Client("edge_gateway")
client.on_disconnect = on_disconnect
client.reconnect_delay_set(min_delay=1, max_delay=30)
client.connect("cloud-broker", 1883)
client.loop_start()
# 【A层】统计延迟与丢包率，生成测试报告
```

### ⑤ 检查验收
| 检查项 | 标准 | 自检 |
|---|---|---|
| 全链路 | 端到端贯通 | □ |
| 延迟 | ≤100ms | □ |
| 断线重连 | 自动恢复 | □ |
| 完整性 | 无丢包 | □ |

### ⑥ 评价反思
- **交付物**：端到端采集脚本 + 测试报告（含延迟/丢包）+ 系统架构图（里程碑M1）
- **反思**：工业级健壮性编程为何如此重要？

---
---

# 模块2　数据分析与可视化

---

## 工单 WO-2-01　《工业数据集导入与Pandas清洗》

**建议学时：** 2　　**难度：** ★★★☆☆

### ① 任务资讯
| 项目 | 内容 |
|---|---|
| **任务场景** | 拿到某工厂注塑机运行日志CSV（含缺失值、异常值），需清洗后才能分析。 |
| **知识点** | Pandas DataFrame、read_csv、缺失值填充（ffill）、异常值过滤（3σ法则）、类型转换、标准化 |
| **技能点** | 数据清洗三板斧 |
| **素质点** | "先清洗后分析"的数据工程习惯 |

### ② 任务计划
1. read_csv导入日志；
2. 缺失值ffill前向填充；
3. 3σ法则过滤异常值。

### ③ 方案决策
- 传感器缺失值为何优先ffill而非均值填充？（符合物理连续性）
- 3σ阈值如何确定？

### ④ 任务实施（分层任务）
```python
import pandas as pd

df = pd.read_csv("injection_log.csv", parse_dates=["timestamp"])
# 【B层】缺失值前向填充
df["temperature"] = df["temperature"].ffill()
# 类型转换
df["device_id"] = df["device_id"].astype("category")

# 【A层】3σ法则过滤异常值
mean, std = df["temperature"].mean(), df["temperature"].std()
df = df[(df["temperature"] > mean - 3*std) &
        (df["temperature"] < mean + 3*std)]
print(df.describe())
```

### ⑤ 检查验收
| 检查项 | 标准 | 自检 |
|---|---|---|
| 数据导入 | 成功读取 | □ |
| 缺失值 | ffill填充 | □ |
| 异常值 | 3σ过滤 | □ |

### ⑥ 评价反思
- **交付物**：数据清洗脚本 + 清洗前后对比统计报告
- **反思**：为何说"特征决定模型上限"？

---

## 工单 WO-2-02　《OEE等多维指标计算与统计分析》

**建议学时：** 2　　**难度：** ★★★☆☆

### ① 任务资讯
| 项目 | 内容 |
|---|---|
| **任务场景** | 管理层需按产线、班次统计OEE、MTBF、MTTR、良品率等KPI。 |
| **知识点** | GroupBy分组聚合、OEE/MTBF/MTTR/良品率公式、跨夜班次日期处理 |
| **技能点** | 多维聚合、KPI计算 |
| **素质点** | 让数据创造价值的数字化意识 |

### ② 任务计划
1. GroupBy按产线/班次分组；
2. 计算各维度KPI；
3. 输出统计摘要。

### ③ 方案决策
- 跨夜班次（22:00-06:00）如何避免日期分组错位？
- MTBF=运行时间/故障次数，MTTR=维修时间/故障次数。

### ④ 任务实施（分层任务）
```python
import pandas as pd

# 【B层】按产线分组计算KPI
kpi = df.groupby("line").agg(
    total_output=("output", "sum"),
    good_output=("good", "sum"),
    fault_count=("fault", "sum"),
    run_time=("run_time", "sum"),
    repair_time=("repair_time", "sum"),
)
kpi["yield_rate"] = kpi["good_output"] / kpi["total_output"]
kpi["MTBF"] = kpi["run_time"] / kpi["fault_count"]
kpi["MTTR"] = kpi["repair_time"] / kpi["fault_count"]
print(kpi)
# 【A层】处理跨夜班次: 用shift调整日期归属
```

### ⑤ 检查验收
| 检查项 | 标准 | 自检 |
|---|---|---|
| GroupBy | 分组正确 | □ |
| KPI公式 | 计算准确 | □ |
| 跨夜班次 | 无错位 | □ |

### ⑥ 评价反思
- **交付物**：指标计算脚本 + 统计分析汇总表
- **反思**：世界级制造OEE≥85%意味着什么？

---

## 工单 WO-2-03　《Pyecharts工业图表开发实战》

**建议学时：** 2　　**难度：** ★★★☆☆

### ① 任务资讯
| 项目 | 内容 |
|---|---|
| **任务场景** | 需将KPI数据可视化，开发折线图、柱状图、仪表盘、热力图四类工业图表。 |
| **知识点** | Pyecharts图表类型、工业配色规范（交通灯语义）、目标线标注 |
| **技能点** | 图表开发、配色设计 |
| **素质点** | 以人为本的"3秒规则"看板设计理念 |

### ② 任务计划
1. 折线图（OEE趋势）、柱状图（产线对比）；
2. 仪表盘（实时KPI）、热力图（设备状态）；
3. 应用交通灯配色（红<60%/黄60-80%/绿≥80%）。

### ③ 方案决策
- 不同数据适配什么图表？（趋势→折线，对比→柱状，单值→仪表盘，矩阵→热力图）

### ④ 任务实施（分层任务）
```python
from pyecharts.charts import Line, Gauge
from pyecharts import options as opts

# 【B层】OEE趋势折线图
line = (Line()
    .add_xaxis(["周一","周二","周三","周四","周五"])
    .add_yaxis("OEE", [82, 85, 78, 88, 90],
               markline_opts=opts.MarkLineOpts(
                   data=[opts.MarkLineItem(y=85, name="目标线")]))
    .set_global_opts(title_opts=opts.TitleOpts(title="OEE趋势")))
line.render("oee_trend.html")

# 【A层】仪表盘(交通灯分段配色)
gauge = (Gauge()
    .add("OEE", [("综合效率", 85)],
         axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(
             color=[(0.6,"#f00"),(0.8,"#ff0"),(1,"#0f0")], width=30))))
gauge.render("oee_gauge.html")
```

### ⑤ 检查验收
| 检查项 | 标准 | 自检 |
|---|---|---|
| 四类图表 | 全部生成 | □ |
| 配色 | 交通灯语义 | □ |
| 目标线 | 正确标注 | □ |

### ⑥ 评价反思
- **交付物**：4类工业图表HTML文件 + 源码
- **反思**：为何工业看板要遵循"3秒规则"？

---

## 工单 WO-2-04　《厂级数据监控Dashboard集成》

**建议学时：** 2　　**难度：** ★★★★☆

### ① 任务资讯
| 项目 | 内容 |
|---|---|
| **任务场景** | 将多个图表整合为一个厂级监控大屏Dashboard，并实现实时数据刷新。 |
| **知识点** | Pyecharts Page组件、Dashboard布局、实时刷新机制（订阅→缓存→渲染→推送） |
| **技能点** | 多图表集成、实时刷新 |
| **素质点** | 面向决策的数据服务意识 |

### ② 任务计划
1. Page组件整合多图表；
2. 设计Dashboard布局；
3. 实现MQTT订阅→Pandas缓存→图表再生成→Flask推送。

### ③ 方案决策
- Page布局用SimplePageLayout还是DraggablePageLayout？
- 刷新频率如何设置？

### ④ 任务实施（分层任务）
```python
from pyecharts.charts import Page

# 【B层】多图表集成
page = Page(layout=Page.SimplePageLayout)
page.add(line_chart, bar_chart, gauge_chart, heatmap_chart)
page.render("dashboard.html")

# 【A层】Flask实时推送
from flask import Flask, render_template_string
app = Flask(__name__)
@app.route("/")
def dashboard():
    # 从MQTT缓存读取最新数据,重新渲染
    return open("dashboard.html").read()
```

### ⑤ 检查验收
| 检查项   | 标准             | 自检 |
| -------- | ---------------- | ---- |
| 集成     | 多图表整合为单页 | □    |
| 布局     | 合理美观         | □    |
| 实时刷新 | 数据自动更新     | □    |

### ⑥ 评价反思

- **交付物**：集成Dashboard HTML + 自动刷新配置
- **反思**：实时刷新链路中，缓存层的作用是什么？

------

## 工单 WO-2-05　《自动化报表生成与数据洞察报告》

**建议学时：** 2　　**难度：** ★★★☆☆　　**里程碑：** M2

### ① 任务资讯

| 项目         | 内容                                                         |
| ------------ | ------------------------------------------------------------ |
| **任务场景** | 管理层需要每周自动收到一份含OEE趋势图与KPI汇总的Excel周报，并通过邮件推送。你还需基于数据撰写生产洞察报告。 |
| **知识点**   | OpenPyXL Excel生成、图表嵌入、SMTP邮件推送、定时任务、数据洞察表达 |
| **技能点**   | 自动化报表、邮件推送、洞察分析                               |
| **素质点**   | 自动化标准化交付习惯、绿色智造思政                           |

### ② 任务计划

1. OpenPyXL生成含OEE趋势图+KPI汇总表的Excel周报；
2. SMTP定时推送邮件；
3. 撰写工厂数据分析洞察报告。

### ③ 方案决策

- 报表模板如何设计便于阅读？
- 洞察报告应聚焦哪些价值点（能耗异常、生产节拍优化）？

### ④ 任务实施（分层任务）

```python
import openpyxl
from openpyxl.chart import LineChart, Reference
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 【B层】生成Excel周报
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "周报KPI"
ws.append(["日期", "OEE", "产量", "良品率"])
for row in weekly_data:
    ws.append(row)

# 嵌入OEE趋势折线图
chart = LineChart()
chart.title = "OEE周趋势"
data = Reference(ws, min_col=2, min_row=1, max_row=8)
chart.add_data(data, titles_from_data=True)
ws.add_chart(chart, "F2")
wb.save("weekly_report.xlsx")

# 【A层】SMTP邮件推送
def send_report(to_addr, file_path):
    msg = MIMEMultipart()
    msg["Subject"] = "工厂生产周报"
    msg["From"] = "report@factory.com"
    msg["To"] = to_addr
    with open(file_path, "rb") as f:
        attach = MIMEApplication(f.read())
        attach.add_header("Content-Disposition", "attachment",
                          filename="weekly_report.xlsx")
        msg.attach(attach)
    with smtplib.SMTP_SSL("smtp.factory.com", 465) as server:
        server.login("report@factory.com", "password")
        server.send_message(msg)
```

### ⑤ 检查验收

| 检查项    | 标准          | 自检 |
| --------- | ------------- | ---- |
| Excel报表 | 图表+表格生成 | □    |
| 邮件推送  | 附件成功送达  | □    |
| 洞察报告  | 有价值发现    | □    |

### ⑥ 评价反思

- **交付物**：自动报表脚本 + 周报Excel样本 + 数据洞察报告（PDF，里程碑M2）
- **反思**：发现能耗异常对碳达峰碳中和有何意义？

------

------

# 模块3　机器学习与预测维护

------

## 工单 WO-3-01　《工业数据集探索与预处理》

**建议学时：** 2　　**难度：** ★★★☆☆

### ① 任务资讯

| 项目         | 内容                                                         |
| ------------ | ------------------------------------------------------------ |
| **任务场景** | 拿到凯斯西储大学（CWRU）轴承故障数据集，需完成探索性分析与预处理，为建模做准备。 |
| **知识点**   | 数据概览、质量检查、缺失值处理、标签编码（LabelEncoder）、归一化（StandardScaler）、train_test_split |
| **技能点**   | 数据预处理全流程                                             |
| **素质点**   | 数据质量校核的严谨科研习惯                                   |

### ② 任务计划

1. 导入CWRU数据集，概览质量；
2. 标签编码、归一化；
3. 分层划分训练集/测试集。

### ③ 方案决策

- 归一化为何对SVM性能提升显著？
- 划分为何要分层（stratify）保持各类故障均衡？

### ④ 任务实施（分层任务）

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# 【B层】数据探索
df = pd.read_csv("cwru_bearing.csv")
print(df.info(), df["fault_type"].value_counts())

# 标签编码
le = LabelEncoder()
df["label"] = le.fit_transform(df["fault_type"])

# 【A层】归一化 + 分层划分
X = df.drop(["fault_type", "label"], axis=1)
y = df["label"]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, stratify=y, random_state=42)
```

### ⑤ 检查验收

| 检查项   | 标准         | 自检 |
| -------- | ------------ | ---- |
| 数据探索 | 质量报告完整 | □    |
| 标签编码 | 类别→数值    | □    |
| 归一化   | 标准化完成   | □    |
| 分层划分 | 各类均衡     | □    |

### ⑥ 评价反思

- **交付物**：数据预处理脚本 + 数据质量报告
- **反思**：训练集测试集比例为何常用8:2？

------

## 工单 WO-3-02　《时频域特征提取与可视化分析》

**建议学时：** 2　　**难度：** ★★★★☆

### ① 任务资讯

| 项目         | 内容                                                         |
| ------------ | ------------------------------------------------------------ |
| **任务场景** | 原始振动信号需提取有区分度的特征。你需从时域、频域提取10维特征并可视化分析。 |
| **知识点**   | 时域6维（均值/标准差/峰值/峰度/波峰因子/均方根）、频域4维（FFT主频/频率中心/均方频率/故障频带能量比）、FFT |
| **技能点**   | 特征工程、FFT频谱分析、可视化                                |
| **素质点**   | "特征决定模型上限"的数据科学认知                             |

### ② 任务计划

1. 提取时域6维统计特征；
2. FFT提取频域4维特征；
3. Matplotlib绘制波形、频谱、特征分布图。

### ③ 方案决策

- 为何峰度对轴承早期故障最敏感？
- 时域与频域特征各捕捉什么故障信息？

### ④ 任务实施（分层任务）

```python
import numpy as np
from scipy.stats import kurtosis
from scipy.fft import fft

# 【B层】时域特征
def time_features(signal):
    return {
        "mean": np.mean(signal),
        "std": np.std(signal),
        "peak": np.max(np.abs(signal)),
        "kurtosis": kurtosis(signal),      # 峰度-早期故障敏感
        "rms": np.sqrt(np.mean(signal**2)),
        "crest_factor": np.max(np.abs(signal)) / np.sqrt(np.mean(signal**2)),
    }

# 【A层】频域特征(FFT)
def freq_features(signal, fs=12000):
    n = len(signal)
    fft_vals = np.abs(fft(signal))[:n//2]
    freqs = np.fft.fftfreq(n, 1/fs)[:n//2]
    main_freq = freqs[np.argmax(fft_vals)]
    freq_center = np.sum(freqs * fft_vals) / np.sum(fft_vals)
    return {"main_freq": main_freq, "freq_center": freq_center}
```

### ⑤ 检查验收

| 检查项   | 标准        | 自检 |
| -------- | ----------- | ---- |
| 时域特征 | 6维正确     | □    |
| 频域特征 | FFT主频合理 | □    |
| 可视化   | 波形+频谱图 | □    |

### ⑥ 评价反思

- **交付物**：特征提取模块 + 可视化分析图表
- **反思**：正常与故障信号在频谱上有何区别？

------

## 工单 WO-3-03　《SVM/随机森林模型训练与调优》

**建议学时：** 2　　**难度：** ★★★★☆

### ① 任务资讯

| 项目         | 内容                                                         |
| ------------ | ------------------------------------------------------------ |
| **任务场景** | 用提取的特征训练故障分类模型。你需训练SVM与随机森林两类模型并调优超参数。 |
| **知识点**   | SVM（C/kernel/gamma）、随机森林（n_estimators/max_depth）、GridSearchCV、StratifiedKFold交叉验证 |
| **技能点**   | 模型训练、超参数调优                                         |
| **素质点**   | 用数据说话的科学态度                                         |

### ② 任务计划

1. 训练SVM与随机森林；
2. GridSearchCV 5折交叉验证调参；
3. 记录最优参数。

### ③ 方案决策

- 调参策略：先粗后细，先定大范围再细化。
- n_jobs=-1并行加速的作用？

### ④ 任务实施（分层任务）

```python
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, StratifiedKFold

cv = StratifiedKFold(n_splits=5)

# 【B层】SVM调优
svm_grid = GridSearchCV(SVC(),
    {"C": [0.1, 1, 10], "kernel": ["rbf"], "gamma": ["scale", 0.1]},
    cv=cv, scoring="f1_weighted", n_jobs=-1)
svm_grid.fit(X_train, y_train)
print("SVM最优:", svm_grid.best_params_, svm_grid.best_score_)

# 【A层】随机森林调优
rf_grid = GridSearchCV(RandomForestClassifier(random_state=42),
    {"n_estimators": [50, 100, 200], "max_depth": [10, 20, None]},
    cv=cv, scoring="f1_weighted", n_jobs=-1)
rf_grid.fit(X_train, y_train)
print("RF最优:", rf_grid.best_params_, rf_grid.best_score_)
```

### ⑤ 检查验收

| 检查项   | 标准         | 自检 |
| -------- | ------------ | ---- |
| 双模型   | 均训练成功   | □    |
| 网格搜索 | 参数网格合理 | □    |
| 交叉验证 | 5折验证      | □    |
| 最优记录 | 参数已保存   | □    |

### ⑥ 评价反思

- **交付物**：模型训练脚本 + 最优参数记录
- **反思**：随机森林为何通常优于SVM约3%？

------

## 工单 WO-3-04　《模型评估、对比分析与报告》

**建议学时：** 2　　**难度：** ★★★☆☆

### ① 任务资讯

| 项目         | 内容                                                     |
| ------------ | -------------------------------------------------------- |
| **任务场景** | 需客观评估并对比两个模型的性能，为部署选型提供依据。     |
| **知识点**   | 混淆矩阵、准确率/精确率/召回率/F1-Score、ROC曲线、加权F1 |
| **技能点**   | 模型评估、多维对比                                       |
| **素质点**   | "宁可误报勿漏报"的安全责任意识                           |

### ② 任务计划

1. 计算混淆矩阵与各项指标；
2. 绘制ROC曲线；
3. 对比SVM vs RF，撰写评估报告。

### ③ 方案决策

- 工业场景为何Recall（召回率）优先？（漏报FN代价 > 误报FP）
- 加权F1为何是多分类的合理指标？

### ④ 任务实施（分层任务）

```python
from sklearn.metrics import (confusion_matrix, classification_report,
                             ConfusionMatrixDisplay)
import matplotlib.pyplot as plt

# 【B层】评估最优模型
best_rf = rf_grid.best_estimator_
y_pred = best_rf.predict(X_test)
print(classification_report(y_test, y_pred))

# 混淆矩阵可视化
cm = confusion_matrix(y_test, y_pred)
ConfusionMatrixDisplay(cm).plot()
plt.savefig("confusion_matrix.png")

# 【A层】双模型加权F1对比
from sklearn.metrics import f1_score
svm_f1 = f1_score(y_test, svm_grid.predict(X_test), average="weighted")
rf_f1 = f1_score(y_test, y_pred, average="weighted")
print(f"SVM加权F1={svm_f1:.3f}, RF加权F1={rf_f1:.3f}")
```

### ⑤ 检查验收

| 检查项   | 标准        | 自检 |
| -------- | ----------- | ---- |
| 混淆矩阵 | 正确绘制    | □    |
| 评估指标 | 全部计算    | □    |
| 加权F1   | ≥0.88验收线 | □    |
| 对比报告 | 结论明确    | □    |

### ⑥ 评价反思

- **交付物**：评估图表 + 模型对比分析报告
- **反思**：为什么工业中漏报比误报更危险？

------

## 工单 WO-3-05　《模型持久化与推理服务部署》

**建议学时：** 2　　**难度：** ★★★★☆　　**里程碑：** M3

### ① 任务资讯

| 项目         | 内容                                                         |
| ------------ | ------------------------------------------------------------ |
| **任务场景** | 将训练好的最优模型部署为可调用的推理服务，供其他系统实时诊断故障。 |
| **知识点**   | pickle/joblib序列化、版本号命名、Flask推理API、JSON接口、响应时间优化 |
| **技能点**   | 模型持久化、API部署、接口测试                                |
| **素质点**   | 从算法到工程服务的落地交付意识                               |

### ② 任务计划

1. joblib持久化最优模型（rf_v1.2.pkl）；
2. Flask构建POST /predict接口；
3. Postman/cURL测试，验证响应≤100ms。

### ③ 方案决策

- 为何用joblib+版本号命名保证可复现？
- 数据漂移F1下降>5%时如何触发重训练？

### ④ 任务实施（分层任务）

```python
import joblib
from flask import Flask, request, jsonify

# 【B层】持久化
joblib.dump(best_rf, "rf_v1.2.pkl")
joblib.dump(scaler, "scaler_v1.2.pkl")

# 【A层】Flask推理API
app = Flask(__name__)
model = joblib.load("rf_v1.2.pkl")
scaler = joblib.load("scaler_v1.2.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = request.json["features"]  # 10维特征
        X = scaler.transform([features])
        pred = model.predict(X)[0]
        proba = model.predict_proba(X).max()
        return jsonify({"fault_type": int(pred),
                        "confidence": round(float(proba), 3)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### ⑤ 检查验收

| 检查项   | 标准         | 自检 |
| -------- | ------------ | ---- |
| 持久化   | .pkl文件生成 | □    |
| API      | 正常返回预测 | □    |
| 响应时间 | ≤100ms       | □    |
| 异常处理 | 错误可捕获   | □    |

### ⑥ 评价反思

- **交付物**：模型持久化文件（.pkl）+ Flask推理服务脚本 + API测试截图（里程碑M3）
- **反思**：模型上线后如何持续监控性能？

------

------

# 模块4　综合项目实战与答辩

------

## 工单 WO-4-01　《需求分析与系统架构设计》

**建议学时：** 2　　**难度：** ★★★★☆

### ① 任务资讯

| 项目         | 内容                                                         |
| ------------ | ------------------------------------------------------------ |
| **任务场景** | 项目小组承接一个工业AIoT系统开发（微型产线监测/能耗异常检测/设备健康管理三选一），首先需完成需求分析与架构设计。 |
| **知识点**   | 端-边-云三层架构、技术选型、架构四原则（边缘优先/松耦合/安全第一/可观测性）、需求规格说明书 |
| **技能点**   | 需求分析、架构设计、WBS分解                                  |
| **素质点**   | 安全第一的系统设计责任、国家工业互联网战略认知               |

### ② 任务计划

1. 组建3人小组，选题；
2. 阅读需求文档，梳理功能清单；
3. 绘制端-边-云架构图，制定WBS与甘特图。

### ③ 方案决策

- 各功能应放在端、边还是云层？（边缘优先原则）
- 关键组件选型（Broker/数据库/框架）及理由？

### ④ 任务实施（分层任务）

- **【A层】** 担任架构师，完成技术选型决策矩阵与架构论证；
- **【B层】** 绘制系统架构图（Draw.io）；
- **【C/D层】** 编写功能清单、约束条件、WBS任务分解。

**架构图要素：** 感知层（传感器）→ 边缘层（树莓派采集/预处理/本地推理）→ 云层（Broker/数据库/Dashboard/模型服务）。

### ⑤ 检查验收

| 检查项   | 标准         | 自检 |
| -------- | ------------ | ---- |
| 需求分析 | 功能清单完整 | □    |
| 架构图   | 三层清晰     | □    |
| 技术选型 | 论证充分     | □    |
| WBS      | 任务分解合理 | □    |

### ⑥ 评价反思

- **交付物**：《系统需求规格说明书》+ 架构设计图（Draw.io）+ WBS甘特图
- **反思**：边缘优先原则对降低云端负载有何意义？

------

## 工单 WO-4-02　《数据采集与通信模块集成》

**建议学时：** 2　　**难度：** ★★★★☆

### ① 任务资讯

| 项目         | 内容                                                         |
| ------------ | ------------------------------------------------------------ |
| **任务场景** | 项目进入开发阶段，首先集成数据采集与通信模块，构建稳定的数据管道。 |
| **知识点**   | Modbus采集、MQTT发布、数据包格式、传输稳定性、抓包验证       |
| **技能点**   | 模块集成、数据管道构建、Git协作                              |
| **素质点**   | 模块化协作的工程化职业习惯                                   |

### ② 任务计划

1. 复用模块1脚本，配置树莓派Modbus采集；
2. 编写MQTT发布脚本；
3. 抓包验证数据链路稳定性。

### ③ 方案决策

- 数据包格式如何统一（JSON schema）？
- 如何验证传输稳定性（丢包率、延迟）？

### ④ 任务实施（分层任务）

- **【A/B层】** 复用WO-1系列组件，集成为项目采集子系统；
- **【C/D层】** 使用Wireshark/mosquitto_sub抓包验证，记录数据日志。

```python
# 项目采集子系统(复用+集成)
import json, time
import minimalmodbus, paho.mqtt.client as mqtt

instr = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
instr.serial.baudrate = 9600
client = mqtt.Client("project_collector")
client.connect("cloud-broker", 1883)

while True:
    temp = instr.read_register(1, 1, functioncode=3)
    payload = json.dumps({"device": "LINE-01", "temp": temp,
                          "timestamp": time.time()})
    client.publish("project/line01/temp", payload, qos=1)
    time.sleep(1)
```

### ⑤ 检查验收

| 检查项 | 标准           | 自检 |
| ------ | -------------- | ---- |
| 采集   | Modbus读取正常 | □    |
| 发布   | MQTT稳定传输   | □    |
| 抓包   | 数据链路验证   | □    |
| Git    | 规范提交       | □    |

### ⑥ 评价反思

- **交付物**：数据采集脚本 + MQTT Broker配置记录 + 抓包验证截图
- **反思**：复用已验证组件体现了什么工程思想？

------

## 工单 WO-4-03　《数据分析看板与ML模型对接》

**建议学时：** 2　　**难度：** ★★★★☆

### ① 任务资讯

| 项目         | 内容                                                         |
| ------------ | ------------------------------------------------------------ |
| **任务场景** | 将采集数据接入分析与展示层，并集成故障预测模型实现在线诊断报警。 |
| **知识点**   | Pandas处理管道、Pyecharts实时Dashboard、模型调用、阈值报警、松耦合对接 |
| **技能点**   | 分析看板对接、ML集成、全链路联调                             |
| **素质点**   | 系统集成的复合工程能力                                       |

### ② 任务计划

1. 采集数据接入Pandas管道；
2. 构建Pyecharts实时Dashboard；
3. 调用WO-3-05模型实现阈值报警。

### ③ 方案决策

- 各子模块如何松耦合对接（MQTT Topic/文件接口）？
- 报警阈值如何设定？

### ④ 任务实施（分层任务）

- **【A层】** 集成故障预测API，实现在线诊断与报警；
- **【B层】** 构建实时Dashboard；
- **【C/D层】** 数据管道接入与联调记录。

```python
import requests, paho.mqtt.client as mqtt, json

def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    # 调用故障预测API
    resp = requests.post("http://localhost:5000/predict",
                         json={"features": data["features"]})
    result = resp.json()
    if result.get("fault_type", 0) != 0:  # 非正常
        print(f"⚠️报警: 设备{data['device']}检测到故障"
              f"类型{result['fault_type']}, 置信度{result['confidence']}")

sub = mqtt.Client("diagnosis")
sub.on_message = on_message
sub.connect("cloud-broker", 1883)
sub.subscribe("project/+/features", qos=1)
sub.loop_forever()
```

### ⑤ 检查验收

| 检查项    | 标准       | 自检 |
| --------- | ---------- | ---- |
| 数据管道  | 接入成功   | □    |
| Dashboard | 实时展示   | □    |
| 模型对接  | 报警触发   | □    |
| 联调      | 全链路贯通 | □    |

### ⑥ 评价反思

- **交付物**：Dashboard截图 + 模型推理脚本 + 报警日志
- **反思**：松耦合设计对系统维护有何好处？

------

## 工单 WO-4-04　《系统联调、测试与优化》

**建议学时：** 2　　**难度：** ★★★★☆

### ① 任务资讯

| 项目         | 内容                                                         |
| ------------ | ------------------------------------------------------------ |
| **任务场景** | 系统各模块已开发完成，需进行端到端全链路测试、性能优化与Bug修复，确保工业级稳定性。 |
| **知识点**   | 端到端测试、功能测试、压力测试、延迟/丢包率统计、性能优化    |
| **技能点**   | 系统测试、性能调优、Bug修复                                  |
| **素质点**   | 工程交付的闭环质量意识                                       |

### ② 任务计划

1. 端到端全链路测试（采集→传输→分析→展示）；
2. 记录延迟与丢包率，执行压力测试；
3. 修复Bug并优化性能，输出测试报告。

### ③ 方案决策

- 如何定位性能瓶颈？
- 压力测试并发量如何设定？

### ④ 任务实施（分层任务）

- **【A层】** 设计测试用例，执行压力测试，定位并优化瓶颈；
- **【B层】** 执行功能测试，记录延迟/丢包；
- **【C/D层】** 整理测试记录，协助Bug修复。

**测试指标表：**

| 指标       | 目标值 | 实测值 |
| ---------- | ------ | ------ |
| 端到端延迟 | ≤100ms | ___    |
| 丢包率     | <0.1%  | ___    |
| 并发量     | ≥100路 | ___    |
| API响应    | ≤100ms | ___    |

### ⑤ 检查验收

| 检查项     | 标准       | 自检 |
| ---------- | ---------- | ---- |
| 端到端测试 | 全链路通过 | □    |
| 性能指标   | 达标       | □    |
| 压力测试   | 稳定运行   | □    |
| Bug修复    | 记录完整   | □    |

### ⑥ 评价反思

- **交付物**：系统测试报告（含性能指标）+ 优化方案说明 + Bug修复记录
- **反思**：压力测试暴露了哪些设计短板？

------

## 工单 WO-4-05　《技术文档撰写与项目路演答辩》

**建议学时：** 2　　**难度：** ★★★★★　　**里程碑：** M4

### ① 任务资讯

| 项目         | 内容                                                         |
| ------------ | ------------------------------------------------------------ |
| **任务场景** | 项目收官，需汇总标准化技术文档，制作路演材料，面向校企联合评审团进行系统演示与答辩，完成工程交付。 |
| **知识点**   | SDS系统设计文档、API接口文档、部署运维手册、路演PPT、Demo视频、答辩技巧 |
| **技能点**   | 技术文档编写、路演表达、答辩应变                             |
| **素质点**   | 精益求精的工匠精神、团队协作与成果表达、职业荣誉感           |

### ② 任务计划

1. 汇总技术文档包（SDS/API/运维手册）；
2. 制作15分钟路演PPT + Demo视频；
3. 面向评审团答辩（15min路演+10min问答+5min评审）。

### ③ 方案决策

- 路演如何组织逻辑（背景→架构→难点→创新→成效）？
- 技术难点与创新点如何凝练表达？

### ④ 任务实施（分层任务）

- **【A层/项目经理】** 主讲系统架构与技术难点，统筹答辩；
- **【B层】** 演示核心功能Demo；
- **【C层】** 负责技术文档编写与Demo视频录制；
- **【D层】** 负责测试记录与素材整理。

**技术文档包清单：**

1. 系统设计文档（SDS）——架构、模块、数据流；
2. API接口文档——接口定义、参数、示例；
3. 部署运维手册——环境、部署步骤、故障处理。

### ⑤ 检查验收（Rubric评分量表）

| 评审项     | 权重 | 得分 |
| ---------- | ---- | ---- |
| 功能完整性 | 30%  | ___  |
| 技术难度   | 25%  | ___  |
| 文档规范   | 20%  | ___  |
| 答辩表现   | 15%  | ___  |
| 创新性     | 10%  | ___  |

### ⑥ 评价反思

- **交付物**：完整技术文档包（SDS/API/运维手册）+ 路演PPT + Demo视频 + 项目源码仓库（Git）+ 个人学习总结与KSA能力自评表（里程碑M4）
- **反思**：本课程从"零基础第一行代码"到"综合系统交付"，你的KSA能力发生了哪些成长？如何对接1+X证书与未来岗位？

------

------

## 【附录】工单交付物汇总与里程碑对照表

| 工单    | 名称               | 核心交付物          | 里程碑 |
| ------- | ------------------ | ------------------- | ------ |
| WO-0-01 | 零基础第一行代码   | .ipynb + 环境截图   |        |
| WO-0-02 | 变量数据类型控制流 | 状态判断脚本        |        |
| WO-0-03 | 内置数据结构       | 数据结构脚本        |        |
| WO-0-04 | 函数封装模块化     | 函数模块            |        |
| WO-0-05 | OEE计算器          | OEE脚本+笔记本      | **M0** |
| WO-1-01 | 边缘节点串口通信   | 串口脚本            |        |
| WO-1-02 | Modbus RTU采集     | Modbus脚本          |        |
| WO-1-03 | MQTT发布订阅       | MQTT脚本            |        |
| WO-1-04 | 多传感器集成       | 集成采集脚本        |        |
| WO-1-05 | 端到端联调         | 测试报告+架构图     | **M1** |
| WO-2-01 | Pandas清洗         | 清洗脚本+报告       |        |
| WO-2-02 | KPI计算            | 指标脚本+汇总表     |        |
| WO-2-03 | Pyecharts图表      | 4类图表HTML         |        |
| WO-2-04 | Dashboard集成      | Dashboard HTML      |        |
| WO-2-05 | 自动报表           | 报表脚本+洞察报告   | **M2** |
| WO-3-01 | 数据预处理         | 预处理脚本+质量报告 |        |
| WO-3-02 | 特征工程           | 特征模块+图表       |        |
| WO-3-03 | 模型训练调优       | 训练脚本+参数记录   |        |
| WO-3-04 | 模型评估对比       | 评估图表+报告       |        |
| WO-3-05 | 模型部署           | .pkl+推理API        | **M3** |
| WO-4-01 | 需求架构设计       | 需求书+架构图       |        |
| WO-4-02 | 采集通信集成       | 采集脚本+抓包       |        |
| WO-4-03 | 看板ML对接         | Dashboard+报警日志  |        |
| WO-4-04 | 联调测试优化       | 测试报告+优化方案   |        |
| WO-4-05 | 文档与答辩         | 文档包+PPT+源码     | **M4** |

------

*《Python工业互联网应用实战工单集》全25个工单编制完毕。本工单集配合《Python编程基础》课程标准与授课计划表使用，实行ABCD分层任务与双元制六步教学法，对接1+X《工业互联网数据采集与边缘计算》职业技能等级证书。*

**主编：** 宫宇伟　　**审核：** 工业互联网教研室
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
