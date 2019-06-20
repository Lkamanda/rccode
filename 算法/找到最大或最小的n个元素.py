from heapq import nlargest, nsmallest
portfile = [
    {'name': "xiaolin", 'shares': 100, 'price': 91.1},
    {'name': "xiaojun", 'shares': 200, 'price': 841.1},
    {'name': "xiaomeng", 'shares': 340, 'price': 8.1},
    {'name': "liu", 'shares': 50, 'price': 1.1}
]
cheap = nlargest(2, portfile, key=lambda s: s['price'])
print(cheap)
expensive = nsmallest(2, portfile, key=lambda s: s['price'])
print(expensive)
