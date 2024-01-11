"""
    DigiPet CLI Application -

        DigiPet is a simple application that lets the user care for one or more cute and lovely pets. Simple activities such as walking, playing and sleeping will affect the DigiPet's
    happiness and energy. Let either one fall too low and your cute and lovely pet will become daisy fertilizer. ( not good! )
 
    Specifications:
        - Use the starter code provided below
        - Add the following commands
            walk - "Implement Walk"
            play - "Implement Play"
            feed - "Implement Feed"
            sleep - "Implement Sleep"
            do trick - "Implement Do Trick"
            switch - "Implement Switch"
            - Any other commands should return “Invalid Command”

        - Update "menu" command to list menu options
            - use a tuple store the menu options

    Process Builders -
        - Refer to yours or some other source of working code that is similar.
        - Plan before you build; pseudo code
        - Ideally, each student will have their own copy with 1 student sharing their screen and everyone working together to decide the code you will all use.
"""

is_active = True

# add menu items #

while is_active:

    command = input("\ncommand-> ")

    if command == "quit":
        is_active = False

    elif command == "menu":
        # add code to list menu items #
        print("Implement menu")

    # add other commands #

print("Have A Nice Day!")