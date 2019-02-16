def whileloop(num):
    i = 0
    numbers = []
    while i < num:
        numbers.append(i)
        i = i + 1
    print "You list : ", numbers

print "Enter the number want to iterate and create a list out of it : ",
j = int(raw_input())

whileloop(j)
