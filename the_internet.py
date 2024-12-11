
"""
File: 
Aut Ananya Thippeswamy
Date: 
Section: 23
E-mail: ho20134@umbc.edu
Description: 
"""
#####################################################################

def create_server(internet_server, user_server_name, user_ip):
    # see if ip is valid
    if not validate_ip(user_ip) or ip_exists(internet_server,user_ip) :
        print("invalid ip or existing ip")
        return
    #  update dictionary
    elif server_exists(internet_server,user_server_name):
        internet_server[user_server_name][0] = [user_ip]
    # else add to dictionary
    else:
        internet_server[user_server_name] = [user_ip]

    print(internet_server)

####################################################################

def create_connection(internet_server, server1, server2, connection_time):
    # if server 1 and server 2 exist in dictionary
    # if server1 or 2 not exists
    if not (server_exists(internet_server, server1) and server_exists(internet_server, server2)):
        print("one or both of these servers do not exist")
        return

    # if connection exists then return
    for values in internet_server[server1]:
        if values == server2:
            print("already servers connected")
            return

    internet_server[server1].append(server2)
    internet_server[server1].append(connection_time)

    internet_server[server2].append(server1)
    internet_server[server2].append(connection_time)

    print("connection is created")

####################################################################

def set_server(internet_server, name_or_ip):
    if (name_or_ip[0].isdigit() and validate_ip(name_or_ip)):
        if not (ip_exists(internet_server,name_or_ip)):
            print("IP doesnot exist")
        else:
            internet_server["current_server"]=get_server_name(internet_server,name_or_ip)
    elif(server_exists(internet_server,name_or_ip)):
        internet_server["current_server"] = name_or_ip
    else:
        print("server not exist")

#######################################################################

def ping_recursive(internet_server, start_server, target_server, visited):
    if start_server == target_server:
        return 0  # target server reached

    visited[start_server] = True
    connections = internet_server[start_server][1:]  # exclude IP column

    # connections both server and time
    for i in range(0, len(connections), 2):
        neighbor_server, time = connections[i], int(connections[i + 1])
        if not visited[neighbor_server]:
            result = ping_recursive(internet_server, neighbor_server, target_server, visited)
            if result != -1:  # path yes
                return time + result

    visited[start_server] = False
    return -1  # no path

#########################################################################

def ping(internet_server, target_server):
    # is base server set
    if not (is_base_server_set(internet_server)):
        return

    # check target is ip and valid ip
    if target_server[0].isdigit() and validate_ip(target_server):

        if not ip_exists(internet_server, target_server):
            print("Error: IP " + target_server + " does not exist in the network.")
            return
        target_server = get_server_name(internet_server, target_server)

    elif not server_exists(internet_server, target_server):
        print("Error: Server " + target_server + " does not exist in the network.")
        return

    start_server = internet_server.get("current_server")

    # server visited False
    visited = {}
    for server in internet_server:
        if server != "current_server":
            visited[server] = False

    # Call the recursive ping function to find the total connection time
    total_time = ping_recursive(internet_server, start_server, target_server, visited)

    # time print
    if total_time == -1:
        print("Error: No route found from " + start_server + " to " + target_server + ".")
    else:
        print("Ping successful! Time taken: " + str(total_time) + " ms.")


#############################################################################


def traceout(internet_server, target_server):
    if not (is_base_server_set(internet_server)):
        return
    # validate input and find the target server by name
    if target_server[0].isdigit() and validate_ip(target_server):
        if not ip_exists(internet_server, target_server):
            print("Error: IP "+target_server+" does not exist in the network.")
            return
        target_server = get_server_name(internet_server, target_server)
    elif not server_exists(internet_server, target_server):
        print("Error: Server "+target_server+" does not exist in the network.")
        return

    # from current server identify if there is connection to target server
    # return connection_time + recursivecall()

    pass

############################################################

def display_server(internet_server):
    # Iterate through each server
    for server, details in internet_server.items():
        if not (server == 'current_server'):
            ip_address = details[0] if details else "No IP address"  # IP address of the current server

        # print the server and IP address
            print("Server: " + server + ", IP: " + ip_address)

        # sub-servers items that are not IP addresses
            sub_servers = [item for item in details[1:] if not item.replace(".", "").isdigit()]

        # list sub-servers and ip
            if sub_servers:
                for sub_server in sub_servers:
                    sub_server_ip = internet_server.get(sub_server, [None])[0]  # Get the sub-server IP
                    print("  Sub-Server: " + sub_server + ", IP: " + str(sub_server_ip))

            print("-" * 40)


################################################################

def ip_config(internet_server):
    if(is_base_server_set(internet_server)):
     print(internet_server["current_server"]+"  "+get_ip_address(internet_server,internet_server["current_server"]))

################################################################

def server_exists(internet_server, user_server):
    return user_server in internet_server

################################################################

def ip_exists(internet_server, user_ip):
    for server in internet_server.values():
        if server and server[0] == user_ip:
            return True
    return False

###################################################################

def get_ip_address(internet_server,user_server):
    if user_server in internet_server:
        return internet_server[user_server][0]

###################################################################

def get_server_name(internet_server,user_ip):
    for server in internet_server.keys():
        for sublist in  internet_server[server]:
         if sublist == user_ip:
             return server

###################################################################

def is_base_server_set(internet_server):
    if internet_server['current_server']:
        return True
    else:
        print("Base Server not set")
        return False
###################################################################

def validate_ip(ip_address):
    parts = ip_address.split('.')
    is_valid = False
    if len(parts) == 4:
        for part in parts:
            #if not part.isdigit() or not (-1 < int(part) < 255):
            if not part.isdigit() or not (0 < int(part) < 255):
                print("Invalid IP address.")
                return is_valid
            is_valid=True
    else:
        print("Invalid IP address.")
        return is_valid
    return is_valid

###################################################################

if __name__ == "__main__":
    internet_server = internet_server = {
                                        'current_server': [],
                                        'hema': ['9.9.9.9'],
                                        'raj': ['8.8.8.8', 'tips', '5'],
                                        'thippu': ['3.5.7.8'],
                                        'tips': ['7.7.7.7', 'anu', '3', 'raj', '5'],
                                        'anu': ['12.3.4.5', 'tips', '3']
                                        }
    # this will have key as server name
    # values will be ip address, connection1, connection_time1, connection2...
    command = input(">>>").lower().split()
    while command[0] != ("quit"):
        # check command and call methods
        #if command[0] == "create-server" and len(command) == 3:
        if command[0] == "cs" and len(command) == 3:
            name = command[1]
            ip_address = command[2]
            create_server(internet_server,name,ip_address)
        #elif  command[0] == ("conn") and len(command) == 4:
        elif  command[0] == ("conn") and len(command) == 4:
            server1 = command[1]
            server2 = command[2]
            connection_time = command[3]
            create_connection(internet_server, server1, server2, connection_time)
        #elif command[0] == "ip-config":
        elif command[0] == "ip":
             ip_config(internet_server)
        #elif command[0] == "set-server" and len(command) == 2:
        elif command[0] == "ss" and len(command) == 2:
            server_or_ip = command[1]
            set_server(internet_server,server_or_ip)
            print(internet_server)
        #elif command[0] == "display-servers":
        elif command[0] == "dis":
            display_server(internet_server)
        #elif command[0] == "ping" and len(command) == 2:
        elif command[0] == "ping" and len(command) == 2:
            target_server = command[1]
            ping(internet_server,target_server)
        #elif command[0] == "traceout" and len(command) == 2:
        elif command[0] == "trace" and len(command) == 2:
            target_server = command[1]
            traceout(internet_server,target_server)

        command = input(">>>").lower().split()

##################################################################################