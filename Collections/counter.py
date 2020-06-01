from collections import Counter

X = int(input())

shoe_size = map(int, input().split())
shoe_size = list(shoe_size)
#print(shoe_size)

shoes = Counter(shoe_size)
#print(shoes)

income = 0

N = int(input())

for x in range(N):
    size, price = map(int, input().split())
    #print([size,price])
    if shoes[size]:
        income += price
        shoes[size] -= 1
print(income)
