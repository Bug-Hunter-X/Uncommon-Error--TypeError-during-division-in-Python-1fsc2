def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid input types")
        return None

# Example demonstrating TypeError
result1 = function_with_uncommon_error(5, "hello")  # TypeError
print(f"Result 1: {result1}")

# Example demonstrating ZeroDivisionError
result2 = function_with_uncommon_error(5, 0)  # ZeroDivisionError
print(f"Result 2: {result2}")

# Example demonstrating correct behavior
result3 = function_with_uncommon_error(10, 2)  # Correct behavior
print(f"Result 3: {result3}")