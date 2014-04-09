from ryu.lib.packet import packet
from ryu.lib.packet import ipv4


class ipv4(object):
    
    def __init__(self,packet_data):
        self.packet_data = packet_data        
        self.dst_ip = ids_utils.get_packet_dst_ip_address(packet_data)
        self.src_ip = ids_utils.get_packet_src_ip_address(packet_data)

    def check_packet(self,mode,src_ip, src_port, dst_ip, dst_port): 
        pkt = packet.Packet(self.packet_data.data)
        for p in pkt:
            print p.protocol_name
            if p.protocol_name == 'ipv4':
                
                match = self.check_ip_match(src_ip, dst_ip, pkt)
                if match == True: 
                    f = open('/home/mininet/RYU295/ryu/lib/ids/log.txt', 'a')  
                    f.write('IP Attack Packet') 
                    f.close()
                    if mode == 'alert':
                        print 'IP Attack Packet'
                        alertmsg = 'IP Attack Packet'
                        return alertmsg
     
     
     
                                
    def check_ip_match(self,src_ip, dst_ip, pkt):
        print 'packet source', self.src_ip
        print 'packet dst', self.dst_ip
        print 'rule source', src_ip
        print 'rule dst', dst_ip
        if ((src_ip == 'any') or (src_ip == self.src_ip)):
            if ((dst_ip == 'any') or (dst_ip == self.dst_ip)):
                return True  