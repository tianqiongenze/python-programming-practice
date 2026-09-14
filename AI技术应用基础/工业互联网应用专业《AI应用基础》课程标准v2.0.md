# 工业互联网应用专业《AI应用基础》课程标准（v2.0）

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
| **课程代码**     | B46021002                                 |
| **开课学院**     | 智能控制学院                                    |
| **课程名称**     | AI应用基础                                    |
| **面向的职业及岗位** | 工业数据采集技术员、边缘计算运维员、工业网络实施与运维工程师、工业互联网平台运维员 |
| **学分**       | 3                                         |
| **总学时**      | 48                                        |
| **理论学时**     | 24                                        |
| **实习（训）学时**  | 24                                        |
| **授课周数**     | 12周                                       |
| **周学时**      | 4课时/周                                     |
| **先修课程**     | 《Python编程基础》建议完成前6周内容                     |

### （二）课程性质与定位

《AI应用基础》是工业互联网应用专业的核心课程，面向专科一年级新生开设。本课程建立在《Python编程基础》基础之上，以工业实际应用为驱动，通过**传统机器学习→深度学习→强化学习→多模态AI**的递进路径，培养学生的AI应用能力。特别强调图像识别、自然语言处理、语音处理等在工业中的实际应用。

**课程定位**：

1. **职业面向**：适配工业互联网四大核心岗位的AI应用需求
2. **知识结构**：ML基础 → 深度学习与神经网络 → 计算机视觉 → NLP与语音 → 强化学习及大模型智能体应用
3. **实践取向**：以工业视觉检测、语音告警、故障预测、设备优化为真实场景
4. **技术前沿**：涵盖当前AI领域的主流技术与实际应用

---

## 二、教学目标

### （一）知识目标

1. **传统机器学习**（回顾）
   
   - 分类、回归、时间序列的基本模型
   - 特征工程与超参数调优

2. **深度学习与神经网络**
   
   - 理解神经网络的结构与前向传播、反向传播
   - 掌握卷积神经网络（CNN）的基本原理
   - 了解循环神经网络（RNN、LSTM）的时间序列能力
   - 理解Transformer模型的自注意力机制

3. **计算机视觉**
   
   - 掌握图像分类、物体检测的方法
   - 理解缺陷检测的工业应用原理
   - 了解迁移学习在工业视觉中的应用

4. **自然语言处理**
   
   - 掌握文本表示与词向量（Word2Vec、BERT）
   - 理解文本分类与情感分析方法
   - 了解序列标注与命名实体识别

5. **语音处理**
   
   - 理解语音信号处理基础
   - 掌握语音识别与语音合成的基本应用
   - 了解多模态（音频+文本）的融合应用

6. **强化学习**
   
   - 理解马尔可夫决策过程（MDP）与值函数
   - 掌握Q-Learning算法基础
   - 了解策略梯度与Actor-Critic方法
   - 理解在工业优化中的应用

### （二）能力目标

1. **深度学习开发能力**
   
   - 能够使用TensorFlow/PyTorch搭建神经网络
   - 能够进行模型训练、验证、测试的完整流程
   - 能够进行模型诊断与超参数优化

2. **计算机视觉应用能力**
   
   - 能够进行图像数据的预处理与增强
   - 能够使用预训练模型进行图像分类
   - 能够进行工业缺陷检测与定位

3. **NLP应用能力**
   
   - 能够进行文本预处理与向量化
   - 能够训练文本分类模型
   - 能够使用预训练语言模型进行故障描述解析

4. **语音处理能力**
   
   - 能够进行语音信号的基本处理
   - 能够调用语音识别API进行实时转录
   - 能够使用文本转语音生成工业告警

5. **强化学习应用能力**
   
   - 能够建模工业优化问题为MDP
   - 能够实现基本的强化学习算法
   - 能够进行算法的验证与改进

### （三）素质目标

1. **AI伦理与责任意识**
   
   - 理解AI在工业应用中的伦理问题
   - 树立"AI为人服务"的意识
   - 关注数据隐私与模型解释性

2. **创新意识**
   
   - 鼓励学生探索AI在工业新应用
   - 培养"技术 + 工业领域知识"的交叉思维

3. **工程化思维**
   
   - 理解从研究到生产环境的差异
   - 掌握模型部署、监控、迭代的完整流程

---

## 三、教学内容

### （一）模块M1：数据处理与特征工程（第1-2周，8课时）

**学习内容**：Pandas数据处理、EDA分析、特征工程、特征选择

**工单项目**：工业设备采样数据清洗与分析

---

### （二）模块M2：传统ML与深度学习基础（第3-6周，16课时）

#### **任务M2.1：分类模型与XGBoost（第3-4周，8课时）**

**学习内容**：

- 分类评估指标、决策树、随机森林、XGBoost
- 工单项目：工业设备故障多分类预测模型

#### **任务M2.2：深度学习与神经网络（第5-6周，8课时）**

**学习目标**：

- 知识：理解神经网络结构、卷积神经网络、循环神经网络的基本原理
- 能力：能够使用TensorFlow/PyTorch搭建简单深度学习模型
- 素质：培养对AI底层原理的理解

**学习流程**：

**第一部分：神经网络基础（2课时）**

1. 神经元、激活函数、损失函数的基本概念
2. 前向传播与反向传播算法
3. 梯度下降与优化方法（SGD、Adam）
4. 过拟合与正则化

**第二部分：卷积神经网络（CNN）— 工业视觉基础（2.5课时）**

1. **CNN基本原理**
   
   - 卷积层、池化层、全连接层
   - 参数共享与特征提取的直观理解

2. **经典架构**
   
   - AlexNet、VGG、ResNet的简单介绍
   - 迁移学习：使用预训练模型

3. **工业应用场景**
   
   - 产品质量检测（OK/NG分类）
   - 设备故障图像识别
   - 零部件缺陷定位

4. **代码实践**
   
   ```python
   import tensorflow as tf
   from tensorflow import keras
   
   # 构建简单CNN模型
   model = keras.Sequential([
       keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(64,64,3)),
       keras.layers.MaxPooling2D((2,2)),
       keras.layers.Conv2D(64, (3,3), activation='relu'),
       keras.layers.MaxPooling2D((2,2)),
       keras.layers.Flatten(),
       keras.layers.Dense(128, activation='relu'),
       keras.layers.Dense(10, activation='softmax')
   ])
   
   model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
   ```

**第三部分：循环神经网络（RNN/LSTM）— 工业时间序列深化（2.5课时）**

1. **RNN与LSTM基本原理**
   
   - 循环结构与序列建模
   - 梯度消失问题与LSTM解决方案
   - 双向LSTM与Attention机制

2. **应用场景**
   
   - 设备性能时间序列预测（vs ARIMA的对比）
   - 故障预警的长期依赖捕捉
   - 传感器数据异常检测

3. **代码实践**
   
   ```python
   from tensorflow.keras.layers import LSTM, Dense
   
   # LSTM模型用于时间序列预测
   model = keras.Sequential([
       LSTM(50, activation='relu', input_shape=(10, 5)),  # 10步长，5个特征
       Dense(25, activation='relu'),
       Dense(1)
   ])
   
   model.compile(optimizer='adam', loss='mse')
   ```

**标准与规范**：

- TensorFlow/PyTorch官方文档
- 深度学习最佳实践（数据归一化、批量归一化等）

**软硬件工具**：

- Python TensorFlow / PyTorch库
- Jupyter Notebook
- GPU支持（可选，但推荐用于实时演示）

**工单项目M2.2**：

- **项目名称**：工业设备故障深度学习预测模型
- **需求描述**：
  1. 使用CNN模型重新实现设备故障分类（对比XGBoost）
  2. 使用LSTM模型进行设备性能时间序列预测
  3. 对比传统ML与深度学习的性能
- **验收标准**：
  - CNN模型的分类准确率≥80%
  - LSTM模型的预测RMSE相对误差≤15%
  - 提供模型对比分析报告
  - 代码规范率≥90%
  - 包含模型训练曲线与诊断图表

---

### （三）模块M3：计算机视觉与缺陷检测（第7-8周，8课时）

**学习目标**：

- 知识：掌握图像分类、物体检测、语义分割的基本方法
- 能力：能够进行工业图像检测和缺陷定位
- 素质：培养工业AI视觉应用的认知

**学习流程**：

**第一部分：图像预处理与特征提取（1.5课时）**

1. 图像颜色空间转换与归一化
2. 图像增强（直方图均衡、对比度调整）
3. 特征金字塔与多尺度特征

**第二部分：图像分类与迁移学习（2.5课时）**

1. 使用预训练模型（ResNet、MobileNet）
   
   ```python
   import tensorflow as tf
   
   # 使用预训练ResNet进行迁移学习
   base_model = tf.keras.applications.ResNet50(weights='imagenet', include_top=False)
   base_model.trainable = False
   
   model = keras.Sequential([
       base_model,
       keras.layers.GlobalAveragePooling2D(),
       keras.layers.Dense(128, activation='relu'),
       keras.layers.Dense(10, activation='softmax')
   ])
   ```

2. 工业应用案例
   
   - 产品OK/NG分类（二分类）
   - 多个产品等级分类（多分类）

**第三部分：物体检测与缺陷定位（2.5课时）**

1. **物体检测基础**
   
   - YOLO、Faster R-CNN等架构简介
   - 边界框回归与类别预测

2. **工业缺陷检测工作流**
   
   - 数据采集与标注（使用标注工具）
   - 模型训练与评估
   - 实时推理与结果展示

3. **代码实践**（使用ultralytics YOLOv5）
   
   ```python
   from ultralytics import YOLO
   
   # 加载预训练YOLO模型
   model = YOLO('yolov5s.pt')
   
   # 检测图像
   results = model.predict(source='device_image.jpg', conf=0.5)
   
   # 可视化结果
   for r in results:
       im_array = r.plot()
       im = Image.fromarray(im_array[..., ::-1])
       im.show()
   ```

**标准与规范**：

- OpenCV、YOLO、TensorFlow Object Detection API文档

**软硬件工具**：

- Python OpenCV、TensorFlow、ultralytics库
- 图像标注工具（LabelImg、Roboflow）

**工单项目M3**：

- **项目名称**：工业产品缺陷检测系统
- **需求描述**：
  1. 采集或使用公开数据集（工业产品、电子元件等）
  2. 标注≥50张图片中的缺陷区域
  3. 训练物体检测模型（YOLO或Faster R-CNN）
  4. 进行实时检测与结果可视化
- **验收标准**：
  - 标注≥50张图片
  - 模型的mAP（平均精确度）≥0.70
  - 检测速度≥10 FPS
  - 包含模型性能评估报告
  - 代码规范率≥90%

---

### （四）模块M4：自然语言处理与语音处理（第9-10周，8课时）

**学习目标**：

- 知识：掌握NLP基本技术、文本分类、语音识别与合成
- 能力：能够进行工业文本分析、故障说明解析、告警生成
- 素质：培养多模态AI的认知

**学习流程**：

**第一部分：自然语言处理基础（2.5课时）**

1. **文本向量化方法**
   
   - TF-IDF、Word2Vec、BERT等方法
   - 预训练语言模型的使用

2. **文本分类应用**
   
   - 故障类型分类（从故障说明文本）
   - 工单优先级分类
   - 故障原因自动标签化

3. **代码实践**
   
   ```python
   from transformers import pipeline
   
   # 使用预训练BERT模型进行文本分类
   classifier = pipeline('text-classification', model='bert-base-chinese')
   result = classifier('这是轴承过热故障，需要立即停机检查')
   print(result)  # 返回故障类别
   
   # 文本相似度计算
   from sentence_transformers import SentenceTransformer, util
   model = SentenceTransformer('distiluse-base-multilingual-cased-v2')
   
   texts = ['轴承过热', '轴承温度异常', '设备温度高']
   embeddings = model.encode(texts)
   similarity = util.pytorch_cos_sim(embeddings[0], embeddings[1])
   ```

**第二部分：语音处理基础（2.5课时）**

1. **语音信号处理**
   
   - 音频加载、频域分析（MFCC、梅尔频谱）
   - 噪声消除与信号增强

2. **语音识别与合成**
   
   - 使用语音识别API（Google Speech-to-Text、百度等）
   - 文本转语音合成（TTS）用于告警通知

3. **工业应用**
   
   - 工业告警语音识别与理解
   - 故障说明的语音输入与转文本
   - 维护人员的语音指令接收

4. **代码实践**
   
   ```python
   # 语音识别示例
   import speech_recognition as sr
   
   recognizer = sr.Recognizer()
   with sr.Microphone() as source:
       print("请说出故障描述...")
       audio = recognizer.listen(source)
       try:
           text = recognizer.recognize_google(audio, language='zh-CN')
           print(f"识别结果：{text}")
       except sr.UnknownValueError:
           print("无法识别")
   
   # 文本转语音示例
   from gtts import gTTS
   
   tts = gTTS('轴承温度过高，请立即停机检查', lang='zh')
   tts.save('alarm.mp3')
   ```

**第三部分：多模态融合（1.5课时）**

1. 视觉 + 文本的故障诊断
2. 音频 + 文本的告警理解
3. 完整的多模态故障处理系统

**标准与规范**：

- Hugging Face Transformers文档
- SpeechRecognition、librosa、TTS库文档

**软硬件工具**：

- Python transformers、librosa、speech_recognition库
- Jupyter Notebook

**工单项目M4**：

- **项目名称**：工业故障多模态分析系统
- **需求描述**：
  1. 收集≥50条设备故障文本数据
  2. 使用BERT/预训练模型进行故障分类
  3. 实现故障语音输入与识别
  4. 根据识别的故障类型自动生成语音告警
- **验收标准**：
  - 文本分类准确率≥80%
  - 语音识别准确率≥85%
  - 支持实时处理
  - 代码规范率≥90%
  - 包含多模态融合的演示

---

### （五）模块M5：强化学习与工业优化（第11-12周，8课时）

**学习目标**：

- 知识：理解强化学习基本概念、Q-Learning、策略梯度
- 能力：能够解决工业优化问题（设备参数优化、能耗最小化）
- 素质：培养将业务问题形式化为AI问题的能力

**学习流程**：

**第一部分：强化学习基础（2.5课时）**

1. **基本概念**
   
   - 马尔可夫决策过程（MDP）：状态、动作、奖励、折扣因子
   - 值函数与策略函数
   - 探索-利用权衡

2. **Q-Learning算法**
   
   ```python
   import numpy as np
   
   class QLearningAgent:
       def __init__(self, state_space, action_space, learning_rate=0.1, discount_factor=0.95):
           self.Q = np.zeros((state_space, action_space))
           self.lr = learning_rate
           self.gamma = discount_factor
   
       def update(self, state, action, reward, next_state):
           target = reward + self.gamma * np.max(self.Q[next_state])
           self.Q[state, action] += self.lr * (target - self.Q[state, action])
   
       def choose_action(self, state, epsilon=0.1):
           if np.random.random() < epsilon:
               return np.random.randint(self.Q.shape[1])
           else:
               return np.argmax(self.Q[state])
   ```

3. **策略梯度方法**
   
   - Actor-Critic架构简介
   - Policy Gradient的基本思想

**第二部分：工业优化应用（2.5课时）**

1. **问题建模**
   
   - 状态空间：设备参数、环境条件
   - 动作空间：控制指令（加速、减速、切换工艺等）
   - 奖励函数：生产效率、能耗、质量的权衡

2. **案例1：设备参数优化**
   
   - 目标：最大化产量，最小化能耗
   - 状态：温度、压力、转速
   - 动作：调整参数
   - 奖励：产量 - 能耗*系数

3. **案例2：动态调度问题**
   
   - 目标：最小化总完成时间
   - 状态：设备状态、任务队列
   - 动作：分配任务到设备
   - 奖励：任务完成时间的减少

**第三部分：DQN与深度强化学习简介（1.5课时）**

1. 深度Q网络（DQN）的基本概念
2. 经验回放与目标网络
3. 工业应用的可行性分析

**代码实践**（工业设备参数优化）

```python
class IndustrialOptimizer:
    def __init__(self):
        self.agent = QLearningAgent(state_space=100, action_space=10)

    def train(self, episodes=1000):
        for episode in range(episodes):
            state = self.get_initial_state()
            total_reward = 0

            for step in range(50):
                action = self.agent.choose_action(state)
                next_state, reward = self.simulate_device(state, action)
                self.agent.update(state, action, reward, next_state)
                total_reward += reward
                state = next_state

            if episode % 100 == 0:
                print(f"Episode {episode}, Total Reward: {total_reward}")

    def simulate_device(self, state, action):
        # 模拟设备状态转移与奖励计算
        # 根据当前参数和动作计算新状态和奖励
        next_state = (state + action) % 100
        reward = -abs(state - 50) + action * 0.1  # 示例奖励函数
        return next_state, reward

# 使用示例
optimizer = IndustrialOptimizer()
optimizer.train()
```

**标准与规范**：

- OpenAI Gym文档（强化学习环境标准）
- Stable-Baselines3库文档

**软硬件工具**：

- Python gym、stable-baselines3库
- 工业模拟环境或真实设备（可选）

**工单项目M5**：

- **项目名称**：工业设备参数优化强化学习系统
- **需求描述**：
  1. 建立简单的设备模型（温度、压力、产量的关系）
  2. 定义状态空间、动作空间、奖励函数
  3. 使用Q-Learning训练优化智能体
  4. 对比随机策略与学习策略的效果
- **验收标准**：
  - 正确定义MDP问题
  - Q-Learning算法训练≥500步
  - 学习策略相比随机策略改进≥50%
  - 代码规范率≥90%
  - 包含收敛曲线与性能对比

---

### （六）综合项目（第12周完成）

**综合项目选题**：

**选项1：完整的工业AI决策支持系统**

- 功能集成：视觉检测 + 文本分析 + 强化学习优化
- 涉及知识点：CNN、NLP、强化学习、多模态
- 工作量：1500+行代码

**选项2：设备故障诊断与预测维护系统**

- 功能集成：时间序列预测 + 异常检测 + 图像缺陷识别
- 涉及知识点：LSTM、目标检测、时间序列
- 工作量：1200+行代码

**选项3：生产流程智能优化系统**

- 功能集成：生产调度 + 质量检测 + 参数优化
- 涉及知识点：强化学习、计算机视觉、数据分析
- 工作量：1300+行代码

---

### （七）教学进度表

| 周次  | 课时  | 模块  | 学习内容              | 工单项目    | 考核方式    |
| --- | --- | --- | ----------------- | ------- | ------- |
| 1   | 4   | M1  | 数据清洗、EDA          | 数据清洗分析  | 代码演示+工单 |
| 2   | 4   | M1  | 特征工程、特征选择         | 特征库设计   | 代码演示+工单 |
| 3   | 4   | M2  | 分类模型、评估指标         | 故障分类预测  | 代码演示+工单 |
| 4   | 4   | M2  | XGBoost、集成学习      | 故障分类预测  | 代码演示+工单 |
| 5   | 4   | M2  | 神经网络基础、CNN        | 深度学习模型  | 代码演示+工单 |
| 6   | 4   | M2  | LSTM、时间序列预测       | 深度学习模型  | 代码演示+工单 |
| 7   | 4   | M3  | 图像分类、迁移学习         | 缺陷检测系统  | 代码演示+工单 |
| 8   | 4   | M3  | 物体检测、缺陷定位         | 缺陷检测系统  | 代码演示+工单 |
| 9   | 4   | M4  | NLP基础、文本分类        | 多模态分析系统 | 代码演示+工单 |
| 10  | 4   | M4  | 语音识别、语音合成         | 多模态分析系统 | 代码演示+工单 |
| 11  | 4   | M5  | 强化学习基础、Q-Learning | 参数优化系统  | 代码演示+工单 |
| 12  | 4   | M5  | 强化学习应用、综合项目       | 综合项目答辩  | 项目演示+答辩 |

---

## 四、课程实施保障条件

### （一）实训条件

1. **硬件配置**
   
   - CPU：i7+ / Ryzen 7+（推荐）
   - 内存：16GB+
   - **GPU**：NVIDIA RTX 2060+ 或 A100（用于深度学习加速）
   - 网络：100Mbps+

2. **软件环境**
   
   - Python 3.9+
   - TensorFlow 2.10+ 或 PyTorch 2.0+
   - 库：scikit-learn、xgboost、opencv、librosa、transformers等
   - IDE：Jupyter Lab（推荐用于深度学习实验）

3. **数据与模型资源**
   
   - 工业图像数据集（产品、缺陷等）
   - 预训练模型（ResNet、YOLO、BERT中文模型等）
   - 模拟工业环境（工业设备仿真）

### （二）教学团队

1. **教师要求**
   
   - 教学经验：≥3年深度学习或AI实战经验
   - 技能：精通TensorFlow/PyTorch、计算机视觉、NLP
   - 工业背景：理解工业应用场景

2. **企业导师**
   
   - AI算法工程师参与案例设计
   - 工业AI应用经验分享

### （三）学习资源

1. **在线平台**
   
   - TensorFlow/PyTorch官方教程
   - Hugging Face模型库与文档
   - Kaggle数据竞赛与解决方案

2. **工业数据集**
   
   - 开源：MIT-BIH心电图、工业故障数据集等
   - 公司数据：脱敏后的真实工业数据

---

## 五、学习评价

### （一）过程性评价（80%）

| 评价维度     | 权重  | 满分     | 评价标准                                     |
| -------- | --- | ------ | ---------------------------------------- |
| **出勤率**  | 10% | 100    | 缺课≤10%为满分                                |
| **课中表现** | 15% | 100    | 积极参与、能解释模型、代码演示清晰                        |
| **工单任务** | 55% | 100/任务 | 功能完整≥80%、代码规范≥90% PEP8、**模型性能达基准值**、文档完整 |

### （二）终结性评价（20%）

| 评价方式     | 权重   | 满分  | 评价标准                     |
| -------- | ---- | --- | ------------------------ |
| **综合项目** | 100% | 100 | 需求分析、模型设计、性能指标、文档与答辩、创新性 |

### （三）模型性能基准值

| 工单项目      | 评估指标     | 合格线   | 良好线   | 优秀线   |
| --------- | -------- | ----- | ----- | ----- |
| M2.1 分类   | F1分数     | ≥0.70 | ≥0.80 | ≥0.90 |
| M2.2 CNN  | 精确度      | ≥0.75 | ≥0.85 | ≥0.95 |
| M2.2 LSTM | RMSE相对误差 | ≤15%  | ≤10%  | ≤5%   |
| M3 缺陷检测   | mAP      | ≥0.65 | ≥0.75 | ≥0.85 |
| M4 文本分类   | 精确度      | ≥0.75 | ≥0.85 | ≥0.95 |
| M4 语音识别   | 字错率      | ≤20%  | ≤15%  | ≤10%  |
| M5 强化学习   | 改进率      | ≥30%  | ≥50%  | ≥70%  |

### （四）通过标准

**及格（60分）**：

- 缺课≤10%
- ≥70%工单完成度≥60%
- 至少2个工单达到模型性能合格线
- 综合成绩≥60分

**良好（80-89分）**：

- 缺课≤5%
- ≥80%工单完成度≥80%
- 至少3个工单达到模型性能良好线
- 综合成绩≥80分

**优秀（90分及以上）**：

- 全勤或缺课≤1次
- 100%工单完成度≥85%
- ≥4个工单达到模型性能优秀线
- 综合项目具有创新性
- 综合成绩≥90分

---

**文档版本**：2.0（v2.0融合版）
**最后更新**：2026年8月
**核心新增**：深度学习 + CNN + RNN/LSTM + 计算机视觉 + NLP + 语音处理 + 强化学习
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
