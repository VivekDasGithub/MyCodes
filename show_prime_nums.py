
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
    lim=int(input('Limit: '))

    print('\nAll prime numbers upto',lim,':')
    for i in range(2,lim+1):
        if isprime(i):
            print(i,end=' ')


input()
