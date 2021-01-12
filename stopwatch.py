from msvcrt import kbhit, getch
import os
from time import sleep

print('Press any key...');    getch()

h=m=s=0;  i=0

while(True):
    os.system('cls')
    print('\n\n\t%02d : %02d : %02d . %02d' %(h,m,s,i))
    if kbhit():
        os.system('cls')
        print('\n\tYour time taken - ',end="")
        if h!=0:
            print('%d hrs, ' %h,end="")
        if m!=0:
            print('%d mins, ' %m,end="")
        if s!=0:
            print('%d secs' %s)
        getch();    break  
    i+=1
    if i>99:
        i=0;  s+=1
    if s>59:
        s=0;  m+=1
    if m>59:
        m=0;  h+=1
    if h==12:
        print(' Enough now !!');  break
    sleep(0.001)
    

input()


