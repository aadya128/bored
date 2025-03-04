const input=document.getElementById("input")

function reversestr(str){
    return str.split("").reverse().join("") 
    
}

function check(){
    const value=input.value
    const reverse=reversestr(value)
    
    if (value===reverse){
        alert("PALINDROME")
    } else{
        alert("NOT PALINDROME")
    }
    input.value=""
}