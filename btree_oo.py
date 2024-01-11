#! /usr/bin/env python3

import graphviz
import random

# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None

# def insert(root, key):
#     if root is None:
#         return TreeNode(key)
#     else:
#         if key < root.key:
#             root.left = insert(root.left, key)
#         else:
#             root.right = insert(root.right, key)
#     return root

def delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = get_min_value(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root


def get_min_value(root):
    while root.left is not None:
        root = root.left
    return root


def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root.key, end=' ')
        in_order_traversal(root.right)


# def pre_order_traversal(root):
#     if root is not None:
#         print(root.key, end=' ')
#         pre_order_traversal(root.left)
#         pre_order_traversal(root.right)


# def post_order_traversal(root):
#     if root is not None:
#         post_order_traversal(root.left)
#         post_order_traversal(root.right)
#         print(root.key, end=' ')

# ----------------------
# POO:

class Bt:
    """binary tree"""

    def __init__(self, key=None):
        self.key = key
        self.left = self.right = None

    def __str__(self):
        # return f"[{self.key},{self.left},{self.right}]"
        keyOut = self.key
        if not keyOut:
            keyOut = "·"
        leftOut = self.left
        if not self.left:
            leftOut = "-"
        rightOut = self.right
        if not self.right:
            rightOut = "-"
        return f"[{leftOut},{keyOut},{rightOut}]"


    def insert(self, key):

        if not self.key: # is None:
            self.key = key
            return

        if key < self.key:
            if not self.left: # == None
                self.left = Bt(key)
                return
            if isinstance(self.left, Bt):
                self.left.insert(key)
                return

        if self.key < key:
            if not self.right: # == None
                self.right = Bt(key)
                return
            if isinstance(self.right, Bt):
                self.right.insert(key)
                return


    def visu(self):

        # - [??] TODO introspeccion del nombre
        # https://stackoverflow.com/questions/1690400/getting-an-instance-name-inside-class-init
        # selfName = self.retrieveName() ...
        selfName = "aName"

        dot = graphviz.Digraph()
        dot.node(str(self.key))

        def add_nodes_edges(aBt):
            if aBt.left:
                dot.node(str(aBt.left.key))
                dot.edge(str(aBt.key), str(aBt.left.key))
                add_nodes_edges(aBt.left)
            if aBt.right:
                dot.node(str(aBt.right.key))
                dot.edge(str(aBt.key), str(aBt.right.key))
                add_nodes_edges(aBt.right)

        add_nodes_edges(self)
        # dot.render('bt_' + str(counter), view=True, format='png')
        dot.render('bt_' + selfName, view=False, format='png')



if __name__ == "__main__":

    bt = Bt()
    # print(bt)
    # bt.visu()

#     x = int(input("dime cuantas bolas quieres: "))

# for i in range(x):
    bt.insert(random.randrange(100))
    print(bt)
    bt.visu()

    # bt.insert(random.randrange(100))
    # print(bt)
    # bt.visu()

    # bt.insert(random.randrange(100))  
    # print(bt)
    # bt.visu()

    # bt.insert(random.randrange(100))  
    # print(bt)
    # bt.visu()

    # bt.insert(random.randrange(100))  
    # print(bt)
    # bt.visu()
