
# print(ans)

for i in range(9):
    for j in range(9):
        if i <= j and i + j <= 8:
            print(" * ", end="")
        elif i >= j and i + j >= 8:
            print(" * ", end="")
        else:
            # pass
            print("   ", end="")
    print()











