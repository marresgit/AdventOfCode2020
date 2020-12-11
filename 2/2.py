
input = []

f = open('input.txt', 'r')

for i in f.read().splitlines():
    input.append(i)


for i in input:
    list_input = i.split()
    #----------FIX FIRST INPUT [X]----------
    numbers = list_input[0].split("-")
    fnum = (int(numbers[0]))
    lnum = (int(numbers[1])+1)
    #print(range(fnum,lnum))
    #----------FIX MIDDLE INPUT [X]----------
    letter = list_input[1].replace(':', '')
    #----------FIX LAST INPUT [X]----------
    #print(list_input[2])
    #----------FIX IF STATEMENT [-] ----------