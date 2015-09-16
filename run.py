from scapy.all import *
import requests
import time
WEB_TASK_URL = 'https://webtask.it.auth0.com/api/run/wt-xmlking+github-gmail_com-0/send_text?webtask_no_cache=1'

def call_webtask():
  data = {
    "Timestamp": time.strftime("%Y-%m-%d %H:%M"),
    "to": '+19513677933',
    "message": 'Tide button pressed'
  }
  r = requests.post(WEB_TASK_URL, data)
  print(r.text)

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      if pkt[ARP].hwsrc == '74:75:48:8a:4f:f0': # Tide
        # print "Pushed Tide"
        call_webtask()
      else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0, count=10)