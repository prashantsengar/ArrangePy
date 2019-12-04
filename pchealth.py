import psutil
import sys
from psutil._common import bytes2human

class system_health():
    
    def userinfo():
        print("User Info:")
        uinfo = psutil.users()
        print("The users connected to the sysytem at present are : ",end='')
        for term in range(0,len(uinfo)):
            print(f"{uinfo[term].name}",end=",")
        print("\n")



    def batteryinfo():
        print("Battery Info:")
        battery = psutil.sensors_battery()

        if battery!= None:
            sec = battery.secsleft
            min ,sec = divmod(sec,60)
            hour,min = divmod(min,60)
            if hour >=0:
                print(f"Time remaining for complete discharge is {hour}hr: {min}min: {sec}sec")
                print(f"Battery percentage left: {battery.percent}%")
                print("\n")
            else:
                print(f"Battery percentage left: {battery.percent}%")
                print("\n")

            if battery.percent < 20 and battery.power_plugged == False:
                print(f"Please connect charger.\nBattery Percentage left is {battery.percent}%\n")   
            if battery.percent > 90 and battery.power_plugged == True:
                print(f"Please disconnect charger.\nBattery Percentage is {battery.percent}%\n")            
        else:
            print("Battery Status Information can't be determined!")
            print("\n")
            


    def system_temp():
        print("System's Temperature:\n")
        temp = psutil.sensors_temperature()
        if len(temp) !=0:
            print("The hardware and their respective temperatuers are: ")
            for key,value in temp:
                print(f"{key:^6}  {value[0].current:^6} C")
                
        else:
            print("The temperature status information can't be determined")


    def fan_speed():
        print("Fan Speed :")
        fans = psutil.sensors_fans()
        if len(fans)!= 0 :
            for hardware,fan in fans:
                print(f"{fan.label:^6}  {fan.current:^6}")
        else:
            print("Fan Speed can't be determined!")



    def memory_info():
        print("Disk Usage: ")
        lis=[]
        template = "{0:^16} {1:^16} {2:^16} {3:^16}"
        disks = psutil.disk_partitions(all=False)
        for disk in disks:
            lis.append(disk.device)
        for drive in lis:
            print(drive)
            memory = psutil.disk_usage(drive)
            print(template.format("Total Memory ","Free Memory","Used Memory","Percent of memory available"))
            print(template.format(bytes2human(memory.total),bytes2human(memory.used),bytes2human(memory.free),str(memory.percent)+ "%"))
        print("\n")



    def virt_memory():
        print("Virtual Memory Stats: ")
        template = "{0:^16} {1:^16} {2:^16} {3:^16} {4:^16}"
        virtual = psutil.virtual_memory()
        print(template.format("Total ","Available memory","Used memory","Free memory","Percent"))
        print(template.format(bytes2human(virtual.total),bytes2human(virtual.available),bytes2human(virtual.used),bytes2human(virtual.free),str(virtual.percent)+ "%"))
        print("\n")
        
    

