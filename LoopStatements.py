List_Names = ['Ashish', 'Pallavi', 'Aishwari', 'Ishana']
#For Loop
for name in List_Names:
    print('Hello, %s Tiwari' % name)
#For loop with Range
for x in range(20):
    print('This is %d' % x)

#While Loop
x = 0
while x < 10:
    print('Value of x is: %d' % x)
    x = x + 1

#For with break
for x in range(101):
    if x > 50:
        break
    elif (x%4) is 0:
        print(x)

List_NumberValue = []
for x in range(101):
    if (x%4) is 0:
        List_NumberValue.append(x)

for x in range(101):
    if x in List_NumberValue:
        continue
    print(x)