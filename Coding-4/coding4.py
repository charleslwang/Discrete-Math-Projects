# COMS3203 DISCRETE MATHEMATICS
# CODING ASSIGNMENT 4

# YOUR NAME(s): Charles Wang
# YOUR UNI(s): clw2198

'''
Returns the GCD of two integers using Euclid's algorithm. Also prints out the
intermediate steps for Euclid's Algorithm on num1 and num2.

Parameters:
num1 (int): First number for the GCD
num2 (int): Second number for the GCD

Returns:
int: GCD of num1 and num2
'''
def euclid(num1, num2):
    a, b = num1, num2

    if b == 0:
        gcd = a
        print(f"GCD({a}, {b}) = {gcd}", end="\n")
        return gcd
    else:
        print(f"GCD({a}, {b}) = ", end="")
        return euclid(b, a % b)

'''
Returns a list of prime numbers up to (and including) a certain input integer, n.

Parameters:
n (int): The target number to generate primes up to.

Returns:
list: List of all prime numbers <= n.
'''
def prime_gen(n):

    primes = [1 for i in range(n+1)]
    primes[0] = primes[1] = 0
    list = []

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = 0

    # Return a list of all prime numbers up to n
    for i in range(2, n+1):
        if primes[i]:
            list.append(i)

    return list

'''
Returns a list of two prime integers that sum up to n.

Parameters:
n (int): The target even integer to check Goldbach's Conjecture for.

Returns:
list: A list of length 2 containing 2 ints that sum up to n.
'''
def check_goldbach(n):

    list = []
    primes = prime_gen(n);

    for i in range(0, len(primes) - 1):
        for a in range(i, len(primes) - 1):
            if primes[i]+primes[a] == n:
                list.append(primes[i])
                list.append(primes[a])
                return list
            else:
                continue

    return list

### DO NOT TURN IN AN ASSIGNMENT WITH ANYTHING BELOW HERE MODIFIED ###
if __name__ == '__main__':
    print("#######################################")
    print("Welcome to Coding 4: Number theory!")
    print("#######################################")
    print()

    print("---------------------------------------")
    print("PART A: Euclid's Algorithm")
    print("---------------------------------------")
    euclid_test_1 = [252, 105]
    print("Test Case 1: GCD of", euclid_test_1[0], "and", euclid_test_1[1])
    print("Test Case 1 Steps: ")
    student_ans = euclid(euclid_test_1[0], euclid_test_1[1])
    print("Test Case 1 (Your Answer):", student_ans)
    print("Test Case 1 (Correct Answer):", 21)
    print("Test Case 1:", ("# PASSED! #" if student_ans == 21  else "# INCORRECT #"))
    print()
    euclid_test_2 = [1071, 462]
    print("Test Case 2: GCD of", euclid_test_2[0], "and", euclid_test_2[1])
    print("Test Case 2 Steps: ")
    student_ans = euclid(euclid_test_2[0], euclid_test_2[1])
    print("Test Case 2 (Your Answer):", student_ans)
    print("Test Case 2 (Correct Answer):", 21)
    print("Test Case 2:", ("# PASSED! #" if student_ans == 21  else "# INCORRECT #"))
    print()
    euclid_test_3 = [85523, 3212]
    print("Test Case 3: GCD of", euclid_test_3[0], "and", euclid_test_3[1])
    print("Test Case 3 Steps: ")
    student_ans = euclid(euclid_test_3[0], euclid_test_3[1])
    print("Test Case 3 (Your Answer):", student_ans)
    print("Test Case 3 (Correct Answer):", 1)
    print("Test Case 3:", ("# PASSED! #" if student_ans == 1  else "# INCORRECT #"))
    print("---------------------------------------")

    print("PART B: Prime Number Generation")
    print("---------------------------------------")
    prime_gen_test_1 = 42
    prime_gen_test_1_ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    print("Test Case 1: Prime Numbers Up To:", prime_gen_test_1)
    print("Test Case 1 (Your Answer):", prime_gen(prime_gen_test_1))
    print("Test Case 1 (Correct Answer):", prime_gen_test_1_ans)
    print("Test Case 1:", ("# PASSED! #" if prime_gen(prime_gen_test_1) == prime_gen_test_1_ans  else "# INCORRECT #"))
    print()
    prime_gen_test_2 = 314
    prime_gen_test_2_ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
    47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
    131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
    293, 307, 311, 313]
    print("Test Case 2: Prime Numbers Up To:", prime_gen_test_2)
    print("Test Case 2 (Your Answer):", prime_gen(prime_gen_test_2))
    print("Test Case 2 (Correct Answer):", prime_gen_test_2_ans)
    print("Test Case 2:", ("# PASSED! #" if prime_gen(prime_gen_test_2) == prime_gen_test_2_ans  else "# INCORRECT #"))
    print()
    prime_gen_test_3 = 884
    prime_gen_test_3_ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
    113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
    199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
    293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
    397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487,
    491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
    601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
    701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
    821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883]
    print("Test Case 3: Prime Numbers Up To:", prime_gen_test_3)
    print("Test Case 3 (Your Answer):", prime_gen(prime_gen_test_3))
    print("Test Case 3 (Correct Answer):", prime_gen_test_3_ans)
    print("Test Case 3:", ("# PASSED! #" if prime_gen(prime_gen_test_3) == prime_gen_test_3_ans  else "# INCORRECT #"))
    print("---------------------------------------")

    print("PART C: Goldbach's Conjecture")
    print("---------------------------------------")
    goldbach_test_1 = 8
    goldbach_test_1_ans = [3, 5]
    student_ans = check_goldbach(goldbach_test_1)
    print("Test Case 1: 2 Primes For:", goldbach_test_1)
    print("Test Case 1 (Your Answer):", check_goldbach(goldbach_test_1))
    print("Test Case 1 (A Correct Answer):", goldbach_test_1_ans)
    print("Test Case 1:", ("# PASSED! #" if student_ans[0] + student_ans[1] == goldbach_test_1  else "# INCORRECT #"))
    print()
    goldbach_test_2 = 482
    goldbach_test_2_ans = [3, 479]
    student_ans = check_goldbach(goldbach_test_2)
    print("Test Case 2: 2 Primes For:", goldbach_test_2)
    print("Test Case 2 (Your Answer):", check_goldbach(goldbach_test_2))
    print("Test Case 2 (A Correct Answer):", goldbach_test_2_ans)
    print("Test Case 2:", ("# PASSED! #" if student_ans[0] + student_ans[1] == goldbach_test_2  else "# INCORRECT #"))
    print()
    goldbach_test_3 = 1152
    goldbach_test_3_ans = [23, 1129]
    student_ans = check_goldbach(goldbach_test_3)
    print("Test Case 3: 2 Primes For:", goldbach_test_3)
    print("Test Case 3 (Your Answer):", check_goldbach(goldbach_test_3))
    print("Test Case 3 (A Correct Answer):", goldbach_test_3_ans)
    print("Test Case 3:", ("# PASSED! #" if student_ans[0] + student_ans[1] == goldbach_test_3  else "# INCORRECT #"))
    print("---------------------------------------")
