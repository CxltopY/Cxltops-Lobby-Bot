import time,requests,os,traceback,sys,json

with open("fortnite.py", encoding='utf-8') as f:
    current = f.read().replace('“','"').replace('”','"')
github = requests.get("https://raw.githubusercontent.com/CxltopY/Cxltops-Lobby-BotV2/blob/main/fortnite.py").text.replace('“','"').replace('”','"')
if current != github:
    print('I found an update, downloading...')
    os.remove("fortnite.py")
    with open("fortnite.py", 'w') as f:
        f.write(github)
    print('Done, starting your bot now.')
elif current == github:
    print('No update!')
os.chdir(os.getcwd())
os.execv(os.sys.executable,['python','fortnite.py'])