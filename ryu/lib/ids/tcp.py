from ryu.lib.packet import packet
from ryu.lib.packet import ipv4
from . import ids_utils


class tcp(object):
    
    def __init__(self,packet_data):
        self.packet_data = packet_data 
        self.dst_ip = ids_utils.get_packet_dst_ip_address(packet_data)
        self.src_ip = ids_utils.get_packet_src_ip_address(packet_data)
        self.dst_port = ids_utils.get_packet_dst_port(packet_data)
        self.src_port = ids_utils.get_packet_src_port(packet_data)      
    

    def check_packet(self,mode,src_ip, src_port, dst_ip, dst_port): 
        pkt = packet.Packet(self.packet_data.data)
        for p in pkt:
            print p.protocol_name
            if p.protocol_name == 'tcp':
                
                match = self.check_tcp_ip_port_match(src_ip, src_port, dst_ip, dst_port, pkt)
                if match == True: 
                    f = open('/home/mininet/RYU295/ryu/lib/ids/log.txt', 'a')  
                    f.write('TCP Attack Packet') 
                    f.close()
                    if mode == 'alert':
                        print 'TCP Attack Packet'
                        alertmsg = 'TCP Attack Packet'
                        return alertmsg
     
     
     
                                
    def check_tcp_ip_port_match(self,src_ip, src_port, dst_ip, dst_port, pkt):

        
        print 'packet source', self.src_ip
        print 'packet dst', self.dst_ip
        print 'rule source', src_ip
        print 'rule dst', dst_ip
        if ((src_ip == 'any') or (src_ip == self.src_ip)):
            if ((dst_ip == 'any') or (dst_ip == self.dst_ip)):
                if ((src_port == 'any') or (src_port == self.src_port)):
                    if ((dst_port == 'any') or (dst_port == self.dst_port)):
                        return True
        