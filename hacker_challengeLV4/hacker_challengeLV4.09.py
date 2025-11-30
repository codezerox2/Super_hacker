## Resolve a hostname to an IP address.

Resolve = {
    'google.com': '216.58.209.46',
    'youtube.com' : '216.58.204.142',
    'facebook.com' : '102.132.97.35'

}   

search = input('inter the hostname: ')

print(f"your domain ip is: {Resolve[search]}")