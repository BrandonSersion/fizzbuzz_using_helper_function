def fizz_buzz(fizz, buzz, limit):
    
    def divisible_by(iterator, divisor):
        if iterator % divisor == 0:
            return True

    for i in range(0, limit):
        if divisible_by(i, fizz*buzz):
            yield "FizzBuzz"

        elif divisible_by(i, fizz):
            yield "Fizz"

        elif divisible_by(i, buzz):
            yield "Buzz"

        else:
            yield str(i)


def main():
    print('\n'.join(fizz_buzz(3, 5, 100)))
    

if __name__ == "__main__":
    main()