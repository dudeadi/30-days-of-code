
actual = list( map(int, input().split()) )
expect = list( map(int, input().split()) )

if actual[2] > expect[2]:
    print('10000')
elif actual[2] < expect[2]:
    print('0')
else:   
    if actual[1] > expect[1]:
        print(str((actual[1]-expect[1])*500))
    elif actual[1] < expect[1]:
        print('0')
    else:
        if actual[0] > expect[0]:
            print(str((actual[0]-expect[0])*15))
        else:
            print('0')       