# fizz buzz => 3배수에서  FIzz를 나오게 하고, 5배수에서 buzz가 나오게 하고, 15배수에서 fizz buzz가 나오게 하면 됨

number = int(input('자연수를 입력하세요 : '))

for i in range(1, number+1):

    if i % 15 == 0:
        print('fizzbuzz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 3 == 0:
        print('fizz')
    else:
        print(i)
