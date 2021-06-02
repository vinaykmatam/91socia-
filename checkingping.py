import os
hostname = "google.com"
response = os.system("ping -c 1 " + hostname)
if response == 0:
    pingstatus = "Network Active"
    print(pingstatus)
else:
    pingstatus = "Network Error"
    print(pingstatus)
