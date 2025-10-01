from random import randint, seed

import StacksQueues as sq

def main():
    seed_val = 22120294
    seed(seed_val)
    with open("testing.txt", "w") as f:
        f.write("Seed: " + str(seed_val) + "\n")
        arr = [randint(0, 100) for _ in range(10)]
        f.write("DSA Testing\n")
        f.write("Test Array: " + str(arr) + "\n")
        f.write("Testing DSA Stack" + "\n")
        f.write("expected output: " + str(arr[::-1]) + "\n")
        stack = sq.DSAStack()
        for i in arr:
           stack.push(i)
        out = []
        while not stack.isEmpty():
            out.append(stack.pop())
        f.write("output: " + str(out) + "\n")
        f.write("Test Passed!" + "\n\n" if out == arr[::-1] else "Test Failed!" + "\n\n")

        f.write("Testing DSA Queues" + "\n")
        f.write("Testing DSA Shuffle Queue" + "\n")
        shuffle_queue = sq.DSAShufflingQueue()
        out = []
        for i in arr:
            shuffle_queue.push(i)
        while not shuffle_queue.isEmpty():
            out.append(shuffle_queue.pop())
        f.write("Expected output: " + str(arr) + "\n")
        f.write("Output: " + str(out) + "\n")
        f.write("Test Passed!" + "\n\n" if out == arr else "Test Failed!" + "\n\n")

        f.write("Testing DSA Circular Queue" + "\n")
        circle_queue = sq.DSACircularQueue()
        out = []
        for i in arr:
            circle_queue.push(i)
        while not circle_queue.isEmpty():
            out.append(circle_queue.pop())
        f.write("Expected Output: " + str(arr) + "\n")
        f.write("Output: " + str(out) + "\n")
        f.write("Test Passed!" + "\n\n" if out == arr else "Test Failed!" + "\n\n")

        f.write("Postfix Testing!\n")
        # (a + b) / (c - (d * e))
        nums = [randint(0, 100) for _ in range(5)]
        expression = f"( {nums[0]} + {nums[1]} ) / ( {nums[2]} - ( {nums[3]} * {nums[4]} ) )"
        f.write(f"Evaluating: {expression}" + "\n")
        expected = (nums[0] + nums[1]) / (nums[2] - (nums[3] * nums[4]))
        output = sq.eval_infix(expression)
        f.write(f"Expected value: {expected:.3f}\n")
        f.write(f"Actual value: {output:.3f}\n")
        f.write("Test Passed!" + "\n\n" if expected == output else "Test Failed!" + "\n\n")






if __name__ == '__main__':
    main()