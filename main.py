
def main():
    print("Hello in Fibonacci Calculator:\n")
    while True:
        print("Enter term number in Fibonacci sequence:", end=" ")
        user_input = input()
        if user_input.isdigit():
            n = int(user_input)
            numeral_string = str(n) + "."
            print(numeral_string, "therm of Fibonacci Sequence:", end=" ")
            print_bold_green(fib(n))
            print("Fibonacci Calculator")
            print("Krzysztof Winiarczyk")
            print("IMST 2.5\n")
        else:
            print_red("ERROR: please enter correct number [natural integer]\n")
            continue


def print_bold_green(text):
    print("\033[01m\033[32m{}\033[0m" .format(text))


def print_red(text):
    print("\033[31m{}\033[0m" .format(text))


# calculate n-th term in Fibonacci sequence (iteratively)
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    c = 0
    a = 0
    b = 1
    while n-2 >= 0:
        c = a+b
        a = b
        b = c
        n = n-1
    return c


if __name__ == '__main__':
    main()
