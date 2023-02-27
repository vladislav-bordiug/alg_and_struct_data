a = int(input('Input number\n'))
if a%3==0:
    print('Fizz',end='')
if a%5 == 0:
    print('Buzz',end='')
if a%3 !=0 and a%5 != 0:
    print(a,end='')
print()
