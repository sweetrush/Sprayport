#sprayport.py
# Purpose: Just another Port Scanner in Python 
# Developed by: Suetena Loia aka SweetrushCoder
# Version: 0.9

import socket
import threading
from queue import Queue

print_lock = threading.Lock()

# Defining Server List
serverAddress = [
"10.3.3.1",
"192.168.114.254",
"202.4.60.21",
"202.4.38.151",
"8.8.8.8"
]

# Iniation of Server Loop Address Holder
# Due ServerAddress List Injection for Threading
activeServertoScan = ""

#Defining Port List
portToScan = [
    80,    # HTTP Standard
    443,   # HTTPS
    8080,  # HTTP Custom
    4100,  # HTTP Custom
    22,    # SSH Standard
    21,    # FTP Standard
    23,    # Telnet Standard
    ]


# Define the Number of Theads to Use.
# threadWorkers = (len(portToScan))

threadWorkers = (1000)


def initPrompt():
    print(
        "\n\n\n",
        "SprayPort Scanner  [verion 0.9] \n",
        "Developed by: Suetena Loia aka [SweetrushCoder]\n"
        "License: GNUv1\n"
        )

def EndingPrompt():
    print("\n\n\n",
    "+=================================================+\n",
    "Scan Completed Successfull \n",
    "Number of IP Scannned: (", (len(serverAddress)), ") \n",
    "Number of Ports Scanned: (", (len(portToScan)), ") \n",
    "+=================================================+\n"
    )

# scan fucation 
def portscan(setPort):
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        conto = sck.connect((activeServertoScan, setPort))
        with print_lock:
            print('\tPort \t', setPort, "\tReturned  ### OPEN ###")
        conto.close()

    except:
        pass

# Running Threading for Speed
def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()


# Main loop for the Program or Main Calling Area 
# Start Here
initPrompt()

# Iniatioing Loops for Scanning Address List
for x in range(len(serverAddress)):

    activeServertoScan = serverAddress[x]
    print(
        "\n---------------------------------------------------",
        "\nScan Result ", activeServertoScan, 
        "\n---------------------------------------------------\n"
        )

    q= Queue()
    
    for gg in range(threadWorkers):
         t = threading.Thread(target=threader)
         t.daemon = True
         t.start()
         
    for y in range(len(portToScan)):
         worker = portToScan[y]
         q.put(worker)


    q.join()

# End of Running Code
EndingPrompt()