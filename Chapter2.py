__author__ = 'Joel'

'''Hello! Python
Exercise from Chapter 2: Hunt the Wumpus game -- INITIAL VERSION


from random import choice

cave_numbers = range(1,21)
wumpus_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while player_location == wumpus_location:
    player_location = choice(cave_numbers)

print 'Welcome to Hunt the Wumpus!'
print 'You can see', len(cave_numbers), 'caves.'
print 'To play, just type the number'
print 'of the cave you wish to enter next.'

while True:
    print 'Danger:', wumpus_location
    print 'You are in cave', player_location
    if (player_location == wumpus_location + 1 or
        player_location == wumpus_location - 1):
        print 'I smell a wumpus!'
    print 'Which cave next?'
    player_input = raw_input('>')
    if (not player_input.isdigit() or
        int(player_input) not in cave_numbers):
        print player_input, 'is not a cave!'
    else:
        player_location = int(player_input)
        if player_location == wumpus_location:
            print 'Aargh! You got eaten by the wumpus!'
            break
'''

'''Hello! Python
Exercise from Chapter 2: Hunt the Wumpus game -- REVISED VERSION


from random import choice

cave_numbers = range(0,20)
caves = []
for i in cave_numbers:
    caves.append([])

for i in cave_numbers:
    for j in range(3):
        caves[i].append(choice(cave_numbers))

wumpus_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while player_location == wumpus_location:
    player_location = choice(cave_numbers)

print 'Welcome to Hunt the Wumpus!'
print 'You can see', len(cave_numbers), 'caves.'
print 'To play, just type the number'
print 'of the cave you wish to enter next.'

while True:
    print 'You are in cave', player_location
    print 'From here you can see caves:',caves[player_location]
    if wumpus_location in caves[player_location]:
        print 'I smell a wumpus!'

    print 'Which cave next?'
    player_input = raw_input('>')
    if (not player_input.isdigit() or
        int(player_input) not in caves[player_location]):
        print player_input + '?'
        print 'That\'s not a direction that I can see!'
    else:
        player_location = int(player_input)
        if player_location == wumpus_location:
            print 'Aargh! You got eaten by the wumpus!'
            break
'''

'''Hello! Python
Exercise from Chapter 2: Hunt the Wumpus game -- Creating connected cave network
'''

from random import choice

cave_numbers = range(0,20)
caves = []
for i in cave_numbers:
    caves.append([])

unvisited_caves = range(0,20)
visited_caves = [0]
unvisited_caves.remove(0)

while unvisited_caves != []:
    i = choice(visited_caves)
    if len(caves[i]) >= 3:
        continue

    next_cave = choice(unvisited_caves)
    caves[i].append(next_cave)
    caves[next_cave].append(i)

    visited_caves.append(next_cave)
    unvisited_caves.remove(next_cave)

    for n in cave_numbers:
        print n, ':',caves[n]
    print 'aaaaaaaa'

for i in cave_numbers:
    while len(caves[i]) < 3:
        caves[i].append(choice(cave_numbers))

    for n in cave_numbers:
        print n, ':', caves[n]
    print '--------'
