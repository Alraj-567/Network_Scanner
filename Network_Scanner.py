from scapy.all import ARP,Ether,srp

def scan_network(target_ip):
    arp = ARP(pdst=target_ip)
    ether=Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    print(f"scanning network ip {target_ip}")

    result = srp(packet , timeout = 2,verbose=0)[0]
    clients=[]

    for sent,received in result:
        clients.append({'ip':received.psrc,'mac':received.hwsrc})
    print("\n Available devices in network : ")
    print("IP"+" "*18 + "MAC")    
    for client in clients:
        print("{:16}     {}".format(client['ip'],client['mac']))



if __name__=="__main__":
    target_ip = input("Enter your IP you want to scan for : ")
    scan_network(target_ip)
