
def isprime(num):
    flag=0
    for i in range(2,num):
        if (num%i)==0:
            flag=1;  break
    if flag==0:
        return True
    else:
        return False

if __name__=='__main__':
    num1=int(input('Number: '))

    for i in range(2,num1+1):
        if isprime(i):
            if num1%i==0:
                print(i)


