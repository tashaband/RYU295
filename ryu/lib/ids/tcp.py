from ryu.lib.packet import packet
from ryu.lib.packet import ipv4


class tcp(object):
    
    def __init__(self,packet_data):
        self.packet_data = packet_data        
    

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
        ip_pkt = pkt.get_protocol(ipv4.ipv4)
        p_dst = ip_pkt.dst
        p_src = ip_pkt.src
        
        ip_pkt = pkt.get_protocol(tcp.tcp)
        p_dst_port = p.dst_port
        p_src_port = p.src_port
        
        print 'packet source', p_src
        print 'packet dst', p_dst
        print 'rule source', src_ip
        print 'rule dst', dst_ip
        if ((src_ip == 'any') or (src_ip == p_src)):
            if ((dst_ip == 'any') or (dst_ip == p_dst)):
                if ((src_port == 'any') or (src_port == p_src_port)):
                    if ((dst_port == 'any') or (dst_port == p_dst_port)):
                        return True
        