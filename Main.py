#-------------------------
# Sparten Trafic-Bot V.0.1.1
# By Mert Can Elsner
# Last Update 25.03.2020
#-------------------------




# Necessary imports
import subprocess
import fileinput
import random
import time
import sys
import os


#-------------------------
# Data for loop
count = 0                   
MaxCount = 200              
w = random.randint(16, 86)
#-------------------------



#-------------------------
# Start
print("----Start----")
print("round", count, "of" ,MaxCount)
print("waiting period", w,"Sek.")
#-------------------------



#-------------------------
# Main loop
while count != MaxCount:
    with open("url.txt") as f:
        for url in f:
            
            #Tab 1 / Tor
            process = subprocess.Popen([r'C:\Users\mert1\OneDrive\Desktop\Tor Browser\Browser\firefox.exe', #<--- YOUR Tor Browser path.
            '-new-tab', (url)])                         #<--- What should happen in the browser
            time.sleep(1)                               #<--- Break
            time.sleep(w)                               #<--- waiting period
            os.system("taskkill /im firefox.exe /f")    #<--- kills the browser (Firefox core, such as Tor)
            time.sleep(5)                               #<--- Break
            
            
            #Notification at the end of a round and the beginning of a new round
            print("____________________")   #<--- round end
            print()                         #<--- placeholder
            print()                         #<--- placeholder
            print()                         #<--- placeholder
            print("____________________")   #<--- round start
            count = count + 1               #<--- round counter
            print("round", count, "of" ,MaxCount)
            w = random.randint(30, 90)      #<--- Waiting time is randomize again
            time.sleep(1)
            print("waiting period", w,"Sek.")                      
#-------------------------



#-------------------------
# End notification + round control unit
if count == MaxCount:  #<--- round control unit

    #End notification
    print("____________________")           
    print("End")
    print("round", count, "of" ,MaxCount)
    print("for:", (url))
    print("____________________")
    time.sleep(9999)
#-------------------------



#-------------------------
#End of the main loop
else:
    pass
#-------------------------