n = ('7' * 40) + ('9' * 40) + ('4' * 50)

while '49' in n or '97' in n or '47' in n:
    if '47' in n:
        n = n.replace('47', '74', 1)
    if '97' in n:
        n = n.replace('97', '79', 1)
    if '49' in n:
        n = n.replace('49', '94', 1)

print(n[26], n[72], n[106])