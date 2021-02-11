def iseven(n: int) -> bool:
    return True if n % 2 == 0 else False


def isprime(n: int) -> bool:
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


print(iseven(10))
