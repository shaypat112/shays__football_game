# This part gives the instructions for the user to follow and understand
def start_game():
    global time_remaining, yards_to_first_down, down, total_yards
    time_remaining = 120  # Start with 2 minutes
    yards_to_first_down = 10  # 10 yards for a first down
    down = 1  # Start on 1st down
    total_yards = 0  # Start at your own goal line
    print("Welcome to the Football Game Adventure!")
    print("You're about to play the most important game of your life.")
    print("You are the quarterback of your team, and the game is on the line.")
    print("It's the fourth quarter, and you have two minutes left to score and win the game.")
    print("You are 100 yards away from the end zone, starting from your own goal line.")
    print("The stadium is packed, and the crowd is roaring.")
    print("It's your turn to lead the team to victory.")
    print("Be careful! Some decisions could lead to injuries or even losing the game!")
    print("What will you do? Type 'stop' to end the game anytime.")

    game_status()

# Display the current game status
def game_status():
    global time_remaining, yards_to_first_down, down, total_yards
    print(f"\nTime remaining: {time_remaining} seconds")
    print(f"Yards to first down: {yards_to_first_down}")
    print(f"Down: {down}")
    print(f"Total yards gained: {total_yards} yards")
    if total_yards >= 100:
        print("\nTouchdown! You've reached the end zone and won the game!")
        end_game()
    elif down > 4:
        print("\nTurnover on downs! You failed to convert, and the game is over.")
        end_game()
    else:
        first_decision()

# This part gives the user the first decision to make
def first_decision():
    print("\nYour coach calls for a pass play. What do you do?")
    print("1. Throw a long pass down the field.")
    print("2. Check for a short pass to the running back.")
    print("3. Try to scramble and run it yourself.")
    print("4. Fake a pass and hand it off to the running back.")
    print("5. Call an audible to change the play.")

    choice = input("> ")

    if choice == "1":
        long_pass()
    elif choice == "2":
        short_pass()
    elif choice == "3":
        scramble_run()
    elif choice == "4":
        fake_and_run()
    elif choice == "5":
        audible_play()
    elif choice.lower() == "stop":
        end_game()
    else:
        print("Please choose a valid option.")
        first_decision()

# Update the game state after a play
def update_game_state(time_used, yards_gained):
    global time_remaining, yards_to_first_down, down, total_yards
    time_remaining -= time_used
    total_yards += yards_gained
    yards_to_first_down -= yards_gained

    if yards_to_first_down <= 0:
        yards_to_first_down = 10
        down = 1
        print("\nFirst down! You reset the downs and continue the drive.")
    else:
        down += 1

    if time_remaining <= 0:
        print("\nTime has run out! You lose the game.")
        end_game()
    else:
        game_status()

# This part gives the user the second decision to make
def long_pass():
    print("\nYou step back in the pocket, take a deep breath, and throw a long pass toward your wide receiver.")
    print("The ball soars through the air, but the cornerback is closing in fast!")
    print("What do you do?")
    print("1. Try to lead your receiver and hope he can make the catch.")
    print("2. Throw the ball out of bounds to avoid an interception.")
    print("3. Look for your tight end as a backup option.")
    print("4. Attempt a trick play by faking a throw and running yourself.")

    choice = input("> ")

    if choice == "1":
        print("\nYour receiver makes an incredible catch for 30 yards!")
        update_game_state(15, 30)
    elif choice == "2":
        print("\nYou throw the ball out of bounds. The clock stops, but you gain no yards.")
        update_game_state(10, 0)
    elif choice == "3":
        print("\nYour tight end catches the ball for 15 yards.")
        update_game_state(10, 15)
    elif choice == "4":
        print("\nYou fake the throw and run for 10 yards!")
        update_game_state(15, 10)
    elif choice.lower() == "stop":
        end_game()
    else:
        print("Please choose a valid option.")
        long_pass()

# This part gives the user the third decision to make
def short_pass():
    print("\nYou decide to check down and throw a short pass to your running back.")
    print("The ball is in the air, but the linebacker is closing in fast!")
    print("What do you do?")
    print("1. Lead your running back and hope he can break the tackle.")
    print("2. Throw the ball away to avoid a sack.")
    print("3. Pump fake and look for another receiver.")
    print("4. Attempt a lateral pass to a nearby teammate.")

    choice = input("> ")

    if choice == "1":
        print("\nYour running back breaks the tackle and gains 8 yards.")
        update_game_state(10, 8)
    elif choice == "2":
        print("\nYou throw the ball away to avoid a sack. No yards gained.")
        update_game_state(5, 0)
    elif choice == "3":
        print("\nYou pump fake and complete a pass for 12 yards.")
        update_game_state(10, 12)
    elif choice == "4":
        print("\nYou attempt a lateral, but it results in a loss of 5 yards!")
        update_game_state(10, -5)
    elif choice.lower() == "stop":
        end_game()
    else:
        print("Please choose a valid option.")
        short_pass()

# This part gives the user the fourth decision to make
def scramble_run():
    print("\nYou decide to scramble and take the ball yourself.")
    print("You break through the pocket and start running downfield.")
    print("The defense is closing in fast. What do you do?")
    print("1. Slide to protect yourself and stop the clock.")
    print("2. Lower your shoulder and try to plow through the defender.")
    print("3. Risk an injury and dive for extra yards.")
    print("4. Attempt to lateral the ball to a nearby teammate.")

    choice = input("> ")

    if choice == "1":
        print("\nYou slide safely after gaining 5 yards.")
        update_game_state(5, 5)
    elif choice == "2":
        print("\nYou plow through the defender and gain 10 yards!")
        update_game_state(10, 10)
    elif choice == "3":
        print("\nYou dive for extra yards but injure yourself, gaining 7 yards before leaving the game.")
        update_game_state(10, 7)
        print("\nGame over due to injury.")
        end_game()
    elif choice == "4":
        print("\nYou lateral the ball and lose 3 yards!")
        update_game_state(10, -3)
    elif choice.lower() == "stop":
        end_game()
    else:
        print("Please choose a valid option.")
        scramble_run()

# Adds a fake and run decision
def fake_and_run():
    print("\nYou fake the pass and hand it off to your running back.")
    print("The defense is caught off guard, and your running back gains 15 yards!")
    update_game_state(10, 15)

# Adds an audible play option
def audible_play():
    print("\nYou call an audible at the line of scrimmage, changing the play to a screen pass.")
    print("The defense is caught off guard, and your running back gains 20 yards!")
    update_game_state(10, 20)

# Adds a trick play option
def trick_play():
    print("\nYou fake the throw and take off running yourself.")
    print("The defense is caught off guard, and you sprint for a huge gain, putting your team in scoring position!")
    update_game_state(15, 25)

# Win and lose scenarios
def receiver_catch():
    print("\nYour receiver leaps into the air and makes a spectacular one-handed catch!")
    print("The crowd goes wild as he races toward the end zone.")
    print("Your team scores a touchdown with just seconds left on the clock!")
    print("You've won the game! Congratulations!")
    end_game()

def end_game():
    print("\nThanks for playing! I hope you had fun.")
    print("Would you like to play again? Type 'yes' to play again, or 'stop' to quit.")
    choice = input("> ")

    if choice.lower() == "yes":
        start_game()
    elif choice.lower() == "stop":
        print("Goodbye! Have a great day!")
    else:
        print("Please choose 'yes' or 'stop'.")
        end_game()

# Start the game
start_game()

