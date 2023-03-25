#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# COMS3203 DISCRETE MATHEMATICS
# CODING ASSIGNMENT 3
#
# Before submitting the file to gradescope make sure of the following:
# 1. The name of the file is coding3.py
# 2. Nothing below the line `if __name__="__main__":` is changed
# 3. Make sure there are no indentation errors and that the code compiles on your end
#
# YOUR NAME(S): Charles Wang
# YOUR UNI(S): clw2198

def is_onto(domain, co_domain, mapping):
    """Determines if the function is onto.

    Args:
        domain [list[int]]: a list of values in the domain
        co_domain [list[int]]: a list of values in the co-domain
        mapping [dict[int,int]]: a dictionary of the function mapping between the domain and co-domain

    Returns:
        meets_definition [bool]: 0 for False, 1 for True
    """

    meets_definition = 1;
    count = {}

    for i in co_domain:
        if i in mapping.values():
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        else:
            count[i] = 0

    for x in count:
        if count[x] == 0:
            meets_definition = 0;
            break;

    return meets_definition


def is_one_to_one(domain, co_domain, mapping):
    """Determines if the function is one-to-one.

    Args:
        domain [list[int]]: a list of values in the domain
        co_domain [list[int]]: a list of values in teh co-domain
        mapping [dict[int,int]]: a dictionary of the function mapping between the domain and co-domain

    Returns:
        meets_definition [bool]: 0 for False, 1 for True

    """

    count = {}
    for i in mapping.values():
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    meets_definition = all(count[x] == 1 for x in count)
    return meets_definition


def is_bijective(domain, co_domain, mapping):
    """Determines if the function is bijective.

    Args:
        domain [list[int]]: a list of values in the domain
        co_domain [list[int]]: a list of values in teh co-domain
        mapping [dict[int,int]]: a dictionary of the function mapping between the domain and co-domain

    Returns:
        meets_definition [bool]: 0 for False, 1 for True

    """
    # WRITE YOUR CODE HERE

    meets_definition = is_one_to_one(domain, co_domain, mapping) and is_onto(domain, co_domain, mapping)

    return meets_definition


def cookies_for_friends(cookie_shop, k):
    """Computes the minimum number of cookies that need to be purchased in
    order to guarantee that k friends get two of the same flavor of cookie.

    Args:
        cookie_shop [list[int]]: a list of how many of each cookie a shop has,
                                 where index 0 is chocolate chip, 1 is macademia nut,
                                 and 2 is oatmeal raisin
        k [int]: number of friends that you want to have two cookies of the same flavor

    Returns:
        min_cookies [int]: either the minimum number of cookies or -1 if impossible

    """

    min_cookies = 0

    if sum(cookie_shop) < 2 * k:
        return -1

    x = cookie_shop[0] // 2
    y = cookie_shop[1] // 2
    z = cookie_shop[2] // 2

    total = x+y+z

    while total > 0 and k > 0:
        k -= 1
        total -= 1
        min_cookies += 2

    return min_cookies + 2



######################################################################
### DO NOT TURN IN AN ASSIGNMENT WITH ANYTHING BELOW HERE MODIFIED ###
######################################################################
if __name__ == '__main__':
    print("#######################################")
    print("Welcome to Coding 3: Functions and PHP!")
    print("#######################################")
    print()
    print("---------------------------------------")
    print("PART A: Function Properties")
    print("---------------------------------------")

    example_1 = [[1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7], {1: 2, 2: 3, 3: 1, 4: 3}]  # not anything
    example_2 = [[1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7], {1: 2, 2: 3, 3: 1, 4: 5}]  # one to one (nothing else)
    example_3 = [[1, 2, 3, 4], [1, 2, 3], {1: 2, 2: 3, 3: 1, 4: 3}]  # onto (nothing else)
    example_4 = [[1, 2, 3, 4], [1, 2, 3, 4], {1: 2, 2: 3, 3: 1, 4: 4}]  # bijective

    print("---------------------------------------")
    print("\'is_onto\' Tests")
    print("---------------------------------------")
    is_onto_tests = [example_1, example_2, example_3, example_4]
    is_onto_answers = [False, False, True, True]

    for count, test in enumerate(is_onto_tests):
        if (is_onto(is_onto_tests[count][0], is_onto_tests[count][1],
                    is_onto_tests[count][2]) == is_onto_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"

        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_onto_answers[count]}')
        print(f'Your Answer: {is_onto(is_onto_tests[count][0], is_onto_tests[count][1], is_onto_tests[count][2])}')

    print("---------------------------------------")
    print("\'is_one_to_one\' Tests")
    print("---------------------------------------")
    is_one_to_one_tests = [example_1, example_2, example_3, example_4]
    is_one_to_one_answers = [False, True, False, True]

    for count, test in enumerate(is_one_to_one_tests):
        if (is_one_to_one(is_one_to_one_tests[count][0], is_one_to_one_tests[count][1],
                          is_one_to_one_tests[count][2]) == is_one_to_one_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"

        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_one_to_one_answers[count]}')
        print(
            f'Your Answer: {is_one_to_one(is_one_to_one_tests[count][0], is_one_to_one_tests[count][1], is_one_to_one_tests[count][2])}')

    print("---------------------------------------")
    print("\'is_bijective\' Tests")
    print("---------------------------------------")
    is_bijective_tests = [example_1, example_2, example_3, example_4]
    is_bijective_answers = [False, False, False, True]

    for count, test in enumerate(is_onto_tests):
        if (is_bijective(is_bijective_tests[count][0], is_bijective_tests[count][1],
                         is_bijective_tests[count][2]) == is_bijective_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"

        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_bijective_answers[count]}')
        print(
            f'Your Answer: {is_bijective(is_bijective_tests[count][0], is_bijective_tests[count][1], is_bijective_tests[count][2])}')

    print("---------------------------------------")
    print("PART B: Pigeon-hole Principle")
    print("---------------------------------------")

    cookie_shops = [[4, 5, 6], [10, 2, 3], [4, 2, 3], [5, 2, 4]]
    num_friends = [3, 2, 5, 1]
    answers = [8, 6, -1, 4]

    print("---------------------------------------")
    print("\'cookies_for_friends\' Tests")
    print("---------------------------------------")

    for count, test in enumerate(zip(cookie_shops, num_friends)):
        if cookies_for_friends(test[0], test[1]) == answers[count]:
            passed = 'PASSED!'
        else:
            passed = 'FAILED!'

        print(f"Test #{count + 1}: {passed}")
        print(f"Correct Answer: {answers[count]}")
        print(f"Your Answer: {cookies_for_friends(test[0], test[1])}")
