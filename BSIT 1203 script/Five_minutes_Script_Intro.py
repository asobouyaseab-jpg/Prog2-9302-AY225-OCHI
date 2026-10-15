import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Input: Get user choice (like gathering data in IT system)
def input_phase():
    print("\n[INPUT PHASE - Story Setup]")
    slow_print("You wake up in a tiny room full of books.")
    slow_print("Only one book left. Boredom is killing you slowly...")
    choice = input("What do you do? (1: Read it gently  2: Panic and scream): ")
    return choice

# Process: Logic based on input (decision making / conflict)
def process_phase(user_choice):
    print("\n[PROCESS PHASE - Conflict & Decision]")
    if user_choice == "1":
        slow_print("You caress the book tenderly...")
        slow_print("But suddenly... smoke under the door! Fire!")
    else:
        slow_print("NOOOOO! I DON'T WANT IT TO END!!!")
        slow_print("You headbutt the wall → GONK GONK GONK!")
        slow_print("Then... fire starts anyway!")

    protect_choice = input("Protect the last book? (1: Try to escape with it  2: Hero pose): ")
    
    if protect_choice == "1":
        slow_print("You trip, drop books, pick up... frantic loop...")
    else:
        slow_print("Book on head like crown. 'Take me, not the book!!!'")
    
    slow_print("Beam falls... blackout.")
    return protect_choice

# Output: Show the result / resolution (story conclusion)
def output_phase():
    print("\n[OUTPUT PHASE - Resolution]")
    slow_print("You wake up again... same room... all books are unread!")
    slow_print("Every morning is fresh. New books forever!")
    slow_print("Boredom defeated! Eternal novelty achieved!")
    
    again = input("\nContinue the loop forever? (y/n): ").lower()
    return again == "y"

# Main story flow (sequence + logic + choices)
print("=== Eternal Library - Story Logic Demo ===")
print("Demonstrates: Input → Process → Output with user choices\n")

loop_continue = True
while loop_continue:
    user_input = input_phase()          # Input
    process_result = process_phase(user_input)  # Process (logic)
    loop_continue = output_phase()      # Output + decision to continue

print("\nTHE END")
print("Story complete. Thanks for playing!")