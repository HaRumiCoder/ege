clients_time = []
clients_data = []
windows = {1: [], 2: []}

with open('for10') as f:
    for i in range(int(f.readline().strip())):
        client = f.readline().strip().split()
        clients_time.append(int(client[0]))
        clients_data.append(list(map(int, client[1:])))

res_window2 = 0
res_window1 = 0
quit_num = 0

print(set(clients_time))
time = min(clients_time)
for i in range(100000):
    if len(windows[1]) > 0:
        windows[1][0] = windows[1][0] - 1
        if windows[1][0] == 0:
            windows[1].pop(0)
            res_window1 += 1
    if len(windows[2]) > 0:
        windows[2][0] = windows[2][0] - 1
        if windows[2][0] == 0:
            windows[2].pop(0)
            res_window2 += 1

    if time in clients_time:
        data = clients_data[clients_time.index(time)]
        if data[1] == 0:
            if len(windows[1]) <= len(windows[2]) and len(windows[1]) < 14:
                windows[1].append(data[0])
            elif len(windows[2]) < 14:
                windows[2].append(data[0])
            else:
                quit_num += 1
        if data[1] == 1:
            if len(windows[1]) < 14:
                windows[1].append(data[0])
            else:
                quit_num += 1
        if data[1] == 2:
            if len(windows[2]) < 14:
                windows[2].append(data[0])
            else:
                quit_num += 1

    time += 1

print(res_window2, quit_num, res_window1, len(clients_time))


