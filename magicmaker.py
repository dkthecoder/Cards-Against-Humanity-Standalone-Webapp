import random
import hashlib

#generates random numebrs
#INPUT: start of range, end of range, number of numbers to generate
def random_number_generator(start, end, num):
    random.seed()
    nums = []
    for i in range(num):
        nums.append(random.randint(start, end))
    return nums

#generate numbers from string
#INPUT: a given word
def numbers_from_word(word):
    hashed = int(hashlib.sha256(word.encode('UTF-8')).hexdigest(), base=16)
    random.seed(hashed)
    nums = random_number_generator(0, len(word), len(word))
    return nums