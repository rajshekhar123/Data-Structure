
def initialise(arr, size, n):
    for i in range(0, n+1):
        arr.append(i)
        size.append(1)
    return arr, size

def root(arr, i):
    while arr[i]!=i:
        i = arr[i]
    return i

def find(arr, a, b):
    if root(a)==root(b):
        return True
    else:
        return False

def weighted_union(arr, size, A, B):
    rootA = root(arr, A)
    rootB = root(arr, B)
    if rootA == rootB:
        return
    if size[rootA]<size[rootB]:
        arr[rootA] = arr[rootB]
        size[rootB] = size[rootB]+size[rootA]
    else:
        arr[rootB] = arr[rootA]
        size[rootA] = size[rootA]+size[rootB]

def main():
    arr = []
    size = []
    n = input()
    arr, size = initialise(arr, size, n)
    print "Enter the number of combination::"
    k = input()
    while k>0:
        a,b = raw_input().split(' ')
        a, b = [int(a), int(b)]
        weighted_union(arr, size, a, b)
        k = k-1
    print 'Array is ',arr
    print 'Size is ',size

if __name__=='__main__':
    main()
