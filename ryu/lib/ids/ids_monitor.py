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
        self.protocol_types={'tcp':tcp.tcp,'ip':ipv4.ipv4,'icmp':icmp.icmp}
        gevent.spawn_later(0, self.read_rules())


    def check_packet(self,msg):
        for rule in self.rules:
            print rule
            rule_contents = rule.split()
            if len(rule_contents) < 6:
                raise Exception("Invalid Alert Rule: Length", len(rule_contents))
            else:
                protocolcls = self.protocol_types.get(rule_contents[1])
                alert_type = rule_contents[0]
                sr_ip = rule_contents[2]
                sr_port = rule_contents[3]
                dst_ip = rule_contents[4]
                dst_port = rule_contents[5]
                ids_pkt = protocolcls(msg)
                alertmsg = ids_pkt.check_packet(alert_type,sr_ip,sr_port, dst_ip, dst_port)
                
            if alertmsg:
                self.send_event_to_observers(AttackAlert(alertmsg,msg))

    def read_rules(self):
        print 'Reading SNORT RULES file'
        fname = '/home/mininet/RYU295/ryu/lib/ids/rules.txt'
        with open(fname) as f:
            self.rules = f.readlines()
            
