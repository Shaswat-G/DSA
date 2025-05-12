def factorial(num: int) -> int:
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


def fibonacci(term: int) -> int:
    if term <= 1:
        return term
    else:
        return fibonacci(term - 1) + fibonacci(term - 2)


def mininmum_array(array: list) -> int:
    if len(array) == 1:
        return array[0]
    else:
        return min(array[0], mininmum_array(array[1:]))


def sum_of_array(array: list) -> int:
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + sum_of_array(array[1:])


def check_palindrome(string: str) -> bool:
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]:
            return check_palindrome(string[1:-1])
        else:
            return False


def reverse_string(string: str) -> str:
    if len(string) == 1:
        return string[0]
    elif len(string) == 0:
        return ""
    else:
        return string[-1] + reverse_string(string[:-1])


def binary_search(array: list, search_item) -> int:
    # assume ascending
    if len(array) % 2 == 0:
        # even
        right_middle = len(array) / 2
        left_middle = right_middle - 1
        if search_item < array[left_middle]:
            return binary_search(array[:left_middle], search_item)
        elif search_item > array[right_middle]:
            return binary_search(array[right_middle:], search_item)
        else:
            if search_item == array[left_middle]:
                return left_middle
            elif search_item == array[right_middle]:
                return right_middle
    else:
        # odd
        middle = int((len(array) - 1) / 2)
        if search_item == array[middle]:
            return middle
        elif search_item < array[middle]:
            return binary_search(array[:middle], search_item)
        else:
            return binary_search(array[middle + 1 :], search_item)


def main():
    num = 5
    print(f"Factorial of {num} is {factorial(num)}")

    num = 10
    sequence = ", ".join([str(fibonacci(i)) for i in range(num)])
    print(f"Fibonaaci Sequence for {num} is {sequence}")

    array = [3, 1, 7, 4, 0, 1, 6]
    print(f" Original sum {sum(array)} and {sum_of_array(array)}")
    print(f" Minimum is {min(array)} and {mininmum_array(array)}")
    print(f" Binary search for 3 is {binary_search(sorted(array), 3)}")

    string = "hello!"
    print(f"Reversed String : {reverse_string(string)}")
    print(f"Check if {string} is a palindrome : {check_palindrome(string)}")

    string = "borroworrob"
    print(f"Check if {string} is a palindrome : {check_palindrome(string)}")


main()
