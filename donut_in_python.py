from math import  *
import os
k = 0

A = float(0)
B  = float(0)
i = float(0)

j = float(0)

z = z = [0.0]*1760
b = bytearray(1760)

#print("\x1b[2J")
os.system("clear")
while True:
    b.extend([32]*1760)
    #z.extend([0]*7040)
    for j in range(int(6.28 / 0.07)):
        j = j * 0.07
        for i in range(int(6.28/0.02)):
            i = i*0.2
            sini = float(sin(i))
            cosj = float(cos(j))
            sinA = float(sin(A))
            sinj  = float(sin(j))
            cosA = float(cos(A))
            cosj2 = cosj+2
            mess = 1/(sini*cosj2*sinA+sinj*cosA+5)
            cosi = cos(i)
            cosB = cos(B)
            sinB = sin(B)
            t = sini*cosj2*cosA-sinj* sinA
            x = int(40+30*mess*(cosi*cosj2*cosB-t*sinB))
            y = int(12+15*mess*(cosi*cosj2*sinB +t*cosB))
            o = int(x+80*y)
            N = int(8*((sinj*sinA-sini*cosj*cosA)*cosB-sini*cosj*sinA-sinj*cosA-cosi *cosj*sinB))
            if 22 > y and y > 0 and x > 0 and 80 > x and mess > z[o]:
                z[o] = mess
                b[o] = ord(".,-~:;=!*#$@"[N if N > 0 else 0])
                #b[o] = "N" if N <= 0 else ".,-~:;=!*#$@"[min(max(int(N), 0), 13)] #= "N" if N <= 0 else list(".,-~:;=!*#$@")[N]
            #print(o)
    for k in range(0, 1761):
        if k % 80:
            print(chr(b[k]), end="")
        else:
            print("\n", end="")
        A += 0.04
        B += 0.02
