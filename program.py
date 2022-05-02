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
def create_new_world(world, ng, width, hight, now, new, all_w, gen):
    for gen in range(gen - 1):
        for line in range(0, world_hight):
            for symbol in range(0, world_length):    
                if world[line][symbol - 1] == '*':
                    ng += 1
                if world[line][(symbol + 1) % width] == '*':
                    ng += 1
                if world[line - 1][symbol - 1] == '*':
                    ng += 1
                if world[line - 1][symbol] == '*':
                    ng += 1
                if world[line - 1][(symbol + 1) % width] == '*':
                    ng += 1
                if world[(line + 1) % hight][symbol - 1] == '*':
                    ng += 1
                if world[(line + 1) % hight][symbol] == '*':
                    ng += 1
                if world[(line + 1) % hight][(symbol + 1) % width] == '*':
                    ng += 1
                
                if  world[line][symbol] == ' ' and ng == 3:
                    now.append('*')
                elif world[line][symbol] == ' ':
                    now.append(' ')
                if world[line][symbol] == '*' and (ng == 2 or ng == 3):
                    now.append('*')
                elif world[line][symbol] == '*':
                    now.append(' ')
                ng = 0
            new.append(now)
            now = []
        time.sleep(0.5)
        if new in all_w:
            break
        for r in new:
            print(''.join(r))  
        world = []  
        world = new.copy()
        new = []
        all_w.append(world)        
        
for i in range(world_hight):
    for j in range(world_length):
        res.append(random.choice(' ' '*'))
    past_world.append(res)
    res = []
for p in past_world:
    print(''.join(p))  
create_new_world(past_world, neighbours, world_length, world_hight, new_line, new_world, all_worlds, count_gen)