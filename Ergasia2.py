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
        x=int(input("Πληκτρολογήστε τον όρο της ακολουθίας: "))
        if x>0:
            break
        else:
            print("Λανθασμένη εισαγωγή δεδομένων.")
    except ValueError:
        print("Λανθασμένη εισαγωγή δεδομένων.")

p=fibo(x)
flag=True
if p>3:
	i=0
	while (flag and i<20):
		a=random.randint(2, p-1)
		if ((a**p)%p)!=a%p:
			flag=False
			print("Ο όρος",x,"της ακολουθίας είναι ο αριθμός",p,"και δεν είναι πρώτος.")
		i+=1

if flag:
    print("Ο όρος",x,"της ακολουθίας είναι ο αριθμός",p,"και είναι πρώτος.")
