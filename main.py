import psutil, os, time

# Get Boot Time of Local System
boot_time = psutil.boot_time()
print(f"System boot time: {time.ctime(boot_time)}")