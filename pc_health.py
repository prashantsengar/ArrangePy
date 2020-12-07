import subprocess


def system_info():
    """

    It Prints the Brief System Information by using the following command.

    """
    command = "systeminfo"
    print("Retrieving Information... ")
    info = subprocess.run(command, shell=True, capture_output=True)
    cat = info.stdout.decode()
    print(cat)


def open_detail():
    """

    It Open the Detailed System Information Window (Windows OS only).

    """
    command = "msinfo32"
    subprocess.run(command, shell=True)


def main():
    """

    This Function takes the input and execute either of the functions above or exit.

    """
    print("++++++++SYSTEM INFORMATION+++++++++")
    print("1. Display a Brief System Information\n2. Display the Detailed System's Software and Hardware Report")
    print("Press any Other Key to Exit")
    choice = input("Enter Here: ")
    if choice == "1":
        system_info()
    elif choice == "2":
        open_detail()
    else:
        print("Exiting...")
        exit(0)


main()
