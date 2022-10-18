

#=============================== Frequency of characters =============================
n=input()
f='abcdefghijklmnopqrstuvwxyz'
d={}.fromkeys(n,0)
print(d)
for i in d:
    if i in f:
        d[i]=d[i]+1
print(d)