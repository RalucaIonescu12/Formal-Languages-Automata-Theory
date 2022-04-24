f=open("input.txt")
N=int(f.readline())#nr stari
Q=[int(x) for x in f.readline().split()]#stari
M=int(f.readline()) #nr tranzitii
tranzitii=[[] for i in range(1,100001)]
chei=[]
ninit=N
for i in range(M):
    aux=[x for x in f.readline().split()]
    tranzitii[int(aux[0])].append([int(aux[1]),aux[2]])
S=int(f.readline())
nrF=int(f.readline())
F=[int(x) for x in f.readline().split()]
NrCuv=int(f.readline())
cuvinte=[]
for i in range(NrCuv):
    cuvinte.append(f.readline().strip("\n"))
print("N:",N)
print("stari  Q:",Q)
print("tranzitii:",tranzitii[:M])
print("stare initiala  S ",S)
print("cuvinte " ,cuvinte)
print("stare finala  F",F)
d={}
for i in range(0,N+1):
    if len(tranzitii[i])!=0:
        d[i] = {tranzitii[i][0][1]:{tranzitii[i][0][0]}}
        for t in tranzitii[i]:
            if t[1] not in chei:
                chei.append(t[1])
            if t[1] not in d[i]:
                d[i][t[1]]={t[0]}
            else:
                if t[0] not in d[i][t[1]]:
                    d[i][t[1]].add(t[0])
print("---------------------------------------------------")
print("dictionarul: ")
print(d)
print("---------------------------------------------------")

#tabel
print ("     a     b ")
print ("   ----------")
for x in d:
    print (x,": ",*d[x].get('a')," , ",*d[x].get('b'))

print("---------------------------------------------------")

#pas 0

seturi1=[]
seturi1.append(F)
seturi1.append([x for x in Q if x not in F])
print("seturi1",seturi1)
seturi={x:1 if x in F else 2 for x in Q}
for x in seturi:
    print(x,":",seturi.get(x))
print("seturi:",seturi)
# print(seturi)
print("---------------------------------------------------")
#pas 1
maxx1=2
maxx2=maxx1
# aux=[[seturi1[0][0]],[seturi1[1][0]]]
# print(aux)
ok=0
while ok==0:
    aux = [[lista[0]] for lista in seturi1]
    for subset in seturi1:
        for i in range(1,len(subset)):
            ok=0
            for lista in aux:
                if seturi.get(*d[lista[len(lista)-1]].get('a')) == seturi.get(*d[subset[i]].get('a')) and seturi.get(*d[lista[len(lista)-1]].get('b')) == seturi.get(*d[subset[i]].get('b')) and seturi.get(subset[i])==seturi.get(lista[len(lista)-1]):
                    #nu sunt diferentiabile
                    print(lista[len(lista)-1],"si",subset[i],"NEDIF")
                    print("lista ", lista)
                    lista.append(subset[i])
                    print(aux)
                    ok=1
                    break
                    print("---------------------------")
            if ok==0:
                # ssunt diferentiabile -adaug un nou subset
                print(lista[len(lista) - 1], "si", subset[i], "DIF")
                print("lista ", lista)
                l = []
                l.append(subset[i])
                aux.append(l)
                maxx2 = maxx2 + 1
                print(aux)
                print("---------------------------")
    print("aux",aux,"seturi1",seturi1)

    if maxx2!=maxx1:
        print("++++")
        ok=0
        for i in range(0,len(aux)):
            for x in aux[i]:
                seturi[x]=i+1
        maxx1=maxx2
        seturi1=[[x for x in lista] for lista in aux]
        print(seturi)
    else:
        ok=1
print(seturi)

print("seturi1",seturi1)
for lista in seturi1:
    for x in lista:
        print (x,": ",*d[x].get('a')," , ",*d[x].get('b'))

seturi11=[] #lista cu noile stari
for lista in seturi1:
    if len(lista)!=1:
        aux=0
        for x in lista:
            aux=aux*10+x
        seturi11.append(aux)
        d[aux]={}
    else:
        seturi11.append(lista[0])
print(d[1].get('a'))
# for lista in seturi1:
print("seturi11",seturi11)
for x in seturi11:
    if x/10==0: #are o sg cifra
        for nr in d[x].get('a'):
            if nr%10 not in seturi11:  #adica nodul x se duce intr-un nod nou cum ar fi 25
                for y in seturi11:
                    if str(nr%10) in str(y):
                        d[x]['a']={y}
                        break
        #else ar ramane in d la fel valoarea lui d[x].get('a')
        for nr in d[x].get('b'):
            if nr%10 not in seturi11:  #adica nodul x se duce intr-un nod nou cum ar fi 25
                for y in seturi11:
                    if str(nr%10) in str(y):
                        d[x]['b']={y}
                        break
    else:
        for y in seturi11:
            for nr in d[x%10].get('a'):
                if str(nr%10) in str(y):
                    d[x]['a'] = {y}
                    break
        # else ar ramane in d la fel valoarea lui d[x].get('a')
        for y in seturi11:
            for nr in d[x % 10].get('b'):
                if str(nr%10) in str(y):
                    d[x]['b'] = {y}
                    break
print(d)
M=0
for y in d:
    if y in seturi11:
        M=M+2
print(M)

# afisare DFA
g=open("output.txt","w")
g.write(str(len(seturi11))+'\n')
for x in seturi11:
    g.write(str(x)+' ')
g.write('\n')
g.write(str(M))
g.write('\n')
for x in d:
    if x in seturi11:
        for y in d[x]:
            g.write(str(x))
            g.write(" ")
            g.write(str(*d[x].get(y)))
            g.write(" ")
            g.write(y)
            g.write('\n')
for x in seturi11:
    for cif in str(x):
        if int(cif)==S:
            g.write(str(x))
            break
nrF=0
finale=[]
for x in seturi11:
    if len(str(x))!=1:
        for cif in str(x):
            if int(cif) in F:
                nrF=nrF+1
                finale.append(x)
                break
    elif x in F:
        finale.append(x)
        nrF=nrF+1
print(finale)
g.write('\n')
g.write(str(nrF))
g.write('\n')
for x in finale:
    g.write(str(x)+' ')
g.write('\n')

g.write(str(NrCuv))
g.write('\n')
for cuv in cuvinte:
    g.write(cuv+'\n')


