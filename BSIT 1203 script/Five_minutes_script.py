import time

def slow_print(text, delay=0.04):
    """Print text slowly for dramatic effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def narrator(text):
    slow_print(f"[Narrator] {text}")

def protagonist(text):
    slow_print(f"Protagonist: {text}")

# Context: Boredom's despair scene
def context_scene():
    print("\n" + "="*50)
    print("          CONTEXT: The Room Where Boredom Kills")
    print("="*50 + "\n")
    
    slow_print("A cramped room full of books. The clock ticks... TICK... TOCK... TICK...")
    time.sleep(1.5)
    
    protagonist("Just... one more book... Once I finish this... my life is over...")
    protagonist("Boredom will kill me... Literally...")
    time.sleep(1)
    
    slow_print("Trembling hands caress the last book like a lover...")
    
    choice = input("\nWhat do you do? (1: Gently caress it  2: Suddenly scream & headbutt): ")
    
    if choice == "1":
        protagonist("You're the last one... Stay with me...")
    else:
        protagonist("NOOOOO! I DON'T WANT IT TO END!!!")
        slow_print("Headbutts the wall! GONK! GONK! GONK!")
    
    slow_print("......Smoke starts seeping under the door...")
    narrator("Fire.")

# Insight: Fire and mad protection scene
def insight_scene():
    print("\n" + "="*50)
    print("          INSIGHT: Books > Life Madness")
    print("="*50 + "\n")
    
    protagonist("Fire!? Wait wait WAIT! My books! They're burning!!")
    time.sleep(1)
    
    slow_print("Grabs armfuls of books, but clutches the last one like a baby...")
    
    choice = input("\nHow do you protect it? (1: Try to run with them  2: Hero pose with book on head): ")
    
    if choice == "1":
        slow_print("Run... trip... drop books... pick up... repeat in panic...")
        protagonist("You alone! I'll protect YOU!")
    else:
        slow_print("Balances the final book on head like a crown. Arms wide in heroic pose...")
        protagonist("Take me! But not the book! NEVER THE BOOK!!!")
    
    slow_print("Pant leg catches fire... Doesn't notice...")
    slow_print("Beam collapses... Hits head...")
    slow_print("Blackout.")

# Conclusion: Loop and eternal freshness
def conclusion_scene():
    print("\n" + "="*50)
    print("          CONCLUSION: Eternal Freshness")
    print("="*50 + "\n")
    
    slow_print("Wakes up... Same room... Sunlight somehow filters in...")
    protagonist("...Where am I? Who am I? Wait—books! So many books! Jackpot!")
    time.sleep(1)
    
    protagonist("All unread!? This is paradise!!")
    
    slow_print("\nThe same morning repeats... (Loop Montage)")
    
    for day in range(2, 5):
        print(f"\n--- Day {day} ---")
        protagonist("...Deja vu? Eh, whatever. Reading time!")
        time.sleep(0.8)
    
    slow_print("\n(Smile slowly widens... manic joy)")
    protagonist("(turning to you, wild-eyed)")
    protagonist("Boredom? What's that? Tastes like victory!")
    protagonist("I'm gonna read new books FOREVER!!!")
    
    slow_print("Manic cackle... HAHAHAHAHA!!!")
    
    narrator("And so he was completely freed from boredom.")
    narrator("Every day fresh. Every day exciting.")
    narrator("...Though he will never remember what he read yesterday.")
    narrator("A small price to pay for eternal novelty.")
    
    choice = input("\nLoop again? (y/n): ").lower()
    return choice == "y"

# Main loop
def main():
    print("=== Eternal Library Loop - Text Adventure (English) ===")
    print("A basic Python demo of Story Flow and user choices\n")
    
    while True:
        context_scene()
        insight_scene()
        if not conclusion_scene():
            print("\nTHE END")
            break
        print("\n" + "-"*60)
        print("Back to the same morning... Loop restarts")
        print("-"*60 + "\n")
        time.sleep(2)

if __name__ == "__main__":
    main()