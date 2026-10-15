import random

def play_game():
    colors = ['Red', 'White', 'Blue'] 
    
    while True: 
        print("\nR - Red\nW - White\nB - Blue\nQ - Quit")
        choice = input("Your choice: ").strip().upper()
        
        if choice == 'Q':
            print("Goodbye!")
            break
        
        if choice not in ['R', 'W', 'B']:
            print("Invalid choice")
            continue
        
        
        user_color = {'R': 'Red', 'W': 'White', 'B': 'Blue'}[choice] 
        comp_color = random.choice(colors)
        print("Computer choice:", comp_color)
        
        if user_color == comp_color:
            print("YOU WIN!")
        else:
            print("YOU LOSE.")
        
        again = input("Play again? (Y/N): ").strip().upper()
        if again != 'Y': 
            print("Thanks for playing!")
            break

play_game() 