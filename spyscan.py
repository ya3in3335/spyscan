# spyscan - by ⚡𝙏𝙞𝙢𝙤
import os
import time

# تثبيت المكتبات تلقائياً
try:
    import colorama
    from colorama import Fore, Style
    import pyfiglet
    import requests
    import socket
except ImportError:
    os.system("pip install colorama pyfiglet requests")
    import colorama
    from colorama import Fore, Style
    import pyfiglet
    import requests
    import socket

colorama.init()

# 🎨 ألوان
RED = Fore.RED
GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
RESET = Style.RESET_ALL

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    clear()
    title = pyfiglet.figlet_format("spyscan", font="slant")
    print(f"{MAGENTA}{title}{RESET}")
    
    print(f"{CYAN}┌" + "─" * 47 + "┐")
    print(f"{CYAN}│{RESET}{' ' * 47}{CYAN}│")
    print(f"{CYAN}│{RESET}  ⚡ Developer : {YELLOW}⚡𝙏𝙞𝙢𝙤{RESET}{' ' * (26 - len('⚡𝙏𝙞𝙢𝙤'))}{CYAN}│")
    print(f"{CYAN}│{RESET}  📢 Telegram : {YELLOW}https://t.me/hacker16_thsb{RESET}{CYAN}│")
    print(f"{CYAN}│{RESET}{' ' * 47}{CYAN}│")
    print(f"{CYAN}└" + "─" * 47 + "┘{RESET}\n")

def menu():
    print(f"""
{GREEN}[1]{RESET} Fast Scan
{GREEN}[2]{RESET} Full Port Scan
{GREEN}[3]{RESET} Stealth Scan (قريبًا)
{GREEN}[4]{RESET} Banner Grabbing
{GREEN}[5]{RESET} OS Detection
{GREEN}[6]{RESET} Vulnerability Check
{GREEN}[7]{RESET} IP Geolocation
{GREEN}[8]{RESET} Save Result
{GREEN}[9]{RESET} Exit
""")

def fast_scan(target):
    print(f"{CYAN}[*] Running fast scan on {target}...{RESET}")
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]
    result = ""
    for port in common_ports:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            print(f"{GREEN}[+] Port {port} is open{RESET}")
            result += f"Port {port} is open\n"
            s.close()
        except:
            pass
    return result

def full_scan(target):
    print(f"{CYAN}[*] Running full port scan on {target} (1-1024)...{RESET}")
    result = ""
    for port in range(1, 1025):
        try:
            s = socket.socket()
            s.settimeout(0.1)
            s.connect((target, port))
            print(f"{GREEN}[+] Port {port} is open{RESET}")
            result += f"Port {port} is open\n"
            s.close()
        except:
            pass
    return result

def banner_grab(target, port):
    print(f"{CYAN}[*] Grabbing banner from {target}:{port}...{RESET}")
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        banner = s.recv(1024)
        print(f"{YELLOW}[BANNER] {banner.decode().strip()}{RESET}")
    except:
        print(f"{RED}[-] Couldn't grab banner from port {port}{RESET}")

def os_detection(target):
    print(f"{CYAN}[*] Detecting OS (guess)...{RESET}")
    try:
        ttl = os.popen(f"ping -c 1 {target}").read()
        if "ttl=64" in ttl:
            print(f"{GREEN}[+] Likely OS: Linux/Unix{RESET}")
        elif "ttl=128" in ttl:
            print(f"{GREEN}[+] Likely OS: Windows{RESET}")
        else:
            print(f"{YELLOW}[?] OS Detection inconclusive{RESET}")
    except:
        print(f"{RED}[-] Ping failed{RESET}")

def vuln_check(port):
    vulns = {
        21: "FTP - Check for anonymous login",
        22: "SSH - Weak credentials",
        80: "HTTP - Outdated server",
        445: "SMB - EternalBlue"
    }
    if port in vulns:
        print(f"{RED}[!] Vulnerability Hint: {vulns[port]}{RESET}")
    else:
        print(f"{GREEN}[+] No known issue for port {port}{RESET}")

def geo_ip(target):
    print(f"{CYAN}[*] Getting geolocation for {target}...{RESET}")
    try:
        response = requests.get(f"http://ip-api.com/json/{target}").json()
        print(f"{GREEN}[+] Country: {response['country']}")
        print(f"[+] City: {response['city']}")
        print(f"[+] ISP: {response['isp']}")
        print(f"[+] Region: {response['regionName']}{RESET}")
    except:
        print(f"{RED}[-] Failed to get location{RESET}")

def save_result(data):
    with open("scan_result.txt", "w") as f:
        f.write(data)
    print(f"{GREEN}[+] Results saved to scan_result.txt{RESET}")

# ===== Main Loop =====
while True:
    banner()
    target = input(f"{YELLOW}[?] Enter target IP/host: {RESET}")
    while True:
        banner()
        print(f"{CYAN}Target: {target}{RESET}")
        menu()
        choice = input(f"{YELLOW}[>>] Choose option: {RESET}")
        if choice == "1":
            result = fast_scan(target)
        elif choice == "2":
            result = full_scan(target)
        elif choice == "3":
            print(f"{CYAN}[i] Stealth scan not implemented yet! Coming soon...{RESET}")
        elif choice == "4":
            port = int(input(f"{YELLOW}[?] Port for banner grabbing: {RESET}"))
            banner_grab(target, port)
        elif choice == "5":
            os_detection(target)
        elif choice == "6":
            port = int(input(f"{YELLOW}[?] Port to check for vulnerability: {RESET}"))
            vuln_check(port)
        elif choice == "7":
            geo_ip(target)
        elif choice == "8":
            try:
                save_result(result)
            except:
                print(f"{RED}[x] No result to save yet.{RESET}")
        elif choice == "9":
            print(f"{CYAN}[*] Exiting...{RESET}")
            exit()
        else:
            print(f"{RED}[x] Invalid choice!{RESET}")
        input(f"\n{YELLOW}Press Enter to return to menu...{RESET}")
