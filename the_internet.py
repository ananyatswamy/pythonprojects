
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
    if not validate_ip(user_ip):# or ip_exists(internet_server,user_ip) :
        print("invalid ip or existing ip")
        return
    #  update dictionary
    elif server_exists(internet_server,user_server_name):
        internet_server[user_server_name][0] = [user_ip]
    # else add to dictionary
    else:
        internet_server[user_server_name] = [user_ip]

    print(internet_server)

def create_connection(internet_server, server1, server2, connection_time):
    # if server 1 and server 2 exist in dictionary
    # if server1 or 2 not exists
    if (server_exists(internet_server, server1) and server_exists(internet_server, server2)):
        print("one or both of these servers do not exist")
        return

    # if connection exists then return
    for values in internet_server[server1]:
        if values == server2:
            print("already connected")
            return

    internet_server[server1].append(server2)
    internet_server[server1].append(connection_time)

    internet_server[server2].append(server1)
    internet_server[server2].append(connection_time)

    print("connection is created")

def set_server(internet_server, name_or_ip):
    #if first digit is numerical then it is ip & is valid ip
        # ip_exist ( true )
    #else see if server exist
      # print not valid server name
      # false ret
    # set the server ip/server name
    pass

def ping(internet_server, target_server):
    # identify if it is ip or name
    # identify if it exists
    # find name if it is ip
    # from current server identify if there is connection to target server
    # return connection_time + recursivecall()
    pass
def traceout(internet_server, target_server):
    # identify if it is ip or name
    # identify if it exists
    # find name if it is ip
    # from current server identify if there is connection to target server
    # return connection_time + recursivecall()
    pass

def display_server(internet_server):
    # print all servers their connections and ip addresses
    pass
def ip_config(internet_server):
     # print() current location
    pass

# helper functions..

def server_exists(internet_server, user_server):
    for server in internet_server.values():
        if server == user_server:
            return True
    # check the server name from the
    # if exists
    # server_valid = True
    return False


def ip_exists(internet_server,user_ip):
    # iterate the dictionary
    #print("Invalid IP address,already exists.")
    # return true or false
    for server in internet_server.values():
        if server == "current_location":
            pass
        elif internet_server[server][0] == user_ip:
            return True
    return False

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
    internet_server = {"current_server": None,
                       "anu": ["12.3.4.5"],
                       "thippu": ["3.5.7.8"]}
    # this will have key as server name
    # values will be ip address, connection1, connection_time1, connection2...
    command = input(">>>").lower().split()
    while command[0] != ("quit"):
        # parsing, command user input
        #if command[0] == "create-server" and len(command) == 3:
        if command[0] == "cs" and len(command) == 3:
            name = command[1]
            ip_address = command[2]
            create_server(internet_server,name,ip_address)
        elif  command[0] == ("conn") and len(command) == 4:
            server1 = command[1]
            server2 = command[2]
            connection_time = command[3]
            create_connection(internet_server, server1, server2, connection_time)
            print(internet_server)
        command = input(">>>").lower().split()
