# 工业互联网应用专业《Python编程基础》课程标准（v2.0）

## 目录

- [一、课程概述](#一课程概述)
- [二、教学目标](#二教学目标)
- [三、教学内容](#三教学内容)
- [四、课程实施保障条件](#四课程实施保障条件)
- [五、学习评价](#五学习评价)

---

## 一、课程概述

### （一）课程基本信息

| 项目           | 内容                                        |
| ------------ | ----------------------------------------- |
| **课程代码**     | B46021001                                 |
| **开课学院**     | 智能控制学院                                    |
| **课程名称**     | Python编程基础                                |
| **面向的职业及岗位** | 工业数据采集技术员、边缘计算运维员、工业网络实施与运维工程师、工业互联网平台运维员 |
| **学分**       | 3                                         |
| **总学时**      | 48                                        |
| **理论学时**     | 24                                        |
| **实习（训）学时**  | 24                                        |
| **授课周数**     | 12周                                       |
| **周学时**      | 4课时/周                                     |
| **开课学期**     | 第一学年第一学期                                  |

### （二）课程性质与定位

《Python编程基础》是工业互联网应用专业的核心基础课程，面向专科一年级新生开设。本课程旨在培养学生扎实的Python程序设计基础，掌握面向对象编程思想，学会应用常用第三方库解决实际问题，为后续数据分析、工业通信、AI应用等课程奠定坚实基础。

**课程定位**：

1. **职业面向**：适配工业互联网四大核心岗位的编程需求
2. **知识结构**：从Python语言基础→面向对象编程→实用第三方库的递进式学习
3. **实践取向**：以工业数据采集、处理、文档生成为真实场景，强调"学中做、做中学"
4. **零基础入门**：面向完全无编程基础的学生，重视概念理解、面向对象思想、工具应用

### （三）关键内容新增说明（v2.0版本）

**相比v1.0的核心改进**：

1. **面向对象编程**（第3-4周融合）：从函数编程升级到类设计、继承、多态、封装的工程实践
2. **常用第三方库**（第8-10周融合）：
   - **jieba**：中文文本分词、关键词提取（设备故障说明解析）
   - **wordcloud**：词云可视化（设备告警频率分析）
   - **Pillow**：图像处理与识别（设备类别识别、故障图片标注）
   - **reportlab**：PDF报告自动生成（工业设备维护报告）

### （四）课程与其他课程的关系

| 序号  | 前续课程    | 相互衔接和关联的知识点、技能点、软硬件工具、标准规范 |
| --- | ------- | -------------------------- |
| 1   | 计算机文化基础 | 计算机系统结构、操作系统、文件管理、网络基础概念   |
| 2   | 数学基础    | 逻辑运算、集合论、统计学基础、线性代数初步      |

| 序号  | 后续课程      | 相互衔接和关联的知识点、技能点、软硬件工具、标准规范                                                      |
| --- | --------- | ------------------------------------------------------------------------------- |
| 1   | AI应用基础    | 知识点：NumPy数组、Pandas数据处理、数据规范化 / 技能点：特征工程、数据清洗、模型输入准备 / 库：scikit-learn、TensorFlow |
| 2   | 计算机网络基础   | 知识点：网络编程（Socket）、HTTP协议、TCP/IP模型 / 技能点：网络抓包分析、网络故障诊断 / 工具：Wireshark、tcpdump     |
| 3   | 工业互联网应用集成 | 知识点：系统集成、数据流程、ETL工程 / 技能点：完整数据管道构建、系统联调测试                                       |

### （五）对接"1+X"证书

- **Python程序设计职业技能等级证书**（中国信息技术教育认证体系）
- **工业互联网应用实践证书**（工信部等行业认证）
- **数据分析师证书**（初级：数据处理与可视化模块）

### （六）课程基本教学理念

1. **项目驱动，真实场景**：围绕工业数据采集、处理、展示的完整任务链设计课程
2. **理实一体，融合教学**：课堂讲解与实训操作同步进行，理论在实践中验证
3. **循序渐进的方法论**：基础语法 → 函数与模块 → 面向对象 → 第三方库应用
4. **代码规范，工程思维**：重视PEP 8规范、注释文档、单元测试等工程实践
5. **协同创新，开放评价**：学生自主探索、小组协作、多维度评价

---

## 二、教学目标

### （一）知识目标

1. **Python语言基础**
   
   - 掌握Python基本语法、数据类型、运算符和表达式
   - 理解控制流（if/for/while）的逻辑结构和应用场景
   - 熟悉函数的定义、调用、参数、返回值

2. **面向对象编程基础**
   
   - 理解类、对象、属性、方法的基本概念
   - 掌握继承、多态、封装的基本原理
   - 理解面向对象设计在工业应用中的价值

3. **数据结构与处理**
   
   - 理解列表、元组、字典、集合等容器的特性
   - 掌握字符串处理、正则表达式的基本用法
   - 了解JSON数据格式的解析与生成

4. **第三方库应用**
   
   - 掌握jieba中文分词与关键词提取
   - 理解wordcloud词云可视化原理
   - 掌握Pillow图像基本操作与处理
   - 了解reportlab PDF报告的自动生成

5. **文件操作与数据持久化**
   
   - 掌握文件I/O操作（读写、追加）
   - 理解数据验证、异常处理、数据清洗的概念
   - 了解数据统计与可视化的基本方法

6. **工业网络通信基础**
   
   - 理解TCP/IP、HTTP、MQTT、Modbus等协议基础
   - 掌握Socket编程基本概念
   - 了解工业数据采集协议的报文结构

### （二）能力目标

1. **编程能力**
   
   - 能够独立编写200-800行规范Python代码
   - 能够设计简单的类，实现继承和多态
   - 能够遵守PEP 8代码规范，编写有效注释和文档字符串

2. **工具应用能力**
   
   - 能够使用jieba进行中文文本处理
   - 能够使用wordcloud生成词云可视化
   - 能够使用Pillow进行图像处理
   - 能够使用reportlab生成自动化报告

3. **数据处理能力**
   
   - 能够进行基本的数据清洗、验证和转换
   - 能够解析JSON/CSV等常见数据格式
   - 能够计算数据的基本统计指标

4. **问题求解能力**
   
   - 能够将实际问题转化为程序逻辑
   - 能够选择合适的数据结构和算法解决问题
   - 能够通过搜索、文档查阅自主学习新知识

5. **工业应用能力**
   
   - 能够编写模拟工业数据采集的Python程序
   - 能够设计工业数据处理流程
   - 能够生成工业应用的数据分析报告

### （三）素质目标

1. **职业素养**
   
   - 培养严谨的代码编写习惯和精益求精的工匠精神
   - 树立安全意识（数据安全、隐私保护）
   - 形成持续学习的意识与能力

2. **创新意识**
   
   - 鼓励学生在项目中创新应用第三方库
   - 激发学生的自主学习与探索精神
   - 培养学生面对复杂问题的分析与创新能力

3. **系统思维**
   
   - 理解对象设计在大型系统中的重要性
   - 认识代码复用与模块化的价值
   - 掌握工程化软件开发的基本思想

---

## 三、教学内容

### （一）模块0：Python编程基础与面向对象（第1-6周，24课时）

#### **任务0.1：环境配置与基本语法（第1周，4课时）**

**学习内容**：Python环境配置、变量、数据类型、运算符、输入输出、代码规范（PEP 8）

**工单项目**：传感器参数初始化程序

---

#### **任务0.2：控制流与程序逻辑（第2-3周，8课时）**

**学习内容**：条件判断（if/elif/else）、循环结构（for/while）、列表推导式、流程优化

**工单项目**：工业传感器数据告警系统

---

#### **任务0.3：函数、模块与面向对象编程（第3-4周，8课时）**

**学习目标**：

- 知识：掌握函数设计、参数传递；理解类、继承、多态、封装的基本概念
- 能力：能够设计可复用的函数；能够设计简单的类；能够进行面向对象建模
- 素质：培养模块化设计思想与对象建模能力

**学习流程**：

**第一部分：函数与模块（1.5课时）**

1. 函数的定义与调用、参数类型、返回值
2. 内置函数与标准库函数
3. 自定义模块与包的组织

**第二部分：面向对象编程基础（2.5课时）**

1. **类与对象的概念**
   
   - 类的定义与对象创建（class关键字、__init__构造方法）
   - 属性与方法的定义与访问
   - self参数的含义

2. **继承与多态**
   
   - 继承的基本概念与语法（单继承）
   - 方法覆盖（override）与方法调用
   - 多态的简单应用

3. **封装与访问控制**
   
   - 私有属性与公有属性（_私有、__强私有）
   - Property装饰器
   - 类变量与实例变量的区别

4. **工业应用案例**
   
   - 设备类的设计（属性：ID、名称、状态；方法：启动、停止、诊断）
   - 传感器类的设计（属性：传感器类型、量程、精度；方法：读取数值、标定）
   - 告警类的设计（属性：告警级别、内容；方法：记录、清除）

**第三部分：高级函数特性（1.5课时）**

1. *args与**kwargs灵活参数
2. Lambda表达式与匿名函数
3. 装饰器基础（简单介绍）
4. 单元测试初步（unittest）

**标准与规范**：

- PEP 257 文档字符串约定
- Google Python 风格指南（函数与类设计章节）

**软硬件工具**：

- JupyterHub / PyCharm IDE
- Python unittest 模块

**典型案例**：

- 案例1：工业设备类库设计，涵盖多个设备类型
- 案例2：继承应用，设计通用设备基类和具体设备子类
- 案例3：多态演示，不同设备类型的通用接口调用

**工单项目0.3**：

- **项目名称**：工业设备对象模型设计
- **需求描述**：设计设备基类和至少3个设备子类（如PLC、变频器、传感器），包含属性、方法、继承关系；编写测试代码演示对象创建、属性访问、方法调用、多态特性
- **验收标准**：
  - 设计≥1个基类+3个子类
  - 实现继承与方法覆盖
  - 演示多态调用
  - 代码规范率≥90%
  - 包含docstring与注释

---

#### **任务0.4：异常处理与调试（第5-6周，8课时）**

**学习目标**：

- 知识：掌握Python异常体系、异常捕获、自定义异常；理解调试与日志的重要性
- 能力：能够编写健壮的错误处理代码；能够使用调试器定位问题；能够记录程序日志
- 素质：培养严谨的代码质量意识

**学习流程**：

1. 异常体系与捕获（try/except/else/finally）
2. 自定义异常与异常链
3. 调试技巧与日志记录（logging模块）
4. 工业应用中的错误处理

**工单项目0.4**：

- **项目名称**：健壮的工业数据采集程序
- **需求描述**：改进之前的数据采集程序，添加完整的异常处理与日志记录；处理至少5种异常，配置日志输出到文件
- **验收标准**：
  - 处理≥5种不同类型的异常
  - 配置logging输出到文件，日志格式清晰
  - 无未捕获异常导致程序崩溃
  - 代码规范率≥90%

---

### （二）模块1：数据结构、第三方库应用与网络编程（第7-12周，24课时）

#### **任务1.1：容器、字符串与正则表达式（第7周，4课时）**

**学习内容**：列表、元组、字典、集合、字符串处理、正则表达式

**工单项目**：工业数据格式转换工具

---

#### **任务1.2：文件操作与第三方库应用（第8-10周，12课时）**

**学习目标**：

- 知识：掌握JSON/CSV处理；掌握jieba、wordcloud、Pillow、reportlab的基本应用
- 能力：能够进行文件数据交换；能够使用第三方库解决实际问题
- 素质：培养工具应用意识

**学习流程**：

**第一部分：文件操作基础（1.5课时）**

- 文件打开、读写、关闭（with语句）
- 文本与二进制文件的区别
- 大文件的流式读取

**第二部分：JSON与CSV处理（1.5课时）**

- JSON数据的序列化与反序列化
- CSV数据的读写
- 数据格式转换

**第三部分：中文文本处理——jieba库（2.5课时）**

1. **jieba基础**
   
   - jieba库的安装与基本分词
   - 简繁体转换
   - 自定义词典与新词识别

2. **应用场景**
   
   - 设备故障说明文本的分词与分析
   - 工业告警信息的关键词提取
   - 故障原因文本的自动标签化

3. **代码实践**
   
   ```python
   import jieba
   import jieba.analyse
   
   # 分词示例
   text = "工业设备发生轴承故障，需要立即进行维护"
   words = jieba.cut(text)
   print(list(words))
   
   # 关键词提取
   keywords = jieba.analyse.extract_tags(text, topK=5)
   print(keywords)
   ```

**第四部分：词云可视化——wordcloud库（1.5课时）**

1. **wordcloud基础**
   
   - wordcloud库的安装与配置
   - 词频统计与词云生成
   - 中文字体配置

2. **应用场景**
   
   - 工业告警频率可视化
   - 设备故障类型分布显示
   - 维护关键词分析结果展示

3. **代码实践**
   
   ```python
   from wordcloud import WordCloud
   import matplotlib.pyplot as plt
   
   # 词云生成
   text = "故障 故障 维护 检查 温度 压力 温度 压力 故障"
   wc = WordCloud(font_path='simhei.ttf', width=800, height=400).generate(text)
   plt.imshow(wc)
   plt.show()
   ```

**第五部分：图像处理——Pillow库（2.5课时）**

1. **Pillow基础**
   
   - Pillow库的安装与图像打开
   - 图像基本属性（尺寸、模式、格式）
   - 图像的显示与保存

2. **图像操作**
   
   - 图像裁剪、缩放、旋转、镜像
   - 图像亮度、对比度、饱和度调整
   - 图像滤镜处理（模糊、锐化）
   - 绘制几何形状与文字标注

3. **应用场景**
   
   - 设备外观图片的批量处理与缩小
   - 故障现象图片的标注与框选
   - 设备拍照的自动旋转与剪裁
   - 故障位置的图片标记

4. **代码实践**
   
   ```python
   from PIL import Image, ImageDraw, ImageFilter
   
   # 图像打开与操作
   img = Image.open('device.jpg')
   img = img.resize((300, 300))
   img = img.filter(ImageFilter.SHARPEN)
   
   # 图像标注
   draw = ImageDraw.Draw(img)
   draw.rectangle([50, 50, 150, 150], outline='red', width=2)
   draw.text((50, 20), 'Fault Area', fill='red')
   
   img.save('marked_device.jpg')
   ```

**第六部分：PDF报告生成——reportlab库（1.5课时）**

1. **reportlab基础**
   
   - reportlab库的安装与基本用法
   - PDF文档的创建与布局
   - 文本、图片、表格的添加

2. **应用场景**
   
   - 设备维护报告的自动生成
   - 采样数据统计报告
   - 故障诊断报告的格式化输出

3. **代码实践**
   
   ```python
   from reportlab.lib.pagesizes import letter
   from reportlab.pdfgen import canvas
   from reportlab.lib import colors
   from reportlab.platypus import Table, TableStyle, Paragraph, SimpleDocTemplate
   from reportlab.lib.styles import getSampleStyleSheet
   
   # 简单PDF生成
   pdf = SimpleDocTemplate("report.pdf", pagesize=letter)
   elements = []
   
   # 添加标题
   style = getSampleStyleSheet()
   title = Paragraph("设备维护报告", style['Title'])
   elements.append(title)
   
   # 添加表格
   data = [['设备ID', '故障类型', '维护时间'],
           ['DEV001', '轴承故障', '2024-08-11']]
   table = Table(data)
   table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke)]))
   elements.append(table)
   
   pdf.build(elements)
   ```

**标准与规范**：

- jieba、wordcloud、Pillow、reportlab官方文档
- Python文件操作最佳实践

**软硬件工具**：

- Python json、csv、jieba、wordcloud、PIL、reportlab库
- 文本编辑器或Excel查看数据文件

**工单项目1.2**：

- **项目名称**：工业设备维护报告自动生成系统
- **需求描述**：
  1. 读取CSV格式的设备故障数据
  2. 使用jieba进行故障描述的分词与关键词提取
  3. 使用wordcloud生成故障类型词云
  4. 使用Pillow标注故障位置图片
  5. 使用reportlab自动生成包含上述内容的PDF维护报告
- **验收标准**：
  - 正确读取并解析CSV数据
  - 使用jieba提取≥3个关键词
  - 生成清晰的wordcloud图片
  - 使用Pillow处理≥2张图片（缩放、旋转、标注任意一个）
  - 生成包含文本、表格、图片的PDF报告
  - 代码规范率≥90%
  - 包含完整的系统说明文档

---

#### **任务1.3：JSON、CSV数据处理（第10-11周，4课时）**

**学习内容**：JSON与CSV数据处理、数据转换、大文件处理

**工单项目**：工业数据文件转换系统

---

#### **任务1.4：网络编程基础（第11周，4课时）**

**学习内容**：网络基础、HTTP请求、Socket编程、工业通信协议初步

**工单项目**：工业数据采集API客户端

- **项目名称**："工业互联网数据采集上报系统"
- **需求描述**：设计完整的数据采集系统，模拟连接Modbus设备（可使用Modbus模拟器），定时采集数据，通过MQTT协议上报到本地或公有云MQTT服务。程序应包含配置文件、异常处理、日志记录、数据验证等功能
- **验收标准**：
  - 正确连接Modbus设备或模拟器
  - 成功读取≥3个不同类型的寄存器
  - 正确发布MQTT消息（至少5条）
  - 处理网络中断与重连
  - 支持配置文件参数化
  - 代码规范率≥90%
  - 包含完整的集成测试与部署说明

---

#### **任务1.5：综合项目（第12周，4课时）**

**综合项目选题**：

**选项1："虚拟产线数据采集与监控系统"**

- 功能：模拟采集5个不同工位的传感器数据，进行实时数据处理、异常检测、上报
- 涉及知识点：文件I/O、数据结构、异常处理、网络通信（HTTP或MQTT）
- 工作量：500-800行代码

**选项2："工业设备参数管理系统"**

- 功能：从JSON配置文件读取设备信息，通过Modbus采集数据，与配置对比验证，异常告警
- 涉及知识点：JSON处理、正则表达式、Modbus通信、异常处理
- 工作量：600-900行代码

**选项3："数据采集与可视化展示"**

- 功能：采集设备数据，存储到CSV，支持数据查询、统计、简单展示
- 涉及知识点：文件I/O、数据结构、CSV处理、函数模块化
- 工作量：400-600行代码

**选项4：设备故障知识库管理系统**

- 功能：管理故障知识库、自动标签化、故障推荐
- 涉及知识点：面向对象、jieba、JSON、正则表达式
- 工作量：600-900行代码

**选项6：完整的工业设备数据处理与报告系统**

- 功能：采集设备数据 → 数据清洗 → 故障分析 → 自动生成报告
- 涉及知识点：文件I/O、面向对象、jieba、Pillow、reportlab
- 工作量：800-1200行代码

**评价标准**：

- 功能完整性：≥80%
- 代码规范性：≥90%（PEP 8）
- 文档完整性：设计文档、使用说明、代码注释
- 创新性：+10-20分加项

---

### （三）教学进度表

| 周次  | 课时  | 模块  | 任务      | 学习内容                  | 工单项目         | 考核方式    |
| --- | --- | --- | ------- | --------------------- | ------------ | ------- |
| 1   | 4   | 0   | 0.1     | Python基础、数据类型、I/O     | 参数初始化        | 代码演示+工单 |
| 2   | 4   | 0   | 0.2     | 条件判断、循环结构             | 告警系统         | 代码演示+工单 |
| 3   | 4   | 0   | 0.2/0.3 | 循环优化、函数基础             | 告警系统         | 代码演示+工单 |
| 4   | 4   | 0   | 0.3     | 面向对象、继承、多态            | 设备模型设计       | 代码演示+工单 |
| 5   | 4   | 0   | 0.3/0.4 | 类设计、异常处理基础            | 设备模型设计       | 代码演示+工单 |
| 6   | 4   | 0   | 0.4     | 异常处理、日志记录             | 健壮采集程序       | 代码演示+工单 |
| 7   | 4   | 1   | 1.1     | 容器、字符串、正则             | 格式转换工具       | 代码演示+工单 |
| 8   | 4   | 1   | 1.2     | 文件I/O、JSON、jieba      | 维护报告系统       | 代码演示+工单 |
| 9   | 4   | 1   | 1.2     | wordcloud、Pillow      | 维护报告系统       | 代码演示+工单 |
| 10  | 4   | 1   | 1.2/1.3 | reportlab、CSV         | 维护报告系统       | 代码演示+工单 |
| 11  | 4   | 1   | 1.3/1.4 | 网络基础、HTTP、Modbus、MQTT | 工业数据采集API客户端 | 代码演示+工单 |
| 12  | 4   | 1   | 1.5     | 综合项目设计实现              | 综合项目答辩       | 项目演示+答辩 |

---

## 四、课程实施保障条件

### （一）实训（实习）条件

1. **硬件条件**
   
   - 计算机教室：≥30台计算机，i5 CPU、8GB内存、256GB SSD
   - 网络条件：≥100Mbps高速网络

2. **软件环境**
   
   - Python 3.9+
   - IDE：JupyterHub 或 PyCharm
   - 必要库：jieba、wordcloud、Pillow、reportlab、requests、pymodbus、paho-mqtt等
   - 版本控制：Git与GitHub

3. **测试与模拟环境**
   
   - Modbus模拟器
   - MQTT Broker（Mosquitto）
   - HTTP API模拟服务

### （二）教学团队

1. **教师要求**
   
   - 教学经验：≥3年Python教学或工业应用经验
   - 技能要求：精通Python、第三方库应用、对象设计；具备工业应用背景
   - 专业发展：参加≥40小时/年的培训

2. **教学支持**
   
   - 校内IT部门技术支持
   - 企业导师参与案例设计与答辩评审

### （三）学习资源

1. **教材与参考书**
   
   - 《Python从入门到精通》
   - 《流畅的Python》
   - 官方库文档（jieba、wordcloud、Pillow、reportlab）

2. **在线资源**
   
   - Python官方文档
   - 第三方库文档与教程
   - GitHub优秀项目示例

---

## 五、学习评价

### （一）过程性评价（80%）

| 评价维度        | 权重  | 满分     | 评价标准                            |
| ----------- | --- | ------ | ------------------------------- |
| **出勤及课中表现** | 10% | 100    | 缺课≤10%为满分                       |
| **团队协作**    | 15% | 100    | 积极参与、能解答问题、代码演示清晰               |
| **工单任务**    | 55% | 100/任务 | 功能完整≥80%、代码规范≥90% PEP8、文档完整、创新性 |

### （二）终结性评价（20%）

| 评价方式     | 权重   | 满分  | 评价标准                 |
| -------- | ---- | --- | -------------------- |
| **综合项目** | 100% | 100 | 需求理解、系统设计、功能实现、文档与答辩 |

### （三）通过标准

**及格（60分）**：

- 缺课≤10%
- ≥70%工单完成度≥60%
- 代码规范率≥70%
- 综合成绩≥60分

**良好（80-89分）**：

- 缺课≤5%
- ≥80%工单完成度≥80%
- 代码规范率≥85%
- 综合成绩≥80分

**优秀（90分及以上）**：

- 全勤或缺课≤1次
- 100%工单完成度≥85%
- 代码规范率≥95%
- 综合成绩≥90分
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
