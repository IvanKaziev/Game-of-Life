import random
import time
world_length = int(input('Введите длину мира: '))
world_hight = int(input('Введите высоту мира: '))
count_gen = int(input('Введите количество поколений: '))
past_world = []
res = []
new_line = []
new_world = []
neighbours = 0
all_worlds = []
count = 0

for i in range(world_hight):
    for j in range(world_length):
        res.append(random.choice(' ' '*'))
    past_world.append(res)
    res = []
for p in past_world:
    print(''.join(p))  

for gen in range(count_gen - 1):
    for line in range(0, world_hight):
        for symbol in range(0, world_length):
            if past_world[line][symbol - 1] == '*':
                neighbours += 1
            if past_world[line][(symbol + 1) % world_length] == '*':
                neighbours += 1
            if past_world[line - 1][symbol - 1] == '*':
                neighbours += 1
            if past_world[line - 1][symbol] == '*':
                neighbours += 1
            if past_world[line - 1][(symbol + 1) % world_length] == '*':
                neighbours += 1
            if past_world[(line + 1) % world_hight][symbol - 1] == '*':
                neighbours += 1
            if past_world[(line + 1) % world_hight][symbol] == '*':
                neighbours += 1
            if past_world[(line + 1) % world_hight][(symbol + 1) % world_length] == '*':
                neighbours += 1
            if  past_world[line][symbol] == ' ' and neighbours == 3:
                new_line.append('*')
            elif past_world[line][symbol] == ' ':
                new_line.append(' ')
            if past_world[line][symbol] == '*' and (neighbours == 2 or neighbours == 3):
                new_line.append('*')
            elif past_world[line][symbol] == '*':
                new_line.append(' ')
            neighbours = 0
        new_world.append(new_line)
        new_line = []
    time.sleep(0.5)
    if new_world in all_worlds:
        break
    for r in new_world:
        print(''.join(r))  
    past_world = []  
    past_world = new_world.copy()
    new_world = []
    all_worlds.append(past_world)
