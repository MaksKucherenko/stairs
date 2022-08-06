import sys
a = int(sys.argv[1])
if a > 0:
    for i in range(1, a+1):
        print(" " * (a - i) + "#" * i)
else:
    print("Число должно быть больше нуля!")
