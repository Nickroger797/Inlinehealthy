import requests
import time

def sync_time():
    try:
        response = requests.get("http://worldtimeapi.org/api/timezone/Etc/UTC")
        response.raise_for_status()
        utc_time = response.json()["unixtime"]
        local_time = int(time.time())

        global TIME_OFFSET
        TIME_OFFSET = utc_time - local_time
        print(f"✅ Time synced successfully! Offset: {TIME_OFFSET} seconds")
    except Exception as e:
        print(f"❌ Error syncing time: {e}")
        TIME_OFFSET = 0

sync_time()
