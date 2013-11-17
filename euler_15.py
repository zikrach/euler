# -*- coding: utf-8 -*-
"""solve 15"""

def row_end_node(x):
    
    if (x + 1) % DELTA_DOWN == 0:
        return True
    
    return False

GRID_SIZE = 20
END_NODE = ((GRID_SIZE + 1) ** 2) - 1
DELTA_DOWN = GRID_SIZE + 1
FIRST_NODE_OF_BOTTOM_ROW = DELTA_DOWN * GRID_SIZE


print(GRID_SIZE, END_NODE, DELTA_DOWN, FIRST_NODE_OF_BOTTOM_ROW)

path_count_from_node = [0 for i in range(END_NODE)]
    

for i in range(END_NODE - 1, -1, -1):
    
    if (i == END_NODE - 1) or (i == END_NODE - DELTA_DOWN):         
        path_count_from_node[i] = 1
        continue
        
    if not row_end_node(i):
        path_count_from_node_right = path_count_from_node[i + 1]
    else:
        path_count_from_node_right = 0
        
    if i < FIRST_NODE_OF_BOTTOM_ROW:
        path_count_from_node_down = path_count_from_node[i + DELTA_DOWN]
    else:
        path_count_from_node_down = 0
        
    path_count_from_node[i] = path_count_from_node_right + \
        path_count_from_node_down
    
print(path_count_from_node[0])

        

