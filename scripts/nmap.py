# этот скрипт выполняет парсинг результата сканирования nmap'ом и должен определить, какой из серверов перед нами
# на основе работы этого скрипта автоматически определяется, какой использовать playbook и просто выдает много информации о сервере

import re

# Open and read the nmap output file
with open('nmap_output.txt', 'r') as f:
    nmap_output = f.read()

# Define regular expressions to extract interesting info
open_ports_regex = re.compile(r'(\d+)/tcp\s+open')
service_info_regex = re.compile(r'(\d+)/tcp\s+(\w+)\s+([\w\.]+)?')

# Extract open ports
open_ports = open_ports_regex.findall(nmap_output)
print("Open ports: ", open_ports)

# Extract service info
service_info = service_info_regex.findall(nmap_output)
for port, service, version in service_info:
    print("Port", port, ":", service)
    if version:
        print("Version:", version)
