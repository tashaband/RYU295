from ryu.lib.packet import packet
from ryu.lib.packet import ipv4
from . import ids_utils
from . import BoyerMooreStringSearch
import MySQLdb as mdb

class tcp(object):
    
    def __init__(self,packet_data):
        self.packet_data =  packet.Packet(packet_data.data)  
        self.dst_ip = ids_utils.get_packet_dst_ip_address(self.packet_data)
        self.src_ip = ids_utils.get_packet_src_ip_address(self.packet_data)
        self.dst_port = ids_utils.get_packet_dst_port(self.packet_data)
        self.src_port = ids_utils.get_packet_src_port(self.packet_data)
        self.length_data = ids_utils.get_packet_length(self.packet_data)      

    def check_packet(self,mode,src_ip, src_port, dst_ip, dst_port,pattern,rule_msg,rule_type): 
        for p in self.packet_data:
            if hasattr(p, 'protocol_name') is True:
                #print p.protocol_name
                if p.protocol_name == 'tcp':
                     match = self.check_tcp_ip_port_match(src_ip, src_port, dst_ip, dst_port)
                     match_content = True
                     pkt_contents = ""  
                     if match == True:
                         length = ids_utils.get_packet_length(self.packet_data)
                         for p in self.packet_data.protocols:
                             if hasattr(p, 'protocol_name') is False:
                                 #print 'Before Call to Print Packet Data in TCP'
                                 #ids_utils.print_packet_data(p, length)
                                 pkt_contents=ids_utils.get_packet_data(p,length)
                                 #print pkt_contents
                                 #print pattern
                             if pattern !='NONE':
                                 match_content = BoyerMooreStringSearch.BMSearch(pkt_contents,pattern)
                             if match_content == True:
                                 f = open('/home/ubuntu/RYU295/ryu/lib/ids/log.txt', 'a')
                                 f.write(rule_msg)
                                 f.close()
                                 self.writeToDB('TCP Attack Packet', 'tcp',rule_msg, 
                                                self.src_ip, self.dst_ip, self.src_port, self.dst_port)
                                 #print 'After Call to Print Packet Data in TCP'
                             if mode == 'alert' and match_content == True:
                                 #print 'TCP Attack Packet'
                                 alertmsg = rule_msg
                                 return alertmsg
     
     
                                
    def check_tcp_ip_port_match(self,src_ip, src_port, dst_ip, dst_port):

        #print 'Print message from tcp.py'
        #print 'packet source', self.src_ip
        #print 'packet dst', self.dst_ip
        #print 'rule source', src_ip
        #print 'rule dst', dst_ip
        #print 'Print Message from tcp.py Ends'
        if (('any' in src_ip) or (self.src_ip in src_ip)):
            if (('any' in dst_ip) or (self.dst_ip in dst_ip)):
                if ((src_port == 'any') or (src_port == self.src_port)):
                    if ((dst_port == 'any') or (dst_port == self.dst_port)):
                        return True
    
    def writeToDB(self,name, protocol, msg, srcip, dstip, srcport, dstport): 
        dbcon = mdb.connect("localhost","testuser","test123","attackdb" )
        cursor = dbcon.cursor()
        try:
            cursor.execute("INSERT INTO attacks(name,protocol, message, sourceip, destip, sourceport, destport)VALUES (%s, %s,%s, %s, %s,%s,%s)",(name, protocol, msg, srcip, dstip, srcport, dstport))
            dbcon.commit()
        except:
            dbcon.rollback()

      
