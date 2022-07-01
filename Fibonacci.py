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
        x=int(input("Type the term of the sequence you want to check:"))
        if x<=0:
            print("Incorrect data.")
        else:
            break
    except:
        print("Incorrect data.")

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
    print("Number ",p," that is the ",x," term on the sequence is prime.")
else:
    print("Number ",p," that is the ",x," term on the sequence isn't prime.")
