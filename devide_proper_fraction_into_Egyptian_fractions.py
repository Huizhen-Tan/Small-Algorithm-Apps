def divide(a,b):
    a1 , b1 = a , b
    while a1!=0 and b1!= 0 and b1 % a1 != 0:
        r = b1%a1
        b1, a1 = a1, r

    a /= a1
    b /= a1
    #print('{},{}'.format(a,b))
    
    if a==1:
        return '{}/{}'.format(int(a),int(b))
    elif a==0:
        return ''
    else:
        q = int(b/a)
        return '{}/{}+{}'.format(1,q+1,divide(a*(q+1)-b,b*(q+1)))

while 1:
    try:
        x = input()
        if x == 'q':
            break
        a,b = [int(i) for i in x.split('/')]
        print(divide(a,b))
    except:
        print('TOO HARD')
