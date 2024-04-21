while True:
    try:
        s = input()

        strs = [0] * 4

        if not s:
            break

        for st in s:
            if 'a' <= st <= 'z':
                strs[0] += 1
            elif 'A' <= st <= 'z':
                strs[1] += 1
            elif '0' <= st <= '9':
                strs[2] += 1
            else:
                strs[3] += 1

    #print(strs)
        print(" ".join(list(map(str, strs))))

    except EOFError:
        break
