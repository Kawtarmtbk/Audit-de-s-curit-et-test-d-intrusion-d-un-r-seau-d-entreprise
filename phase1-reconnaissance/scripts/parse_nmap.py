#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import sys
import os

def parse_nmap_xml(xml_file):
    if not os.path.exists(xml_file):
        print(f"[-] Fichier introuvable : {xml_file}")
        sys.exit(1)

    tree = ET.parse(xml_file)
    root = tree.getroot()

    print("=" * 60)
    print(f"RAPPORT D'ANALYSE NMAP XML : {xml_file}")
    print("=" * 60)

    for host in root.findall('host'):
        # Extraction de l'IP
        address = host.find('address')
        ip = address.attrib.get('addr') if address is not None else "Inconnue"

        # État de l'hôte
        status = host.find('status')
        state = status.attrib.get('state') if status is not None else "unknown"

        print(f"\n[+] Hôte : {ip} (État: {state.upper()})")
        print("-" * 40)
        print(f"{'PORT':<10} {'ETAT':<10} {'SERVICE':<15} {'VERSION'}")
        print("-" * 40)

        ports = host.find('ports')
        if ports is not None:
            for port in ports.findall('port'):
                port_id = port.attrib.get('portid')
                protocol = port.attrib.get('protocol')

                state_elem = port.find('state')
                port_state = state_elem.attrib.get('state') if state_elem is not None else "unknown"

                service_elem = port.find('service')
                service_name = "unknown"
                product = ""
                version = ""

                if service_elem is not None:
                    service_name = service_elem.attrib.get('name', 'unknown')
                    product = service_elem.attrib.get('product', '')
                    version = service_elem.attrib.get('version', '')

                full_version = f"{product} {version}".strip()
                print(f"{port_id}/{protocol:<5} {port_state:<10} {service_name:<15} {full_version}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 parse_nmap.py <fichier_nmap.xml>")
        sys.exit(1)

    parse_nmap_xml(sys.argv[1])
