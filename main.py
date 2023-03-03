import requests
import random
import string

print("""
███╗░░██╗██╗████████╗██████╗░░█████╗░  ░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝""")
    

NumOfLinks = int(input("How much Links: "))
ProxyFile = input("Proxy File To Use: ")



with open("NitroGens.txt", "a+") as GenNitro:
    print("[*] Generating Nitro Codes (Could Take A While)\n")
    
    for i in range(NumOfLinks):
        link = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))
        
        GenNitro.write("https://discordapp.com/api/v6/entitlements/gift-codes/"+link+"\n")
    
    print("[+] Generated")

with open("NitroGens.txt", "r") as NitroCheck:
    n = 0
    for line in NitroCheck.readlines():
        nitro = line.strip('\n')
        
        try:
            req = requests.get(nitro)
        except:
            continue
        if req.status_code==200:
            print(f"[+]Code Found | {nitro}")
            break
        else:
            print(f"[-]Invalid | {nitro}")