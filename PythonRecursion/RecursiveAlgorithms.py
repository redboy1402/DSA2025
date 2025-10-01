import functools
from linecache import cache


def factorialIterative(n: int) -> int:
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Invalid input")
    nFactorial = 1
    for i in range (n, 1, -1):
        nFactorial *= i
    return nFactorial

def factorialRecursive(n: int) -> int:
    factorial = 1

    if n < 0:
        raise ValueError("Import must not be negative")
    if n != 0:
        factorial = n * factorialRecursive(n - 1)
    return factorial

def fibonnacciIterative(n: int) -> int:
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Invalid import")
    fibVal = 0
    currVal = 1
    lastVal = 0

    if n == 0:
        fibVal = 0
    elif n == 1:
        fibVal = 1
    else:
        for i in range(2, n + 1):
            fibVal += currVal + lastVal
            lastVal = currVal
            currVal = fibVal
    return fibVal

def fibonnacciRecursive(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("Import must be int")

    if n == 0:
        fibVal = 0
    elif n == 1:
        fibVal = 1
    else:
        fibVal = fibonnacciRecursive(n - 1) + fibonnacciRecursive(n - 2)
    return fibVal

# algorithm found at https://math.stackexchange.com/questions/111150/changing-a-number-between-arbitrary-bases
# and modified to suit a programmatic approach
def convertBase(n, targetBase) -> str:
    if targetBase not in range(2,17):
        raise ValueError("Target base must be between 2 and 16")
    if not isinstance(n, int):
        raise ValueError("Import be int")
    if n < 0:
        return "-" + convertBase(-n, targetBase)
    values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if n >= targetBase:
        return f'{convertBase(n // targetBase, targetBase)}{values[int(n % targetBase)]}'
    else:
        return values[int(n)]


#source: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
#uses the Euclidean Algorithm to recursively simplify the GCD until we arrive at 2 numbers which have modulo 0, and thus have found the GCD
def GCD(a, b) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        if a < b:
            a, b = b, a
        a = a%b
        return GCD(b, a)


def towers(n: int) -> None:
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Import must be non-negative int")
    _hanoiTowers(n, 1, 3, 0)

def _hanoiTowers(n, src, dest, recursion):
    def moveDisk():
        print("\t" * recursion + f"Recursion Level: {recursion}")
        print("\t" * recursion + f"Moving disk {n} from source {src} to destination {dest} ")
        print("")

    recursion += 1
    if n == 1:
        moveDisk()
    else:
        tmp = 6 - src - dest
        _hanoiTowers(n-1, src, tmp, recursion)
        moveDisk()
        _hanoiTowers(n-1, tmp, dest, recursion)


def main():
   print(GCD(5.3, 10))

if __name__ == "__main__":
    main()