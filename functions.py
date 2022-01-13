import random

def number_guess(num):
    if num == 42:
        print('True')
    else:
        print('False')

def find_lowest(numlist):
    lowest=numlist[0]
    for num in numlist:
        if num < lowest:
            lowest=num
    return(lowest)

def find_shortest(stringlist):
    shortest_length=len(stringlist[0])
    shortest_string=stringlist[0]
    for string in stringlist:
        if len(string) < shortest_length:
            shortest_length=len(string)
            shortest_string=string
    return(shortest_string)

def range_value(high,low,numlist):
    range_list=[]
    for num in numlist:
        if num > low and num < high:
            range_list.append(num)
    return(range_list)

def password_strength(password):
    caps=0
    lower=0
    num=0
    special=0
    for letter in password:
        if letter.isupper():
            caps=1
        elif letter.islower(): 
            lower=1
        elif letter in ['0','1','2','3','4','5','6','7','8','9']:
            num=1
        else:
            special=1

    if (len(password) <= 6 or caps != 1 or lower != 1 or num != 1 or special != 1):
        print("Weak Password")
    else:
        print("Strong Password")

number_guess(random.randint(40,45))

numlist=[1,3,5,6,2,6,8,9,2,34,5,23,56,2,4]
print(find_lowest(numlist))

stringlist=["dev","sabina","suvan","reva"]
print(find_shortest(stringlist))

print(range_value(30,5,numlist))
        

password_strength("Test3123!")
