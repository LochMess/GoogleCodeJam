def calcDamage(code):
    damage = 1
    totDamage = 0
    for j in code:
        if j.lower() == 's':
            totDamage += damage
        else:
            damage += damage
    return totDamage

def hack(code):
    swapPoint = code.rfind('CS')
    codeList = list(code)
    codeList[swapPoint], codeList[swapPoint+1] = codeList[swapPoint+1], codeList[swapPoint]
    return ''.join(codeList)

for i in range(int(input())):
    test = input()
    hp = int(test[0:test.find(' ')])
    code = test[test.find(' ')+1:]
    hacks = 0
    if code.count('S') > hp:
        print('Case #{}: IMPOSSIBLE'.format(i+1))
    else:
        while calcDamage(code) > hp:
            code = hack(code)
            hacks += 1
        print('Case #{}: {}'.format(i+1, hacks))
