import time, os, threading, requests, random, ctypes, dhooks, sys
from colorama import Fore
from dhooks import Webhook

def center(var:str, space:int=None):
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())


if sys.platform == "win32":
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")

start = time.perf_counter()

class NitroGen():
    def __init__(self):
        self.nitroGen = ''
        char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        for i in range(16):
            self.nitroGen = self.nitroGen + random.choice(char)

def getWebhook():
    with open("webhook.txt", "r") as webhook:
        result = webhook.read()
        webhook.close()
    return result

def getProxies():
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000&ssl=yes')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.replace('\r', '')
        if proxy:
            proxies.append(proxy)
    return proxies

def testnitroGen():
    webhook = getWebhook()
    if webhook == "None":
        usingWebhook = False
    else:
        usingWebhook = True
    testedCodesGen = 0
    for i in range(3):
        ProxyList = getProxies()
        for proxy in ProxyList:
            ProxyParameters ={'http://': proxy,'https://': proxy}
            for i in range(3):
                nitrogen = NitroGen()
                url = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitrogen.nitroGen}", proxies=ProxyParameters, timeout=5)
                if url.status_code == 200:
                    if usingWebhook == True:
                        hook = Webhook(webhook)
                        hook.send(content=f"@everyone nitro is ready https://discord.gift/{nitrogen.nitroGen}")
                    with open('nitroCodesGen.txt', 'w') as nitros:
                        nitros.write(nitrogen.nitroGen)
                        nitros.close()
                    print(f"{Fore.WHITE}[{Fore.GREEN}>{Fore.WHITE}] {Fore.GREEN}VALID CODE{Fore.WHITE} : https://discord.gift/{nitrogen.nitroGen}")
                print(f"{Fore.WHITE}[{Fore.RED}>{Fore.WHITE}] {Fore.RED}Invalid{Fore.WHITE} : https://discord.gift/{nitrogen.nitroGen}")
                testedCodesGen += 1
    with open('testedCodesGen.txt', 'r+', encoding="utf8") as file:
        count = file.read()
        newCount = int(count) + testedCodesGen
        file.close()

    with open('testedCodesGen.txt', 'w', encoding="utf8") as file:
        file.write(str(newCount))
        file.close()
    testnitroGen()

class Console():
    def ui(self):
        os.system(f'cls && title DiscordNitroGen ^| xann wrld#0101 ' if os.name == "nt" else "clear")
        print(center(f"""\n\n



███╗   ██╗██╗████████╗██████╗  ██████╗  ██████╗ ███████╗███╗   ██╗
████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗██╔════╝ ██╔════╝████╗  ██║
██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║██║  ███╗█████╗  ██╔██╗ ██║
██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║██║   ██║██╔══╝  ██║╚██╗██║
██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝╚██████╔╝███████╗██║ ╚████║
╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                By: xann wrld#0101
                                                        
> https://github.com/xannbtw/ ~ https://discord.gg/Ww4kgVdJ
\n\n
	""").replace('█', Fore.CYAN + "█" + Fore.RESET).replace('>', Fore.CYAN+ ">" + Fore.RESET).replace('~', Fore.CYAN+ "~" + Fore.RESET))       

clear()
Console().ui()


finished = time.perf_counter()
timeToLoad = finished-start
print("[>] Threads : 1 - 150\n")
print("[>] Attention to the CPU\n")
print("[>] Do you want to receive the code with a webhook? (Y/N) ? \n")
webhook = str(input('-> '))
if webhook == "Y" or "y":
    webhooklink = str(input('[>] Webhook link => '))
    webhookExample = 'https://discord.com/api/webhooks/'
    if webhookExample in webhooklink:
        with open('webhook.txt', 'w') as webhookFile:
            webhookFile.write(webhooklink)
            webhookFile.close()
    else:
        print('There is a problem with your webhook.')
        time.sleep(1)
        clear()
        main(start)
elif webhook == "N":
    with open('webhook.txt', 'w') as webhookFile:
        webhookFile.write("None")
        webhookFile.close()
else:
    print(f'{Fore.RED}[!] Your request is not valid!')
    time.sleep(1)
    clear()
    main(start)

try:
    threads = int(input('Threads => '))
    clear()
    Console().ui()
    if threads <= 150:
        for i in range(threads):
            thread = threading.Thread(target=testnitroGen)
            thread.start()       
    else:
        print(f'{Fore.RED}[!] Your request is not valid!')
        time.sleep(1)
        clear()
        main(start)
except ValueError:
    clear()
    main(start)
