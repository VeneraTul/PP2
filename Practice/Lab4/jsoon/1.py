import json

file=open("libr.json")

libr_json=file.read()

libr=json.loads(libr_json)

print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")


for i in libr["imdata"]:
   dn_key=i["l1PhysIf"]["attributes"]["dn"]
   descr_key=i["l1PhysIf"]["attributes"]["descr"]
   speed_key=i["l1PhysIf"]["attributes"]["speed"]
   mtu_key=i["l1PhysIf"]["attributes"]["mtu"]
   print(dn_key,"                     ",descr_key,"      ",speed_key," ",mtu_key)
