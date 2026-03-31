#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 13:06:19 2026

@author: Martin Bielak
bielak@optics.upol.cz
"""

import serial
import serial.tools.list_ports

def get_all_dev_info():
    """
    Lists a table of all available COM ports and their parameters.
    """
    ports = serial.tools.list_ports.comports()
    
    print(f"{'Port':<15} | {'Serial Number':<20} | {'VID:PID':<10} | {'Description'}")
    print("-" * 70)
    
    for port in ports:
        vid = f"{port.vid:04X}" if port.vid is not None else "N/A"
        pid = f"{port.pid:04X}" if port.pid is not None else "N/A"
        sn = port.serial_number if port.serial_number else "No SN"
        
        print(f"{port.device:<15} | {sn:<20} | {vid}:{pid:<10} | {port.description}")
    return 0

def find_port_by_serial(sn):
    """
    Finds a port by serial number.
    Returns the port name (str) or None if the device is not found.
    """
    ports = serial.tools.list_ports.comports()
    for p in ports:
        if p.serial_number == sn:
            return p.device
    print (f'Device with SN = {sn} detected')
    return None

if __name__ == '__main__':
    target_sn = "D308C3ID"  # dvecices SN to be connected
    port_name = find_port_by_serial(target_sn)

