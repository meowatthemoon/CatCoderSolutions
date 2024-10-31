import math

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    for a in range(5, int(math.sqrt(number)) + 1, 6):
        if number % a == 0 or number % (a + 2) == 0:
            return False
    return True

def count_deletable(number) -> int:
    str_number : str = str(number)
    n_digits = len(str_number)

    if n_digits == 1:
        return 1 if is_prime(number) else 0

    count = 0
    for i in range(n_digits):
        new_number = int(str_number[:i] + str_number[i + 1:])
        if not is_prime(new_number):
            continue
        count += count_deletable(new_number)
    return count


if __name__ == '__main__':
    deletable = int(input("Input:"))
    count = count_deletable(deletable)
    print(count)
