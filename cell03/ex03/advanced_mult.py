#!/usr/bin/env python3
for i in range(11):
    print(f"Table de {i}: " + " ".join(str(i * j) for j in range(11)))
