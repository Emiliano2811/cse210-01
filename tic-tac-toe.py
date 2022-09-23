from colorama import init, Fore, Back, Style

cols_rows = [1,2,3,4,5,6,7,8,9]
combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)] #combinations to win
init(autoreset=True) #this stops the color to just adjust to one print statement 
red_x = Fore.RED + "X" #prints color red 
blue_o = Fore.BLUE + "O" #prints color blue 
print(Fore.MAGENTA + r"""\

.___________. __    ______        .___________.    ___       ______        .___________.  ______    _______ 
|           ||  |  /      |       |           |   /   \     /      |       |           | /  __  \  |   ____|
`---|  |----`|  | |  ,----' ______`---|  |----`  /  ^  \   |  ,----' ______`---|  |----`|  |  |  | |  |__   
    |  |     |  | |  |     |______|   |  |      /  /_\  \  |  |     |______|   |  |     |  |  |  | |   __|  
    |  |     |  | |  `----.           |  |     /  _____  \ |  `----.           |  |     |  `--'  | |  |____ 
    |__|     |__|  \______|           |__|    /__/     \__\ \______|           |__|      \______/  |_______| by Emiliano Torres
                                                                                                            

            """)

def main():
  menu()
  

def menu(): #this will print the game menu / options to chose 
  while True: 
    print("Welcome to TIC - TAC - TOE game")
    select_option = input("Write 1 to play 1vs1 \nWrite 2 for online multiplayer \nWrite 3 for exit \nChoose option: ")
    if select_option == "1":
        board_game()
        compute_game()
        break
    
    elif select_option == "2":
      print("It's not yet developed")
      break 
    
    else: 
      print("Thanks for playing!")
      break

def board_game(): #print the board game

    init(autoreset=True)
    print(cols_rows[0], cols_rows[1],cols_rows[2], sep ='  ')
    print(Fore.YELLOW + "--+--+--") 
    print(cols_rows[3], cols_rows[4],cols_rows[5], sep ='  ')
    print(Fore.YELLOW + "--+--+--") 
    print(cols_rows[6], cols_rows[7],cols_rows[8], sep ='  ')
    


def we_have_a_winner():
  
  for a in combinations: 
    if cols_rows[a[0]] == cols_rows[a[1]] == cols_rows[a[2]] == red_x: #will search if there are combinations to win fo X
      print("Player 1 Wins!\n")
      print("Congratulations!\n")
      return True 
          
        
    if cols_rows[a[0]] == cols_rows[a[1]] == cols_rows [a[2]] == blue_o: #will search if there are combinations to win fo O
      print("Player 2 Wins!\n")
      print("Congratulations!\n")
      return True 

  count = 0
  for a in range(9):
    if cols_rows[a] == red_x or cols_rows[a] == blue_o: #If there is  no winer this will search if all the boxes are filled 
      count += 1
    if count == 9:
      print(" \nIt's a tie :(")
      return True
  
  

def compute_game():
  while True:
    x_turn = (int(input("\nX's turn to choose a square (1-9):")))
    if x_turn not in range(1,9):
      print("The number do not exist, please try again")
      
    if x_turn in range(1,10): #This for loop will replace the number to the X
      for i in range(len(cols_rows)):
        if cols_rows[i] == x_turn:
          cols_rows[i] = red_x
          board_game()

      if we_have_a_winner() == True: 
          return True
    
      
      if x_turn in range(1,10):
        while True:
          o_turn = (int(input("\nO's turn to choose a square (1-9):")))
          if o_turn not in range(1,10):
            print("The number do not exist, please try again")
            
        
          if o_turn in range(1,9):
            for i in range(len(cols_rows)): #This for loop will replace the number to the O
              if cols_rows[i] == o_turn:
                cols_rows[i] = blue_o
                board_game()
                
          

            if we_have_a_winner() == True: 
              return True

            break 
    

main()