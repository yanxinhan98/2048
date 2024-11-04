import random 

# global variable indicating the grid size 
grid_size = 4 

# Initializing the grid with 4*4 0s
# 0 represents an empty cell 
def initialize_grid():
    return [[0] * grid_size for _ in range(grid_size)] 


# Randomly generate a 2 in empty cells
# Collect all empty cells in a list and randomly choose one from it
# Assign the value of it to 2
def generate_random_two(grid):
    
    empty_cells = []
    
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 0:
                empty_cells.append((i,j))
                
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2 
      


# Function to display the grid
# Mark empty cell as .
# Using tab character to split different cells next to each other 
def display_grid(grid):
    for row in grid:
        print('\t'.join(str(cell) if cell != 0 else '.' for cell in row))
    print("\n")


        
# The standard transform of numbers in a single row after the player conducts one move.
# It takes a row of number as input, and returns the result row of numbers if the player conducts a left move.
def transform(row):
    row = [cell for cell in row if cell!= 0]
    
    for i in range(len(row) - 1):
        if row[i] == row[i+1]:
            row[i] *= 2 
            row[i+1] = 0
            
    row = [cell for cell in row if cell!= 0]
    row += [0]*(grid_size - len(row))
    return row 

# Move left operation
# For each row of the grid, conducts a left move (transform)
def move_left(grid):
    
    for i in range(grid_size):
        grid[i] = transform(grid[i])
    
    return grid

# Move right operation 
# For each row of the grid, conducts a right move by reversing it, conducting a left move, and reversing back
def move_right(grid):
    

    for i in range(grid_size):
        grid[i] = transform(grid[i][::-1])[::-1]
    
    return grid


# Move up operation
# For each column of the grid, which represents a list from top to bottom, conducts a left move
def move_up(grid):
    
  
    for j in range(grid_size):
        
        column = [grid[i][j] for i in range(grid_size)]
        column = transform(column)
        
        for i in range(grid_size):
            grid[i][j] = column[i]

    return grid 

# Move down operation
# For each column of the grid, which represents a list from top to bottom, conducts a right move
def move_down(grid): 

    for j in range(grid_size):
        
        column = [grid[i][j] for i in range(grid_size)][::-1]
        column = transform(column)[::-1]
        
        for i in range(grid_size):
            grid[i][j] = column[i]
   
            
    return grid


# Check if the game is over, using flag to indicate different game over scenarios
# Winning: There is at least one cell equals 2048 (flag = 2)
# Losing: There is no empty cell, and no more further operations can be done (flag = 0)
# Running: Game continues (flag = 1)
def game_over(grid):
    
    flag = 0 
    for i in range(grid_size):
        
        for j in range(grid_size):
            
            if grid[i][j] == 2048:
                flag = 2 
                break 
            
            if grid[i][j] == 0:
                flag = 1
            
            if i < grid_size - 1 and grid[i][j] == grid[i+1][j]:
                flag = 1  
            
            if j < grid_size - 1 and grid[i][j] == grid[i][j+1]:
                flag = 1  
            
    return flag  



    