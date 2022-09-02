import urllib.request
import json
import datetime
from time import sleep
now = datetime.datetime.now()
today=now.strftime("%Y-%m-%d")
temp=now.strftime("%d")
loop=int(temp)
print ("Current date and time : ",today)
print("Παρακαλώ περιμένετε...\n (Το πρόγραμμα ελέγχει 180 κληρώσεις ,με 20 αριθμούς η καθεμία, για κάθε ημέρα του τρέχοντα μήνα.)")
for i in range(loop):
    max=0
    Arithmos=0
    ListaKlhrwsewn=[]
    Emfaniseis=[]
    for z in range(80):
        Emfaniseis.append(0)
    k=str(i+1).zfill(2)
    b=now.strftime("%Y-%m-")+k
    #Prwta travaw ta ID kathe klhsrwshs gia thn hmera
    url1="https://api.opap.gr/draws/v3.0/1100/draw-date/"+b+"/"+b+"/draw-id"
    r=urllib.request.urlopen(url1)
    html=r.read()
    html=html.decode()
    DrawId=json.loads(html,strict=False)
    #print(DrawId)
    #Gia kathe id sth lista DrawId travaw ta noumera pou kerdisan se kathe klhrwsh
    for q in range(len(DrawId)):
        DrawId[q]=str(DrawId[q])
        url2="https://api.opap.gr/draws/v3.0/1100/"+DrawId[q]
        r=urllib.request.urlopen(url2)
        # print(url2)
        # print(b)
        html=r.read()
        html=html.decode()
        data=json.loads(html,strict=False)
        #Vazw se mia lista me onoma list mono ola ta nikhtiria noumera
        list=data["winningNumbers"]["list"]
        #print(list)
        #gia to length tou list, ston pinaka Emfaniseis ,me deikth ton aritmo pou vghke ,pros8etw 1
        for j in range(len(list)):
            Emfaniseis[list[j]-1]+=1
        #print(list)
    #me mia if vriskw ayton poy emfanisthke pio syxna gia kathe mera kai pio katw ton emfanizw
    for m in range(0,len(Emfaniseis)):
        if max<Emfaniseis[m]:
            max=Emfaniseis[m]
            Arithmos=m+1
    #print(Emfaniseis)
    if list!=[]:
        print("Ο αριθμός με τις περισσότερες εμφανίσεις για την",b," είναι ο" ,Arithmos,"με",max,"εμφανίσεις\n")
    else:
        print("Δεν υπάρχουν κληρώσεις για την",k,"μέρα του μήνα που ζητήσατε")
