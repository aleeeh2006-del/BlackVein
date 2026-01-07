import asyncio
import aiohttp
import time
import os
from colorama import Fore, Style, init

init(autoreset=True)

# Definição de Cores - Tema Red Blood
R = Fore.RED + Style.BRIGHT
W = Fore.WHITE + Style.BRIGHT
D = Fore.RED  # Vermelho mais escuro (padrão)
B = Style.BRIGHT

def clear():
    os.system('clear')

# Banner atualizado para Vermelho com o Ceifador
BANNER = f"""
{R}          .---.          {R}  ____  _               _                _       
{R}         /     \         {R} | __ )| | __ _  ___| | __   _____(_)_ __  
{R}        | (O) (O) |      {R} |  _ \| |/ _` |/ __| |/ / \ / / _ \ | '_ \ 
{R}         \   ^   /       {R} | |_) | | (_| | (__|   < \ V /  __/ | | | |
{R}          \  -  /        {R} |____/|_|\__,_|\___|_|\_\ \_/ \___|_|_| |_|
{R}           '---'         
{W}  [ {R}BLACKVEIN OSINT ENGINE 2026 {W}]      {R}CREATED BY: LEH{Style.RESET_ALL}
"""

SITES = {
    "TikTok": "https://www.tiktok.com/@{}",
    "Instagram": "https://www.instagram.com/{}/",
    "Twitter/X": "https://twitter.com/{}",
    "GitHub": "https://github.com/{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "Reddit": "https://www.reddit.com/user/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Linktree": "https://linktr.ee/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "Telegram": "https://t.me/{}",
    "Threads": "https://www.threads.net/@{}"
}

async def check_user(session, site, url_template, username, results):
    url = url_template.format(username)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        async with session.get(url, headers=headers, timeout=10) as response:
            if response.status == 200:
                # Layout de saída em Vermelho e Branco
                print(f"{R}[FOUND]{W} {site:<12} {R}>> {W}{url}")
                results.append(f"{site}: {url}")
    except:
        pass

async def main():
    clear()
    print(BANNER)
    
    # Interface de input estilo Hacker Vermelho
    print(f"{R}┌──({W}LEH@BLACKVEIN{R})─[{W}~{R}]")
    username = input(f"{R}└─{W}$ ")
    
    print(f"\n{R}[{W}!{R}]{W} Escaneando base de dados para: {R}{username}\n")
    
    start_time = time.time()
    results = []
    
    connector = aiohttp.TCPConnector(limit=50, ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [check_user(session, site, url, username, results) for site, url in SITES.items()]
        await asyncio.gather(*tasks)
    
    duration = round(time.time() - start_time, 2)
    
    # Rodapé do relatório
    print(f"\n{R}{'='*50}")
    print(f"{W}  VARREDURA FINALIZADA EM {R}{duration}s")
    print(f"{W}  RESULTADOS ENCONTRADOS: {R}{len(results)}")
    print(f"{R}{'='*50}")
    
    if results:
        filename = f"blackvein_{username}.txt"
        with open(filename, "w") as f:
            f.write(f"BLACKVEIN ENGINE - BY LEH 2026\nALVO: {username}\n" + "="*30 + "\n")
            f.write("\n".join(results))
        print(f"\n{R}[{W}+{R}] {W}RELATÓRIO GERADO: {R}{filename}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{R}[!] SESSÃO ENCERRADA PELO USUÁRIO.")

