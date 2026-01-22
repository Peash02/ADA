lis = list(map(int, input("Enter the ELements:").split()))
for i in range(len(lis)):
    min = i
    for j in range(i + 1, len(lis)):
        if lis[j] < lis[min]:
            min = j
    lis[min], lis[i] = lis[i], lis[min]
print(lis)
