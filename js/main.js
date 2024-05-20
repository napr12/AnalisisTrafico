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


const interface = async()=>{
    const obtenerInterfaz=await fetch('https://0628904f-b494-453a-8817-211833085ef0.mock.pstmn.io/obtenerInterface')
    const listarInterfaz=await obtenerInterfaz.json()
    listarInterface(listarInterfaz)
}
const listarInterface = (listarInterfaz)=>{
    const select = document.getElementById('Interfaz')
    for(let i =0;i<listarInterfaz.length;i++){
        const option = document.createElement('option')
        option.value=listarInterfaz[i]
        option.text=listarInterfaz[i]
        select.add(option)
    }
}
const cargarTabla=(captura)=>{
    console.log(captura)
    tbody=document.getElementById('tbody')
    tbody.innerHTML=""
    for(let i=0; i<captura.length;i++){
        tr=document.createElement('tr')
        tdOrigen=document.createElement('td')
        tdOrigen.id="origen"+i
        tdProtocolo=document.createElement('td')
        tdProtocolo.id="protocolo"+i
        tdDestino=document.createElement('td')
        tdDestino.id="destino"+i
        tdPeso=document.createElement('td')
        tdPeso.id="peso"+i
        tdOrigen.innerText=captura[i]._ipOrigen
        tdProtocolo.innerText=captura[i]._protocolo
        tdDestino.innerText=captura[i]._ipDestino
        tdPeso.innerText=captura[i]._tamanio
        tr.appendChild(tdOrigen)
        tr.appendChild(tdProtocolo)
        tr.appendChild(tdDestino)
        tr.appendChild(tdPeso)
        tbody.appendChild(tr)
    }
}

const capturar=async ()=>{
    interfaz=document.getElementById('Interfaz')
    tiempo=document.getElementById('Tiempo')
    const obtenerCaptura = await fetch(`https://e74561e0-cb82-4356-85fc-ef6449fafcd5.mock.pstmn.io/capturar?interface=${interfaz}&tiempo=${tiempo}`)
    const listarCaptura = await obtenerCaptura.json()
    cargarTabla(listarCaptura._paquetes)
}

const filtraProtocolo = async()=>{
    
    const obtenerCaptura = await fetch(
        `http://127.0.0.1:5000/filtrar?filtro=${protocolo}`,{
            method:'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(captura)
        }
    )
    const capturaACargar = await obtenerCaptura.json()
    cargarTabla(capturaACargar._paquetes)

}

const habilitarBusqueda = ()=>{
    document.getElementById('Tiempo').disabled=false
    document.getElementById('Interfaz').disabled=false

}
const deshabilitarBusqueda = ()=>{
    document.getElementById('Tiempo').disabled=true
    document.getElementById('Interfaz').disabled=true
    
}
const busar = document.getElementById('buscar')
buscar.addEventListener("click",()=>{
    if (selectOpcion.value==1){
        capturar()
    }else if(selectOpcion.value==2){
        ipDestino()
    }else if(selectOpcion.value==3){
        ipOrigen()
    }else if(selectOpcion.value==4){
        filtraProtocolo()
    }
})

const selectOpcion = document.getElementById('opcion')

selectOpcion.addEventListener("change",()=>{
    
    if (selectOpcion.value==1){
        habilitarBusqueda()
    }else if(selectOpcion.value==2){
        deshabilitarBusqueda()
    }else if(selectOpcion.value==3){
        deshabilitarBusqueda()
    }else if(selectOpcion.value==4){
        deshabilitarBusqueda()
    }
})
interface()

{/* <option value="1">Capturar trafico</option>
<option value="2">IP destino más repetida</option>
<option value="3">IP origen más repetida</option>
<option value="4">Filtrar por protocolo</option> */}