def rev(var):
    str =""
    for i in var:
        str = i + str
    return str

s = 'Helloworld'
res = rev(s)
print(res)
