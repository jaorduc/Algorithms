A = [3,2,1,0,5,7]

for j in range(len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key 
print(A)
