# Problem: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# Score: 20


def jumping_on_clouds(n, c):
    c.append(0)
    ans = 0
    position = 0
    while position < n-1:
        position += (c[position+2] == 0) + 1
        ans += 1
    return ans


n = int(input())
c = list(map(int, input().rstrip().split()))
print(jumping_on_clouds(n, c))
