def memorized_cut_rod(p, n):
    r = []
    for i in range(n+1):
        r.append(-float('inf'))

    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]

    if n == 0:
        r[n] = 0
    else:
        for i in range(1, n+1):
            r[n] = max(r[n], p[i] + memoized_cut_rod_aux(p, n-i, r))

    return r[n]


def bottom_up_cut_rod(p, n):
    r = [0]

    for i in range(1, n+1):
        r.append(-float('inf'))

        for j in range(1, i+1):
            r[i] = max(r[i], p[j] + r[i-j])

    return r[n]


def extended_bottom_up_cut_rod(p, n):
    r = [0]
    s = [0]

    for i in range(1, n+1):
        r.append(-float('inf'))
        s.append(0)

        for j in range(1, i+1):
            if r[i] < p[j] + r[i-j]:
                r[i] = p[j] + r[i-j]
                s[i] = j

    return r, s


n = 10
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
r, s = extended_bottom_up_cut_rod(p, n)

print(r)
print(s)

while n > 0:
    print(s[n])
    n -= s[n]










