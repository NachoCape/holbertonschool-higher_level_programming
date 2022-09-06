#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        print("0", end="")
    if i <= 98:
        print(f"{i}", end=", ")
    else:
        print(f"{i}")
