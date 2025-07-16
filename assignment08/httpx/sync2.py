import requests
import time

url = ["https://httpbin.org/delay/3"]*5

start = time.time()
for u in url:
    response = requests.get(u)
    print(f'Status Code: {response.status_code}')
end = time.time()
print(f"Total time: {round(end - start, 2)} seconds")