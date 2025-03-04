const body = document.getElementsByTagName("body")[0]

function setcolor(name){
    body.style.backgroundColor=name;
}

function randomcolor() {
    const red=Math.round(math.random()*255)
    const green=Math.round(math.random()*255)
    const blue=Math.round(math.random()*255)

    const color=`rgb(${red}, ${green}, ${blue})`
    body.style.backgroundColor=color;
}