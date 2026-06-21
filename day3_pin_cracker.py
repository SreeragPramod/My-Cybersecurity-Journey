print("--- 4-Digit PIN Brute Force Simulator ---")
# This is the secret PIN the "hacker" is trying to guess
target_pin = "7392"
# We start our guessing at zero
guess = 0
print("Initiating attack...")

# A "while loop" runs over and over until we tell it to stop
while True:
  
    # .zfill(4) is a cool trick that turns the number 5 into "0005"
    formatted_guess = str(guess).zfill(4)
    
    # Did we guess correctly?
    if formatted_guess == target_pin:
        print("\n[!] SUCCESS! System bypassed.")
        print("[!] The secret PIN was cracked:", formatted_guess)
        print("[!] Total guesses made:", guess + 1)
        break # The 'break' command tells the loop to stop running
    
    # If the guess was wrong, we add 1 and the loop starts over!
    guess = guess + 1
