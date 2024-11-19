#!/usr/bin/env python3
def displaymultiplicationtables():
    for i in range(11): 
        print(f"Table de {i}: ", end="")
        for j in range(11):
            print(i * j, end=" ")
        print()

if __name__ == "main":
    import sys
    if len(sys.argv) > 1:
        print("none")
    else:
        displaymultiplicationtables()