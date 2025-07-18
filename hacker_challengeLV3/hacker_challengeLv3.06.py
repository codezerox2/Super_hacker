### Store ports and services in a dictionary and allow user queries.
services = {
    80: "http",
    21: "ftp",
    22: "ssh",
    445: "SMB",
    443:"https"
}
portscan = int(input("input your port num: "))
if portscan in services:
    print(services[portscan])
        
else:
    print("error:port missing")