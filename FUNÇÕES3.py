import nmap

def funcao_nmap(ip_address):

    nm = nmap.PortScanner()
    nm.scan(ip_address, '22-500')
    nm.command_line()
    # 'nmap -oX - -p 22-443 -sV 127.0.0.1'
    nm.scaninfo()
    # {'tcp': {'services': '22-443', 'method': 'connect'}}
    nm.all_hosts()
    # ['127.0.0.1']
    nm[ip_address].hostname()
    # 'localhost'
    nm[ip_address].state()
    # 'up'
    nm[ip_address].all_protocols()
    # ['tcp']
    nm[ip_address]['tcp'].keys()
    # [80, 25, 443, 22, 111]
    nm[ip_address].has_tcp(22)
    # True
    nm[ip_address].has_tcp(23)
    # False
    nm[ip_address]['tcp'][22]
    # {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh'}
    nm[ip_address].tcp(22)
    # {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh'}
    nm[ip_address]['tcp'][22]['state']
    # 'open'

    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        relatorio = open('relatorio.txt', 'a')
        relatorio.write('State: ')
        relatorio.writelines(nm[host].state())

        relatorio.write('\n')
        relatorio.write('Host: ')
        relatorio.write(host)
        relatorio.write('\n')
        #relatorio.write(host)
        relatorio.close()

        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
            relatorio = open('relatorio.txt', 'a')
            relatorio.write('Protocol: ')
            relatorio.write(proto)

            relatorio.write('\n')
            #relatorio.write(host)
            relatorio.close()

            lport = nm[host][proto].keys()
            #lport.sort()
            for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
                relatorio = open('relatorio.txt', 'a')
                relatorio.write('Portas: ')
                relatorio.writelines(nm[host][proto][port])
                relatorio.write('\n')
                relatorio.close()

if __name__ == '__main__':
    funcao_nmap()


