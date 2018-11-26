import numpy as np

HEIGHT = 17
WIDTH = 17
LANES = 4

TOTAL = 100

# edge locations are already taken care of
# obstacles = []
cars = []

all_road_maps = {}

for k in range(TOTAL):
    cars = []
    for i in range(LANES):
        lane_val = 9 + 2 * i
        for j in range(np.random.randint(0,4)):
            car = (np.random.randint(3,14), lane_val)
            if car not in cars:
                cars.append(car)
    
    temp = 9 + 2*np.random.randint(0,4)
    start = (HEIGHT-1, temp)
    goal = (0, temp)
    
    # start, goal, varying obstacles
    temp_road = (start, goal, cars)
    all_road_maps[k] = temp_road

np.save('/home/parth/cs332/hierarchical_IL_RL/hierarchical_imitation_learning_Maze_Domain/road_maps.npy', all_road_maps, True)
