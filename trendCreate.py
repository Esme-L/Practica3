import rrdtool
path_rrd = "/home/esme/Escritorio/Admonredes/Practica3/RRD/"

def BDRRD (tipo:str):
    try:
        rrdtool.create(path_rrd +"BD"+ tipo + ".rrd",
                    "--start",'N',
                    "--step",'20',
                    "DS:" + tipo + ":GAUGE:60:U:U",
                    "RRA:AVERAGE:0.5:1:24"
                    )
    except Exception as e:
        print("Error al crear el rrd" + str(e))


BDRRD('cargaCPU0')
BDRRD('RAM')
BDRRD('NETWORK')