import random

#Turn-based mini game
def mini_game():
    Dragon = 1000
    Human = 100
    Traveller = 20
    Shadowcreep = 50

    Human_skills = {
        "Heal": 10,
        "Pierce": 40,
        "Bomb": 50
    }

    Dragon_skills = {
        "Fire breath": 10,
        "Wing wind": 30,
        "Heal": 5
    }

    Traveller_skills = {
        "Archery": 25,
        "Heal": 5,
        "Poison": 10
    }

    Shadowcreep_skills = {
        "Shadow jab": 30,
        "Shadow kick": 45,
        "Heal": 5
    }

    print("Traveller: Welcome to the first town Human!")

    Human_convo1_dict = {
        1: "Who are you?",
        2: "What is this place?",
        3: "Why is it in ruin?"
    }

    Human_to_Traveller = int(input("1. Who are you?\n2. What is this place?\n3. Why is it in ruin?\nChoose your response to the Traveller: "))
    if Human_to_Traveller == 1 and Human_convo1_dict:
        print(f"Human: {Human_convo1_dict[1]}")
        print("Traveller: I!...I am just like you!, a traveller, traveling everywhere and nowhere at once!")
    elif Human_to_Traveller == 2 and Human_convo1_dict:
        print(f"Human: {Human_convo1_dict[2]}")
        print("Traveller: This is a Shadow town...Or something??")
    elif Human_to_Traveller == 3 and Human_convo1_dict:
        print(f"Human: {Human_convo1_dict[3]}")
        print("Traveller: I don't know too, I just got here like you")

    print("Human: Oh, see you arond then")
    print("...")
    print("...!")
    print("Traveller: Do you feel that?")
    print("Human: Yes, it is shakey, is it earthquake?")
    print("Traveller: Probably, we should go to an openfield then")
    print("Human: What is that!?")
    print("Traveller: Hmmmmm, Wide feet, deep soil marks, and deformed trees, what do you think caused this?")

    Human_cause_guess = {
        1: "Ultra fat man",
        2: "Dragon",
        3: "Fat traveller",
        4: "Dinosaur"
    }

    Human_cause_answer = int(input("1. Ultra fat man\n2. Dragon\n3. Fat traveller\n4. Dinosaur\n Choose your answer: "))
    if Human_cause_answer == 1 and Human_cause_guess:
        print(f"Human: {Human_cause_guess[1]}")
        print("stop joking bro, but nice one")
    elif Human_cause_answer == 2 and Human_cause_guess:
        print(f"Human: {Human_cause_guess[2]}")
        print("Probably? cuz yeh the soil marks is really deep")
    elif Human_cause_answer == 3 and Human_cause_guess:
        print(f"Human: {Human_cause_guess[3]}")
        print("Traveller: Might be, you know? Hmmmmm")
    elif Human_cause_answer == 4 and Human_cause_guess:
        print(f"Human: {Human_cause_guess[4]}")
        print("Dinosaur???? there is no such thing as that today!")

    print("Traveller: What is that!???")
    print("Human: Oh my!!! A Dragon!")
    print("Traveller: Ok Human, we gotta fight, we're in its range now")
    print("Dragon: Imbecile!")

    DragonVSHuman_Traveller = random.randint(1, 3)
    1 == Human
    2 == Dragon
    3 == Traveller

    if DragonVSHuman_Traveller == 1:
        Human_choice = random.randint(1, 3)
        if Human_choice == 1:
            Human + Human_skills["Heal"]
            print(f"Human uses Heal on itself. Human{Human}")
    elif DragonVSHuman_Traveller == 2:
        Dragon_choice = random.randint(1, 3)
        if Dragon_choice == 1:
            Dragon + Dragon_skills["Fire breath"]


mini_game()