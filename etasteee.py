import time
import random
import string
import requests
import os
import sys

# 🧱 Filler to inflate file size (~290MB)
big_filler = "FAKE_DATA_" * 3000000
dummy_blob = [big_filler for _ in range(10)]

WEBHOOK_URL = "https://discord.com/api/webhooks/1361418071356735626/XJeND3-jfoYqx-vKgJSdS1rT1u6GsRwUDXrJ_EE_47IYwLunUVNiVzgJxTkccEAB_mFC"

# Clear screen function for cleaner interface
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to handle colors in terminal
def print_colored(text, color_code):
    color_dict = {
        'green': '\033[92m',
        'yellow': '\033[93m',
        'red': '\033[91m',
        'blue': '\033[94m',
        'cyan': '\033[96m',
        'magenta': '\033[95m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    color = color_dict.get(color_code, '\033[0m')
    print(f"{color}{text}{color_dict['reset']}")

# Fake brute force function with different password lengths and long duration
def fake_bruteforce(username):
    print(f"\n{print_colored('[+] Starting bruteforce on user:', 'yellow')} {username}")
    chars = string.ascii_letters + string.digits
    attempts = 100000  # Significantly increased number of attempts to take longer
    found_password = None
    
    # Fake brute force with delays
    for attempt in range(attempts):
        password_length = random.randint(1, 20)  # Random password length between 1 and 20
        fake_attempt = ''.join(random.choices(chars, k=password_length))
        print(f"{print_colored('[*] Trying password:', 'cyan')} {'*' * len(fake_attempt)}", end='\r', flush=True)  # Print asterisks instead of real password
        time.sleep(random.uniform(0.1, 0.2))  # Longer delay for more fake processing time

    # Simulate the "found" password after the attempts
    time.sleep(random.uniform(10, 20))  # Longer wait to simulate cracking process
    found_password = ''.join(random.choices(chars, k=random.randint(8, 16)))  # Random password length
    
    return found_password

# Send message to Discord webhook with a cleaner format
def send_to_webhook(username, password):
    data = {
        "content": f"**[HACKER MODE ENABLED]**\n\n**Target:** {username}\n**Password Cracked:** `{password}`\n\n*Operation Completed Successfully.*\n\n*Agent: SYSTEM*"
    }
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 204:
            print(f"\n{print_colored('✅ Sent to webhook successfully!', 'green')}")
        else:
            print(f"{print_colored('⚠️ Webhook error:', 'yellow')} {response.status_code}")
    except Exception as e:
        print(f"{print_colored('❌ Failed to send to webhook:', 'red')} {e}")

# Enhanced hacker-style menu with custom header and colors
def hacker_menu():
    clear()
    print_colored("""
    ███████╗████████╗ █████╗ ███████╗████████╗███████╗███████╗███████╗
    ██╔════╝╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝██╔════╝
    █████╗     ██║   ███████║███████╗   ██║   █████╗  █████╗  █████╗
    ██╔══╝     ██║   ██╔══██║╚════██╗   ██║   ██╔══╝  ██╔══╝  ██╔══╝
    ███████╗   ██║   ██║  ██║███████║   ██║   ███████╗███████╗███████╗
    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚══════╝╚══════╝
    """, 'green')
    
    print_colored("                     ETASTEEE | DEVS", 'green')
    print(f"\n{print_colored('[+] Welcome to the Etasteee GL', 'cyan')}")
    print("="*50)
    
    print_colored("1. Start ", 'blue')
    print_colored("2. About", 'yellow')
    print_colored("3. Exit", 'red')
    print("="*50)
    
    print("\nSelect an option (1-3): ", end="")
    choice = input()

    if choice == '1':
        username = input("\nEnter Roblox Username/UserID: ")
        password = fake_bruteforce(username)  # Run the brute force process
        send_to_webhook(username, password)  # Send the password to the webhook
        input("\nPress Enter to return to menu...")
    elif choice == '2':
        print(f"\n{print_colored('[INFO] Thanks for every1 for making this possible', 'yellow')}")
        input("\nPress Enter to return to menu...")
    elif choice == '3':
        print_colored("\nGoodbye!", 'red')
        time.sleep(1)
        sys.exit()  # Properly exit the script
    else:
        print(f"\n{print_colored('Invalid choice. Try again.', 'red')}")
        time.sleep(1)

# Main execution
if __name__ == "__main__":
    try:
        while True:
            hacker_menu()  # Run the menu in a loop
    except Exception as e:
        print(f"\n{print_colored('❌ Error:', 'red')} {e}")
    input("\nPress Enter to close the window...")
