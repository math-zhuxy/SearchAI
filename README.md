
# SearchAI

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

SearchAI是一个开源项目，旨在为接入的大模型API增加网络查询功能。通过我们的前端页面，用户可以轻松地与这些大模型交互，并利用网络查询功能增强模型的响应能力。

## 特性

- **增强模型能力**：通过整合实时网络数据，提升模型的回答质量和准确性。
- **用户友好的前端界面**：提供简洁直观的用户界面，用于展示对话历史以及管理用户信息。
- **灵活配置**：支持自定义用户API名称、接口地址、函数调用等设置，满足不同用户的特定需求。

## 快速开始

### 前提条件

在运行本项目之前，请确保您已经安装了以下软件：
- python v3.8+
- pip v21.0+

### 安装

克隆仓库到本地：

```bash
git clone https://github.com/yourusername/SearchAI.git
cd SearchAI
```

创建虚拟环境（推荐）:
```bash
python -m venv venv
```


激活虚拟环境：
windows：
```bash
venv\Scripts\activate
```
在Unix或MacOS上:
```bash
source venv/bin/activate
```
使用pip安装所有依赖：
```bash

pip install -r requirements.txt
```

### 配置

请创建名为`setting.json`的文件，并将`setting_template.json`文件中的内容赋值到该文件中，同时填写好相关信息，不同键的含义如下：

|键名 | 含义 |
|---|---|
|apikey | 您的大模型API key|
|url | 大模型接口地址，可以在官网查询|
| name | 需要调用的大模型名称 |
| tool | 包含三种选择："auto", "force", "none" |
| sys | 您要输入的第一句话 |
| func | 进行网络查询的函数说明 |
| para | 参数说明 |
| port | 本地服务运行的端口 |
| max_num | 网络查询的最大搜索范围 |
| cookie | 需要从bing上获取浏览器cookie |

tool包含三种选择： "auto"指的是大模型自动选择是否调用函数，"force"指函数必须强制调用函数，"none"指函数禁止调用函数。

### 运行

启动服务器：

```bash
python main.py
```

现在，您可以通过浏览器访问`http://127.0.0.1:port`来查看您的SearchAI应用了。


## 贡献

我们欢迎任何形式的贡献，无论是代码改进还是新特性提议。

## 许可证

本项目采用MIT许可证，详情请参见[LICENSE](LICENSE)文件。

---

由 [math-zhuxy] 和所有[贡献者](https://github.com/yourusername/SearchAI/graphs/contributors)共同维护。
