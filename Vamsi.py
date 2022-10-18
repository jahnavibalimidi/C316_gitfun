#==================================== Gresstest among list without using func ============================================
# #n=int(input())
l=[12,6,4,3,8,144]
d=l[0]
for i in range(1,len(l)):
    if(d<l[i]):
        d=l[i]
#print(d)
l.remove(d)
d=l[0]
for i in range(1,len(l)):
    if(d<l[i]):
        d=l[i]
print(d)
