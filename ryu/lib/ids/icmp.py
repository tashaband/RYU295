from ryu.lib.packet import packet
from . import ids_utils
from . import BoyerMooreStringSearch
import MySQLdb as mdb

class icmp(object):
    
    def __init__(self,packet_data):
        self.packet_data =  packet.Packet(packet_data.data)  
        self.dst_ip = ids_utils.get_packet_dst_ip_address(self.packet_data)
        self.src_ip = ids_utils.get_packet_src_ip_address(self.packet_data)


    def check_packet(self,mode,src_ip, src_port, dst_ip, dst_port,pattern): 
        for p in self.packet_data:
            if hasattr(p, 'protocol_name') is True:
                #print p.protocol_name
                if p.protocol_name == 'icmp':
                     match = self.check_ip_match(src_ip, dst_ip)
                     match_content = True
                     if match == True:
                         length = ids_utils.get_packet_length(self.packet_data)
                         for p in self.packet_data.protocols:
                             if hasattr(p, 'protocol_name') is False:
                                 #print 'Before Call to Print Packet Data in ICMP'
                                 #ids_utils.print_packet_data(p, length)
                                 pkt_contents=ids_utils.get_packet_data(p,length)
                                 #print pkt_contents
                                 #print pattern
                             if pattern !='NONE':
                                 match_content = BoyerMooreStringSearch.BMSearch(pkt_contents,pattern)
                             if match_content == True:
                                 f = open('/home/mininet/RYU295/ryu/lib/ids/log.txt', 'a')
                                 f.write('ICMP Attack Packet')
                                 f.close()
                                 self.writeToDB("ICMP Attack Packet", "icmp","ICMP Attack Packet",self.src_ip, self.dst_ip)
                                 #print 'After Call to Print Packet Data in ICMP' 
                             if mode == 'alert':
                                 #print 'ICMP Attack Packet'
                                 alertmsg = 'ICMP Attack Packet'
                                 return alertmsg

     
                                
    def check_ip_match(self,src_ip, dst_ip):
        #print 'packet source', self.src_ip
        #print 'packet dst', self.dst_ip
        #print 'rule source', src_ip
        #print 'rule dst', dst_ip
        #print 'Print Message from ICMP Module'
        if (('any'in src_ip) or (self.src_ip in src_ip)):
            if (('any' in dst_ip) or (self.dst_ip in dst_ip)):
                return True

    def writeToDB(self,name, protocol, msg, srcip, dstip): 
        dbcon = mdb.connect("localhost","testuser","test123","attackdb" )
        with dbcon:
	    cursor = dbcon.cursor()
       	    try:
               cursor.execute("INSERT INTO attacks(name,protocol, message, sourceip, destip)VALUES (%s, %s,%s, %s, %s)",(name, protocol, msg, srcip, dstip))
               dbcon.commit()
            except:
               dbcon.rollback()
       

