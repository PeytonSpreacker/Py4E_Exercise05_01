#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the average of the numbers entered. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
sum = 0.0
count = 0
while True :
    snum = input('Enter a number:')
    if snum == 'done' :
        break
    try:
        num = float(snum)
    except:
        print('Invalid input')
        continue
    sum = sum + num
    count = count + 1
print(sum/count)