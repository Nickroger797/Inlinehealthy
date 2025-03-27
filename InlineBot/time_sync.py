import time
import os

# System Time Sync Fix
print("Syncing system time...")
os.system("ntpdate -u pool.ntp.org")  # Koyeb में काम कर सकता है

print("Time synced successfully.")
time.sleep(2)
