h, b, c, s = map(int, input().split())

print(f'{h * b * c * s / 8 / 1024 / 1024:.1f} MB')