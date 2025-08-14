# battlegame.py

# -------------------------
# Task 1: Set Up the Game
# -------------------------

# Characters (as strings)
wizard = "Wizard"
elf = "Elf"
human = "Human"

# Character HP (as integers)
wizard_hp = 70
elf_hp = 100
human_hp = 150

# Character Damage (as integers)
wizard_damage = 150
elf_damage = 100
human_damage = 20

# Dragon Stats (as integers)
dragon_hp = 300
dragon_damage = 50

#task 2&3:Player Choice Prompt and Selection
while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")

    character_choice = input("Choose your character: ")

    if character_choice == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character_choice == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    