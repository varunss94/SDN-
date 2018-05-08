from mininet.topo import Topo

class MyTopo( Topo ):
	" simple topology "

	def __init__( self ):
#Initialize topology

		Topo.__init__( self )

#Add hosts and switches

		FirstHost = self.addHost( 'h1' )
		SecondHost = self.addHost( 'h2' )
		ThirdHost = self.addHost( 'h3' )
		FourthHost = self.addHost( 'h4' )

		firstSwitch = self.addSwitch( 's1' )

#Add Links 
		self.addLink( firstSwitch,FirstHost)
		self.addLink( firstSwitch,SecondHost)
		self.addLink( firstSwitch,SecondHost)
		self.addLink( firstSwitch,ThirdHost)
		self.addLink( firstSwitch,FourthHost)

topos = { 'mytopo': (lambda: MyTopo() ) }
