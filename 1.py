L = [2,6,8,9]
h = L[0]
for a in range(1, len(L)):
    if(h < L[a]):
        h = L[a]
print(h)
