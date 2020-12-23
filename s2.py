decode = input()
decode = list(decode)
code = {}

for i in range(len(decode)):
    check = decode[i]
    if check.isalpha() == True:
        if check == "I":
            decode[i] = 1
        if check == "V":
            decode[i] = 5
        if check == "X":
            decode[i] = 10
        if check == "L":
            decode[i] = 50
        if check == "C":
            decode[i] = 100
        if check == "D":
            decode[i] = 500
        if check == "M":
            decode[i] = 1000

for x in range(len(decode)//2 - 1):
    spot = x*2 +1
    value = decode[spot]
    if value < decode[spot + 2]:
        decode[spot] = decode[spot] * -1
sum = 0
for z in range(len(decode)//2):
    spot = z*2
    sum = sum + int(decode[spot])* int(decode[spot+1])

print(sum)