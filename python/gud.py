from socket import socket, AF_INET, SOCK_RAW, IPPROTO_TCP
from sys import argv
from kaitaistruct import KaitaiStream, BytesIO

def setup_socket(iface):
    return socket(AF_INET, SOCK_RAW, IPPROTO_TCP)
    
def get_raw_eth(soc):
    eth_protos = 3
    #s.bind(iface)
    return soc.recvfrom(65565)

#if __name__ == 'main':
iface = argv[1]
soc = setup_socket(iface)
print(get_raw_eth(soc))
http://formats.kaitai.io/ethernet_frame/python.html
http://formats.kaitai.io/ethernet_frame/python.html
