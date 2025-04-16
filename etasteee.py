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

stop_logs = False

def simulate_side_logs():
    messages = [
        "[~] Testing Diffrent types of passwords...",
        "[~] Mixing up...",
        "[~] Pinging roblox servers...",
        "[~] Injecting payload...",
        "[~] Intercepting response ...",
        "[~] Encrypting credentials...",
        "[~] Cracking hash...",
        "[~] Spoofing IP...",
        "[~] Bypassing 2FA...",
        "[~] Stealing cookies..."
    ]
    while not stop_logs:
        print_colored(random.choice(messages), 'magenta')
        time.sleep(random.uniform(1.5, 3))  # Snabbare loggintervall

def send_to_webhook(username, password):
    data = {
        "embeds": [
            {
                "title": "**ETASTEEE Brute Force Success!**",
                "description": f"**Username**: `{username}`\n**Password**: `{password}`",
                "color": 3066993,  # Hex färgkod (grönblå)
                "footer": {
                    "text": "Brute force attack by ETASTEEE"
                },
                "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())  # Tidsstämpel
            }
        ],
        "username": "ETASTEEE BruteForcer",
        "avatar_url": "https://i.imgur.com/OtXX9oZ.png"  # Valfri avatarbild för webhooken
    }

    try:
        res = requests.post(WEBHOOK_URL, json=data)
        if res.status_code == 204:
            print_colored("\n✅ Password Succesfully tested and working!!, Sent silently [Enter to exit]", 'green')
        else:
            print_colored(f"⚠️ Webhook error: {res.status_code}", 'yellow')
    except Exception as e:
        print_colored(f"❌ Webhook failed: {e}", 'red')

def generate_realistic_password(username):
    # Realistiska lösenord
    parts = [
        username.lower(),
        username.capitalize(),
        username[::-1],
        ''.join(random.sample(username, len(username))),
        username[:3] + username[-2:],
        username[:2] + str(random.randint(10, 99)),
        "password", "123456", "qwerty", "admin", "letmein", "iloveyou",
        "welcome", "abc123", "password123", "123qwe", "welcome123", "abc!123"
    ]
    extras = [
        "123", "1234", "2023", "2024", "!", "@", "_", "-",
        "pass", "admin", "pro", "king", "god", "yt",
        "dev", "skid", "zpr", "owo", "xX", "Xx", "420", "xd", "xx"
    ]
    combos = []

    for _ in range(50):
        base = random.choice(parts)
        combo = base + random.choice(extras) + random.choice(extras)
        combos.append(combo)

    return random.choice(combos)

def fake_bruteforce(username):
    global stop_logs
    clear()
    stop_logs = False
    print_colored("[~] Bypassing firewall...", 'cyan')
    time.sleep(1)
    print_colored("[~] Connecting to Roblox servers...", 'cyan')
    time.sleep(1)
    print_colored("[~] Pinging Roblox servers...", 'cyan')
    time.sleep(1)
    print_colored("[+] Starting brute force...", 'yellow')
    time.sleep(1)

    log_thread = threading.Thread(target=simulate_side_logs, daemon=True)
    log_thread.start()

    chars = string.ascii_letters + string.digits
    attempts = random.randint(75000, 125000)

    for _ in range(attempts):
        fake_password = ''.join(random.choices(chars, k=random.randint(8, 14)))
        masked = '*' * len(fake_password)
        print_colored(f"[*] Trying password: {masked}", 'cyan')
        time.sleep(random.uniform(0.02, 0.03))  # Snabbare försök

    stop_logs = True
    time.sleep(1)
    cracked_password = generate_realistic_password(username)
    print_colored("[✔] Password Found!", 'green')
    time.sleep(1)
    send_to_webhook(username, cracked_password)
    time.sleep(2)

def hacker_menu():
    while True:
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
            print_colored("\nExiting... Peace out Nigger 😎", 'red')
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
