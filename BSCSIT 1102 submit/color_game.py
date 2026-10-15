import random

def play_game():
    colors = ['Red', 'White', 'Blue']
    credits = 1000
    game_active = True
    
    while game_active:
        print(f"\nCurrent credits: {credits}")
        
        # Get valid bet amount
        while True:
            try:
                bet = int(input("How much would you like to bet? "))
                if bet <= 0:
                    print("Bet must be a positive number.")
                elif bet > credits:
                    print(f"Bet cannot exceed your current credits ({credits}).")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")
        
        # Get valid color choice
        while True:
            print("\nR - Red\nW - White\nB - Blue\nQ - Quit")
            choice = input("Your color choice: ").strip().upper()
            
            if choice == 'Q':
                print("Thanks for playing!")
                game_active = False
                break
                
            if choice not in ['R', 'W', 'B']:
                print("Invalid choice. Please choose R, W, or B.")
                continue
                
            user_color = {'R': 'Red', 'W': 'White', 'B': 'Blue'}[choice]
            comp_color = random.choice(colors)
            print("Computer choice:", comp_color)
            
            if user_color == comp_color:
                print("YOU WIN!")
                credits += bet
            else:
                print("YOU LOSE.")
                credits -= bet
            
            # Check if credits are depleted
            if credits <= 0:
                print("All credits lost! Game over!")
                game_active = False
                break
                
            # Ask to play again
            while True:
                again = input("Play again? (Y/N): ").strip().upper()
                if again in ['Y', 'N']:
                    break
                print("Please enter Y or N.")
                
            if again == 'N':
                print("Thanks for playing!")
                game_active = False
            
            break

play_game()