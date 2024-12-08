
"""
File: 
Aut Ananya Thippeswamy
Date: 
Section: 23
E-mail: ho20134@umbc.edu
Description: 
"""

def create_server(internet_server, user_server_name, user_ip):
    # see if ip is valid
    # see if ip is existing in dictionary (internet_server,user_ip)
    # if exists return error message
    # elif server name exists overwrite ip
    # else add to dictionary

def create_connection(internet_server, server1, server2, connection_time):
    # if server 1 and server 2 exist in dictionary

    # if server1 or 2 not exists
    # print ( to create connection both servers should exist in the server list)

    # if connection exists then return
    # print ( connection exists )

    # if not connected add server name and connection time to both servers
    # print ( connection exists )

def set_server(internet_server, name_or_ip):
    #if first digit is numerical then it is ip & is valid ip
        # ip_exist ( true )
    #else see if server exist
      # print not valid server name
      # false ret
    # set the server ip/server name


def ping(internet_server, target_server):
    # identify if it is ip or name
    # identify if it exists
    # find name if it is ip
    # from current server identify if there is connection to target server
    # return connection_time + recursivecall()

def traceout(internet_server, target_server):
    # identify if it is ip or name
    # identify if it exists
    # find name if it is ip
    # from current server identify if there is connection to target server
    # return connection_time + recursivecall()


def display_server(internet_server):
    # print all servers their connections and ip addresses

def ip_config(internet_server):
     # print() current location


# helper functions..

def server_exists(internet_server,server):
    server_valid = False
    # check the server name from the
    # if exists
    # server_valid = True
    return server_valid;

def ip_exists(internet_server,user_ip):
    # iterate the dictionary
    #print("Invalid IP address,already exists.")
    # return true or false

def validate_ip(ip_address):
    parts = ip_address.split('.')
    is_valid = False
    if len(parts) == 4:
        for part in parts:
            if not part.isdigit() or not (0 < int(part) < 255):
                print("Invalid IP address.")
                return is_valid
            is_valid=True
    else:
        print("Invalid IP address.")
        return is_valid
    return is_valid



if __name__ == "__main__":
    internet_server = {"current_server": None}
    # this will have key as server name
    # values will be ip address, connection1, connection_time1, connection2...
    command = input(">>>").lower().split()
    while command != ("quit"):
        # parsing, command user input
        if command == "create-server":
            if len(parts) == 3 and parts[0] == "create-server":
                domain = command[1]
                ip_address = command[2]
                if validate_ip(ip_address):
                    pass
        elif command == "":
            pass
        elif command == "":
            pass
        elif command == "":
            pass
        elif command == "":
            pass
        elif command == "":
            pass
        elif command == "":
            pass
        elif command == "":
            pass
