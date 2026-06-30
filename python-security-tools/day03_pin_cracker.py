"""
Day 03 - 4-Digit PIN Brute Force Simulator
Demonstrates how quickly a 4-digit PIN can be cracked using sequential
brute force when there is no rate limiting or lockout policy.
Security use case: This is exactly why systems implement account lockout
after N failed attempts, rate limiting, and CAPTCHA challenges.
"""
import time


def brute_force_pin(target_pin):
    print("Initiating attack...")
    start_time = time.time()
    guess = 0

    while True:
        formatted_guess = str(guess).zfill(4)

        if formatted_guess == target_pin:
            elapsed = time.time() - start_time
            print(f"\n[!] SUCCESS! PIN cracked: {formatted_guess}")
            print(f"[!] Total guesses: {guess + 1}")
            print(f"[!] Time taken: {elapsed:.4f} seconds")
            return guess + 1, elapsed

        guess += 1


def simulate_lockout_defense(max_attempts=3):
    """
    Shows the defensive countermeasure: locking the account after
    a small number of failed attempts makes brute force infeasible.
    """
    print(f"\n--- Defense Simulation: Account locks after {max_attempts} failed attempts ---")
    print(f"With a lockout policy, an attacker only gets {max_attempts} guesses")
    print(f"out of 10,000 possible PINs before being blocked.")
    print(f"Success probability per lockout window: {max_attempts / 10000:.4%}")


if __name__ == "__main__":
    target_pin = "7392"
    brute_force_pin(target_pin)
    simulate_lockout_defense()
