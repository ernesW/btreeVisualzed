import btree_oo
import random

if __name__ == "__main__":

    pt = btree_oo.Bt()
    
    x = int(input("dime cuantas bolas quieres: "))

    for i in range(x):
        pt.insert(random.randrange(100))
        print(pt)
        pt.visu()