############################################
The files uploaded are
1) mytopo.py
2) firewallpolicies.py
3) firewall.py
4) Readme.txt
5) Individual Contribution.txt
############################################


Steps to run the firewall:


Open 2 terminal windows

In one of the terminal windows run the custom topology. This should start the mininet.

In another terminal window, run the Pox controller. This should start the POX controller. 

Once both of them has started goto the terminal window where the mininet was started and ping all the hosts using the 'pingall' command. 

Once all the above steps are follwed the firewall should be successfully running.


Note: 
1)The firewall.py file was in the /home/ubuntu/pox/pox/forwarding/firewall.py path on the SDN hub tutorial vm when this project was done. It would throw up errors if the file is not in this path.

2)The custom built topology file was in the /home/ubuntu/mininet/ path on the SDN hub tutorial vm when this project was done. It would throw up errors if the file is not in this path.

3)The path to the csv file was in /home/ubuntu/pox/pox/misc/firewallpolicies.csv. It could be anywhere. However the path to the same should be changed in the firewall.py file. 





