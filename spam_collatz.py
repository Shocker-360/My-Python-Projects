while True:
    num = int(input("Enter your number: "))

    def collatz(num):
        while num != 1:
            if num % 2 == 0:
                result = num / 2
                print(result)
                num = result
            elif num % 2 == 1:
                result = num * 3 + 1
                print(result)
                num = result

    collatz(num)
