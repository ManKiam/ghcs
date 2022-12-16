import requests, os
r = requests.get('https://raw.githubusercontent.com/ManKiam/ghcs/main/ghcs.py').content
open('ghcs.py', 'wb').write(r)
os.system("python3 ghcs.py")
