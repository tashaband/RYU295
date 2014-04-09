


def get_packet_dst_ip_address(pkt):
    for p in pkt:
            if p.protocol_name == 'ipv4':
                p_dst = p.dst
                return p_dst
    return None



def get_packet_src_ip_address(pkt):
    for p in pkt:
            if p.protocol_name == 'ipv4':
                p_src = p.src
                return p_src
    return None


def get_packet_dst_port(pkt):
    for p in pkt:
            if p.protocol_name == 'tcp':
                p_dstport = p.dst_port
                return p_dstport
    return None


def get_packet_src_port(pkt):
    for p in pkt:
            if p.protocol_name == 'tcp':
                p_srcport = p.src_port
                return p_srcport
    return None