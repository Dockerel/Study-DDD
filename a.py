import os

for i in range(4, 12):
    s = "0" + str(i) if i < 10 else str(i)
    ret = os.mkdir(f"Chap_{s}")
