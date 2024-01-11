# print 1-150

for i in range(151):
    print(i)

# print multiplies of 5 to 1000

for i in range(1001):
    if i % 5 == 0:
        print(i)

# print 1-100, if devisible by 5 print coding instead, if 10 print coding dojo

for i in range(101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# add all odd int from 0 to 500,000 and print the sum

sum = 0
for i in range(500001):
    if i % 2 != 0:
        sum += i
    print(sum)

# print all positive int from 2018 to 0 by 4

for i in range(2018, 0, -4):
    print(i)

# flexible counter

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
