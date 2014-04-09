from ryu.lib.packet import packet
from ryu.lib.packet import ipv4
from . import ids_utils

class icmp(object):
    
    def __init__(self,packet_data):
        self.packet_data =  packet.Packet(packet_data.data)  
        self.dst_ip = ids_utils.get_packet_dst_ip_address(self.packet_data)
        self.src_ip = ids_utils.get_packet_src_ip_address(self.packet_data)


    def check_packet(self,mode,src_ip, src_port, dst_ip, dst_port): 
        for p in self.packet_data:
            print p.protocol_name
            if p.protocol_name == 'icmp':
                
                match = self.check_ip_match(src_ip, dst_ip)
                if match == True: 
                    f = open('/home/mininet/RYU295/ryu/lib/ids/log.txt', 'a')  
                    f.write('ICMP Attack Packet') 
                    f.close()
                    if mode == 'alert':
                        print 'ICMP Attack Packet'
                        alertmsg = 'ICMP Attack Packet'
                        return alertmsg
     
     
     
                                
    def check_ip_match(self,src_ip, dst_ip):
        print 'packet source', self.src_ip
        print 'packet dst', self.dst_ip
        print 'rule source', src_ip
        print 'rule dst', dst_ip
        if ((src_ip == 'any') or (src_ip == self.src_ip)):
            if ((dst_ip == 'any') or (dst_ip == self.dst_ip)):
                return True
        