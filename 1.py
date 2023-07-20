L = [1,2,3,4]
h = L[0]
for b in range(1, len(L)):
    if(h < L[b]):
        h = L[b]
print(h)
