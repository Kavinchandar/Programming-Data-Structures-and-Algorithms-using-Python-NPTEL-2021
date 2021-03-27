n, m = map(int, input().split())


def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)


print(gcd(n, m))
