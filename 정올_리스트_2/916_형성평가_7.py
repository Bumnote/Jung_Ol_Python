n = int(input())
L = list(map(int, input().split()))

L.sort(reverse=True)
for i in L:
    print(i)
