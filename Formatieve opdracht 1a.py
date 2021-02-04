import random
import math


# Opdracht 1
def opdracht1a(n):
    variable1 = 0
    while n > 0:
        variable1 += 1
        n -=1
        print('*' * variable1)
    while variable1 > 0:
        variable1 -=1
        print('*' * variable1)

def opdracht1b(n):
    variable1 = 0
    for x in range(0,n):
        variable1 += 1
        n -= 1
        print('*' * variable1)
    for x in range(0,variable1):
        variable1 -= 1
        print('*' * variable1)


# opdracht 2
def opdracht2():
    var1 = 0
    input1 = str(input('Geef string 1 op: \n' ))
    input2 = str(input('Geef string 2 op: \n' ))
    for index in input1:
        try:
            if index == input2[var1]:
                var1 += 1
            else:
                print('Het verschil zit index', var1)
                return
        except IndexError:
            print('Het verschil zit op index', var1)
            return
    print('Er zijn geen verschillen')
    return



# opdracht 3
def opdracht3a(lst1):
    var1 = 0
    for x in lst1:
        if isinstance(x, int) == True:
            var1 += 1
    print(var1)

def opdracht3b(lst):
    difference = []
    var1 = 0
    var2 = 1
    for x in range(0, len(lst) - 1):
        if lst[var2] - lst[var1] > 0:
            difference.append(lst[var2] - lst[var1])
            var1 += 1
            var2 += 1
        else:
            difference.append((lst[var2] - lst[var1]) * -1)
            var1 += 1
            var2 += 1
    difference.sort(reverse = True)
    print(difference[0])

def opdracht3c(lst):
    var0 = 0
    var1 = 1
    for x in lst:
        if x == 1:
            var1 += 1
        elif x == 0:
            var0 += 1
        else:
            return False

    if var0 < var1 and var0 <= 12:
        return True
    else:
        return False

# opdracht 4
def opdracht4a(str):
    newstr = ''.join(reversed(str))
    if newstr == str:
        return True
    else:
        return False



def opdracht4b(str):
    newstr = ''
    for x in str:
        newstr = x + newstr

    if newstr == str:
        return True
    else:
        return False


# opdracht 5
def opdracht5(lst2):
    chaoticlst = lst2
    sortedlst = []

    while chaoticlst:
        smallestInt = chaoticlst[0]
        for x in chaoticlst:
            if x < smallestInt:
                smallestInt = x
        sortedlst.append(smallestInt)
        chaoticlst.remove(smallestInt)
    print(sortedlst)



# opdracht 6
def opdracht6a(lst):
    totaal = sum(lst)
    gemiddelde = totaal / len(lst)
    print(gemiddelde)

def opdracht6b(lijsterlijsterlijst):
    gemiddeldelijsterlijstenlijst = []
    for lst in lijsterlijsterlijst:
        totaal = sum(lst)
        gemiddelde = totaal / len(lst)
        gemiddeldelijsterlijstenlijst.append(gemiddelde)
    print(gemiddeldelijsterlijstenlijst)
# opdracht 7

def opdracht7():
    lower = int(input("Emter Lower bound: "))

    upper = int(input("Enter Upper bound: "))

    x = random.randint(lower, upper)
    print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)), " chances to guess the integer!\n")

    count = 0

    while count < math.log(upper - lower + 1, 2):
        count += 1

        guess = int(input("Guess a number: "))

        if x == guess:
            print("Congratulations you did it in ", count, " try")
            break

        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")

    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")

# opdracht 8
def opdracht8(oldfile):
    print('Old file:')
    print(oldfile)
    updatefile = oldfile.split('\n')
    newfile = ''
    for line in updatefile:
        line = line.strip('\t')
        line =line.strip(' ')
        if line == '':
            continue
        else:
            newfile = newfile + line + '\n'

    print('\nNew file: ')
    print(newfile.strip(''))
# opdracht 9

# opdracht 10

# opdracht 11

# opdracht 12

# opdracht1a(int(input('Geef een getal op: ')))
# opdracht1b(int(input('Geef een getal op: ')))
# opdracht2()
# opdracht3a([0,4,2,6,34,432,4335351,345,543,34,3,-1,-3443,4,34,534,69,420])
# opdracht3b([0,4,2,6,34,432,4335351,345,543,34,3,-1,-3443,4,34,534,69,420])
# print(opdracht3c([0,0,0,0,0,0,0,1]))
# print(opdracht3c([0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1]))
# print(opdracht3c([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
# print(opdracht4a('lepel'))
# print(opdracht4b('lepel'))
# opdracht5([1,3,5,2,4,7,6,9,8,10])
# opdracht6a([1,45,23,15,34,23])
opdracht6b([[1,3,5,2], [1,3,2,5,34,53,4], [1,3,42333333333,69,420]])
# opdracht7()