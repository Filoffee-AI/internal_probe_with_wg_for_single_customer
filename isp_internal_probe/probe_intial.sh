#!/bin/bash

sudo python3 /home/isp_internal_probe/get_edge_devices.py
sudo python3 /home/isp_internal_probe/get_isp_details.py
sudo python3 /home/isp_internal_probe/update_if_index.py
sudo python3 /home/isp_internal_probe/get_meraki_links.py
sudo python3 /home/isp_internal_probe/push_links_to_core.py
sudo python3 /home/isp_internal_probe/update_public_ip_and_vendor.py
sudo python3 push_isp_and_device_to_core.py