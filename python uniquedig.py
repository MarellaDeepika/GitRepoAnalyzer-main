def isUnique(n):
    """Check if all digits in the number are unique."""
    digits = str(n)
    return len(set(digits)) == len(digits)
def countUniqueDigitNumbers(n1, n2):
    """Count numbers with all unique digits in the given range [low, high]."""
    count = 0
    for number in range(n1, n2 + 1):
        if isUnique(number):
            count += 1
    return count
n1=int(input())
n2=int(input())
print(countUniqueDigitNumbers(n1, n2))
``