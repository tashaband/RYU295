from ryu.lib.packet import packet
from ryu.lib.packet import ethernet


class tcp(object):
    
    def __init__(self,packet_data):
        self.packet_data = packet_data        
    

    def check_packet(self,mode,src_ip, src_port, dst_ip, dst_port): 
        pkt = packet.Packet(self.packet_data.data)
        eth_pkt = pkt.get_protocol(ethernet.ethernet)
        
        p_dst = eth_pkt.dst
        p_src = eth_pkt.src
        if (src == 'any' or src_ip == p_src):
            if (dst == 'any' or dst_ip == p_dst):
                if mode == 'alert':
                    alertmsg = 'Ethernet Attack Packet'
                    self.send_event_to_observers(AttackAlert(alertmsg,msg))