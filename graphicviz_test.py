from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

g = Digraph()

g.attr(rankdir='LR')
g.attr('node',fontname='sans-serif', fontsize='12')
g.attr('edge',fontname='sans-serif', fontsize='10', pad="10")
g.attr('node', shape='box')

with g.subgraph(name='graph1') as c:
    c.node('Concept', 'Concept')
    c.node('Review', 'Non-Flight\nReview')
    c.node('Release', 'Non-Flight\nRelease')

    c.edge('Concept','Review',label='<<br/><br/><b>Engineer</b><br/>Submit for <br/>Non-Flight Review>')
    c.edge('Review','Release',label='<<br/><br/><b>TD</b><br/>Approved>')
    c.edge('Review','Concept',label='<<br/><br/><b>TD</b><br/>Edits Required>')

with g.subgraph(name='graph2') as c:
    c.node('Concept2', 'Concept')
    c.node('Review2', 'Non-Flight\nTD Review')
    c.node('Release2', 'Non-Flight\nRelease')
    c.node('DC2', 'Non-Flight\nDC Review')

    c.edge('Concept2', 'Review2',
           label='<<table border="0"><tr><td cellpadding="2" border="0">' \
                 '<b>Engineer</b><br/>Submit for <br/>Non-Flight Review' \
                 '</td></tr></table>>')

    c.edge('Review2', 'DC2',
           label='<<table border="0"><tr><td cellpadding="2" border="0">' \
                 '<b>TD</b><br/>Approval' \
                 '</td></tr></table>>')

    c.edge('Review2', 'Concept2',
           label='<<table border="0"><tr><td cellpadding="2" border="0">' \
                 '<br/><br/><b>TD</b><br/>Edits Required' \
                 '</td></tr></table>>')

    c.edge('DC2', 'Release2',
           label='<<table border="0"><tr><td cellpadding="2" border="0">' \
                 '<br/><br/><b>Doc Control</b><br/>Approved' \
                 '</td></tr></table>>')


g.render('test', format='svg', view=True)