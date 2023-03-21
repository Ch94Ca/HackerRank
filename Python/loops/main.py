if __name__ == '__main__':
    n = int(input())

    for number in list(map(lambda r: r ** 2, list(range(0, n)))):
        print(number)
