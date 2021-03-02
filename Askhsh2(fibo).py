from time import time
import random
from random import randint

def fibo(x):
    i=1
    j=1
    for k in range(x-2):
        tmp=i
        i+=j
        j=tmp
    return i

while True:
    try:
        x=int(input("Πληκτρολογήστε τον όρο της ακολουθίας που θέλετε να ελέγξετε: "))
        if x<=0:
            print("Λανθασμένα δεδομένα.")
        else:
            break
    except:
        print("Λανθασμένα δεδομένα.")

p=fibo(x)
flag=0
if p>3:
    for i in range(20):
        a=random.randint(2, p-1)
        if ((a**p)%p)!=a%p:
            flag+=1
        else:
            flag=0
if flag==0:
    print("Ο αριθμός",p,"που ειναι ο",x,"όρος είναι πρώτος.")
else:
    print("Ο αριθμός",p,"που ειναι ο",x,"όρος δεν είναι πρώτος.")
