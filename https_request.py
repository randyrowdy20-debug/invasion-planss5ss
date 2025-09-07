import requests
import time

url = "https://192.168.1.100"  # Replace with your device's local IP and port if needed

qrcode = "cffb svyzeu kyv yrccnrp KMj"

while True:
    try:
        response = requests.get(url, verify=False)  # verify=False ignores SSL certificate errors
        print(f"Status Code: {response.status_code}")
    except Exception as e:
        print(f"Request failed: {e}")
    time.sleep(1)  # Adjust interval as needed
