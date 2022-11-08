# Python program to find greatest of numbers

print '------------------------------------------------------'
print 'We will find the greatest number of numbers entered'
counter = ()
smallest = ()

Operator = raw_input('How many numbers would you like to compare ')

while (Operator==0):
    print ('Invalid input!')
    Operator = raw_input('How many numbers would you like to compare ')

if (Operator>0):
    while (counter<=Operator):
     counter += 1
    num = raw_input('enter the number ')

    if (smallest<num):
        smallest=num
print('smallest number was ', smallest)





