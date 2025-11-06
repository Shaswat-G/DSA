def fibonacci(n: int) -> int:

    if n <= 1:
        return n

    nth_term = fibonacci(n - 1) + fibonacci(n - 2)

    return nth_term


def fibonacci_memo(n: int) -> int:

    memo_table = [-1] * (n + 1)
    memo_table[0] = 0
    memo_table[1] = 1

    def rec_helper(n: int) -> int:
        if memo_table[n] == -1:
            memo_table[n] = rec_helper(n - 1) + rec_helper(n - 2)
        return memo_table[n]

    return rec_helper(n)


def fibonacci_tabulation(n: int) -> int:

    if n <= 1:
        return n

    prev_1 = 1
    prev_2 = 0

    for _ in range(n - 1):
        cur = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = cur

    return cur


def main():
    n = int(input("Enter 'N' for Fibonacci sequence \n"))
    print(f"Fibonnaci of {n} is : {fibonacci_tabulation(n)}")


if __name__ == "__main__":
    main()
