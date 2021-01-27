Simple PoC for DISPY framework
how to use:

1. Get the IP addresses of machine that will be in cluster
2. Open inbound and outbound port (by default it is 61590) for dispynode utility:
     - On win machine on Search field type Firewall.
     - Open 'Windows Defender Firewall and Advanced Security'
     - Create new rules for Inbound and Outbound Rules for opening port for in/out TCP connections
3. On Node machines install Python and packages, that are listed in requirements.txt. 
   See instruction inside requirements.txt how to install packages 
4. Run node using following command using cmd utility:
       
        dispynode.py -i 192.168.1.111 -p 61590
       
    On Node machine can be used for creating and running cluster
5. In main.py configure list of NODEs by specifying IP addresses:

        cluster = dispy.JobCluster(compute, nodes=["192.168.1.111", "192.168.1.112"])

    if non-default port is used, then specify 'dispy_port' parameter in cluster creation
6. Run main.py