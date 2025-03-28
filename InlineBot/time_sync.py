import time
import requests

def sync_time():
    try:
        response = requests.get("http://worldtimeapi.org/api/timezone/Etc/UTC").json()
        server_time = response["unixtime"]
        local_time = int(time.time())
        global TIME_OFFSET
        TIME_OFFSET = server_time - local_time  # अब यह variable define हो गया है
        print(f"✅ Time synced successfully! Offset: {TIME_OFFSET} seconds")
    except Exception as e:
        print(f"⚠️ Time sync failed: {e}")

sync_time()
