# TITE luokka ping
from threading import Thread
import subprocess
import time

# time.sleep(s)


def get_hosts_for_classroom(classroom:str) -> list:
    '''
    Creates and returns a list of hosts to ping for a classroom.

    The list contains tuples with the hostname and the ip address of the host: [(hostname, ip), ...].
    Hostnames are in the format '{classroom}-XXX' where XXX is a number from 001 to 020. For example: 521-014
    The ip addresses are in the format '172.20.XX.2YY' where XX is the classroom number (without the '5') and YY is a number from 01 to 20.
    The last host is the OPE (kouluttajan) host. It's ip address ends in 200.
    '''
    lista = []
    for i in range(1, 21):
        hostname = f'{classroom}-{i:03}'
        ip_address = f'172.20.{classroom[1:]}.2{i:02}'
        lista.append((hostname, ip_address))
    lista.append((f'{classroom}-OPE', f'172.20.{classroom[1:]}.200'))
    return lista

def ping(ip:str) -> bool:
    '''
    Pings the given ip address and returns True if the host responds, False otherwise.
    
    The function calls operating system's `ping` command with the given ip address: 'ping -n 1 -w 300 <ip>'.
    Parameter `-n 1` specifies that only one ping is sent, and `-w 300` specifies the timeout in milliseconds.

    The host is pinged up to three times. The function returns True if the host responds at least once, False otherwise.
    '''
    cmd = f'ping -n 1 -w 300 {ip}'
    
    # Vaihtoehto 1:
    # exit_status = os.system(cmd:str)

    # Vaihtoehto 2:
    # completedProcess = subprocess.run(cmd.split()) # exit_status = completedProces.returncode

    # Vaihtoehto 3:
    # exit_status = subprocess.call(cmd.split())

    for _ in range(3):
        if subprocess.call(cmd.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
            return True
    return False

def ping_host(hostname:str, ip:str) -> None:
    '''Ping a host and stores the response in the hosts_responses dictionary with the hostname as the key.'''
    while not shutdown:
        responses[hostname] = ping(ip)
        time.sleep(1)

def print_responses() -> None:
    '''Prints the responses of the hosts in the hosts_responses dictionary in the format 'hostname: response'.'''
    while not shutdown:
        for hostname, response in responses.items():
            print(f'{hostname}: {response}')
        print()
        time.sleep(1)


if __name__ == '__main__':
    # Get hosts to ping
    hosts = get_hosts_for_classroom('521')
    
    # Initialize hosts_responses dictionary: {hostname: response, ...}
    responses = {hostname: False for hostname, _ in hosts}
    
    shutdown = False

    # Launch ping threads
    threads = []
    for hostname, ip in hosts:
        thread = Thread(target=ping_host, args=(hostname, ip))
        thread.start()
        threads.append(thread)
    
    thread = Thread(target=print_responses)
    threads.append(thread)
    thread.start()

    while input('Write exit to end: ') != 'exit':
        pass

    shutdown = True

    # Wait for all pings to end
    for thread in threads:
        thread.join()

    # Print responses
    #print_responses()
    