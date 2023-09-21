def main():
    x = 7
    y = 5
    product = recursive_multiply(x, y)
    print('{x} * {y} = {product}')

def recursive_multiply(x, y):
    if y == 1:
        return x
    else:
        return x + recursive_multiply(x, y - 1)

if __name__ == "__main__":
    main()
