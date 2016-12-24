print("Enter the number of teeth and thickness in inches Diametral Pitch 20")
teeth = int(input('Number of teeth: '))
thick = float(input('Thickness: '))
name = input('Program number: ')
dia = float((teeth+2)/20)
print ("Gear blank OD is",dia,"with a thickness of",thick)
print()
print("O"+name+" ("+str(teeth)+" Tooth "+str(thick)+" thick gear)")
print("N1 G90 G17")
print("N2 G20")
print("N3 G53 G0 Z0")
print("N4 T10 M06")
print("N5 s1146 M03")
print("N6 G57")
print("N7 M08")
print("N8 G0 A0")
print("N9 G0 X-.5 Y"+str((dia/2)+1)+" Z0")
a = 0
n = 10
hd = 0.112
y = ((dia/2.000)+1)
for d in range (5):
    y += -.020
    y = round(y, 3)
    print("N"+str(n), 'G1 Y'+str(y)+' F34.')
    for i in range(teeth):
        print ('N'+str(n+1), 'G0 A',a)
        print ('N'+str(n+2), 'G1 X'+str(thick+0.125))
        print ('N'+str(n+3), 'G1 X-0.5')
        a += 360.0/teeth
        n += 3
    a = 0
y += -.012
print("N"+str(n), 'G1 Y'+str(y))
n += 1
for i in range(teeth):
    print ('N'+str(n+1), 'G0 A',a)
    print ('N'+str(n+2), 'G1 X'+str(thick+0.125))
    print ('N'+str(n+3), 'G1 X-0.5')
    a += 360.0/teeth
    n += 3