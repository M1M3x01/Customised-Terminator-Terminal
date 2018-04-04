import requests

print('Downloading Terminator')

url = 'https://launchpad.net/terminator/gtk3/1.91/+download/terminator-1.91.tar.gz'
r = requests.get(url)

with open('/root/Downloads/terminator.tar.gz', 'wb') as f:
    f.write(r.content)

print('Download Complete')
