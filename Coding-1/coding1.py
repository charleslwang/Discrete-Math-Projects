# COMS3203 DISCRETE MATHEMATICS
# CODING ASSIGNMENT 1

# YOUR NAME(s): Charles Wang
# YOUR UNI(s): clw2198

'''
Counts the number of vowels in a given string.
Parameters:
s (string): lowercase string without spaces, numbers, or special characters.
Returns:
int: number of vowels in s
'''
#This project is complete.
def vowel_counter(s):
    # WRITE YOUR CODE HERE

    x = 0
    for letter in s:
        if letter in list('aeiou'):
            x += 1

    return x

'''
Counts the number of vowels in a given string, implementing the sometimes 'y' rule.
Parameters:
s (string): lowercase string without spaces, numbers, or special characters.
Returns:
bool: whether 'y' is in the string or not
int: number of vowels without the 'y' rule
int: number of vowels with the 'y' rule
'''
def sometimes_y(s):
    # WRITE YOUR CODE HERE

    a = vowel_counter(s)
    b = a
    existsY = False

    for letter in s:
        if (letter == 'y'):
            existsY = True

    if(len(s) - 1 >= 0):
        if (s[len(s) - 1] == 'y'):
            b += 1

# y is in string (bool), number of vowels orginally in string (int), number of vowels with y rule (int)
    return existsY, a, b

'''
Counts the number of vowels in each word within a sentence.
Parameters:
sentence (string): a string of words separated by spaces, with punctuation but without numbers. Capital letters are allowed.
Returns:
list: a list containing the number of vowels in each word in the sentence
'''
def sentence_counter(sentence):
    # WRITE YOUR CODE HERE

    vowels = []
    word = ""
 
    for letter in sentence:

        if(letter not in list(".,!? ")):
            word += letter

        if(letter == " "):
            vowels.append(sometimes_y(word.lower())[2])
            word = ""
    
    vowels.append(sometimes_y(word.lower())[2]) 
    
    return vowels
# list containing number of vowels for each word (list)

'''
Returns a code decoder dictionary
Parameters: 
secret_alphabet (string): a 26 letter string of unique characters without spaces.
Returns:
dict: a dictionary mapping from each secret language letter to its english alphabet equivalent.
'''
def create_code(secret_alphabet):
    # WRITE YOUR CODE HERE
    decoder = {}
    alpha = "abcdefghijklmnopqrstuvwxyz"
    index = 0

    for x in secret_alphabet:
        decoder[x] = alpha[index]
        index += 1

    return decoder # dict

'''
Returns the decoded version of a string using a decoder dictionary
Parameters:
decoder (dict): a dictionary mapping from each secret language letter to its english alphabet equivalent.
encoded_word (str): a string made up only of characters in the secret language.
Returns:
str: the decoded word.
'''
def decode(decoder, encoded_word):
    # WRITE YOUR CODE HERE
    decoded_word = ""

    for letter in encoded_word:
        decoded_word += decoder[letter]

    return decoded_word # str

'''
Returns an integer that is the nth Fibonacci number.
Parameters:
n (int): The nth Fibonacci number you want.
Returns:
int: the nth fibonacci number.
'''
def recursive_fib(n):
    # WRITE YOUR CODE HERE
    if(n <= 1):
        return n
    fib_n = recursive_fib(n-1) + recursive_fib(n-2)
    return fib_n # int

'''
Returns an integer that is the nth Fibonacci number.
Parameters:
n (int): The nth Fibonacci number you want.
Returns:
int: the nth fibonacci number.
'''
def iterative_fib(n):
    # WRITE YOUR CODE HERE
    fib_n, second = 0, 1
    for x in range(n):
        fib_n, second = second, fib_n + second

    return fib_n # int

######################################################################
### DO NOT TURN IN AN ASSIGNMENT WITH ANYTHING BELOW HERE MODIFIED ###
######################################################################
if __name__ == '__main__':
    print("#######################################")
    print("Welcome to Coding 1: Python Introduction!")
    print("#######################################")
    print()

    print("---------------------------------------")
    print("PART A: Vowel Counting")
    print("---------------------------------------")
    
    print("---------------------------------------")
    print("\'vowel_counter\' Tests")
    print("---------------------------------------")
    
    vowel_counter_tests = ['apple', 'cake', 'zzzz', 'aeiou', 'pneumonoultramicroscopicsilicovolcanoconiosis']
    vowel_counter_answers = [2, 2, 0, 5, 20]
    
    for count, test in enumerate(vowel_counter_tests):
        if (vowel_counter(vowel_counter_tests[count]) == vowel_counter_answers[count]):
          passed = 'PASSED!'
        else:
          passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {vowel_counter_answers[count]}')
        print(f'Your Answer: {vowel_counter(vowel_counter_tests[count])}')
        
        
    print("---------------------------------------")
    print("\'sometimes_y\' Tests")
    print("---------------------------------------")
    
    sometimes_y_tests = ['apple', 'syzygy', 'zzzz', 'aeiouy', 'pneumonoultramicroscopicsilicovolcanoconiosis', 'yellow', 'yesterday', 'y']
    sometimes_y_answers = [(False, 2, 2), (True, 0, 1), (False, 0, 0), (True, 5, 6), (False, 20, 20), (True, 2, 2), (True, 3, 4), (True, 0, 1)]

    for count, test in enumerate(sometimes_y_tests):
        if (sometimes_y(sometimes_y_tests[count]) == sometimes_y_answers[count]):
          passed = 'PASSED!'
        else:
          passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {sometimes_y_answers[count]}')
        print(f'Your Answer: {sometimes_y(sometimes_y_tests[count])}')
        
    print("---------------------------------------")
    print("\'sentence_counter\' Tests")
    print("---------------------------------------")
    
    sentence_counter_tests = ['The boy, Sam, walked to the store.',
                              'Hello, how are you?',
                              'On a sunny day, the funny, punny bunny ran up the hill.',
                              'I went to office hours, and the TAs were so friendly!!!']

    sentence_counter_answers = [[1, 2, 1, 2, 1, 1, 2],
                                [2, 1, 2, 2],
                                [1, 1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1],
                                [1, 1, 1, 3, 2, 1, 1, 1, 2, 1, 3]]
    
      
    for count, test in enumerate(sentence_counter_tests):
        if (sentence_counter(sentence_counter_tests[count]) == sentence_counter_answers[count]):
          passed = 'PASSED!'
        else:
          passed = 'FAILED!'
        
        print("Test #{}: {}".format(count + 1, passed))   
        print(f'Correct Answer: {sentence_counter_answers[count]}')
        print(f'Your Answer: {sentence_counter(sentence_counter_tests[count])}')
        
    print("---------------------------------------")
    print("\'create_code\' Tests")
    print("---------------------------------------")
        
    alphabet_1 = 'Hh!@mbM*()QWERTYUIOPASDFGZ'
    decoder_1={'H': 'a', 
              'h':'b',
              '!':'c',
              '@': 'd', 
              'm': 'e', 
              'b': 'f',
              'M': 'g', 
              '*': 'h', 
              '(': 'i',
              ')':'j',
              'Q': 'k', 
              'W': 'l', 
              'E':'m',
              'R': 'n', 
              'T': 'o', 
              'Y':'p', 
              'U': 'q', 
              'I':'r',
              'O': 's', 
              'P':'t',
              'A':'u',
              'S':'v', 
              'D': 'w', 
              'F': 'x', 
              'G': 'y',
              'Z': 'z'}
    
    alphabet_2 = 'Hh!@mbM*()qwertyUIOPAS5FGZ'
    decoder_2={'H': 'a', 
              'h':'b',
              '!':'c',
              '@': 'd', 
              'm': 'e', 
              'b': 'f',
              'M': 'g', 
              '*': 'h', 
              '(': 'i',
              ')':'j',
              'q': 'k', 
              'w': 'l', 
              'e':'m',
              'r': 'n', 
              't': 'o', 
              'y':'p', 
              'U': 'q', 
              'I':'r',
              'O': 's', 
              'P':'t',
              'A':'u',
              'S':'v', 
              '5': 'w', 
              'F': 'x', 
              'G': 'y',
              'Z': 'z'}
    
    create_code_tests = [alphabet_1, alphabet_2]
    create_code_answers = [decoder_1, decoder_2]
    
    for count, test in enumerate(create_code_tests):
        if (create_code(create_code_tests[count]) == create_code_answers[count]):
          passed = "PASSED!"
        else:
          passed = "FAILED!"
          
        print("Test #{}: {}".format(count + 1, passed)) 
        print(f'Correct Answer: {create_code_answers[count]}')
        print(f'Your Answer: {create_code(create_code_tests[count])}')
        
    print("---------------------------------------")
    print("\'decode\' Tests")
    print("---------------------------------------")
    
    decode_tests = [[decoder_1, '@TM'], [decoder_2, '!HP']]
    decode_answers = ['dog', 'cat']
    
    for count, test in enumerate(decode_tests):
        if (decode(decode_tests[count][0], decode_tests[count][1]) == decode_answers[count]):
          passed = 'PASSED!'
        else:
          passed = 'FAILED!'
          
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {decode_answers[count]}')
        print(f'Your Answer: {decode(decode_tests[count][0], decode_tests[count][1])}')
        print()
      
    print("---------------------------------------")
    print("PART B: Fibonacci")
    print("---------------------------------------")
    tests = [[1, 1], [4, 4], [10, 10]]
    answers = [[1, 1], [3, 3], [55, 55]]
    for count, test in enumerate(tests):
        if(answers[count][0] == recursive_fib(test[0]) and
            answers[count][1] == iterative_fib(test[1])):
            passed = "PASSED!"
        else:
            passed = "FAILED!"

        print("Test #{}: {}".format(count + 1, passed))
        print("Recursive Fibonacci (Correct): ", answers[count][0])
        print("Recursive Fibonacci (Your Answer): ", recursive_fib(test[0]))
        print("Iterative Fibonacci (Correct): ", answers[count][1])
        print("Iterative Fibonacci (Your Answer): ", iterative_fib(test[1]))