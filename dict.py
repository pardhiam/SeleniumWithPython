var = [1, 2, 3, 4, 5]
var2 = [5, 7, 9, 8, 6]

res = {}
for key in var:
    for value in var2:
        res[key] = value
        var2.remove(value)
        break
print("Output is" + str(res))
