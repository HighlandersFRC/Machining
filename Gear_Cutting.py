import io

def generate_Gcode(teeth, thick, name):
    output = io.StringIO()
    dia = float((teeth + 2) / 20)
    output.write('%\n')
    output.write("O" + name + " (" + str(teeth) + " Tooth " + str(thick) + " thick gear)\n")
    output.write("N1 G90 G17\n")
    output.write("N2 G20\n")
    output.write("N3 G53 G0 Z0\n")
    output.write("N4 T13 M06\n")
    output.write("N5 s286 M03\n")
    output.write("N6 G57\n")
    output.write("N7 M08\n")
    output.write("N8 G0 A0\n")
    output.write("N9 G0 X-.5 Y" + str((dia / 2) + 1) + " Z0\n")
    a = 0
    n = 10
    hd = 0.112
    y = ((dia / 2.000) + 1)
    for d in range(2):
        y += -.050
        y = round(y, 3)
        output.write("N" + str(n) + ' G1 Y' + str(y) + ' F13.\n')
        for i in range(teeth):
            output.write('N' + str(n + 1) + ' G0 A ' + str(a) + "\n")
            output.write('N' + str(n + 2) + ' G1 X' + str(thick + 0.0625) + "\n")
            output.write('N' + str(n + 3) + ' G1 X-0.5\n')
            a += 360.0 / teeth
            a = round(a, 3)
            n += 3
        a = 0

    y += -.012
    output.write("N" + str(n) + ' G1 Y' + str(y) + "\n")
    n += 1
    for i in range(teeth):
        output.write('N' + str(n + 1) + ' G0 A ' + str(a) + "\n")
        output.write('N' + str(n + 2) + ' G1 X' + str(thick + 0.0625) + "\n")
        output.write('N' + str(n + 3) + ' G1 X-0.5' + "\n")
        a += 360.0 / teeth
        a = round(a, 3)
        n += 3

    output.write('N' + str(n) + " M09\n")
    output.write('N' + str(n + 1) + " G1 X-0.75\n")
    output.write('N' + str(n + 2) + " M05\n")
    output.write('%\n')
    code = output.getvalue()
    output.close()
    return code

if __name__ == "__main__":
    print("Enter the number of teeth and thickness in inches Diametral Pitch 20")
    teeth = int(input('Number of teeth: '))
    thickness = float(input('Thickness: '))
    name = input('Program number: ')
    filename = input("Enter a filename")
    gCode = generate_Gcode(teeth, thickness, name)
    f = open(filename, "w+")
    f.write(gCode)
    f.close()



