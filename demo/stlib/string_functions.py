# String functions

def hasupper(st):
    """
    Returns true if the given string has any uppercase letter otherwise false
    """
    for c in st:
        if c.isupper():
            return True

    return False


def countdigits(st):
    count = 0
    for c in st:
        if c.isdigit():
            count += 1

    return count


if __name__  == '__main__':
   print("String Functions 1.0")
