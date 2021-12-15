const paragrafos = document.querySelectorAl1("p");

let contador1 = 1;
let contador2 = 1;
let contador3 = 1;

function uma_funcao_qualquer() {
    contador2 = contador2 * 2;
    paragrafos[1] .innerText = contador2;
}

paragrafos[0].onclick = function () {
    contador1++;
    paragrafos[0].innerText = contador1;
}


paragrafos[1].onmouseover = uma_funcao_qualquer;

paragrafos[2].addEventListener("click", function(){
    contador3--;
    paragrafos[2].innerText = contador3;
});

















// const div = document.querySelector("div.b");
// let par1 = document.createElement("p");
// let par2 = document.createElement("p");

// par1.innerText = "Paragrafo 1";
// par2.innerText = "Paragrafo 2";

// div.appendChild(par2);
// div.appendChild(par1);













// const a = document.getElementById("div").innerText = "Teste de div";



// function classifica_bicho(animal) {

//     let classificacao;

//     switch(animal) {

//         case "cachorro":
//         case "gato":
//         case "hamster":
//         case "vaca":
//             classificacao = "mamifero";
//             break;
//         case "avestruz":
//         case "galinha":
//         case "papagaio":
//         case "pato":
//             classificacao = "ave";
//             break;
//         case "cobra":
//         case "crocodilo":
//         case "sapo":
//             classificacao = "reptil";
//             break;
//             default:
//             classificacao = "desconhecido";    
//     }

//     return classificacao;

// }

// let bichos = ["arara", "hamster", "pato", "cachorro", "cobra", "jacaré"];
// let i = 0

// while (i < bichos.length) {
//     console.log(classifica_bicho(bichos[i]));
//     i++;
// }






// function funcao(vetor, x) {
//     let i = 0;
//     for (i = 0; i < vetor.length && vetor[i] != x; i = i + 1){}
//     if (i < vetor.length) {
//         return true;
//     } else {
//         return false;
//     }
// }

// let pessoas = ["Ana", "Betriz", "Carlos", "Daniel", "Eduardo"];
// let a = funcao(pessoas, "Ana");
// let b = funcao(pessoas, "João");
// let c = funcao(pessoas, "Eduardo");
// let d = funcao(pessoas, "Fabiana");

// console.log(a);
// console.log(b);
// console.log(c);
// console.log(d);




// let x = [11, 12, 20, 25, 27, 30];
// let y = [];
// let qtd = 0;

// for (let i = 0; i < x.length; i++) {
//     if (x[i] % 2 == 0) {
//         qtd++;
//         y.push(x[i]);
//     }
// }

// document.write(y);
// document.write("<br>");
// document.write(qtd);

// console.log(y);
// console.log(qtd);


// const x = document.getElementsByTagName("div");
// let i;
// for (i = 1; i < x.length - 1; i++) {
//     x[i].style.backgroundColor = "blue";
// }







    