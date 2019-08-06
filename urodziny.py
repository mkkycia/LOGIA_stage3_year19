def urodziny(data, n):
    md = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
    for i in range(1, len(md)):
        md[i] = md[i - 1] + md[i]
    def data2ndnia(data):
        d = int(data[1:3])
        m = int(data[3:5])
        r = int(data[5:])
        ndnia = 365 * r + md[m - 1] + d + r // 4 - r // 100 + r // 400
        if r % 4 == 0 and (r % 100 != 0 or r % 400 == 0) and m < 3:
            ndnia -= 1
        return ndnia
    def ndnia2data(ndnia):
        r = ndnia // 365
        while ndnia - (365 * r + r // 4 - r // 100 + r // 400) <= 0:
            r -= 1
        ndnia = ndnia - (365 * r + r // 4 - r // 100 + r // 400)
        if ndnia > 365:
            ndnia -= 366
            r += 1
        if r % 4 == 0 and (r % 100 != 0 or r % 400 == 0):
            if ndnia == 31 + 28:
                return 29, 2, r
            if ndnia < 31 + 29:
                ndnia += 1
        m = 1
        while ndnia - md[m] > 0:
            m += 1
        ndnia = ndnia - md[m - 1]
        return ndnia, m , r
    wy = ndnia2data( n * 1000 + data2ndnia(data))
    return 'u{:02}{:02}{:04}'.format(*wy)

print(urodziny("u06042093", 1))
