# WiFi Monitoring System

## Overview
This project is a Python-based WiFi monitoring system that displays the current WiFi signal strength and estimates the number of devices connected to the same network.

## Features
- Detects WiFi signal strength in real time
- Alerts the user when the signal strength is weak
- Estimates the number of active devices connected to the network
- Simple graphical user interface

## Technologies Used
- Python
- Tkinter (GUI)
- OS and networking commands

## How It Works
- WiFi signal strength is obtained using system-level commands
- Connected devices are estimated using the ARP table
- The GUI updates the information periodically and notifies the user when the signal drops below a threshold

## Limitations
- Device count is an approximation
- Accurate device count requires router-level access
- Results may vary depending on operating system

## Future Enhancements
- Router API integration for accurate device count
- Improved UI design
- Cross-platform optimization
