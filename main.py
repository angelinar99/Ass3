
"""
Upper and Lower
"""
# Task1
# Provide your solution here
def count_upper_lower(string):
    upper_count = 0
    lower_count = 0

    for char in string:

        if char.isupper():
            upper_count += 1

        elif char.islower():
            lower_count += 1

    print("No. of Upper case characters:", upper_count)
    print("No. of Lower case characters:", lower_count)

count_upper_lower("Hello World")

"""
Check 33
"""
def has_33(numbers):
    for i in range(len(numbers)):
        if numbers[i] == 3 and numbers[i+1] == 3:
            return True
        return False

if __name__ == '__main__':
    call1 = [1, 3, 3]
    call2 = [1, 3, 1, 3]
    call3 = [3, 1, 3]

    print(has_33(call1))
    print(has_33(call2))
    print(has_33(call3))