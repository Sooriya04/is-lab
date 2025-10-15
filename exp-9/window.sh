echo sooriyab-23IT155 > sooriya.txt

openssl aes-128-cbc -e -in sooriya.txt -out cipher.bin -k "password" -nosalt

type cipher.bin

openssl enc -aes-128-cbc -d -in cipher.bin -k "password" -nosalt -p

openssl aes-128-cbc -d -in cipher.bin -out pt.txt -k "password" -nosalt

type pt.txt

(echo|set /p=SOORIYA-23IT155) > plain.txt

openssl aes-128-cbc -e -in plain.txt -out cipher2.bin -k "password" -nosalt

fc /b cipher.bin cipher2.bin

openssl genrsa -out pvtkey.pem 2048

openssl rsa -pubout -in pvtkey.pem -out pubkey.pem

openssl rsa -text -in pvtkey.pem

openssl rsautl -encrypt -in plain.txt -pubin -inkey pubkey.pem -out c1.bin

openssl rsautl -decrypt -in c1.bin -inkey pvtkey.pem -out decrypted.txt

openssl rsautl -decrypt -in c1.bin -inkey pvtkey.pem -out decrypted_rsa.txt

type decrypted_rsa.txt

openssl md5 plain.txt

openssl sha256 plain.txt

openssl dgst -sha256 -sign pvtkey.pem -out s.bin plain.txt

openssl dgst -sha256 -verify pubkey.pem -signature s.bin plain.txt




Sure! Since you’re building a basic site-to-site VPN topology with three routers and two PCs (as shown in your Packet Tracer screenshot), I’ll provide the step-by-step CLI configuration you need for Router1 (Middle), Router2 (Left), and Router3 (Right).


---

✅ Assumptions Based on Your Setup

Device	Interface	IP Address	Connected To

PC0	NIC	192.168.1.2/24	Router2
Router2	Fa0/0	192.168.1.1/24	PC0
	Serial0/0	1.0.0.2/30	Router1
Router1	Serial0/0	1.0.0.1/30	Router2
	Serial0/1	2.0.0.1/30	Router3
Router3	Serial0/0	2.0.0.2/30	Router1
	Fa0/0	192.168.2.1/24	PC1
PC1	NIC	192.168.2.2/24	Router3



---

🔧 Router Configurations

🟢 Router2 (Left)

enable
conf t
hostname Router2

interface FastEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown

interface Serial0/0
 ip address 1.0.0.2 255.255.255.252
 clock rate 64000
 no shutdown

ip route 192.168.2.0 255.255.255.0 1.0.0.1

end
wr


---

🔵 Router1 (Center - Hub)

enable
conf t
hostname Router1

interface Serial0/0
 ip address 1.0.0.1 255.255.255.252
 no shutdown

interface Serial0/1
 ip address 2.0.0.1 255.255.255.252
 no shutdown

ip route 192.168.1.0 255.255.255.0 1.0.0.2
ip route 192.168.2.0 255.255.255.0 2.0.0.2

end
wr


---

🔴 Router3 (Right)

enable
conf t
hostname Router3

interface FastEthernet0/0
 ip address 192.168.2.1 255.255.255.0
 no shutdown

interface Serial0/0
 ip address 2.0.0.2 255.255.255.252
 clock rate 64000
 no shutdown

ip route 192.168.1.0 255.255.255.0 2.0.0.1

end
wr


---

✅ Test Connectivity

From PC0, try:

ping 192.168.2.2

If successful ✅ — Your basic network is ready.


---

🚀 Next Step: VPN (IPSec / GRE / DMVPN)

Tell me:

1. Do you want Static IPSec or GRE over IPSec?


2. Is Router1 acting as VPN Hub?



I'll then give you exact VPN commands to secure the tunnel 🔒.

Shall I continue with IPSec config?

