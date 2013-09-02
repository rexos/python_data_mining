def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


def main():
    try:
        num = int(raw_input('input --> '))
    except Exception:
        print "Wrong Input"
    else:
        print "factorial is : ", str(factorial(num))

if __name__ == '__main__':
    main()
