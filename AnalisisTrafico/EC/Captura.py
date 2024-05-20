import json
class Captura:
    def __init__(self,paquetes):
        if len(paquetes)==0:
            raise Exception("La captura no contiene paquete")
        elif isinstance(paquetes, list):
            self._paquetes = list(paquetes)
        else:
            raise Exception("El argumento no es una lista")
    @property
    def paquetes(self):
        return list(self._paquetes)
    def toJSON(self):
        return json.dumps(self,default= lambda x: x.__dict__,sort_keys=True)
    def __str__(self):
        lineas=""
        for paquete in self._paquetes:
            lineas+=f'{paquete}\n'
        return lineas