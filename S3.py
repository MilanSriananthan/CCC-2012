num = int(input())
readings = []
for i in range(num):
    hold = int(input())
    readings.append(hold)

def MostValue(seq):
    top = []
    past = 0
    for i in seq:
        total = seq.count(i)
        if total == past:
            top.append(i)
        elif total > past:
            top.clear()
            past = total
            top.append(i)
    return top
next = []
first = MostValue(readings)
for i in range(len(readings)):
    if readings[i] not in first:
        next.append(readings[i])
difference = 0
for i in first:
    for x in first:
        if i - x != 0:
            if i - x < 0:
                if x - i > difference:
                    difference = x - i
            elif i - x > difference:
                difference = i - x

if difference == 0:
    second = MostValue(next)
    for i in second:
        if first[0] - i != 0:
            if first[0] - i < 0:
                if i - first[0] > difference:
                    difference = i - first[0]
            elif first[0] - i > difference:
                difference = first[0] - i
print(difference)

'''
7
3
7
7
7
4
4
3



'''