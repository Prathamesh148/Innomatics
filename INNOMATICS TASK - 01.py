a=[8,9,6,6,4,3,10,1,2,7]
print('Given list of 1 st N natural numbers:',a)

def Repeat(x):
    size = len(x)
    repeated = []
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
print ('Repeated value in list:',Repeat(a))

b=[]
while a:
    min = a[0]  
    for x in a: 
        if x < min:
            min = x
    b.append(min)
    a.remove(min)
    

d=b[0]
e=b[-1]
def createList(r1, r2): 
    if (r1 == r2): 
        return r1 
    else: 
        res = [] 
        while(r1 < r2+1 ): 
            res.append(r1) 
            r1 += 1
        return res 
r1, r2 = d, e
f=createList(r1, r2)


Missing = [i for i in f if not i in b or b.remove(i)]
print('Missing number:',Missing)




 





























