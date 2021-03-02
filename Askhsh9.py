Emfaniseis=[]
emfaniseis=[]
for i in range(26):
    Emfaniseis.append(0)
    emfaniseis.append(0)
with open("two_cities_ascii.txt") as f:
    data = f.read()
    data_monogrammata=""
    data_monogrammata_mona=""
    for char in data:
        if (ord(char) >=65 and ord(char)<=90) or (ord(char) >=97 and ord(char)<=122):
            data_monogrammata+=char
for ch in data_monogrammata:
    if ord(ch)%2!=0:
        data_monogrammata_mona+=ch
#Check an perasan mono ta mona
# with open("file.txt", "w") as file:
#     file.write(data_monogrammata_mona)
list="ACEGIKMOQSUWYacegikmoqsuwy"
for ch in data_monogrammata_mona:
    for i in range(len(list)):
        if ch==list[i]:
            emfaniseis[i]+=1
for i in range(26):
    pososto=0
    pososto=emfaniseis[i]/len(data_monogrammata_mona)*100
    pososto=int(pososto)+1
    print("\nΤο ποσοστό εμφάνισης του",list[i],"είναι:",end="")
    for j in range(pososto):
        print("*",end="")
    print("%")
