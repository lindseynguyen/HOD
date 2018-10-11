import os
from tld import get_tld

def get_nmap(options, ip):
    command = "nmap " + options + " " + ip
    process = os.popen(command)
    results = str(process.read())
    return results

#return all information about domain

def get_whois(url):
    command = "whois " + url
    process = os.popen(command)
    results = str(process.read())
    return results


#whoisurl = input("Enter url")
#print(get_whois(whoisurl))

def get_ping(ip):
    command = " ping : " + ip + " "
    process = os.system(command)
    results = str(process.read)
    return results

#checkping

def get_ping(hostname):
    print("Now it's ping function")
    hostname = input("Enter your address: ")
    response = os.system("ping -c 8 " + hostname)

    #check the response...
    if response == 0:
        print(hostname, 'is up!')
    else:
        print(hostname, 'is down!')

#main

def All_info(options,ip):
    print(get_nmap(option, ip))
    print(get_whois(ip))
    print(get_ping(ip))



option = input("Enter option : ")
ip = input("Enter Address : ")

All_info(option,ip)