i = 1

for a1 in ['У', 'О', 'А']:
    for a2 in ['У', 'О', 'А']:
        for a3 in ['У', 'О', 'А']:
            for a4 in ['У', 'О', 'А']:
                for a5 in ['У', 'О', 'А']:
                    for a6 in ['У', 'О', 'А']:
                        word = a1 + a2 + a3 + a4 + a5 + a6
                        if word == 'ОУУУОО':
                            print(i)
                            break
                        i += 1