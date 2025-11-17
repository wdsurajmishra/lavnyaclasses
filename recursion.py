# def factorial(n):
#     """Calculate the factorial of a non-negative integer n using recursion.

#     Args:
#         n (int): A non-negative integer whose factorial is to be calculated.

#     Returns:
#         int: The factorial of the given integer n.
#     Raises:
#         ValueError: If n is a negative integer.
#     """

#     if n < 0:
#         raise ValueError("Factorial is not defined for negative integers.")
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)


# print(factorial(5))  # Output: 120


nums = [i for i in range(1, 11)]

name = "Suraj"

print(name if name == "Suraj" else "Not Suraj")

# count = 1

# while True:
#     if count == 11:
#         break
#     nums.append(count)
#     count += 1

print(nums)