import psutil
import datetime

def cpu_info():
    cpu_usage_per_core = psutil.cpu_percent(interval=1, percpu=True)
    num_cores = psutil.cpu_count(logical=True)
     # logical = True ,Get the number of logical cpu cores.. logical = False, get the number of physical cpu core

     # Print CPU usage for each core along with its index
    for core_index, usage in enumerate(cpu_usage_per_core):
     print(f"CPU {core_index + 1}: {usage}%")
    #  print(num_cores)

    """Alternatively, you can print the same information with a loop over the range
    for core_index in range(num_cores):
    print(f"CPU{core_index + 1}: {cpu_usage_per_core[core_index]}%")"""
def memory_info():
    virtual_memory=psutil.virtual_memory()
    print(virtual_memory)

def disk_usage():
    path=input("Write down the path of the disk (eg: /home/username) : ")
    try:
     used_disk=psutil.disk_usage(f"{path}") # usage of specific disk
     print(used_disk)
    except:
        print(f"{path} doesn't exist")

def battery_info():
    info_battery=psutil.sensors_battery()
    print("Battery available: ", info_battery[0], "%")
    print("Power plugged status : ", info_battery[2])

def system_uptime():
    uptime=psutil.boot_time() # counting form the epoch time
    # print(datetime.datetime.fromtimestamp(uptime))
    print("Your system was last booted on: ", end=" ")
    print(datetime.datetime.fromtimestamp(uptime).strftime("%Y-%m-%d %H:%M:%S"))
    # datetime.datetime.fromtimestamp(uptime) this already returns an object in %Y-%m-%d %H:%M:%S format, strftime is used to customize the output as per user.

def get_cpu_temperature():
    try:
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as file:
            temp_str = file.read()
            temp_str=float(temp_str)/1000.0
            """
            the temperature values are provided in a format where the raw value represents the temperature multiplied by a scaling factor. The scaling factor may be a power of 10. In your case, it seems like the temperature is being reported in a format where the raw value needs to be divided by 1000 to get the actual temperature in degrees Celsius.
            """
            print(f"CPU temperature is {temp_str} °C")
            return temp_str # else it will return none
    except FileNotFoundError:
        return None

def info_about_user():
    print(psutil.users())
    # pid = process id
    # started is the last boot time


# ............................................main program .................................................................
choice=input("Enter number between 1 to 5 -> \n 1 for info about cpu \n 2 for info about memory \n 3 for info about disk \n 4 for battery and charge status \n 5 for last boot info \n 6 to know the temp of CPU \n 7 to see info about users \n Choice :")
print("")

# operations based on choices
if choice=="1":
 cpu_info()
elif choice=="2":
 memory_info()
elif choice=="3":
 disk_usage()
elif choice=="4":
    battery_info()
elif choice=="5":
 system_uptime()
elif choice=="6":
 get_cpu_temperature()
elif choice=="7":
 info_about_user()