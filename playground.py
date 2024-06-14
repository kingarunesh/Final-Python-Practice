a = [1, 2, [3, [4], [5, 6]], [7]]


total = 0

def fun(data):
    global total
    for i in range(len(data)):
        if type(data[i]) != list:
            total += data[i]
        else:
            fun(data=data[i])
    return total
            
result = fun(data=a)
print(result)