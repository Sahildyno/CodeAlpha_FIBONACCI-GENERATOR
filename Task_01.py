def fibonacci_recursive(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage
n = 10
print([fibonacci_recursive(i) for i in range(1, n + 1)])
