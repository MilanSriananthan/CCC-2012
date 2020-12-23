start = int(input())

def possible(num):
    total = 0
    for i in range(1, num):
        for x in range(1, num):
            if x == i:
                break
            else:
                for p in range(1,num):
                    if p == x:
                        break
                    else:
                        total = total + 1

    return total

print(possible(start))