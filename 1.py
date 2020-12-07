# wont make anything fancy

expence_list = []

f = open('expence.txt', 'r')

# Add expence to array
for i in f.read().split():
    expence_list.append(i)


for i in range(0,len(expence_list)):
    for y in expence_list:
        if int(expence_list[i]) + int(y) == 2020:
            expence_list[i]
