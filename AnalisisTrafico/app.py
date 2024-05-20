import json
from EC.Captura import Captura
from EC.Paquete import Paquete
from flask import Flask, jsonify,request
from Logica.LogicaCaptura import LogicaCaptura
app=Flask(__name__)
@app.route("/capturar")
def get_captura():
    interface=request.args.get('interface')
    tiempo=request.args.get('tiempo')
    if interface and tiempo:
        captura=LogicaCaptura.obtenerCaptura(int(tiempo),interface)
        return jsonify(captura.toJSON()),200

@app.route("/filtrar",methods=['POST'])
def post_filtrar():
    if request.method=='POST':
        filtro=request.args.get('filtro')
        datos=request.get_json()
        captura=list()
        for dato in(json.loads(datos))['_paquetes']:
            destino=dato['_ipDestino']
            origen=dato['_ipOrigen']
            protocolo=dato['_protocolo']
            tamanio=dato['_tamanio']
            captura.append(Paquete(origen,destino,protocolo,tamanio))
        lista=LogicaCaptura.filtrarProtocolo(Captura(captura),filtro)
        return jsonify(lista.toJSON()),200

@app.route("/destino", methods=['POST'])
def post_destino():
    if request.method=='POST':
        datos = request.get_json()
        captura = list()
        for dato in (json.loads(datos))['_paquetes']:
            destino = dato['_ipDestino']
            origen = dato['_ipOrigen']
            protocolo = dato['_protocolo']
            tamanio = dato['_tamanio']
            captura.append(Paquete(origen, destino, protocolo, tamanio))
        destinoSolicitados=LogicaCaptura.ipDestinoMasSolicitada(Captura(captura))
        return destinoSolicitados,200

@app.route("/origen", methods=['POST'])
def post_origen():
    if request.method=='POST':
        datos = request.get_json()
        captura = list()
        for dato in (json.loads(datos))['_paquetes']:
            destino = dato['_ipDestino']
            origen = dato['_ipOrigen']
            protocolo = dato['_protocolo']
            tamanio = dato['_tamanio']
            captura.append(Paquete(origen, destino, protocolo, tamanio))
        origenSolicitados=LogicaCaptura.ipOrigenMasSolicitada(Captura(captura))
        return origenSolicitados,200
@app.route("/obtenerInterface")
def get_interface():
    interface=json.dumps([LogicaCaptura.obtenerInterface()])
    response=jsonify(interface)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response,200
if __name__ =='__main__':
    app.run(debug=True)