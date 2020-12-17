import time
from datetime import datetime as dt

hosts_path = r"\etc\hosts" #C:\Windows\System32\drivers for windows machines host directory
redirect ="127.0.0.1"
wesbite_list = ["www.facebook.com", "www.instagram.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,00) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,3):
        print("site blocking active...")
        with open(hosts, 'r+') as file:
            content = file.read()
            for website in wesbite_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        print("site blocking not active...")
    time.sleep(5)
