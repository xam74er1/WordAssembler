import * as THREE from 'https://unpkg.com/three/build/three.module.js';
import * as model from "./model.js";
import { OrbitControls } from "https://threejs.org/examples/jsm/controls/OrbitControls.js";

const renderer = new THREE.WebGLRenderer();
var scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );


var font = undefined;
var mainWord = undefined
var listCube = [];

var ligthTheme = false;

renderer.setSize( window.innerWidth, window.innerHeight );

document.body.appendChild( renderer.domElement );
if(ligthTheme) {
    scene.background = new THREE.Color(0xffffff);
}
var controls = new OrbitControls (camera, renderer.domElement);

var gridXZ = new THREE.GridHelper(100, 10);
gridXZ.setColors( new THREE.Color(0xff0000), new THREE.Color(0xffffff) );
scene.add(gridXZ);

//Load font et creation des ellement
loadFont();

// controls.target.set(30, 0, 0);
controls.update();

const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshBasicMaterial( { color: "blue" } );





camera.position.z = 5;

const animate = function () {
    requestAnimationFrame( animate );



    renderer.render( scene, camera );
};

animate();

function createWord(){
var textColor = 0xffffff;
var ballColor = "#34d9eb";
if(ligthTheme){
    textColor = 0;
    ballColor = "#2c489d"
}
    mainWord = new model.Entiter(" Main Word ","red",font,textColor)
    mainWord.setPostion(0,0,0)
    mainWord.addToScene(scene)

    for(let i =0;i<10;i++){
        let tmp = new model.Entiter(" entiter "+i,ballColor,font,textColor)
        tmp.setPostion(i*5,0,0)
        tmp.addToScene(scene);
        listCube.push(tmp);
    }
}

function loadFont() {

    const loader = new THREE.FontLoader();
    loader.load( 'static/fonts/helvetiker_bold.typeface.json', function ( response ) {

        font = response;

        createWord()

    } );

}

function updateWord(resulta){
    let i = 0;

    let multi = 2;

    let word = resulta.word;
  mainWord.changeText(word,font)

    let listWord = resulta.listWordVect;
    let vectWorld = listWord[word]




    for(let [nom,vecteur] of Object.entries(listWord) ){
        //Pour ne pas affiche 2 fois le nom
        if(nom!=word) {
            let shpere = listCube[i];
            shpere.setPostion((vecteur[0]-vectWorld[0]) * multi, (vecteur[1]-vectWorld[1]) * multi, (vecteur[2]-vectWorld[2]) * multi)
            shpere.changeText(nom, font)
            i++;
        }
    }
}

function appelAjax() {
    var resultat;
    $.ajax({
        url: '/getword',
        data: {
            "word": document.getElementById("textSerch").value
        },
        cache: false,
        type: "get",
        success: function(response) {
            console.log("------")
            console.log(response)
            //cube.material.color.setHex(response)
            resultat = response;
            updateWord(response)

        }
    });
    return resultat;
}

$(function() {
    $('a#test').on('click', function(e) {
        e.preventDefault()
        appelAjax()
        return false;
    });
});


