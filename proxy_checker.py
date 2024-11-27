import threading
import queue
import requests

q = queue.Queue()
valid = []

# Read proxies from the file and add them to the queue
with open("proxy_list.txt", 'r') as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)

def check():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get("http://ipinfo.io/json", proxies={"http": proxy, "https": proxy}, timeout=5)
            if res.status_code == 200:
                valid.append(proxy)
                with open("valid_proxies.txt", "a") as valid_file:
                    valid_file.write(proxy + "\n")
        except:
            continue

# Start threads
threads = []
for _ in range(10):
    t = threading.Thread(target=check)
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("Valid proxies saved to valid_proxies.txt")

with open(valid_proxy, "w", encoding="utf-8") as f:
        for p in valid:
            f.write(f"{p}\n")