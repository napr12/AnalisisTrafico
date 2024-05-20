class Paquete{
    constructor(ipOrigen,ipDestino,protocolo,tamanio){
        this.ipOrigen=ipOrigen
        this.ipDestino=ipDestino
        this.protocolo=protocolo
        this.tamanio=tamanio
    }
    
}
class Captura{
    constructor(paquetes){
        this.paquetes=paquetes
    }
}

const obtenerInterface = async()=>{
    fetch('http://127.0.0.1:5000/obtenerInterface')
    .then(response => response.text())
    .then(data => {
        console.log(data)
    })
    .catch(error => {
        console.error('Error al obtener el contenido:', error)
    })
    console.log(interfaceJson)
}

const listarInterafece=()=>{
    const select = document.getElementById('Interface')
    for(let i =0;i<interfaceJson;i++){
        const option = document.createElement('option')
        option.value=interfaceJson[i]
        option.text=interfaceJson[i]
        select.add(option)
    }
}
window.onload = async()=>{
    await obtenerInterface()
}
