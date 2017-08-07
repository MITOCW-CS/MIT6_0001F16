while True:
    try:
        s = []
        s = input().split()
        n = int(s[0])
        del s[0]
        for i in range(0, n):
            s[i] = int(s[i])
        tmp = []
        for i in range(1, n):
            tmp.append(abs(s[i] - s[i - 1]))
        tmp.sort()
        check_jolly = True
        for i in range(0, n - 1):
            # print(i, ' -', tmp[i], end=' ')
            if tmp[i] != i + 1:
                check_jolly = False
                break
        if check_jolly:
            print('Jolly')
        else:
            print('Not jolly')
    except EOFError:
        break

