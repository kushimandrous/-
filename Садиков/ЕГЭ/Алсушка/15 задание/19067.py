for i in range(300):
    k = 0
    for x in range(300):
        for y in range(300):
            if (x + 2 * y < i) or (y > x) or (x > 30):
                k += 1
    if k == 90_000:
        print(i)
        break