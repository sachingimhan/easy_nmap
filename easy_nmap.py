import os
import subprocess

banner = """

    ███████╗ █████╗ ███████╗██╗   ██╗    ███╗   ██╗███╗   ███╗ █████╗ ██████╗
    ██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝    ████╗  ██║████╗ ████║██╔══██╗██╔══██╗
    █████╗  ███████║███████╗ ╚████╔╝     ██╔██╗ ██║██╔████╔██║███████║██████╔╝
    ██╔══╝  ██╔══██║╚════██║  ╚██╔╝      ██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝
    ███████╗██║  ██║███████║   ██║       ██║ ╚████║██║ ╚═╝ ██║██║  ██║██║
    ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝       ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝
    ----------------------------Author:DarkMRX--------------------------------
    ------------Youtube : CyberSL (https://youtu.be/pM7TeSrsXrI)--------------
"""
W = "\033[0m"
G = "\033[32;1m"
R = "\033[31;1m"
B = "\033[34;1m"
Y = "\033[33;1m"


def is_tools():
    try:
        devnull = open(os.devnull)
        subprocess.Popen(["nmap"], stdout=devnull,
                         stderr=devnull).communicate()
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            return False
    return True


def checkifExsistNmap():
    if(is_tools() == False):
        print("[!] Error: nmap not Found!")
        print("[-] Info: Please Install nmap")
        exit(0)


def waitekey():
    input("Press any key to continue...")


def info_help():
    print(Y + """
    1. Host Scan (basic)
    2. Port Scan
    3. Services Discovery

    98. Help
    99. Exit
    """ + W, "\n")


def checkHttp(host):
    if ('https://' in host):
        print(R + "\n[!]Error: Please Enter URL without 'https://' \n" + W)
        return False
    elif('http://'in host):
        print(R + "\n[!]Error: Please Enter URL without 'http://' \n" + W)
        return False
    else:
        return True


def HostScanMenu():
    print(Y + """
    1. IP/Domain Scan
    2. IP/Domain Scan (More Details)
    3. IP/Domain Scan with OS Detection
    4. IP/Domain Scan with OS Detection (Advance)

    0. Back
    """ + W)


def PortScanMenu():
    menu = """
    1.
    """


def hostDiscovery():
    HostScanMenu()
    try:
        value = int(input("Enter : "))
        print(
            B + "\n[#]Hint: IP/URL/IP Range OR Subnet Ex: (10.10.10.1/24) \n" + W)
        #hosts = str(input("IP/URL : "))
        if(value == 1):
            hosts = str(input("IP/URL : "))
            if(checkHttp(host=hosts) == True):
                cmd = "nmap {0}".format(hosts)
                os.system(cmd)
                waitekey()
                hostDiscovery()
        elif(value == 2):
            hosts = str(input("IP/URL : "))
            if(checkHttp(host=hosts) == True):
                cmd1 = "nmap -v {0}".format(hosts)
                os.system(cmd1)
                waitekey()
                hostDiscovery()
        elif(value == 3):
            hosts = str(input("IP/URL : "))
            if(checkHttp(host=hosts) == True):
                cmd2 = "nmap -O {0}".format(hosts)
                os.system(cmd2)
                waitekey()
                hostDiscovery()
        elif(value == 4):
            hosts = str(input("IP/URL : "))
            if(checkHttp(host=hosts) == True):
                cmd3 = "nmap -v -O --osscan-guess {0}".format(hosts)
                os.system(cmd3)
                waitekey()
                hostDiscovery()
        elif(value == 0):
            main()
        else:
            print(R + "[!] Error: Please Enter Valid Number" + W)
            main()
    except ValueError as e:
        print(R + f"[!] Error:{e}" + W)


def main():
    os.system("clear")
    print(banner)
    checkifExsistNmap()
    info_help()
    value = int(input("Enter : "))
    try:
        if(value == 1):
            hostDiscovery()
        elif(value == 99):
            print("Thank for using Easy Nmap. ~DarkMRX~")
            exit(0)
        else:
            print(R + "[!] Error: Please Enter Valid Number" + W)
            waitekey()
            main()
    except ValueError as e:
        print(R + f"[!] Error:{e}" + W)


if __name__ == '__main__':
    main()
