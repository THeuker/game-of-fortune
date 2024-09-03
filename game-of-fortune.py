import random
import time
from datetime import datetime, timezone

banner = """
 ███████████                     █████                                  
░░███░░░░░░█                    ░░███                                   
 ░███   █ ░   ██████  ████████  ███████   █████ ████ ████████    ██████ 
 ░███████    ███░░███░░███░░███░░░███░   ░░███ ░███ ░░███░░███  ███░░███
 ░███░░░█   ░███ ░███ ░███ ░░░   ░███     ░███ ░███  ░███ ░███ ░███████ 
 ░███  ░    ░███ ░███ ░███       ░███ ███ ░███ ░███  ░███ ░███ ░███░░░  
 █████      ░░██████  █████      ░░█████  ░░████████ ████ █████░░██████ 
░░░░░        ░░░░░░  ░░░░░        ░░░░░    ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░       

Guess all the numbers and win :D
"""

def get_epoch_ms():
    return int(time.time() * 1000)

def get_timestamp(epoch : int):
    return datetime.fromtimestamp(int(epoch / 1000), timezone.utc)

def print_lucky_numbers():
    lucky_numbers = ""
    for i in range(5):
        number = random.randint(1,1000)
        lucky_numbers += f"{number} "
    print(f"Your lucky numbers are: {lucky_numbers}")

def get_flag():
    return open("./flag.txt").read()

def main():
    print(banner)
    
    epoch_ms = get_epoch_ms()
    random.seed(epoch_ms)
    curr_time = str(get_timestamp(epoch_ms)).replace("+00:00", "")
    print(f"Time: {curr_time}")

    print_lucky_numbers()
    
    count = 1
    while count <= 100:
        guess = input(f"Guess nr {count}: ")
        try:
            guess = int(guess)
        except:
            print("What do you think you're doing? •`_´•")
            exit()

        if(guess == random.randint(1,1000)):
            print("Correct :D")
            count += 1
            continue
        else:
            print("Sorry thats wrong, fortune was not on your side :(")
            exit()

    flag = get_flag()
    print(f"CONGRATULATIONS YOU WON\nHere is your price: {flag}")
    


if __name__ == "__main__":
    main()