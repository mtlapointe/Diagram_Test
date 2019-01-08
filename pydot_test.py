import pydot
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

graph = pydot.Dot(graph_type='graph')

edge = pydot.Edge("AAA","BBB")
graph.add_edge(edge)
edge = pydot.Edge("AAA","CCC")
graph.add_edge(edge)
edge = pydot.Edge("CCC","BBB")
graph.add_edge(edge)

graph.write_svg('example1_graph.svg')



graph = pydot.Dot(graph_type='digraph')

node_concept = pydot.Node("Concept", shape='box')
graph.add_node(node_concept)
node_nf_review = pydot.Node("Non-Flight Review", shape='box')
graph.add_node(node_nf_review)
node_nf_release = pydot.Node("Non-Flight Release", shape='box')
graph.add_node(node_nf_release)

graph.add_edge(pydot.Edge(node_concept, node_nf_review, label="Submit for Non-Flight Review"))
graph.add_edge(pydot.Edge(node_nf_review, node_nf_release, label="TD Approval"))
graph.add_edge(pydot.Edge(node_nf_review, node_concept, label="Edits Required"))

graph.write_svg('example2_graph.svg')