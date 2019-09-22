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
    input("Press Enter key to continue...")


def help():
    os.system("clear")
    print(B + banner + Y + """
    Easy NMAP - Author:DarkMRX
    Youtube Channel: CyberSL(Sinhala)

    1. If you want to ignore discovery type '-Pn' flag before IP address
        ex: IP/URL : -Pn 10.10.10.1

    2. If you want to save all the output in to the .txt file type '-oN filename.txt' flag before IP address
        ex: IP/URL : -oN result.txt 10.10.10.1

    3. If you want to use any othe nmap flag(s) type it before IP address
        ex: IP/URL : -sV -sV 10.10.10.1

    Thanks for using this tool if you like this tool go and subscribe my youtube channel.
    https://www.youtube.com/channel/UCKbiSLwJj8yMQ0Mg9AQZfcw

    """ + W)
    waitekey()
    main()


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


def ServicesDiscoveryMenu():
    print(Y + """
    1. Standard Service Detection
    2. Detect OS and Services (Slow)

    0. Back
    """ + W)


def HostScanMenu():
    print(Y + """
    1. IP/Domain Scan
    2. IP/Domain Scan (More Details)
    3. IP/Domain Scan with OS Detection
    4. IP/Domain Scan with OS Detection (Advance)

    0. Back
    """ + W)


def PortScanMenu():
    print(Y + """
    1. Scan Single/Multiple Port(s) or Port Range in Host/Hosts
    2. Scan 100 Most Common Ports (Fast)
    3. Scan All Ports (65535) (Very Slow)
    4. Scan TCP Ports
    5. Scan UDP Ports

    0. Back
    """ + W)


def ServicesDiscovery():
    ServicesDiscoveryMenu()
    try:
        value = int(input("Enter : "))
        print(
            B + "\n[#]Hint: IP/URL/IP Range OR Subnet Ex: (10.10.10.1/24) \n" + W)
        if (value == 1):
            hosts = str(input("IP/URL : "))
            if(checkHttp(host=hosts) == True):
                cmd = "nmap -sV {0}".format(hosts)
                os.system(cmd)
                waitekey()
                ServicesDiscovery()
        elif(value == 2):
            hosts = str(input("IP/URL : "))
            if(checkHttp(host=hosts) == True):
                cmd1 = "nmap -A {0}".format(hosts)
                os.system(cmd1)
                waitekey()
                ServicesDiscovery()
        elif(value == 0):
            main()
        else:
            print(R + "[!] Error: Please Enter Valid Number" + W)
            main()
    except ValueError as e:
        print(R + f"[!] Error:{e}" + W)


def portDiscovery():
    PortScanMenu()
    try:
        value = int(input("Enter : "))
        print(
            B +
            """[#]Hint: IP/URL/IP Range OR Subnet Ex: (10.10.10.1/24)
[#]Hint: Port(s),Port Range Ex: 8080,21-59,443""" + W)
        if(value == 1):
            hosts = str(input("IP/URL : "))
            ports = str(input("Port(s) : "))
            if(checkHttp(host=hosts) == True):
                cmd = "nmap -v -p {0} {1}".format(ports, hosts)
                os.system(cmd)
                waitekey()
                portDiscovery()
        elif(value == 2):
            hosts = str(input("IP/URL : "))
            if(checkHttp(host=hosts) == True):
                cmd1 = "nmap -v -F {0}".format(hosts)
                os.system(cmd1)
                waitekey()
                portDiscovery()
        elif(value == 3):
            hosts = str(input("IP/URL : "))
            if(checkHttp(host=hosts) == True):
                cmd2 = "nmap -v -p- {0}".format(hosts)
                os.system(cmd2)
                waitekey()
                portDiscovery()
        elif(value == 4):
            hosts = str(input("IP/URL : "))
            if(checkHttp(host=hosts) == True):
                cmd3 = "nmap -v -sT {0}".format(hosts)
                os.system(cmd3)
                waitekey()
                portDiscovery()
        elif(value == 5):
            hosts = str(input("IP/URL : "))
            ports = str(input("Port(s) : "))
            if(checkHttp(host=hosts) == True):
                cmd4 = "nmap -v -sU -p {0} {1}".format(ports, hosts)
                os.system(cmd4)
                waitekey()
                portDiscovery()
        elif(value == 0):
            main()
        else:
            print(R + "[!] Error: Please Enter Valid Number" + W)
            main()
    except ValueError as e:
        print(R + f"[!] Error:{e}" + W)


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
                cmd = "nmap -v {0}".format(hosts)
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
                cmd2 = "nmap -v -O {0}".format(hosts)
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
        elif(value == 2):
            portDiscovery()
        elif(value == 3):
            ServicesDiscovery()
        elif(value == 98):
            help()
        elif(value == 99):
            print(G + "Thank for using Easy Nmap.\n ~DarkMRX~" + W)
            exit(0)
        else:
            print(R + "[!] Error: Please Enter Valid Number" + W)
            waitekey()
            main()
    except ValueError as e:
        print(R + f"[!] Error:{e}" + W)


if __name__ == '__main__':
    main()
