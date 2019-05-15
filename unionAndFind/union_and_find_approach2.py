

def initialise(arr, n):
    for i in range(0, n+1):
        arr.append(i)
    return arr

def root(arr, i):
    while arr[i]!=i:
        i = arr[i]
    return i

def find(arr, a, b):
    if root(arr, a) == root(arr, b):
        return True
    else:
        return False

def union(arr, a, b):
    root_a = root(arr, a)
    root_b = root(arr, b)
    arr[root_a] = root_b
def main():
    print "Enter the limit of n"
    n = input()
    arr = []
    arr = initialise(arr, n)
    print "Enter the no of pairs::"
    k = input()
    while k>0:
        a,b = raw_input().split(' ')
        a,b = [int(a), int(b)]
        union(arr,a,b)
        k = k-1
    print find(arr,1,4)
    print find(arr,3,5)
    print arr
if __name__ == '__main__':
    main()
