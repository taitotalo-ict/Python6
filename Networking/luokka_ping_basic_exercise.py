# TITE luokka ping


def get_hosts_for_classroom(classroom:str) -> list:
    '''
    Creates and returns a list of hosts to ping for a classroom.

    The list contains tuples with the hostname and the ip address of the host: [(hostname, ip), ...].
    Hostnames are in the format 'classroom-XXX' where XXX is a number from 001 to 020.
    The ip addresses are in the format '172.20.XX.2YY' where XX is the classroom number (without the '5') and YY is a number from 001 to 020.
    The last host is the OPE (kouluttajan) host. It's ip address ends in 200.
    '''
    pass

def ping(ip:str) -> bool:
    '''
    Pings the given ip address and returns True if the host responds, False otherwise.
    
    The function calls operating system's `ping` command with the given ip address: 'ping -n 1 -w 300 <ip>'.
    Parameter `-n 1` specifies that only one ping is sent, and `-w 300` specifies the timeout in milliseconds.

    The host is pinged up to three times. The function returns True if the host responds at least once, False otherwise.
    '''
    pass

def ping_host(hostname:str, ip:str) -> None:
    '''Ping a host and stores the response in the hosts_responses dictionary with the hostname as the key.'''
    pass

def print_responses() -> None:
    '''Prints the responses of the hosts in the hosts_responses dictionary in the format 'hostname: response'.'''
    pass
    

if __name__ == '__main__':
    # Get hosts to ping
    
    # Initialize hosts_responses dictionary: {hostname: response, ...}
    
    # Launch ping threads
    
    # Wait for all pings to end

    # Print responses

    pass