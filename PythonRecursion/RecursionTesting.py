import random
import timeit
import RecursiveAlgorithms as ra

if __name__ == "__main__":
    startVal = 750
    maxTime = 0.1
    recursive_iterative_foos = [ra.factorialRecursive, ra.factorialIterative]

    f = open("output.txt", "w")

    #test recursive vs iterative functions
    for foo in recursive_iterative_foos:
        startTime = timeit.default_timer()
        currTime = timeit.default_timer()
        repeat = startVal
        while currTime - startTime < maxTime:
            foo(repeat)
            repeat += 1
            currTime = timeit.default_timer()
        f.write(f"{foo.__name__} from {startVal} to {repeat} finished in {(currTime - startTime):.3f} seconds.\n")

    #test GCD
    startTime = timeit.default_timer()
    currTime = timeit.default_timer()
    repeat = startVal
    while currTime - startTime < maxTime:
        ra.GCD(random.uniform(1, 1000000), random.uniform(1, 1000000))
        repeat += 1
        currTime = timeit.default_timer()
    f.write(f"{ra.GCD.__name__} found {repeat} GCD's of random pairs. finished in {(currTime - startTime):.3f} seconds.\n")

    #test Base Conversion
    startTime = timeit.default_timer()
    currTime = timeit.default_timer()
    repeat = startVal
    while currTime - startTime < maxTime:
        ra.convertBase(int(random.uniform(1, 1000)), int(random.uniform(2, 17)))
        repeat += 1
        currTime = timeit.default_timer()
    f.write(f"{ra.convertBase.__name__} converted {repeat} random values to random bases. finished in {(currTime - startTime):.3f} seconds.\n")

    f.close()