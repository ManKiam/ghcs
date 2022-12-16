import requests
r = requests.get('https://raw.githubusercontent.com/ManKiam/ghcs/main/ghcs.py').content
open('ghcs.py', 'wb').write(r)
import ghcs
