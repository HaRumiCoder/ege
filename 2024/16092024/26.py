f = open('for26')

N = int(f.readline().strip())
K = int(f.readline().strip())

parts = {}
parts_li = []
containers = {}
containers_li = []

for i in range(N):
    p = int(f.readline().strip())
    parts[p] = (parts.get(p) or 0) + 1
    parts_li.append(p)

for i in range(K):
    c = int(f.readline().strip())
    containers[c] = (containers.get(c) or 0) + 1
    containers_li.append(c)

parts = dict(sorted(parts.items()))
containers = dict(sorted(containers.items()))
parts_li = list(sorted(parts_li))
containers_li = list(sorted(parts_li))
add = []

for part in parts_li:
    for container in containers_li:
        if container >= part:
            add.append(part)
            ost = container - part
            containers_li.pop(0)
            if ost != 0:
                containers_li.insert(0, ost)
            break

print(sum(add), len(add))

