import os
print('Recon Phase - Ultron Initiating')
option = input("Enter the number of the option you would like: \n1 - Create Workspace\n2 - Enter Domain List\n3 - Run Domain Modules\n4 - Load netblocks\n5 - Run Netblock Modules\n:")
org = input("Enter target org name\n:")

if option == '1':
	print(org)
	cmd1 = "sudo /opt/recon-ng/recon-cli -w " + org
	print(cmd1)
	os.system(cmd1)
elif option == '2':
	init_domains_path  = input("Enter full path to list of domains:")
	cmd_load_domians = "sudo /opt/recon-ng/recon-cli -w " +org+" -m import/list -c \"options set COLUMN domain\" -c \"options set FILENAME "+init_domains_path+"\" -c \"options set TABLE domains\" -c \"run\""
elif option == '3':
	dm =  ["recon/domains-companies/pen","recon/domains-contacts/pen","recon/domains-contacts/pgp_search","recon/domains-contacts/whois_pocs","recon/domains-contacts/wikileaker","recon/domains-hosts/binaryedge","recon/domains-hosts/censys_domain","recon/domains-hosts/certificate_transparency","recon/domains-hosts/hackertarget","recon/domains-hosts/mx_spf_ip","recon/domains-hosts/netcraft","recon/domains-hosts/shodan_hostname","recon/domains-hosts/ssl_san","recon/domains-hosts/threatcrowd","recon/domains-hosts/threatminer","recon/domains-vulnerabilities/ghdb","recon/domains-vulnerabilities/xssed"]
	l1 = len(dm)
	str1 = "loading " + str(l1) + " modules" 
	print(str1)
	for m in dm:
		print(m)
		cmdm = "sudo /opt/recon-ng/recon-cli -w " +org+" -m "+ m + " -x"
		print(cmdm)
		os.system(cmdm)
elif option == '4':
	init_netblocks_path =  input("Enter full path to list of netblocks")
	cmd_load_netblocks = "sudo /opt/recon-ng/recon-cli -w " +org+" -m import/list -c \"options set COLUMN netblock\" -c \"options set FILENAME "+init_netblocks_path+"\" -c \"options set TABLE netblocks\" -c \"run\""
	os.system(cmd_load_netblocks)
elif option == '5':
	dm = ["sudo /recon/netblocks-companies/censys_netblock_company","recon/netblocks-hosts/censys_netblock","recon/netblocks-hosts/reverse_resolve","recon/netblocks-hosts/shodan_net","recon/netblocks-hosts/virustotal","recon/netblocks-ports/censysio"]
	l1 = len(dm)
	str1 = "loading " + str(l1) + " modules"
	print(str1)
	for m in dm:
                print(m)
                cmdm = "sudo /opt/recon-ng/recon-cli -w " +org+" -m "+ m + " -x"
                print(cmdm)
                os.system(cmdm)
else:
	print("NAUGHTY INPUT DETECTED")





