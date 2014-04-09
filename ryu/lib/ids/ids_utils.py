import struct
from ryu.lib.packet import stream_parser

UNPACK_STR = '!%ds'

def get_packet_dst_ip_address(pkt):
    for p in pkt:
            if hasattr(p, 'protocol_name') is True:
                if p.protocol_name == 'ipv4':
                    p_dst = p.dst
                    return p_dst
    return None



def get_packet_src_ip_address(pkt):
    for p in pkt:
            if hasattr(p, 'protocol_name') is True:
                if p.protocol_name == 'ipv4':
                    p_src = p.src
                    return p_src
    return None


def get_packet_dst_port(pkt):
    for p in pkt:
            if hasattr(p, 'protocol_name') is True:
                if p.protocol_name == 'tcp':
                    p_dstport = p.dst_port
                    return p_dstport
    return None


def get_packet_src_port(pkt):
    for p in pkt:
            if hasattr(p, 'protocol_name') is True:
                if p.protocol_name == 'tcp':
                    p_srcport = p.src_port
                    return p_srcport
    return None

def get_packet_length(pkt):
    for p in pkt:
            if hasattr(p, 'protocol_name') is True:
                if p.protocol_name == 'ip':
                    p_length = p.total_length
                    return p_length
    return 0

def print_packet_data(buf, total_lenth):
    unpack_str = UNPACK_STR % (len(buf))
    pac_len = struct.calcsize(unpack_str)
    if len(buf) < pac_len:
            raise stream_parser.StreamParser.TooSmallException(
                '%d < %d' % (len(buf), pac_len))
    print 'unpack string : ' , unpack_str
    data_string = struct.unpack_from(unpack_str, buf)
    print 'data string : ', data_string