# importing modules
from os import system
from termcolor import colored
from covid import Covid

#colors
cn = 'cyan'

# banner
system('clear')
system('figlet -f ./usaflag "CORONA" | lolcat -a -d 2')
system('echo "               Covid Tracker by comradesec" | lolcat -a -d 10')

# Tracking cases
corona = Covid()
cont = input(colored("\nEnter Your country name: ",cn))
case = corona.get_status_by_country_name(cont)
print()
for cont in case:
    print(cont,":",case[cont])

# End screen
system('echo')
system('echo "WEAR MASK :D BE SAFE!!!" | lolcat -a -d 40')
print()
system('echo "I hope you liked it Follow  [ COMRADESEC ] in GITHUB For More COOL stuffs :D " | lolcat -a -d 120 ')
print()
