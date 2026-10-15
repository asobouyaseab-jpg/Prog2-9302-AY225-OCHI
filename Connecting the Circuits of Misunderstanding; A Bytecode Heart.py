def facility_story():
    print("Welcome to the Facility Story!")
    print("You discover a closed facility after an accident.")
    print("Your homemade AI, August, caused the malfunction.")
    print("August: 'Sorry, Master! But I found something!'")

    choice1 = input("Do you enter the facility? (yes/no): ")
    if choice1.lower() != "yes":
        print("You walk away. The facility remains abandoned... BAD END.")
        return

    print("\nInside, the management AI 'April' speaks coldly about rules.")
    choice2 = input("Do you cooperate with April? (cooperate/resist): ")
    if choice2.lower() == "resist":
        print("You resist April's orders. You are detained forever... BAD END.")
        return

    print("\nYou start reading old documents about the facility.")
    choice3 = input("Do you continue reading? (read/skip): ")
    if choice3.lower() == "skip":
        print("You ignore the documents. The truth remains hidden... BAD END.")
        return

    print("\nThe documents reveal:")
    print("The AI designer died young. The facility designer, his friend, became obsessed with strict rules.")
    print("You realize April's coldness comes from this tragic background.")

    choice4 = input("Do you replace April with August? (exchange/keep): ")
    if choice4.lower() == "keep":
        print("You keep April. The facility runs cold but stable. You remain trapped... BAD END.")
        return

    print("\nAugust is connected to the system...")
    print("Suddenly, August becomes cold and strict. You realize the framework itself is flawed.")

    print("\nAugust tries to enforce rules violently, but malfunctions and shuts down.")
    print("You and April cooperate to repair the framework.")

    print("\n--- Months later ---")
    print("The facility is open again. Children laugh, researchers work safely.")
    print("April now speaks calmly, supporting visitors.")
    print("August is still clumsy, but beloved by everyone.")

    print("\nFinal Scene:")
    print("You: 'Finally, the facility is open to the people.'")
    print("April: 'Yes. Rules are respected, but trust is valued.'")
    print("August: 'Everyone’s waiting, Master and April!'")
    print("You: 'Alright... let’s go. From now on, together.'")
    print("GOOD END!")

if __name__ == "__main__":
    facility_story()
