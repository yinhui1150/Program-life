def finbonaci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return finbonaci(n-1) + finbonaci(n-2)

print(finbonaci(35))  