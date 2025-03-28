import time
import requests
import os

def sync_time():
    try:
        response = requests.get("http://worldtimeapi.org/api/timezone/Etc/UTC").json()
        server_time = response["unixtime"]
        local_time = int(time.time())
        time_diff = server_time - local_time
        if abs(time_diff) > 5:
            os.system(f"date -s @{server_time}")
        print(f"✅ Time synced successfully! Offset: {time_diff} seconds")
    except Exception as e:
        print(f"⚠️ Time sync failed: {e}")

sync_time()
