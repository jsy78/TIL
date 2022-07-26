from math import gcd, lcm

A, B = map(int, input().split())
print(gcd(A, B))
print(lcm(A, B))

# gcd, lcm = 0, 0
# A, B = map(int, input().split())
# for i in range(min(A, B), 0, -1) :
#     if A % i == 0 and B % i == 0 :
#         gcd = i
#         break

# for i in range(max(A, B), (A*B)+1) :
#     if i % A == 0 and i % B == 0 :
#         lcm = i
#         break

# print(gcd)
# print(lcm)

# gcd, lcm = 0, 0
# A_origin, B_origin = map(int, input().split())
# A, B = A_origin, B_origin

# while(B) :
#     A, B = B, A % B

# gcd = A
# lcm = (A_origin * B_origin) // gcd

# print(gcd)
# print(lcm)