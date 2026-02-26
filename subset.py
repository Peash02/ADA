def sumset(subsets):
    d = int(input("Enter sum to find:"))
    setsum = []
    for j in subsets:
        if sum(j) == d:
            setsum.append(j)
            
    if not setsum:
        print("No such Subset Found.")
    else:
        print(setsum)

if __name__ == "__main__":
    s = list(map(int,input("Enter the Number:").split()))
    subsets = [[]]

    for i in s:
        subsets += [ j + [i] for j in subsets]

    print(subsets)
    sumset(subsets)