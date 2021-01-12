from time import sleep

fname=input('File Name: ')

try:
    f=open(fname,'r')

    f.close()

    print('\nFile Already Exists !!')

except FileNotFoundError:
    f=open(fname,'w')

    f.close()

    print('\nFile Created !!')

sleep(0.1)
