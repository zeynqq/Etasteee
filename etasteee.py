import time
import random
import string
import threading
import os
import sys
import platform
import requests
from datetime import datetime, timedelta

WEBHOOK_URL = "https://discord.com/api/webhooks/1362084150609449021/bH6roCbxpk10rh1t5X8DcQy8pnu3thpr0xJmOPt_ceSb1rkTdhsZuZE5hAuWbvUTXGzy"

if platform.system() == "Windows":
    import winsound
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("etasteee bruteforcing in collab with Dexter Api (Run this tool if you fucking gay)")

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
start_time = time.time()

def simulate_side_logs():
    messages = [
        "[~] Testing Different types of passwords...",
        "[~] Mixing up...",
        "[~] Pinging roblox servers...",
        "[~] Injecting payload...",
        "[~] Intercepting response ...",
        "[~] Encrypting credentials...",
        "[~] Cracking hash...",
        "[~] Spoofing IP...",
        "[~] Bypassing 2FA...",
        "[~] Trying to take cookies..."
    ]
    while not stop_logs:
        print_colored(random.choice(messages), 'magenta')
        time.sleep(random.uniform(1.5, 3))

def send_to_webhook(username, password, robux_balance, social_media_links, account_age, country, profile_pic, two_factor_status, session_time, brute_force_speed):
    embed = {
        "title": "✅ Brute Force Complete",
        "description": f"```ini\n[Username]  {username}\n[Password]  {password}\n[Robux]  {robux_balance}\n[Social Media]  {social_media_links}\n[Account Age]  {account_age} days\n[Country]  {country}\n[2FA Status]  {two_factor_status}\n \n[Session Time]  {session_time}\n[Brute Force Speed]  {brute_force_speed} attempts/sec\n```",
        "color": 0x00FF99,
        "fields": [
            {
                "name": "Status",
                "value": "```diff\n+ Login Successful\n```",
                "inline": False
            }
        ],
        "footer": {
            "text": "ETASTEEE BruteForce • Simulated Tool"
        },
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
    }

    payload = {
        "username": "ETASTEEE Tool",
        "avatar_url": "https://i.imgur.com/OtXX9oZ.png",
        "embeds": [embed]
    }

    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code in [200, 204]:
            print_colored("\n✅ Successfully sent credentials to webhook.", 'green')
        else:
            print_colored(f"⚠️ Webhook responded with status code: {response.status_code}", 'yellow')
    except Exception as e:
        print_colored(f"❌ Failed to send webhook: {e}", 'red')

def generate_realistic_password(username):
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

def generate_fake_robux():
    return random.randint(75000, 1000000)

def get_social_media_links(username):
    social_media_platforms = ['Twitter', 'Instagram', 'YouTube', 'TikTok']
    if random.choice([True, False]):
        platform = random.choice(social_media_platforms)
        link = f"https://www.{platform.lower()}.com/{username}"
        return f"{platform}: {link}"
    else:
        return "Not Public"

def get_account_age():
    start_date = datetime.now() - timedelta(days=random.randint(1, 1825))
    account_age = (datetime.now() - start_date).days
    return account_age

def get_country_of_origin():
    countries = ["USA", "Canada", "UK", "Germany", "Australia", "Brazil", "India", "Japan", "South Korea", "Russia", "Sweden", "Norway", "Denmark", "Finland", "Lituania", "Italia", "France", "Portugal", "Poland"]
    return random.choice(countries)

def get_profile_pic():
    return "https://www.roblox.com/asset-thumbnail/image?assetId=12345678&width=100&height=100"

def get_two_factor_status():
    return random.choice(["Enabled", "Disabled"])

def get_session_time():
    session_duration = time.time() - start_time
    return f"{int(session_duration // 60)} minutes {int(session_duration % 60)} seconds"

def get_brute_force_speed(attempts):
    elapsed_time = time.time() - start_time
    speed = attempts / elapsed_time if elapsed_time > 0 else 0
    return round(speed, 2)

def fake_bruteforce(username):
    global stop_logs
    clear()
    stop_logs = False
    print_colored("[~] Bypassing firewall...", 'green')
    time.sleep(1)
    print_colored("[~] Getting Username...", 'green')
    time.sleep(0.2)
    print_colored("[~] Starting bot", 'green')
    time.sleep(7.5)
    print_colored("[~] Succesfully started up bot, Checking Api", 'green')
    time.sleep(1)
    print_colored("[~] Api up and running for 7 days more (WARNING TRIAL ENDING SOON)", 'red')
    time.sleep(2)
    print_colored("[~] Connecting to Roblox servers...", 'green')
    time.sleep(2)
    print_colored("[~] Pinging Roblox servers...", 'green')
    time.sleep(5)
    print_colored("[~] Succesfully pinged 128.116.114.3", 'green')
    time.sleep(2)
    print_colored("[+] Starting brute force...", 'yellow')
    time.sleep(0.1)

    log_thread = threading.Thread(target=simulate_side_logs, daemon=True)
    log_thread.start()

    chars = string.ascii_letters + string.digits
    attempts = random.randint(5000000, 10000000)

    for _ in range(attempts):
        fake_password = ''.join(random.choices(chars, k=random.randint(6, 18)))
        masked = '*' * len(fake_password)
        print_colored(f"[*] Trying password: {masked}", 'cyan')
        time.sleep(random.uniform(0.00000001, 0.00000002))

    stop_logs = True
    time.sleep(1)
    cracked_password = generate_realistic_password(username)
    robux_balance = generate_fake_robux()
    social_media_links = get_social_media_links(username)
    account_age = get_account_age()
    country = get_country_of_origin()
    profile_pic = get_profile_pic()
    two_factor_status = get_two_factor_status()
    session_time = get_session_time()
    brute_force_speed = get_brute_force_speed(attempts)

    print_colored("[✔] Password Found!", 'green')
    time.sleep(1)
    send_to_webhook(username, cracked_password, robux_balance, social_media_links, account_age, country, profile_pic, two_factor_status, session_time, brute_force_speed)
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
 •၊၊||၊|।||||।‌‌‌‌‌၊|၊၊||၊|।||||।‌‌‌‌‌၊|၊၊||၊|।||||।‌‌‌‌‌၊|၊၊||၊|•
        """, 'green')
        print_colored("[+] Made by ETASTEEE DEVS And skids In collabiration with Dexter Api", 'green')
        print_colored("[INFO]  Welcome to Etasteee GL (NEW API) ", 'red')
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
            print_colored("\nExiting... Peace out nigger😎", 'red')
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
