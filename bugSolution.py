def improved_function_with_error_handling(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        return result
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

# Example demonstrating improved error handling
result1 = improved_function_with_error_handling(5, "hello")
print(f"Result 1: {result1}")  # Output: Error: Inputs must be numbers

result2 = improved_function_with_error_handling(5, 0)
print(f"Result 2: {result2}")  # Output: Error: Cannot divide by zero

result3 = improved_function_with_error_handling(10, 2)
print(f"Result 3: {result3}")  # Output: Result 3: 5.0