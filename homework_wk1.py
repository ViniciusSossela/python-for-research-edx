# Exercise 1a
import string
alphabet = string.ascii_letters

alphabet


# Exercise 1b
sentence = 'Jim quickly realized that the beautiful gowns are expensive'
count_letters = {}
for letter in sentence:
    if letter in alphabet:
        if letter in count_letters:
            count_letters[letter] += 1
        else:
            count_letters[letter] = 1

count_letters


# Exercise 1c
def counter(sentence):
    if type(sentence) is str:
        count_letters = {}
        sentence = str().join(s for s in sentence if s.isalnum())
    
        for letter in sentence:
            if letter in count_letters:
                count_letters[letter] += 1
            else:
                count_letters[letter] = 1
        return count_letters
    return {}

counter(sentence)


# Exercise 1d
address = """Four score and seven years ago our fathers brought forth on this continent, a new nation, 
conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a 
great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. 
We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final 
resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper 
that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- 
this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add 
or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. 
It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so 
nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored 
dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here 
highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of 
freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."""   

address_count = counter(address)
address_count


# Exercise 1f
list({k: v for k, v in sorted(address_count.items(), key=lambda item: item[1])})[-1]


# Exercise 2a
import math
math.pi / 4


# Exercise 2b
import random

random.seed(1)

def rand():
   return random.uniform(-1,1)

rand()


# Exercise 2c
def distance(x, y):
    x1 = x[0]
    x2 = x[1]
    y1 = y[0]
    y2 = y[1]
    return math.sqrt((x1 - y1)**2 + (x2 - y2)**2)

distance((0,0), (1,1))


# Exercise 2c
def in_circle(x, origin = [0,0]):
    _isLessThanOne = distance(x, origin) < 1
    return _isLessThanOne

in_circle([1,1])


# Exercise 2e
random.seed(1) 

R = 10000
inside = []
for i in range(R): 
    inside.append(in_circle([rand(), rand()]))
    
allTrues = list(filter(lambda x: x, inside))

insideAmount = len(allTrues)

insideAmount / R


# Exercise 2f
(math.pi / 4) - (insideAmount / R)


# Exercise 3a
def moving_window_average(x, n_neighbors=1):
    n = len(x) #6
    width = n_neighbors*2 + 1 #3
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    return [sum(x[i:(i+width)]) / width for i in range(n)]

x = [0,10,5,3,1,5]
averages = moving_window_average(x, 1)

averages


# Exercise 3b
R = 1000
x = [random.uniform(0, 1) for i in range(0, 1000)]
Y = [x] + [moving_window_average(x, n_neighbors) for n_neighbors in range(1, 10)]
len(Y)


# Exercise 3c
ranges = [max(x)-min(x) for x in Y]
ranges