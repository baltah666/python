#!/usr/bin/env python
# import built-in os library
# https://docs.python.org/3/library/os.html

import os


def main():
    """
    This code is reusable.
    Executes each funtion in the script
    """
    results_file = open("results.txt", "w")
    print(len(create_ip_list("192.167.1.", 41)))
    ping_list(results_file, "192.167.1.", 41)
    results_file.close()
#    print (response)

def create_ip_list(subnet, num):
    """Appends the concatenated ip to the ip_list"""
    ip_list = []
    for ip in range(1, num):
        ip_list.append(subnet + str(ip))
    return ip_list


def ping_list(results_file, subnet, num):
    """Outputs ping ip_list reults up or down"""
    ip_addresses = create_ip_list(subnet, num)
    for ip in ip_addresses:
        response = os.popen(f"ping -c 1 {ip} ").read()
#	print (response)
        if "0% packet loss"  in response:
            print(f"UP {ip} Ping Successful")
            results_file.write(f"UP {ip} Ping Successful" + "\n")
        else:
            print(f"Down {ip} Ping Unsuccessful")
            results_file.write(f"Down {ip} Ping Unsuccessful" + "\n")


if __name__ == "__main__":
    main()
