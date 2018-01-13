# coding=utf8
"""
本示例使用 networkx 库构建复杂、更人性化的的关系图
安装 pip install networkx
参考 https://networkx.github.io/
"""

from __future__ import unicode_literals

import networkx as nx
from networkx.readwrite import json_graph
from pyecharts import Graph

g = nx.Graph()
g.add_node('G1', name='Gateway 1')
g.add_node('N2', name='Node 2')
g.add_node('N3', name='Node 3')
g.add_edge('G1', 'N2')
g.add_edge('G1', 'N3')
g_data = json_graph.node_link_data(g)
eg = Graph('设备最新拓扑图')
eg.add('Devices', nodes=g_data['nodes'], links=g_data['links'])
eg.render()
