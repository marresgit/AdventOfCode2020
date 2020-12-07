# wont make anything fancy

expence_list = []
result = []

f = open('expence.txt', 'r')

# Add expence to array
for i in f.read().split():
    expence_list.append(i)


for index_number in range(0,len(expence_list)):
    for expences in expence_list:
        if int(expence_list[index_number]) + int(expences) == 2020:
          result.append(int(expence_list[index_number]))


print(int(result[0]) * int(result[1]))