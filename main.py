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
print(d)
newstates=[]
for x in d:
    # print(d.get(x))
    for y in d[x]:
        # print(d[x].get(y))
        if len(d[x].get(y))!=1 and d[x].get(y) not in newstates:
            if set(d[x].get(y)) not in newstates:
                newstates.append(set(d[x].get(y)))
nr=0
print(newstates)
deschimbat={}
for n in newstates:
    for a in F:
        if a in n:
            F.append(N+1)
    final=[]
    N = N + 1
    d[N]={}
    for litera in chei:
        # print("litera=", litera)
        aux=[d[x].get(litera) for x in n]
        aux.append(litera)
        final.append(aux)
    print("final: ")
    for x in final:
        print(x)
    print("---------------------------------")
    for x in final:
        mul = []
        for i in range(0, len(x) - 1):
            if x[i] is not None:
                for elem in x[i]:
                    if elem not in mul:
                        mul.extend(x[i])
        # print("mul pt i=",i,":",mul)
        if len(mul)!=0:
            mul = set(mul)
            d[N][x[len(x)-1]]=mul
        print("mul: ", mul)
    for x in d:
        for y in d[x]:
            if d[x].get(y) == n:
                d[x][y]={N}

M=0
for y in d:
    for x in d[y]:
        M=M+len(d[y].get(x))
print(d)
g=open("output.txt","w")
g.write(str(N))
g.write('\n')
for x in d.keys():
    g.write(str(x))
    g.write(" ")
g.write('\n')
g.write(str(M))
g.write('\n')
for x in d:
    for y in d[x]:
        for z in d[x].get(y):
            g.write(str(x))
            g.write(" ")
            g.write(str(z))
            g.write(" ")
            g.write(y)
            g.write('\n')
g.write(str(S)+'\n')
g.write(str(len(F)))
g.write('\n')
for x in F:
    g.write(str(x))
    g.write(" ")
g.write('\n')
g.write(str(NrCuv))
g.write('\n')
for cuv in cuvinte:
    g.write(cuv+'\n')


