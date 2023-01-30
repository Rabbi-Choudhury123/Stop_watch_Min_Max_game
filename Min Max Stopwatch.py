def largest(arr,n):
    max = arr[0]

    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]

    return max

def smallest(arr,n):
    min = arr[0]

    for i in range(1,n):
        if arr[i] < min:
            min = arr[i]

    return min

print("these are the time from stop-watch in seconds")
arr = [10,324,45,90,900,40]
n = len(arr)
Ans1 = largest(arr,n)
Ans2 = smallest(arr,n)
print("Largest in given array is",Ans1)
print("Smallest in given array is",Ans2)