function iniciar(e){
    document.querySelector(".bars").onclick=desplegarrMenu;
    subir = document.getElementById("subir");
    subir.onclick=scrollCielo;
    resise(e);
    console.log(window.PaginaActual.PaginaActual,'pagina');
    if(window.PaginaActual.PaginaActual== "Home"){
        inicilizacionSlider(".tarjetas",3000,true);
        inicilizacionSlider(".cartas",3200,true);
        inicilizacionSlider("#cartas02",3400,true);
        inicilizacionSlider(".card",3600,true);
        inicilizacionSlider(".target",3700,true);
        inicilizacionSlider("#alianza",2000,true);
    }else if(window.PaginaActual.PaginaActual== "Nosotros"){
        inicilizacionSlider(".HistoriaSlider",3000,false);
    }else if(window.PaginaActual.PaginaActual== "Servicios" ){
        inicilizacionSlider("#Servicos_Categorias",1,false);        
    }
}
function scrollear(){
    var a=1
    if (document.querySelector(".active")) {
        a=0;       
    }
    var header = document.querySelector("header");
    header.classList.toggle("abajo",window.scrollY * a > 150);    
    if(window.scrollY>700){
        subir.style.opacity = "1";
    }else{
        subir.style.opacity = "0";
        subir.style.transform= "scale(1)"
    }
}
function desplegarrMenu(){        
    var navBar = document.querySelector(".nav-bar");    
    navBar.classList.toggle("active");
    scrollear()
}
function scrollCielo(){
    var desplaza = document.documentElement.scrollTop;
    if (desplaza > 0) {
        window.requestAnimationFrame(scrollCielo);
        window.scrollTo(0, desplaza - ( desplaza / 20));
        subir.style.transform= "scale(0)"
    }
}
///////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////// Actividades Complementarias
function clonar( hijo , padre ){  
    var clonado = hijo.cloneNode(true);
    padre.appendChild(clonado)
    return padre    
}
function OrdenarRangoSlider( slider ){
    if (slider.carrusel.scrollWidth / slider.carrusel.clientWidth < 2) {
        duplicarElemento( slider );}
    if( slider.hijoInicios == slider.carrusel.children.length ){//Si tiene solos los elementos de inicio ----duplicalos
        duplicarElemento( slider );}
    if (slider.final[ slider.final.length - 1 ] > slider.carrusel.scrollWidth - slider.carrusel.clientWidth ){
        duplicarElemento( slider );}
    if( slider.carrusel.children.length / slider.hijoInicios > 3){//Si m1 es muy grande para la canidad de elementos originales ---eliminar duplicados    
        if(slider.carrusel.scrollWidth / slider.carrusel.clientWidth > 3){
            eliminarElementos( slider );
        }
    }
}
function duplicarElemento( slider ){
    for (let index = 0; index < slider.hijoInicios ; index++) {
        clon = slider.carrusel.children[index];
        slider.carrusel = clonar( clon , slider.carrusel );        
    }    
}
function eliminarElementos( slider ){
    for (index = 0; index < slider.hijoInicios; index++) {
        slider.carrusel.removeChild(slider.carrusel.lastChild);        
    }
}
function listandoElementos( slider ){
    div = [];
    reccorido = 0
    for (let index = 0; index < slider.hijoInicios ; index++) {       
        ancho = slider.carrusel.children[index].clientWidth +10;// + 10;
        div.push(slider.carrusel.children[index])       
        slider.elementos.push(ancho);
        slider.distancia.push(reccorido);
        reccorido += ancho;
        slider.final.push(reccorido)        
    }
    if(slider.nombreID == '.target'){
        slider.div = div
        console.log(div,'este es el div');
    }
    
}
//////////////////////////////////////////////////////////////////////////////////// Animaciones y movimiento
function start( slider ){ 
    //console.log('start');
    if(slider.automatico == true){
        slider.intervalo = setInterval( RecorridoX , slider.t , false , slider );
    }  
}
function RecorridoX ( a , slider ){
    if(slider.isDesplazaOn==true){ clearInterval(slider.desplaza); }
    if(slider.automatico == true){
        OrdenarRangoSlider( slider );
    }    
    slider.pos = 0
    while(slider.carrusel.scrollLeft >= slider.final[ slider.final.length - 1 ] ){
        slider.carrusel.scrollLeft -= slider.final[ slider.final.length - 1 ]
    }
    slider.distancia.forEach(function(element, indice , array) {
        if(slider.carrusel.scrollLeft >= element){
            slider.pos = indice
        }
    });        
    slider.contador = 0    
    slider.desplaza = setInterval(desplazamiento , 1 , slider )        
}
function desplazamiento( slider ){    
    slider.contador++
    step = parseInt(animacionStep( slider , 1 ) ) // 2)
    slider.isDesplazaOn = true
    if (slider.direccionMovimiento == true){
        desplazaAdelante( slider , step );
    }else{
        desplazaAtras( slider , step );
    }
}
function desplazaAdelante(slider,step){
    if ( slider.carrusel.scrollLeft < slider.final[ slider.pos ] ) {  
        slider.carrusel.scrollLeft += step;
    }else{
        slider.carrusel.scrollLeft = slider.final[ slider.pos ]
        breakdesplazamiento(slider);
    }
}
function desplazaAtras(slider,step){
    if ( slider.carrusel.scrollLeft > slider.distancia[ slider.pos ] ) {  
        slider.carrusel.scrollLeft -= step;
    }else{
        slider.carrusel.scrollLeft = slider.distancia[ slider.pos ];
        if (slider.pos == 0){
            if(slider.automatico == true){
                slider.carrusel.scrollLeft = slider.final[ slider.final.length - 1 ];
            }
        }
        slider.direccionMovimiento = true
        breakdesplazamiento(slider);
    }

}
function breakdesplazamiento(slider){    
    slider.isDesplazaOn = false
    clearInterval(slider.desplaza)
}
function animacionStep( slider , steppos ){
    paso = Math.cos(slider.contador * 0.1) + 0.7
    if (paso < 0){paso = paso * -1;}
    step = parseInt((paso * 10)/2) * steppos
    if (step < 7){ step = 7;
    }else if (step > 8){ step = 8; }    
    return step 
}
///////////////////////////////////////////////////////////////////////////////////////////////// evento del mouse
function stop(s){
    clearInterval( s.intervalo );
}
function press( s,e ){    
    s.isPressedDown = true;
    clearInterval( s.desplaza );
}
function Upp( s , e ) {    
    s.isPressedDown=false;
    if(window.PaginaActual.PaginaActual== "Servicios" ){
        if (s.SeMovio == false){
            Categorias_de_Servicios( s , e );
        }else{ 
            RecorridoX( true , s ); }
    }else{
        RecorridoX( true , s );
    }
    s.SeMovio = false
}
function move(e, slider){    
    if (!slider.isPressedDown) return;
    if (e > 0 ){
        slider.direccionMovimiento = false;
        slider.SeMovio = true;
    }else if(e < 0){
        slider.direccionMovimiento = true;
        slider.SeMovio = true;
    }    
    //
    //console.log(e,'se movio');
    slider.carrusel.scrollLeft -= e;
}
///////////////////////////////////////////////////////////////////////////////////////////////////////// Declaraciones iniciales
class Carrusel{
    constructor( nombreID , t){
        this.carrusel = document.querySelector(nombreID);
        this.hijoInicios = this.carrusel.children.length;
        this.nombreID = nombreID;
        this.t = t;
        
        this.isPressedDown = false;
        this.isDesplazaOn = false;
        this.direccionMovimiento = true;
        this.automatico = true
        this.SeMovio = false
        this.desplaza
        this.intervalo

        this.div

        this.contador = 0;
        this.pos = 0;
        this.touch = 0;

        this.elementos = [];
        this.distancia = [];
        this.final = [];
   }
}
function inicilizacionSlider(nombre,tiempo,automata){
    console.log('evento');
    const slider = new Carrusel(nombre , tiempo);
    slider.automatico = automata
    slider.carrusel.addEventListener("mouseover", function(){ stop(slider) });    
    slider.carrusel.addEventListener("mouseout", function() {  start( slider ); } );
    slider.carrusel.addEventListener("mousedown", function(e){press(slider,e)} );
    slider.carrusel.addEventListener("mouseup", function(e) { Upp( slider ,e);} );
    slider.carrusel.addEventListener("mousemove", function(e) { 
        e.preventDefault();
        move( e.movementX ,slider ); 
    });

    slider.carrusel.addEventListener("touchstart", function(e){press(slider,e)} );
    slider.carrusel.addEventListener("touchend", function(e){ 
        slider.touch = 0;
        Upp( slider ,e.touches[0]);
    } );
    slider.carrusel.addEventListener("touchmove", function(e){touchmovementX( e,slider ); });
    listandoElementos(slider)    
    start( slider );
}
function touchmovementX( e , slider ) {
    if(slider.touch == 0){
        slider.touch = e.touches[0].pageX;
        move( 0 , slider );
    }else{
        move( e.touches[0].pageX - slider.touch , slider );
        slider.touch = e.touches[0].pageX;
    }
}
///////////////////////////////////////////////////////////////////////////////////////////
function resise(e){
    console.log(document.documentElement.clientWidth, 'resize');
    if(window.PaginaActual.PaginaActual== "Nosotros"){
        if (document.documentElement.clientWidth<950){
            document.querySelector(".HistoriaSlider").style.width = ""+(document.documentElement.clientWidth - 40) +"px";
        }else{
            document.querySelector(".HistoriaSlider").style.width = "950px";
        }
    }else if(window.PaginaActual.PaginaActual== "Servicios"){
        if (document.documentElement.clientWidth<950){
            document.querySelector("#Servicos_Categorias").style.width = ""+(document.documentElement.clientWidth-40 ) +"px";
        }else{
            document.querySelector("#Servicos_Categorias").style.width = "950px";
        }
    }
    documenoresise()
}
///////////////////////////////////////////////////////////////////////////////////////////
function documenoresise(){
    if(window.PaginaActual.PaginaActual== "Documentos"){
        if(document.documentElement.clientWidth>706){
            if (window.columnajs.columnajs != 3){
                EditarDocumento(3);
                window.columnajs.columnajs = 3;
            }            
        }else if(document.documentElement.clientWidth<=706 &&  document.documentElement.clientWidth>466){
            if (window.columnajs.columnajs != 2){
                EditarDocumento(2);
                window.columnajs.columnajs = 2;
            }
        }else{
            if (window.columnajs.columnajs != 1){
                EditarDocumento(1);
                window.columnajs.columnajs = 1;
            }
        }
    }
}
function eliminando(elemento){
    if(elemento != null){
        while (elemento.children.length>0) {
            elemento.removeChild(elemento.children[0]);
    }}
}
function EditarDocumento(columnas){
    let data = window.data.data;
    let cantidad_por_columna = 0;
    let inicio = 0
    let final = 0
    let base = 0
    let hijo = 0
    let padre = 0

    for (index = 0; index < data.length; index++) {
        for (let i = 2; i < 4; i++) {
            eliminando( document.getElementById(''+index+data[index]+i) );
        }
    }

    for (index = 0; index < data.length; index++) {
        cantidad_por_columna = data[index] / columnas;
        redondeo = Math.round(cantidad_por_columna)
        cantidad_por_columna = Math.max(redondeo , parseInt(cantidad_por_columna))
        inicio  = 0;
        final   = 0;        
        base = document.getElementById(''+index+data[index]+'1');
        if(base != null){
            for (let colum = 1; colum <= columnas; colum++) {
                inicio  = cantidad_por_columna * (colum - 1);
                final   = cantidad_por_columna *  colum ;

                if(data[index] - final  < 0 ){final = data[index];}
                
                for (let element = inicio; element < final; element++) {
                    
                    hijo = base.children[element];
                    hijo.style.display = 'grid';
                    
                    if (colum > 1){
                        padre = document.getElementById(''+index+data[index]+(colum));
                        padre.style.display = 'grid'
                        padre = clonar( hijo , padre );                
                        hijo.style.display = 'none';
                    }
                }
            }
            for (let colelimina = columnas + 1; colelimina <= 3; colelimina++) {
                document.getElementById(''+index+data[index]+(colelimina)).style.display = 'none'
        }}
    }

    for (index = 0; index < data.length; index++) {
        for (let i = 2; i < 4; i++) {
            if ( document.getElementById( '' + index + data[index] + i ) != null){
                console.log( document.getElementById( '' + index + data[index] + i ).children.length, '' + index + data[index] + i );            
                if( document.getElementById( '' + index + data[index] + i ).children.length == 0){
                    document.getElementById( '' + index + data[index] + i ).style.display = 'none';
            }}           
        }
    }

}
///////////////////////////////////////////////////////////////////////////////////////////
function Categorias_de_Servicios( slider , categoria ){
    var Categorias = document.getElementById('Servicioscard')

    if(slider.carrusel.children[categoria.target.id-1].id == "Categoria_seleccionada"){

        slider.carrusel.children[categoria.target.id-1].id = categoria.target.id;
        for (let i = 0; i < slider.carrusel.children.length; i++) {
            slider.carrusel.children[i].children[0].style.marginLeft = "10px";
        }
        for (let i = 0; i < Categorias.children.length; i++) {
            Categorias.children[i].style.display = "grid";
        }
    }else{

        for (let i = 0; i < slider.carrusel.children.length; i++) {
            slider.carrusel.children[i].id = i+1 ;
            slider.carrusel.children[i].children[0].style.marginLeft = "10px";
        }
        slider.carrusel.children[parseInt(categoria.target.id) - 1].children[0].style.marginLeft = "0px";
        slider.carrusel.children[categoria.target.id - 1].id = "Categoria_seleccionada";    
        if (slider.SeMovio == false){
            for (let i = 0; i < Categorias.children.length; i++) {
                if(Categorias.children[i].id != categoria.target.id){
                    Categorias.children[i].style.display = "none"
                } 
                if(Categorias.children[i].id == categoria.target.id){
                    Categorias.children[i].style.display = "grid"
                }
            }
        }
    }
}
///////////////////////////////////////////////////////////////////////////////////////////

window.addEventListener('resize', resise,false);
window.addEventListener('scroll',scrollear,false);
window.addEventListener('load',iniciar,false);
