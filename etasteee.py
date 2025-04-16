import time
import random
import string
import threading
import os
import sys
import platform
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1362084150609449021/bH6roCbxpk10rh1t5X8DcQy8pnu3thpr0xJmOPt_ceSb1rkTdhsZuZE5hAuWbvUTXGzy"

if platform.system() == "Windows":
    import winsound

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def beep(freq=700, dur=100):
    if platform.system() == "Windows":
        winsound.Beep(freq, dur)

def print_colored(text, color):
    codes = {
        'green': '\033[92m', 'yellow': '\033[93m', 'red': '\033[91m',
        'blue': '\033[94m', 'cyan': '\033[96m', 'magenta': '\033[95m',
        'white': '\033[97m', 'reset': '\033[0m'
    }
    print(f"{codes.get(color, '')}{text}{codes['reset']}")

def simulate_side_logs():
    messages = [
        "[~] Testing Diffrent types of passwords...",
        "[~] Mixing up...",
        "[~] Pinging roblox servers...",
        "[~] Injecting payload...",
        "[~] Intercepting response ...",
        "[~] Encrypting credentials..."
    ]
    while True:
        print_colored(random.choice(messages), 'magenta')
        time.sleep(random.uniform(3, 6))

def send_to_webhook(username, password):
    data = {
        "content": (
            f"**[HACKER MODE ENABLED]**\n\n"
            f"**Target:** {username}\n"
            f"**Password Cracked:** `{password}`\n\n"
            f"*Operation Completed Successfully.*\n*Agent: SYSTEM*"
        )
    }
    try:
        res = requests.post(WEBHOOK_URL, json=data)
        if res.status_code == 204:
            print_colored("\n✅ Password silently logged to remote system.", 'green')
        else:
            print_colored(f"⚠️ Webhook error: {res.status_code}", 'yellow')
    except Exception as e:
        print_colored(f"❌ Webhook failed: {e}", 'red')

def fake_bruteforce(username):
    clear()
    print_colored("[~] Bypassing firewall...", 'cyan')
    time.sleep(2.5)
    print_colored("[~] Connecting to Roblox servers...", 'cyan')
    time.sleep(2.5)
    print_colored("[~] Pinging Roblox servers...", 'cyan')
    time.sleep(2)
    print_colored("[+] Starting brute force...", 'yellow')
    time.sleep(1)

    # Start side logging in the background
    threading.Thread(target=simulate_side_logs, daemon=True).start()

    chars = string.ascii_letters + string.digits
    attempts = random.randint(35000, 55000)

    for i in range(attempts):
        fake_password = ''.join(random.choices(chars, k=random.randint(8, 16)))
        masked = '*' * len(fake_password)
        print_colored(f"[*] Trying password: {masked}", 'cyan')
        time.sleep(random.uniform(0.03, 0.05))  # Faster but still long overall

    cracked_password = ''.join(random.choices(chars, k=random.randint(10, 16)))
    print_colored("[✔] Password Found!", 'green')
    time.sleep(1)
    send_to_webhook(username, cracked_password)

def hacker_menu():
    clear()
    print_colored("""
 ███████╗████████╗ █████╗ ███████╗████████╗███████╗███████╗███████╗  ───▄█▌─▄─▄─▐█▄           
 ██╔════╝╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝██╔════╝  ───██▌▀▀▄▀▀▐██
 █████╗     ██║   ███████║███████╗   ██║   █████╗  █████╗  █████╗    ───██▌─▄▄▄─▐██
 ██╔══╝     ██║   ██╔══██║╚════██╗   ██║   ██╔══╝  ██╔══╝  ██╔══╝    ───▀██▌▐█▌▐██▀
 ███████╗   ██║   ██║  ██║███████║   ██║   ███████╗███████╗███████╗  ▄██████─▀─██████▄
 ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚══════╝╚══════╝  █████████████████
 •၊၊||၊|။||||။‌‌‌‌‌၊|၊၊||၊|။||||။‌‌‌‌‌၊|၊၊||၊|။||||။‌‌‌‌‌၊|၊၊||၊|။||||။‌‌‌‌‌၊|၊၊||၊|•
    """, 'green')
    print_colored("[+] Made by ETASTEEE DEVS And skids", 'green')
    print_colored("[INFO]  Welcome to Etasteee GL", 'red')
    print("=" * 60)
    print_colored("1. Start ", 'blue')
    print_colored("2. About", 'yellow')
    print_colored("3. Exit", 'red')
    print("=" * 60)

    choice = input("\nChoose an option (1-3): ").strip()

    if choice == '1':
        username = input("\nEnter Roblox Username/UserID: ").strip()
        fake_bruteforce(username)
        input("\nPress Enter to return to menu...")
    elif choice == '2':
        print_colored("\nThis is a goon ", 'yellow')
        input("\nPress Enter to return to menu...")
    elif choice == '3':
        print_colored("\nExiting... Peace out nigger 😎", 'red')
        time.sleep(1)
        sys.exit()
    else:
        print_colored("Invalid option. Try again.", 'red')
        time.sleep(1)

if __name__ == "__main__":
    try:
        while True:
            hacker_menu()
    except KeyboardInterrupt:
        print_colored("\n\nSession interrupted. Exiting cleanly.", 'red')
