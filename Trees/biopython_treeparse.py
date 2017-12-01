#!/usr/bin/env python3

from Bio import Phylo
trees = Phylo.parse("treefile1.tre", "newick")

def all_parents(tree):
    parents = {}
    for clade in tree.find_clades(order='level'):
        for child in clade:
            parents[child] = clade
    return parents


for tree in trees:
    print(tree)
    Phylo.draw_ascii(tree)

    for tip in tree.get_terminals():
        print("terminal tip",tip)
    term_names = [term.name for term in tree.get_terminals()]

    parents = all_parents(tree)
    clades = tree.find_clades("E")
    for myclade in clades:  # get first instance of 'E'
        parent_of_myclade = parents[myclade]
        
        print(parent_of_myclade.get_terminals())
