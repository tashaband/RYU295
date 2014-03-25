class IDStcp(object):
            
        
    def check_packet(msg,mode,protocol,src_ip,src_port,dst_ip,dst_port): 
        pkt = packet.Packet(msg.data)
        tcp_pkt = pkt.get_protocol(tcp.tcp)
        
        p_protocol = tcp_pkt.protocol
        p_src = tcp_pkt.src
        p_dst = tcp_pkt.dst
        p_dst_port = tcp_pkt.dst_port
        p_src_port = tcp_pkt.src_port
        
        
        if p_protocol_name == 'tcp':
           if src_ip == 'any' | p_src == src_ip:
               if dst_ip == 'any' | p_dst == dst_ip:
                   if src_port == 'any' | p_src_port == src_port:
                      if dst_port == 'any' | p_dst_port == dst_port:
                         if mode == 'alert':
                            print 'TCP Attack Packet'
