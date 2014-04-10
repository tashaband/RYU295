from ryu.lib.packet import packet
from ryu.lib.packet import ipv4
from . import ids_utils
from . import BoyerMooreStringSearch

class ipv4(object):
    
    def __init__(self,packet_data):
        self.packet_data =  packet.Packet(packet_data.data)      
        self.dst_ip = ids_utils.get_packet_dst_ip_address(self.packet_data)
        self.src_ip = ids_utils.get_packet_src_ip_address(self.packet_data)

    def check_packet(self,mode,src_ip, src_port, dst_ip, dst_port,pattern):
        for p in self.packet_data:
            if hasattr(p, 'protocol_name') is True:
                #print p.protocol_name
                if p.protocol_name == 'ipv4':
                     match = self.check_ip_match(src_ip, dst_ip)
                     match_content = True
                     if match == True:
                         length = ids_utils.get_packet_length(self.packet_data)
                         for p in self.packet_data.protocols:
                             if hasattr(p, 'protocol_name') is False:
                                 print 'Before Call to Print Packet Data in IPV4'
                                 #ids_utils.print_packet_data(p, length)
                                 pkt_contents=ids_utils.get_packet_data(p,length)
                                 print pkt_contents
                                 print pattern
                             if pattern !='NONE':
                                 match_content = BoyerMooreStringSearch.BMSearch(pkt_contents,pattern)
                             if match_content == True:
                                 f = open('/home/mininet/RYU295/ryu/lib/ids/log.txt', 'a')
                                 f.write('IPV4 Attack Packet')
                                 f.close()
                                 print 'After Call to Print Packet Data in IPV4'
                             if mode == 'alert':
                                 print 'IPV4 Attack Packet'
                                 alertmsg = 'IPV4 Attack Packet'
                                 return alertmsg
     
     
     
                                
    def check_ip_match(self,src_ip, dst_ip):
        # print 'packet source', self.src_ip
        #print 'packet dst', self.dst_ip
        #print 'rule source', src_ip
        #print 'rule dst', dst_ip
        if ((src_ip == 'any') or (src_ip == self.src_ip)):
            if ((dst_ip == 'any') or (dst_ip == self.dst_ip)):
                return True  
