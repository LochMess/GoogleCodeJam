def magic(nI, I):
    odds = I[1::2]
    odds.sort(reverse=True)
    evens = I[0::2]
    evens.sort(reverse=True)
    for i in range(nI):
        if len(evens) != 0 and len(odds) != 0:
            if (i%2 == 0 and evens[-1] <= odds[-1]):
                evens.pop(-1)
            elif (i%2 == 1 and odds[-1] <= evens[-1]):
                odds.pop(-1)
            else:
                return i
    return 'OK'

for i in range(int(input())):
    noIntergers = int(input())
    intergers = list(map(int, input().split()))
    print('Case #{}: {}'.format(i+1, magic(noIntergers, intergers)))
