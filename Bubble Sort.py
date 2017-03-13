# Bubble sort, keeping count of swaps made to order array

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numswaps = 0
for i in range(0, n-1):
    for j in range(0, n-1):
        if a[j] > a[j+1]:
            b = a[j]
            a[j] = a[j+1]
            a[j+1] = b
            numswaps += 1

print("Array is sorted in " + numswaps + " swaps.")
print("First Element: " + a[0])
print("Last Element: " + a[n-1])
    
bubble(a,n)
