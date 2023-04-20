# WFQ assignment

# Pseudocode
# Print 3 Priority packets until until Priority queue is empty
# Then print 2 Standard packets until standard queue is empty
# Then print 1 Economy packet until economy queue is empty

# space with file
f = open("C:/Users/iqmal/Documents/School/S23/CS162/input queue.txt", 'r')
lines = f.readlines()
print(lines)
# initialize priority queues
premium = []
standard = []
economy = []
# fill priority queues
for x in lines:
    if x[0] == 'P':
        # remove class marker as queue is now class marker, also do extra characters at same time
        premium.append(x.strip('P \n'))
    elif x[0] == 'S':
        standard.append(x.strip('S \n'))
    else:
        economy.append(x.strip('E \n'))
print(premium, standard, economy)

# print to priority scheme
# check that queues are not empty
while len(premium) > 0 or len(standard) > 0 or len(economy) > 0:
    for x in range(3):  # 3 in a row
        if len(premium) != 0:
            print(premium.pop(0))
    for x in range(2):  # 2 in a row
        if len(standard) != 0:
            print(standard.pop(0))
    if len(economy) != 0:  # once
        print(economy.pop(0))

f.close()
