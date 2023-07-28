import csv
import nmap

# Create a new NmapScanner object
nm = nmap.PortScanner()

# Perform a basic Nmap scan on a target (replace 'scanme.nmap.org' with your desired target)
result = nm.scan('scanme.nmap.org', arguments='-p 1-100')

# Extract scan results for the target IP (assuming only one target)
target_ip = '45.33.32.156'
scan_results = result['scan'][target_ip]['tcp']

# Save the scan results to a CSV file
csv_file = 'nmap_results.csv'
with open(csv_file, 'w', newline='') as file:
    fieldnames = ['Port', 'State', 'Service']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for port, port_info in scan_results.items():
        writer.writerow({'Port': port, 'State': port_info['state'], 'Service': port_info['name']})
