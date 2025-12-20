import psutil

def system_health_check():
    # Take thresholds from user
    cpu_threshold = int(input("Enter CPU usage threshold (%): "))
    memory_threshold = int(input("Enter Memory usage threshold (%): "))
    disk_threshold = int(input("Enter Disk usage threshold (%):"))

    # Get current CPU and Memory usage
    current_cpu = psutil.cpu_percent(interval=1)
    current_memory = psutil.virtual_memory().percent
    current_disk = psutil.disk_usage('C:\\').percent

    print("\n--- System Health Report ---")
    print(f"CPU Usage    : {current_cpu}%")
    print(f"Memory Usage : {current_memory}%")
    print(f"Disk Usage : {current_disk}%")

    # CPU check
    if current_cpu > cpu_threshold:
        print("ALERT: CPU usage is HIGH")
        print("CPU alert sent to Admin")
    else:
        print("CPU is in safe state")

    # Memory check
    if current_memory > memory_threshold:
        print("ALERT: Memory usage is HIGH")
        print("Memory alert sent to Admin")
    else:
        print("Memory is in safe state")

    # Disk check
    if current_disk > disk_threshold:
        print("ALERT: Disk usage is HIGH")
        print("Disk alert sent to Admin")
    else:
        print("Disk is in safe state")    

# Call the function
system_health_check()
