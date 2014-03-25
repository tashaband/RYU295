import os
import gevent
from ryu.base import app_manager
from ryu.controller import event
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
        gevent.spawn_later(0, self.read_rules())


    def check_packet(self,msg):
        for rule in rules:
            print rule
        my_array = array('B', msg.data)
        pkt = packet.Packet(my_array)
        for p in pkt:
            print p.protocol_name
            if p.protocol_name == 'icmp':
                alertmsg = 'ICMP ATTACK'
                self.send_event_to_observers(AttackAlert(alertmsg,msg))

    def read_rules(self):
        print 'Reading SNORT RULES file'
        fname = 'rules.txt'
        with open(fname) as f:
            self.rules = f.readlines()
            