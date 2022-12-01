import sys
import rrdtool
import time
import datetime
from  Notify import send_alert_attached
import time

rrdpath = '/home/esme/Escritorio/Admonredes/Practica3/RRD/'
imgpath = '/home/esme/Escritorio/Admonredes/Practica3/IMG/'
ALERTACPU = [True, True, True]
ALERTARAM = [False, False, False]
ALERTARED = [False, False, False]

def graficaCPU(ultima_lectura):

    tiempo_final = int (ultima_lectura)
    tiempo_inicial = tiempo_final - 400
    try:
        ret = rrdtool.graphv(imgpath+"CPU0.png",
                            "--start",str(tiempo_inicial),
                            "--end",str(tiempo_final),
                            "--vertical-label=Cpu load",
                            '--lower-limit', '0',
                            '--upper-limit', '100',
                            "--title=Carga del CPU del agente Usando SNMP y RRDtools \n Detección de umbrales",
                            "DEF:cargaCPU0="+rrdpath+"BDcargaCPU0.rrd:cargaCPU0:AVERAGE",

                            "AREA:cargaCPU0#863A6F:Carga del CPU0",

                             "HRULE:45#F7A40C:Umbral  45%",
                             "HRULE:50#EF3620:Umbral  50%",
                             "HRULE:90#BE1704:Umbral  90%",
                        )

    except Exception as e:
        print('Error al momento de graficar CPU: '+ str(e))

def graficaRAM(ultima_lectura):

    tiempo_final = int (ultima_lectura)
    tiempo_inicial = tiempo_final - 400
    try:
        ret = rrdtool.graphv(imgpath+"RAM.png",
                            "--start",str(tiempo_inicial),
                            "--end",str(tiempo_final),
                            "--vertical-label=RAM load",
                            '--lower-limit', '0',
                            '--upper-limit', '100',
                            "--title=Carga de la RAM del agente Usando SNMP y RRDtools \n Detección de umbrales",
                            "DEF:RAM="+rrdpath+"BDRAM.rrd:RAM:AVERAGE",

                            "AREA:RAM#D989B5:Carga de la RAM",

                             "HRULE:45#F7A40C:Umbral  45%",
                             "HRULE:50#EF3620:Umbral  50%",
                             "HRULE:90#BE1704:Umbral  90%",
                        )

    except Exception as e:
        print('Error al momento de graficar RAM: '+ str(e))

def graficaRED(ultima_lectura):

    tiempo_final = int (ultima_lectura)
    tiempo_inicial = tiempo_final - 400
    try:
        ret = rrdtool.graphv(imgpath+"RED.png",
                            "--start",str(tiempo_inicial),
                            "--end",str(tiempo_final),
                            "--vertical-label=Uso de Red load",
                            '--lower-limit', '0',
                            '--upper-limit', '200',
                            "--title=Carga de la RED del agente Usando SNMP y RRDtools \n Detección de umbrales",
                            "DEF:NETWORK="+rrdpath+"BDNETWORK.rrd:NETWORK:AVERAGE",

                            "AREA:NETWORK#975C8D:Carga de la RED",

                             "HRULE:140#F7A40C:Umbral  140",
                             "HRULE:150#EF3620:Umbral  150",
                             "HRULE:180#BE1704:Umbral   180",
                        )

    except Exception as e:
        print('Error al momento de graficar RED: '+ str(e))

while (1):

    ultima_actualizacion = rrdtool.lastupdate(rrdpath + "BDcargaCPU0.rrd")
    timestamp=ultima_actualizacion['date'].timestamp()
    dato=ultima_actualizacion['ds']["cargaCPU0"]

    if dato > 45 and ALERTACPU[0]:
        graficaCPU(int(timestamp))
        send_alert_attached("Sobrepaso el primer umbral", "El CPU ha pasado el 45%, del agente 192.168.100.245 ","CPU0")
        print("Sobrepasa el umbral")
        ALERTACPU[0] = False

    if dato > 50 and ALERTACPU[1]: 
        graficaCPU(int(timestamp))
        send_alert_attached("Sobrepaso el segundo umbral", "El CPU ha pasado el 50%, del agente 192.168.100.245 ","CPU0")
        print("Sobrepasa el umbral")
        ALERTACPU[1] = False

    if dato > 90 and ALERTACPU[2]:
        graficaCPU(int(timestamp))
        send_alert_attached("Sobrepaso el tercer umbral", "El CPU ha pasado el 90% ","CPU0")
        print("Sobrepasa el umbral")
        ALERTACPU[2] = False
    time.sleep(20)

    ultima_actualizacionR = rrdtool.lastupdate(rrdpath + "BDRAM.rrd")
    timestampR=ultima_actualizacionR['date'].timestamp()
    datoR=ultima_actualizacionR['ds']["RAM"]

    if datoR > 45 and ALERTARAM[0]:
        graficaRAM(int(timestampR))
        send_alert_attached("Sobrepaso el primer umbral", "La RAM ha pasado el 45%","RAM")
        print("Sobrepasa el umbral")
        ALERTARAM[0] = False

    if datoR > 50 and ALERTARAM[1]:
        graficaRAM(int(timestampR))
        send_alert_attached("Sobrepaso el segundo umbral", "La RAM ha pasado el 50%","RAM")
        print("Sobrepasa el umbral")
        ALERTARAM[1] = False

    if datoR > 90 and ALERTARAM[2]:
        graficaRAM(int(timestampR))
        send_alert_attached("Sobrepaso el tercer umbral", "La RAM ha pasado el 90%","RAM")
        print("Sobrepasa el umbral")
        A
    time.sleep(20)

    ultima_actualizacionRED = rrdtool.lastupdate(rrdpath + "BDNETWORK.rrd")
    timestampRED=ultima_actualizacionRED['date'].timestamp()
    datoRED=ultima_actualizacionRED['ds']["NETWORK"]

    if datoRED > 140 and ALERTARED[0]:
        graficaRED(int(timestampRED))
        send_alert_attached("Sobrepaso el primer umbral", "La RED ha pasado el 140","RED")
        print("Sobrepasa el umbral")
        ALERTARED[0] = False

    if datoRED > 150 and ALERTARED[1]:
        graficaRED(int(timestampRED))
        send_alert_attached("Sobrepaso el segundo umbral", "La RED ha pasado el 150","RED")
        print("Sobrepasa el umbral")
        ALERTARED[1] = False

    if datoRED > 180 and ALERTARED[2]:
        graficaRED(int(timestampRED))
        send_alert_attached("Sobrepaso el tercer umbral", "La RED ha pasado el 180","RED")
        print("Sobrepasa el umbral")
        ALERTARED[2] = False
    time.sleep(20)
