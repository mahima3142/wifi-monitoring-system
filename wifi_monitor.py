import tkinter as tk
from tkinter import messagebox

#Check WiFi signal strength
import subprocess
import re

def get_wifi_signal():
    result = subprocess.check_output(
        ["netsh", "wlan", "show", "interfaces"],
        shell=True,
        encoding="utf-8"
    )

    match = re.search(r"Signal\s*:\s*(\d+)%", result)
    if match:
        return int(match.group(1))
    return None

signal = get_wifi_signal()

if signal is None:
    print("WiFi not connected")
elif signal < 40:
    print("Weak signal. Move closer to the WiFi router.")
else:
    print(f"Signal strength is good: {signal}%")

#Count connected devices (local network scan)
def count_connected_devices():
    result = subprocess.check_output(
        ["arp", "-a"],
        shell=True,
        encoding="utf-8"
    )

    devices = set()
    for line in result.splitlines():
        if "-" in line and "dynamic" in line.lower():
            devices.add(line.split()[1])

    return len(devices)
device_count = count_connected_devices()
print(f"Devices connected to this WiFi (approx): {device_count}")

#This function is the bridge between your brain code and the UI.
def check_wifi():
    signal = get_wifi_signal()
    devices = count_connected_devices()

    if signal is None:
        status_label.config(text="WiFi not connected", fg="red")
        return

    if signal < 40:
        status = "Weak signal. Move closer to the router."
        status_label.config(text=status, fg="red")
    else:
        status = f"Signal strength is good: {signal}%"
        status_label.config(text=status, fg="green")

    device_label.config(text=f"Connected devices : {devices}")

#Create the UI window
root = tk.Tk()
root.title("WiFi Monitoring System")
root.geometry("400x250")
root.resizable(False, False)

#Add UI elements (labels + button)
title_label = tk.Label(
    root,
    text="WiFi Monitoring System",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=10)

status_label = tk.Label(
    root,
    text="Click the button to check WiFi status",
    font=("Arial", 11)
)
status_label.pack(pady=10)

device_label = tk.Label(
    root,
    text="",
    font=("Arial", 11)
)
device_label.pack(pady=10)

check_button = tk.Button(
    root,
    text="Check WiFi",
    font=("Arial", 11),
    command=check_wifi
)
check_button.pack(pady=15)

#Start the UI loop
root.mainloop()
