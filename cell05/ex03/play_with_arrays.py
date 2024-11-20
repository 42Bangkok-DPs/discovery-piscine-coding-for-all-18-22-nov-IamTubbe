#!/usr/bin/env python3
a = [2, 8, 9, 48, 8, 22, -12, 2]
b = list(set(x + 2 for x in a if x > 5))
print(f"{a}\n{b}")
