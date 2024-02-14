# 02/12/2024 start_time: 19:22


"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""


# By converting Int to string very easy solution
def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


# lets try without converting int to String
def is_palindrome_2(x: int) -> bool:
    if x < 0 :
        return False
    div = 1
    while x >= 10 * div:
        div *= 10
    while x:
        print("Divider", div)
        print("x", x)
        right = x % 10
        left = x // div
        print(f"Right: {right}, left: {left}")
        if left != right:
            return False
        x = (x % div) // 10
        div = div / 100
    return True



print(is_palindrome_2(121))