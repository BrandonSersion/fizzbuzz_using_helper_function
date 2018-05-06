def fizz_buzz(fizz, buzz, limit):

    # helper
    def divisible_by(iterator, divisor):
        if iterator % divisor == 0:
            return True

    for i in range(0, limit):
        if divisible_by(i, fizz*buzz):
            print("FizzBuzz")
            
        elif divisible_by(i, fizz):
            print("Fizz")

        elif divisible_by(i, buzz):
            print("Buzz")

        else:
            print(i)


def main():
    fizz_buzz(3, 5, 100)

if __name__ == "__main__":
    main()