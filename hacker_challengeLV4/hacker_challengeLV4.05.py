## Check if an IP address is valid.
import ipaddress
ip = input('inter your ip:')

try:
    check = ipaddress.ip_address(ip)
    print('this ip vaild')
except:
    print('this ip not vaild')
