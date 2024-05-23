//  for loops
for (let i=0;i<5;i++){
   console.log("for loop",i);
}

// while loops
let i=0;
while(i<6){
    if(i%2==0){
        console.log("while loop",i);
    }
    i++;
}


// do while loops

do{
    console.log("do while",i);
    i++;

}while(i<=5);

// for in loops
const person={
    name:'mr. x',
    age:23
}
for(let key in person){
    console.log(key,person[key]);
}


const colors=['blue','green','red']
for (let index in colors){
    console.log(index,colors[index]);
}


// for of loops

for(let color of colors){
    console.log(color)
}
