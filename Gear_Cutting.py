'''
This python script was created to generate Gcode For 20dp Gears on a 4th axis
'''
print("Enter the number of teeth and thickness in inches Diametral Pitch 20")
teeth = int(input('Number of teeth: '))
thick = float(input('Thickness: '))
name = input('Program number: ')
dia = float((teeth+2)/20)
print("Gear blank OD is",dia,"with a thickness of",thick)
print()
outputfile = open("gear.nc","w+")
outputfile.write('%\n')
outputfile.write("O"+name+" ("+str(teeth)+" Tooth "+str(thick)+" thick gear)\n")
outputfile.write("N1 G90 G17\n")
outputfile.write("N2 G20\n")
outputfile.write("N3 G53 G0 Z0\n")
outputfile.write("N4 T13 M06\n")
outputfile.write("N5 s286 M03\n")
outputfile.write("N6 G57\n")
outputfile.write("N7 M08\n")
outputfile.write("N8 G0 A0\n")
outputfile.write("N9 G0 X-.5 Y"+str((dia/2)+1)+" Z0\n")
a = 0
n = 10
hd = 0.112
y = ((dia/2.000)+1)
for d in range (2):
    y += -.050
    y = round(y, 3)
    outputfile.write("N"+str(n)+ ' G1 Y'+str(y)+' F13.\n')
    for i in range(teeth):
        outputfile.write ('N'+str(n+1)+ ' G0 A '+str(a)+"\n")
        outputfile.write ('N'+str(n+2)+ ' G1 X'+str(thick+0.0625)+"\n")
        outputfile.write ('N'+str(n+3)+ ' G1 X-0.5\n')
        a += 360.0/teeth
        a = round(a, 3)
        n += 3
    a = 0

y += -.012
outputfile.write("N"+str(n)+ ' G1 Y'+str(y)+"\n")
n += 1
for i in range(teeth):
    outputfile.write ('N'+str(n+1)+ ' G0 A '+str(a)+"\n")
    outputfile.write ('N'+str(n+2)+ ' G1 X'+str(thick+0.0625)+"\n")
    outputfile.write ('N'+str(n+3)+ ' G1 X-0.5'+"\n")
    a += 360.0/teeth
    a = round(a, 3)
    n +=3 

outputfile.write ('N'+str(n)+" M09\n")
outputfile.write ('N'+str(n+1)+" G1 X-0.75\n")
outputfile.write ('N'+str(n+2)+" M05\n")
outputfile.write('%\n')
outputfile.close()
