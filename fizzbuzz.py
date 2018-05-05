def fizz_buzz(fizz, buzz, limit):

    # helper
    def divisible_by(iterator, divisor):
        if iterator % divisor == 0:
            return True

    for i in range(1, limit+1):
        if divisible_by(i, fizz*buzz):
            print("FizzBuzz")
            
        elif divisible_by(i, fizz):
            print("Fizz")

        elif divisible_by(i, buzz):
            print("Buzz")

        else:
            print(i)


fizz_buzz(3, 5, 100)