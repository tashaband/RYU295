import os
import gevent
from ryu.base import app_manager
from ryu.controller import event
from ryu.lib.packet import packet
from . import tcp,ipv4,icmp
from array import *




class AttackAlert(event.EventBase):
    def __init__(self, alertmsg, data):
        super(AttackAlert, self).__init__()
        self.alertmsg = alertmsg
        self.data = data
        

class IDSMonitor(app_manager.RyuApp):
    def __init__(self):
        super(IDSMonitor, self).__init__()
        self.name = 'ids_monitor'
        self.rules = []
        self.sr_ip_addr = []
        self.dst_ip_addr = []
        self.protocol_types={'tcp':tcp.tcp,'ip':ipv4.ipv4,'icmp':icmp.icmp}
        gevent.spawn_later(0, self.read_rules())


    def check_packet(self,msg):
        for rule in self.rules:
            #print rule
            rule_contents = rule.split()
            if len(rule_contents) < 6:
                raise Exception("Invalid Alert Rule: Length", len(rule_contents))
            else:
                protocolcls = self.protocol_types.get(rule_contents[1])
		print 'rule_contents[1] from IDS Monitor'
	 	print rule_contents[1]
                alert_type = rule_contents[0]
                var_sr_ip = rule_contents[2]
                var_dst_ip = rule_contents[4]
                if var_sr_ip == "$HOME_NET":
                    fname = '/home/mininet/RYU295/ryu/lib/ids/conf.txt'
                    with open(fname) as f:
                       conf_file = f.readlines()
                       for conf_var in conf_file:
                           conf_contents = conf_var.split() 
                           if conf_contents[1] == 'SRC_IP_ADDRESSES':
                              sr_ip_addr = conf_contents[2].split(',')
 		else:
                    #sr_ip_addr.append(rule_contents[2])
                     sr_ip_addr = rule_contents[2]
                #print 'Source IP Address List:'
                #print sr_ip_addr[0:]
                sr_port = rule_contents[3]

                if var_dst_ip == "$HOME_NET":
                    fname = '/home/mininet/RYU295/ryu/lib/ids/conf.txt'
                    with open(fname) as f:
                       conf_file = f.readlines()
                       for conf_var in conf_file:
                           conf_contents = conf_var.split()
                           if conf_contents[1] == 'DST_IP_ADDRESSES':
                              dst_ip_addr = conf_contents[2].split(',')
                else:
                    #dst_ip_addr.append(rule_contents[4])
                     dst_ip_addr = rule_contents[4]
                #dst_ip = rule_contents[4]


                dst_port = rule_contents[5]
                pattern = rule_contents[6]
                print 'From IDS_Monitor'
	        print pattern
                rule_msg = rule_contents[7]
                rule_type = rule_contents[8] 
		print 'From IDS Monitor'
		print rule_type
                #print pattern  
                ids_pkt = protocolcls(msg)
                #alertmsg = ids_pkt.check_packet(alert_type,sr_ip,sr_port, dst_ip, dst_port,pattern)
                alertmsg = ids_pkt.check_packet(alert_type,sr_ip_addr,sr_port, dst_ip_addr, dst_port,pattern,rule_msg,rule_type)

            if alertmsg:
                self.send_event_to_observers(AttackAlert(alertmsg,msg))

    def read_rules(self):
        print 'Reading SNORT RULES file'
        fname = '/home/mininet/RYU295/ryu/lib/ids/rules.txt'
        with open(fname) as f:
            self.rules = f.readlines()
            
