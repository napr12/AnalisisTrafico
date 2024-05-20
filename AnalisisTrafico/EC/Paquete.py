class Paquete:
    def __init__(self,ipOrigen,ipDestino,protocolo,tamaño):
        self._ipOrigen = ipOrigen
        self._ipDestino=ipDestino
        self._protocolo = Paquete.nombreProtocolo(protocolo) if isinstance(protocolo,int) else protocolo
        self._tamanio = tamaño
    @property
    def ipOrigen(self):
        return self._ipOrigen
    @ipOrigen.setter
    def ipOrigen(self, ipOrigen):
        self._ipOrigen=ipOrigen
    @property
    def ipDestino(self):
        return self._ipDestino
    @ipDestino.setter
    def ipDestino(self,ipDestino):
        self._ipDestino=ipDestino
    @property
    def protocolo(self):
        return self._protocolo
    @protocolo.setter
    def protocolo(self,protocolo):
        self._protocolo=protocolo
    @property
    def tamaño(self):
        return self._tamanio
    @tamaño.setter
    def tamaño(self,tamaño):
        self._tamanio=tamaño
    @staticmethod
    def nombreProtocolo(numeroProto):
        nombre_protocolos={
            6:"TCP",
            17:"UDP"
        }
        return nombre_protocolos.get(numeroProto)
    def __str__(self):
        return f'IP origen:{self._ipOrigen}; IP destino:{self._ipDestino}; Protocolo:{self._protocolo}; Tamaño:{self._tamanio}'