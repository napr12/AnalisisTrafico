from scapy.all import *
from EC.Paquete import Paquete
from EC.Captura import Captura
from collections import Counter
class LogicaCaptura:
    @staticmethod
    def obtenerCaptura(tiempo, interface):
        print(tiempo)
        print(interface)
        if not isinstance(tiempo,int):
            raise Exception("Se debe ingresar únicamente un entero.")
        captura=sniff(filter="ip",iface=interface, timeout=tiempo)
        capturaDevolver=list()
        for paquete in captura:
            print(paquete)
            origen = paquete[IP].src
            destino = paquete[IP].dst
            protocolo = paquete[IP].proto
            tamaño = len(paquete)
            capturaDevolver.append(Paquete(origen, destino, protocolo, tamaño))
        return Captura(capturaDevolver)
    @staticmethod
    def filtrarProtocolo(captura,protocolo):
        print(captura)
        return Captura(list(filter(lambda x: x.protocolo==protocolo,list(captura.paquetes))))
    @staticmethod
    def paquetesCapturado(captura):
        return len(captura.paquetes)
    @staticmethod
    def ipDestinoMasSolicitada(captura):
        ips=list()
        for paquetes in captura.paquetes:
            ips.append(paquetes.ipDestino)
        repetidos=Counter(ips).most_common(5)
        return repetidos
    @staticmethod
    def ipOrigenMasSolicitada(captura):
        ips=list()
        for paquetes in captura.paquetes:
            ips.append(paquetes.ipOrigen)
        repetidos=Counter(ips).most_common(5)
        return repetidos

    @staticmethod
    def obtenerInterface():
        return conf.iface.name

