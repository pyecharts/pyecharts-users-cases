## pyecharts 示例项目

## 概述

本仓库放置 pyecharts 的一些使用示例，这些示例均要求 pyecharts 在 0.3 以上。

## 索引

### 数据构建

* [networkx-graph](/samples/networkx-graph.py) - 使用 networkx 库构建关系图数据

### 本地渲染

* [advance-usage](/advance-usage) 自定义模板与引擎

### Jupyter Notebook示例

* [notebook-users-cases](/notebook-users-cases) 

### Django框架

* [demo-django](/demo-django) - 在 Django 中使用 pyecharts 绘图

### Flask 框架

* [demo-flask](/demo-flask) 在 Flask 中使用 pyecharts绘图

### Tornado 框架

* [demo-tornado](/demo-tornado) - 在 Tornado 中使用 pyecharts绘图

## 外部资源

*（这些资源不在本仓库托管之内，仅以链接列出）*

### Jupyter Notebook 在线示例

* [图例集锦](http://nbviewer.jupyter.org/github/pyecharts/pyecharts-users-cases/blob/master/notebook-users-cases/notebook-user-cases.ipynb)

### Flask 高级使用示例

* [flask_demo](https://github.com/pyecharts/flask_demo) 在Flask 中使用 pyecharts，整合了内置 `Flask.jinja2.engine` 引擎

### Django整合库

* [django-echarts](https://github.com/kinegratii/django-echarts) django-echarts 是一个 [Echarts](http://echarts.baidu.com/index.html) 整合的 [Django](https://www.djangoproject.com/) App，使用 [pyecharts](https://github.com/chenjiandongx/pyecharts) 的作为图表构建库。

## 协作

欢迎大家提供示例至本仓库！

提交规范：

* 如果示例项目在一个文件之内，可以单独放置在 *samples* 文件内，但必须在文件注明功能说明、依赖库。
* 如果示例项目是包含多个文件，应当独立创建一个项目目录，并提供必要的说明文件。
* 如果示例项目与图表效果有关，也应当独立创建一个项目目录，并在此目录提交效果图。
* 如果示例项目含有特定的项目模板，建议另外创建一个仓库，并在本 Readme 中 注明链接。
