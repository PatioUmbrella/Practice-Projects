import pandas as pd
import time

Q1 ='what show was bob barker on?'
A1 ='the price is right'

Q2 = 'what has a larger population, italy or brazil?'
A2 = 'brazil'

Q3 = 'who wrote the novel "IT"?'
A3 = 'stephen king'

Q4 = 'what is the name of the ship that rescued the people of the titanic shipwreck'
A4 = 'carpathia'

Q5 = 'who was the 33rd president of the united states'
A5 = 'harry truman'

Q6 = 'name one member of atribe called quest'
A6a = 'q-tip'
A6b = 'phife dawg'
A6c = 'ali shaheed muhammad'
A6d = 'jarobi white'

Q7 = 'who directed da five bloods'
A7 = 'spike lee'

Q8 = 'who is the main character of the da vinci code'
A8 = 'robert langdon'

Q9 = 'who was the first emporer of japan'
A9 = 'jimmu'

Q10 = 'what single-celled reproductive unit is capable of giving rise to a new organism without sexual fusion'
A10 = 'spore'

df_base = [[Q1,A1], [Q2, A2], [Q3, A3]]

right = 0
wrong = 0

print('Please keep all answers in lowercase and be specific!')

print(Q1)
user_answer = input()
if user_answer == A1:
    right += 1
    print('right')
else:
    wrong += 1
    print('wrong')
time.sleep(1.8)

print(Q2)
user_answer = input()
if user_answer == A2:
    right += 1
    print('right')
else:
    wrong += 1
    print('wrong')
time.sleep(1.8) 

print(Q3)
user_answer = input()
if user_answer == A3:
    right += 1
    print('right')
else:
    wrong += 1
    print('wrong')
time.sleep(1.8)

print(Q4)
user_answer = input()
if user_answer == A4:
    right += 1
    print('right')
else:
    wrong += 1
    print('wrong')
time.sleep(1.8)

print(Q5)
user_answer = input()
if user_answer == A5:
    right += 1
    print('right')
else:
    wrong += 1
    print('wrong')
time.sleep(1.8)

print(Q6)
user_answer = input()
if (user_answer == A6a) or (user_answer == A6b) or (user_answer == A6c) or (user_answer == A6d):
    right += 1
    print('right')
else:
    wrong += 1
    print('wrong')
time.sleep(1.8)

print(Q7)
user_answer = input()
if user_answer == A7:
    right += 1
    print('right')
else:
    wrong += 1
    print('wrong')
time.sleep(1.8)

print(Q8)
user_answer = input()
if user_answer == A8:
    right += 1
    print('right')
else:
    wrong += 1
    print('wrong')
time.sleep(1.8)

print(Q9)
user_answer = input()
if user_answer == A9:
    right += 1
    print('right')
else:
    wrong += 1
    print('wrong')
time.sleep(1.8)

print(Q10)
user_answer = input()
if user_answer == A10:
    right += 1
    print('right')
else:
    wrong += 1
    print('wrong')
time.sleep(1.8)

print("You got this many answers right: " + str(right))
print("You got this many answers wrong: " + str(wrong))