from functions import initialize_grid, generate_random_two, move_left, move_right, move_up, move_down, game_over, display_grid



def main():
    
    # Initialize the game 
    grid = initialize_grid()
    generate_random_two(grid)
    generate_random_two(grid)

    print("Game start!")

    # Recursively get input from players until the game ends 
    while True:
        
        # Initialize variables indicatiing whether to end game or restart game 
        end_game = False
        restart_game = False  
        
        # Display the current grid at first after each user movement 
        display_grid(grid)
        
        
        # Try parsing input from users indicating the next movement
        try:
            move = input("Please enter your move (w = up, s = down, a = left, d = down)")
            if move not in 'wasdq':
                raise ValueError("Invalid move! Please enter w,a,s,d!" )
            
            # Store the current grid  
            pre_grid = [row[:] for row in grid]
            
            # Parse the input and transform the grid accordingly 
            if move == 'w':
                grid = move_up(grid)
            elif move == 'a':
                grid = move_left(grid)
            elif move == 's':
                grid = move_down(grid)
            elif move == 'd':
                grid = move_right(grid)
            elif move == 'q':
                print('Goodbye!')
                break
            
            # Check if winning condition is meet
            if game_over(grid) == 2:
                print("Congratulations! You won! Wanna restart? Press y/n")
                
                # Try parsing input from users indicating restart or end 
                while True: 
                    try:
                        restart = input()
                        if restart == 'y':
                            restart_game = True 
                            break 
                        elif restart == 'n':
                            end_game = True
                            break 
                        else:
                            raise ValueError("Invalid input! Please enter y/n!" )
                    except ValueError as e:
                        print(e)
                    except Exception as e:
                        print(e)
            
            # Restart or end the game accordingly              
            if end_game:
                print('Goodbye!')
                break 
            
            if restart_game:
                grid = initialize_grid()
                generate_random_two(grid)
                generate_random_two(grid)
                print("Game start!")
                continue 
            
            # Check if this move is making any changes
            # If it is, generate a new 2; if not, do nothing
            if pre_grid != grid:
                generate_random_two(grid)
            
            # Check if the game is over after generating the new 2 
            if game_over(grid) == 0:
                display_grid(grid)
                print("Game over! No possible moves left. Wanna restart? Press y/n")
                
                # Try parsing input from users indicating restart or end 
                while True: 
                    try:
                        restart = input()
                        if restart == 'y':
                            restart_game = True 
                            break 
                        elif restart == 'n':
                            end_game = True
                            break 
                        else:
                            raise ValueError("Invalid input! Please enter y/n!" )
                    except ValueError as e:
                        print(e)
                    except Exception as e:
                        print(e)
            
            # Restart or end the game accordingly 
            if end_game:
                print('Goodbye!')
                break 
            
            if restart_game:
                grid = initialize_grid()
                generate_random_two(grid)
                generate_random_two(grid)
                print("Game start!")
                continue 
        
        except ValueError as e:
            print(e)
        
        except Exception as e:
            print(e)
                
# The main 
if __name__ == "__main__":
    main()