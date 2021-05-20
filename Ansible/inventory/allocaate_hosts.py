import argparse


def generate_hosts():
    """
    Write out all host addresses to hosts.ini.
    """
    with open("hosts_inventory.ini") as f:
        save_hosts = False
        hosts = []
        
        with open("hosts.ini", "w") as file:
            print("[instances]", file=file)
            
            for line in f.readlines():
                line = line.replace("\n", "")

                if save_hosts:
                    if line != "":
                        hosts.append(line)
                        print(line, file=file)
                    else:
                        save_hosts = False

                # starts reading hosts
                if line == "[instances]":
                    save_hosts = True

            print("", file=file)
    
    return hosts


def generate_hosts_for_application(hosts, n_application: int, name: str):
    """
    Write out the host addresses to be allocated for application deployment.
    """
    hosts_for_application = []
    
    # allocate unused hosts
    for host in hosts:
        if not host in used_hosts:
            used_hosts.append(host)
            hosts_for_application.append(host)
            n_application -= 1
        if n_application == 0:
            break

    # allocate used hosts if number of unused hosts are not enough
    if n_application > 0:
        for i in range(n_application):
            if not hosts[i] in hosts_for_application:
                hosts_for_application.append(hosts[i])
    
    with open("hosts.ini", "a") as file:
        print("[{}]".format(name), file=file)
        for host in hosts_for_application:
            print(host, file=file)
        print("", file=file)


def generate_swarm(hosts):
    """
    Write out the host addresses for the master and worker nodes.
    """
    with open("hosts.ini", "a") as file:
        print("[database:children]", file=file)
        print("masternode", file=file)
        print("workers", file=file)
        print("", file=file)
        print("[masternode]", file=file)
        print("{}".format(hosts[0]), file=file)
        print("", file=file)
        print("[workers]", file=file)
        for host in hosts[1:]:
            print("{}".format(host), file=file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', help='number of hosts for Twitter harvester')
    parser.add_argument('-w', help='number of hosts for the web application')
    args = parser.parse_args()

    hosts = generate_hosts()
    n_hosts = len(hosts)
    used_hosts = []

    if args.t:
        n_harvester = int(args.t)
        if n_hosts >= n_harvester:
            generate_hosts_for_application(hosts, n_harvester, "harvester")
        else:
            raise Exception("Too few hosts for number of application required")
    else: # default: allocate 1 host
        generate_hosts_for_application(hosts, 1, "harvester")

    if args.w:
        n_frontend = int(args.w)
        if n_hosts >= n_frontend:
            generate_hosts_for_application(hosts, n_frontend, "frontend")
        else:
            raise Exception("Too few hosts for number of application required")
    else: # default: allocate 1 host
        generate_hosts_for_application(hosts, 1, "frontend")

    generate_swarm(hosts)