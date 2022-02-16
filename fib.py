n = int(input("Enter any number:"))
a = 0
b = 1
for i in range(0, n + 1):
    print(a, end=' ')
    nxt = a + b
    a = b
    b = nxt
