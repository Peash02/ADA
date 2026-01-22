def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    lis = []
    n = int(input("Enter Number of Elements:"))
    print("Enter The list:")
    for _ in range(n):
        x = int(input())
        lis.append(x)
    res = bubble_sort(lis)
    print(res)
