def buildPuzzle():
    N = 100  

    puzzle = {}

    for i in range(1, N + 1, 1):
        if i < 22 or i % 10 == 1:
            a = 0
        else:
            a = i - 20 - 1

        if i <= 20 or i % 10 == 0:
            b = 0
        else:
            b = i - 20 + 1    

        if i % 10 == 1 or i % 10 == 2 or i <= 10:
            c = 0
        else:
            c = i - 10 - 2

        if i % 10 == 9 or i % 10 == 0 or i <= 10:
            d = 0
        else:
            d = i - 10 + 2

        if i % 10 == 1 or i % 10 == 2 or i >= 90:
            e = 0
        else:
            e = i + 10 - 2

        if i % 10 == 9 or i % 10 == 0 or i >= 90:
            f = 0
        else:
            f = i + 10 + 2

        if i >= 81 or i % 10 == 1:
            g = 0
        else:
            g = i + 20 - 1

        if i > 79 or i % 10 == 0:
            h = 0
        else:
            h = i + 20 + 1

        puzzle[str(i)] = [a, b, c, d, e, f, g, h]

    return puzzle