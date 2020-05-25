
def hexer(code):
    hexx, out = [], []
    d = {}
    for i in list(range(0, 256)):
        if i < 16:
            s  = hex(i)
            hexx.append("0" + s[-1])
            d["0"+s[-1]] = i
        else:
            s = hex(i)
            hexx.append(s[-2] + s[-1])
            d[s[-2]+s[-1]] = i

    codes = [code[-6] + code[-5], code[-4] + code[-3], code[-2] + code[-1]]
    i,j, x, = -1, 1, 0
    while x < 3:
        f = d[codes[x]]

        if f + i < 0 or j > 16:
            out.append(codes[x][0] * 2)
            x += 1
            i = -1
            j = 1
            continue
        if  f + j > 255:
            out.append(codes[x][0] * 2)
            x += 1
            x = -1
            j = 1
            continue
        if hexx[f + i][0] == hexx[f + i][1]:
            if abs(i) <= j :
                out.append(hexx[f + i])
                x += 1
                i = -1
                j = 1

        if hexx[f + j][0] == hexx[f + j][1]:
            if j <= abs(i):
                out.append(hexx[f + j])
                x += 1
                i = -1
                j = 1
        i -= 1
        j += 1

    return "#" + "".join(out)

print(hexer("#010000"))