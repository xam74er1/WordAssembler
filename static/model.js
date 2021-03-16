import * as THREE from 'https://unpkg.com/three/build/three.module.js';

const multi = 1;
export class Entiter{
    constructor(nom,couleur,font) {
        this.nom=nom;
        this.couleur=couleur;

        this.sphereGeo = new THREE.SphereGeometry( 1*multi, 32, 32 );
        this.sphereMat = new THREE.MeshBasicMaterial( {color: this.couleur} );
        this.sphere = new THREE.Mesh(this.sphereGeo, this.sphereMat);

        const loader = new THREE.FontLoader();

        this.textGeo = new THREE.TextGeometry( this.nom, {
            font: font,
            size: 0.5*multi,
            height: 0.01*multi,
            curveSegments: 8,

        } );

        var textMaterial = new THREE.MeshBasicMaterial( {color: 0xffffff} );


        this.text = new THREE.Mesh( this.textGeo, textMaterial );


    }

    setPostion(x,y,z){
        this.sphere.position.set(x,y,z);

        if(this.text!=null){
            this.textGeo.computeBoundingBox();
             var textWidth = this.textGeo.boundingBox.max.x - this.textGeo.boundingBox.min.x;
            this.text.position.set( x-0.5*textWidth , y+(1.5*multi) , z );
        }

    }

    addToScene(scene){
        scene.add( this.sphere);
        if(this.text!=null){
            scene.add(this.text);
        }

    }
    changeText(text,font){

                this.textGeo = new THREE.TextGeometry( text, {
            font: font,
            size: 0.5*multi,
            height: 0.01*multi,
            curveSegments: 8,

        } );
this.text.geometry = this.textGeo;
        console.log(this.text)

    }
    generate(){
        return this.sphere;
    }

}

