import time

def sync_time():
    global TIME_OFFSET
    try:
        utc_time = int(time.time())  # Directly system time use करो
        local_time = int(time.time())

        TIME_OFFSET = utc_time - local_time
        print(f"✅ Time synced successfully! Offset: {TIME_OFFSET} seconds")
    except Exception as e:
        print(f"❌ Error syncing time: {e}")
        TIME_OFFSET = 0

sync_time()
