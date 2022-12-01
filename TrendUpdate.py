import time
import rrdtool
from getSNMP import consultaSNMP
rrdpath = '/home/esme/Escritorio/Admonredes/Practica3/RRD/'
cargaCPU0 = 0
CPU0 = "1.3.6.1.2.1.25.3.3.1.2.6"
RAMTOTAL = "1.3.6.1.2.1.25.2.3.1.5.2"
RAMUSO = "1.3.6.1.2.1.25.2.3.1.6.2"
OCTINPUT = "1.3.6.1.2.1.2.2.1.10.11"
OCOUTPUT = "1.3.6.1.2.1.2.2.1.16.11" 
SPEED = "1.3.6.1.2.1.2.2.1.5.11"

while 1:
    cargaCPU0 = int(consultaSNMP('EsmeraldaZP','192.168.100.245',CPU0))
    RAMT = int(consultaSNMP('EsmeraldaZP','192.168.100.245',RAMTOTAL))
    RAMU = int(consultaSNMP('EsmeraldaZP','192.168.100.245',RAMUSO))
    OCIN = int(consultaSNMP('EsmeraldaZP','192.168.100.245',OCTINPUT))
    OCOUT = int(consultaSNMP('EsmeraldaZP','192.168.100.245',OCOUTPUT))
    CSPEED = int(consultaSNMP('EsmeraldaZP','192.168.100.245',SPEED))

    PORRAM = int((RAMU * 100)/ RAMT)
    RED = int((OCIN+OCOUT*8*100)/CSPEED)

    valorC = "N: " + str(cargaCPU0)
    valorR = "N: " + str(PORRAM) 
    valorTI = "N: " + str(RED)
    
    print (valorC + " " + valorR + " " + valorTI)

    rrdtool.update(rrdpath+'BDcargaCPU0.rrd', valorC)
    rrdtool.dump(rrdpath+'BDcargaCPU0.rrd',rrdpath+'BDcargaCPU0.xml')

    rrdtool.update(rrdpath+'BDRAM.rrd', valorR)
    rrdtool.dump(rrdpath+'BDRAM.rrd',rrdpath+'BDRAM.xml')

    rrdtool.update(rrdpath+'BDNETWORK.rrd', valorTI)
    rrdtool.dump(rrdpath+'BDNETWORK.rrd',rrdpath+'BDNETWORK.xml')

    time.sleep(5)

if ret:
    print (rrdtool.error())
    time.sleep(300)
