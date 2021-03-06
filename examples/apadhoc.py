#!/usr/bin/python

"""
This example shows how to work with in ns APs
"""
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink
import sys

net = Mininet(link=TCLink)

def topology(mobility):

	"Create a network."
	if mobility:
		sta1 = net.addStation('sta1', mac='00:00:00:00:00:01', ip='10.0.0.1/8', range='20')
	else:
		sta1 = net.addStation('sta1', mac='00:00:00:00:00:01', ip='10.0.0.1/8', range='20', position='20,60,0')
	sta2 = net.addStation('sta2', mac='00:00:00:00:00:02', ip='10.0.0.2/8', range='20', position='90,60,0')
	ap1 = net.addAPAdhoc('ap1', mac='02:00:00:00:01:00', ip='10.0.0.11/8', ssid="apadhoc-ssid", mode="g", channel="1", position='40,60,0', range='30')
	ap2 = net.addAPAdhoc('ap2', mac='02:00:00:00:02:00', ip='10.0.0.12/8', ssid="apadhoc-ssid", mode="g", channel="6", position='80,60,0', range='30')

	print "*** Configuring wifi nodes"
	net.configureWifiNodes()

	net.plotGraph(max_x=120, max_y=120)

	print "*** Adding Link"
	net.addLink(ap1, ap2)  # wired connection

	print "*** Starting network"
	net.build()
	
	if mobility:
		net.startMobility(startTime=1, AC='ssf')
		net.mobility(sta1, 'start', time=1, position='20.0,60.0,0.0')
		net.mobility(sta1, 'stop', time=5, position='63.0,60.0,0.0')
		net.stopMobility(stopTime=6)

	if mobility == False:
		net.autoAssociation()

	print "*** Running CLI"
	CLI(net)

	print "*** Stopping network"
	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	mobility = True if '-m' in sys.argv else False
	topology(mobility)

