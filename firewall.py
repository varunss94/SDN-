
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple 
import os
from csv import DictReader

log = core.getLogger()
policyFile = "%s/pox/pox/misc/firewallpolicies.csv" % os.environ[ ' HOME ' ]

# Add the global variables here...

# Note: Policy is data structure which contains a single source-destination flow to be blocked on the controller.

Policy = namedtuple('Policy', ('dl_src','dl_dst'))

class Firewall (EventMixin):

	def __init__ (self):
		self.listenTo(core.openflow)
		log.debug("Enabling Firewall Module")
	
	def read_policies (self,file):
		with open(file, 'r') as f:
			reader = DictReader(f, delimiter = " ,")
			policies = {}
			for row in reader:
				policies[row['id']] = Policy(EthAddr(row['mac_0']), EthAddr(row['mac_1']))
		return policies

	def _handle_ConnectionUp (self,event):
		policies = self.read_policies(policyFile)
		for policy in policies.itervalues():
		#TODO : implement the code to add a rule to block the flow
		#between the source and destination specified in each policy


			log.debug("--> Source Mac is %s", policy.dl_src)
			log.debug("--> Destination Mac is %s", policy.dl_dst)
			
			match = of.ofp_match(dl_src = policy.dl_src, dl_dst = policy.dl_dst)
			fm = of.ofp_flow_mod()
			fm.priority = 20
			fm.match = match
			event.connection.send(fm)
			
			log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch():
#starting the firewall module

	core.registerNew(Firewall)
