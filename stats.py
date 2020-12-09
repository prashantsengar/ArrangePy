# import this library to obtain a huge list of underlying system info and features
# importing required libraries
import platform
import wmi
import psutil
import sys
import subprocess
import datetime
import GPUtil
from tabulate import tabulate

# global stat holder. will contain all our data
stats = {}
# initalising the system info object using uname module
# of the platform library
sys_info = platform.uname()
# initialising the hardware info object using the WMI module
# of the wmi library
_info = wmi.WMI()
wmi_info = _info.Win32_ComputerSystem()[0]
# system software and hardware info
stats["manufacturer"] = wmi_info.manufacturer
stats["model"] = wmi_info.model
stats["name"] = wmi_info.name
stats["number_of_processors"] = wmi_info.NumberOfProcessors
stats["sys_type"] = wmi_info.SystemType
stats["sys_family"] = wmi_info.SystemFamily
stats["release"] = sys_info.release
stats["version"] = sys_info.version
stats["processor"] = sys_info.processor
stats["architecture"] = platform.architecture()
stats["machine"] = platform.machine()
stats["node_id"] = platform.node()
stats["system"] = platform.system()
stats["total_system_info"] = platform.uname()
# another possible system info , verbose
id = subprocess.check_output(["systeminfo"]).decode("utf-8").split("\n")
new = []
for data in id:
    new.append(str(data.split("\r")[:-1]))
# saving system information to global list
stats["complete_sys_info"] = new
# extracting timestamp of first boot
boot_timestamp = psutil.boot_time()
# converting epoch to year,month,day,hour,minute,second format
time = datetime.datetime.fromtimestamp(boot_timestamp)
# storing first boot time data
stats["boot_timestamp_year"] = time.year
stats["boot_timestamp_month"] = time.month
stats["boot_timestamp_day"] = time.day
stats["boot_timestamp_hour"] = time.hour
stats["boot_timestamp_minute"] = time.minute
stats["boot_timestamp_second"] = time.second
# extracting number of CPU cores (physical and logical)
stats["cpu_physical_cores"] = psutil.cpu_count(logical=False)
stats["cpu_total_cores"] = psutil.cpu_count(logical=True)
stats["cpu_virtual_cores"] = stats["cpu_total_cores"] - stats["cpu_physical_cores"]
cpu_freq = psutil.cpu_freq()
# Note : CPU Frequency returned in MHz
stats["cpu_frequency_max"] = cpu_freq.max
stats["cpu_frequency_min"] = cpu_freq.min
stats["cpu_frequency_current"] = cpu_freq.current
# extracting core usage data for every CPU core
cpu_core_usage_stats = []
for i, percent in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    cpu_core_usage_stats.append((i, percent))
# storing core usage data in global list
stats["per_core_usage_stats"] = cpu_core_usage_stats
stats["total_core_usage"] = psutil.cpu_percent()
# extracting memory statistics
# Note : Memory stats are in GB (converted by dividing output by 1024^3)
memory = psutil.virtual_memory()
stats["total_memory"] = memory.total / 1024 ** 3
stats["available_memory"] = memory.available / 1024 ** 3
stats["used_memory"] = memory.used / 1024 ** 3
stats["used_memory_percentage"] = memory.percent
# extracting swap memory details and saving in global list
swap_mem = psutil.swap_memory()
stats["total_swap_memory"] = swap_mem.total
stats["free_swap_memory"] = swap_mem.free
stats["used_swap_memory"] = swap_mem.used
stats["used_swap_memory_percentage"] = swap_mem.percent
# extracting data about disk partitions
disk_partition = psutil.disk_partitions()
partition_data = []
for partition in disk_partition:
    partition_data.append((partition.device, partition.mountpoint, partition.fstype))
# saving partitions data to global list
stats["partition_info"] = partition_data
# extracting disk usage statistics , usage output in GB
disk_usage = []
for partition in disk_partition:
    try:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_usage.append(
            (
                (usage.total / 1024 ** 3),
                (usage.used / 1024 ** 3),
                (usage.free / 1024 ** 3),
                (usage.percent / 1024 ** 3),
            )
        )
    # handling mountpoint permission denied error (partition may not be ready to use)
    except PermissionError:
        continue
stats["partition_usage"] = disk_usage
# get statistics about total disk read and write operations since first boot time
disk_io = psutil.disk_io_counters()
stats["total_disk_reads"] = disk_io.read_bytes / 1024 ** 3
stats["total_disk_writes"] = disk_io.write_bytes / 1024 ** 3
# extracting network data and saving in global list
net_data = psutil.net_if_addrs()
interface_details = []
for if_name, if_address in net_data.items():
    for address in if_address:
        interface_details.append((address.address, address.netmask, address.broadcast))
stats["net_interface_details"] = interface_details
# total data sent and received over network
# Note : Output is in Bytes , Can be converted to GB by dividing by 1024^3
net_io = psutil.net_io_counters()
# stats['total_data_sent_GB'] = net_io.bytes_sent/1024 ** 3
# stats['total_data_received_GB'] = net_io.bytes_recv/1024 ** 3
stats["total_data_sent"] = net_io.bytes_sent
stats["total_data_received"] = net_io.bytes_recv
# extracting GPU details and storing to global list
gpu_data = GPUtil.getGPUs()
gpus = []
for gpu in gpu_data:
    gpus.append(
        (
            gpu.id,
            gpu.name,
            gpu.load * 100,
            gpu.memoryFree / 1024,
            gpu.memoryUsed / 1024,
            gpu.memoryTotal / 1024,
            gpu.temperature,
            gpu.uuid,
        )
    )
stats["gpu_data"] = gpus
# few pre-defined functions for pretty printing
# function to print total system info
def print_system_info():
    print("System Info :")
    print("-------------")
    for info in new:
        print(info[2:-2])


# function to print usage of every core. shows implementation of the tabulate function
def print_each_core_stat():
    print(
        tabulate(
            enumerate(psutil.cpu_percent(percpu=True, interval=1)),
            headers=("id", "percentage"),
        )
    )
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")


# function to print the usage of and data of every GPU. shows implementation of the tabulate function
def print_pretty_GPU():
    print(
        tabulate(
            gpus,
            headers=(
                "id",
                "name",
                "load",
                "free memory (GB)",
                "used memory (GB)",
                "total memory (GB)",
                "temperature (C)",
                "uuid",
            ),
        )
    )
