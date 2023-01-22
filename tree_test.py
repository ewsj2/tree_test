from ete3 import Tree, TreeStyle
t = Tree()
t.populate(10, random_branches=True)
ts=TreeStyle()
ts.show_leaf_name=True
ts.show_branch_length=True
ts.show_branch_support=True
t.show(tree_style=ts)
