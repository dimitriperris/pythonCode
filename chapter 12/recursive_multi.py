def multiply_recursive(x, y):
    if y == 1:
        return x
    else:
        return x + multiply_recursive(x, y - 1)
    
result = multiply_recursive(8, 5)
print('The result of multiplication is:', result)
