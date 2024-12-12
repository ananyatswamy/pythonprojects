"""
File: the_internet.py
Aut Ananya Thippeswamy
Date: 12/11/2024
Section: 23
E-mail: ho20134@umbc.edu
Description: the internet recursive server connection finding
"""

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


def create_connection(internet_server, server1, server2, connection_time):
    # if server 1 and server 2 exist in dictionary
    # if server1 or 2 not exists
    if not (server_exists(internet_server, server1) and server_exists(internet_server, server2)):
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
    if (name_or_ip[0].isdigit() and validate_ip(name_or_ip)):
        if not (ip_exists(internet_server,name_or_ip)):
            print("IP doesnot exist")
        else:
            internet_server["current_server"]=get_server_name(internet_server,name_or_ip)
    elif(server_exists(internet_server,name_or_ip)):
        internet_server["current_server"] = name_or_ip
    else:
        print("server doesnot exist")


def recursive(internet_server, start_server, target_server, visited):
    if start_server == target_server:
        return 0  # Reached the target, no additional time needed

    visited[start_server] = True
    connections = internet_server[start_server][1:]  # Skip the IP address

    # Process connections in pairs (server, time)
    for i in range(0, len(connections), 2):
        neighbor, time = connections[i], int(connections[i + 1])
        if not visited[neighbor]:
            result = recursive(internet_server, neighbor, target_server, visited)
            if result != -1:  # Path found
                return time + result

    visited[start_server] = False
    return -1  # Path not found


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

    # Get the current server
    start_server = internet_server.get("current_server")

    # Initialize visited dictionary
    #visited = {server: False for server in internet_server.keys() if server != "current_server"}

    visited = {}
    for server in internet_server:
        if server != "current_server":
            visited[server] = False

    # Call the recursive ping function to find the total connection time
    total_time = recursive(internet_server, start_server, target_server, visited)

    # Output the result
    if total_time == -1:
        print("Error: No route found from " + start_server + " to " + target_server + ".")
    else:
        print("Ping successful! Time taken: " + str(total_time) + " ms.")


def traceout(internet_server, target_server):
    if not (is_base_server_set(internet_server)):
        return
    # Validate input and identify the target server by name
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
    current_server = internet_server.get("current_server")
    visited = {}
    count = -2
    for server in internet_server:
        count += 1
        if server != "current_server":
            visited[server] = False
            print(f"{count}\t{internet_server[server][0]}\t{server}")

    # Recursive ping to find the path
    path_time = recursive(internet_server, current_server, target_server, visited)

    if path_time == -1:
        print(f"No route found from {current_server} to {target_server}")
    else:
        print(f"Trace successful! Total time: {path_time} ms.")


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


def ip_config(internet_server):
    if(is_base_server_set(internet_server)):
     print(internet_server["current_server"]+"  "+get_ip_address(internet_server,internet_server["current_server"]))


def server_exists(internet_server, user_server):
    return user_server in internet_server


def ip_exists(internet_server, user_ip):
    for server in internet_server.values():
        if server and server[0] == user_ip:
            return True
    return False


def get_ip_address(internet_server,user_server):
    if user_server in internet_server:
        return internet_server[user_server][0]


def get_server_name(internet_server,user_ip):
    for server in internet_server.keys():
        for sublist in  internet_server[server]:
         if sublist == user_ip:
             return server


def is_base_server_set(internet_server):
    if internet_server['current_server']:
        return True
    else:
        print("Base server not set")
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
    internet_server = internet_server = {'current_server': []}
    # this will have key as server name
    # values will be ip address, connection1, connection_time1, connection2...
    command = input(">>>").lower().split()
    while command[0] != ("quit"):
        # check command and call methods
        if command[0] == "create-server" and len(command) == 3:
            name = command[1]
            ip_address = command[2]
            create_server(internet_server,name,ip_address)
        elif  command[0] == ("conn") and len(command) == 4:
            server1 = command[1]
            server2 = command[2]
            connection_time = command[3]
            create_connection(internet_server, server1, server2, connection_time)
        elif command[0] == "ip-config":
             ip_config(internet_server)
        elif command[0] == "set-server" and len(command) == 2:
            server_or_ip = command[1]
            set_server(internet_server,server_or_ip)
            print(internet_server)
        elif command[0] == "display-servers":
            display_server(internet_server)
        elif command[0] == "ping" and len(command) == 2:
            target_server = command[1]
            ping(internet_server,target_server)
        elif command[0] == "traceout" and len(command) == 2:
            target_server = command[1]
            traceout(internet_server,target_server)

        command = input(">>>").lower().split()
