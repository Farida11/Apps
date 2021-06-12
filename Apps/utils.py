# A function return nвЂ™th number of Fibonacci sequence
def fibonacci(n):
    if isinstance(n, str) or isinstance(n, bool):
       return print("Input not in correct format. Please, input a number")
    elif n == 0 or n == 1:
        return print("fibonacci(", n, ") = ", n)
    elif n > 1 and not isinstance(n, float):
        left, right, result = 1, 0, 0
        for i in range(1, n):
            result = left + right
            right = left
            left = result
        return print("fibonacci(", n, ") = ", result)
    else:
        return print("The value must be a positive integer.")


fibonacci(True)
fibonacci('f')
fibonacci(1.2)
fibonacci(0)
fibonacci(1)
fibonacci(2)
fibonacci(3)
fibonacci(4)
fibonacci(5)
fibonacci(6)
fibonacci(7)
fibonacci(8)
fibonacci(9)
fibonacci(-9)
