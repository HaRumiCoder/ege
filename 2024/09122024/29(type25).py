print('')
for a1 in range(0, 10):
    for a2 in range(0, 10):
        for b1 in ['', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            for b2 in ['', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                num = int('3' + str(a1) + '12' + str(a2) + '14' + b1 + b2 + '5')
                if num % 1917 == 0:
                    print(num, num // 1917)

