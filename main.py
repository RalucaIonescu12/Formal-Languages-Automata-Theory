def back(k,cuvant,nod,tranzitii,F):
    global ok
    if k==len(cuvant):
        if nod in F:
            g.write("da\n")
            ok=1
    else:
        for t in tranzitii[nod]:
            if t[1]==cuvant[k]:
                back(k+1,cuvant,t[0],tranzitii,F)
            elif t[1]=='l':
                for x in tranzitii[t[0]]:
                    if cuvant[k]==x[1]:
                        back(k + 1, cuvant, x[0], tranzitii, F)

f=open("input.txt")
N=int(f.readline())#nr stari
Q=[int(x) for x in f.readline().split()]#stari
M=int(f.readline()) #nr tranzitii
tranzitii=[[] for i in range(1,100001)]

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
print("stari:",Q)
print("tranzitii:",tranzitii[:M])
print("stare initiala ",S)
print("cuvinte " ,cuvinte)
print("stare finala",F)
g=open("output.txt","w")


for cuv in cuvinte:
    ok=0
    k=0
    back(k,cuv,S,tranzitii,F)
    if ok==0:
        g.write("nu\n")

f.close()
g.close()
