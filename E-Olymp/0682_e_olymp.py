n = int(input())
a = [0] + list(map(int, input().split()))
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i]
m = int(input())
result = []
for _ in range(m):
    l, r = map(int, input().split())
    result.append(str(s[r] - s[l - 1]))
print("\n".join(result))
