L = [5,6,7,8]
h = L[0]
for c in range(1, len(L)):
    if(h < L[c]):
        h = L[c]
print(h)
