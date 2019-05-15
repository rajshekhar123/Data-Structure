


def initialise(arr, n):
    for i in range(0, n+1):
        arr.append(i)
    return arr


def union(arr, a, b, n):
    temp = arr[a]
    for i in range(0, n+1):
        if arr[i] == temp:
            arr[i] = arr[b]

def main():
    print "Enter the size of array::"
    n = input()
    arr = []
    arr = initialise(arr, n)
    print "Enter the combinations the number of combination"
    k = input()
    while k>0:
        a, b = raw_input().split(' ')
        a, b = [int(a), int(b)]
        union(arr, a, b, n)
        k= k-1
    print arr
if __name__ == '__main__':
    main()
