const quotes=[
    "The beautiful thing about learning is that nobody can take it away from you." ,
    "The only person who is educated is the one who has learned how to learn...and change." ,
    "Education is the most powerful weapon which you can use to change the world." ,
    "An investment in knowledge pays the best interest." ,
    "College is what you make it." ,
    "The college years are the best of your life because you have few responsibilities, little money, and much energy.",
    "College is not a time for comfort, it's a time for growth." ,
    "College is a place where you learn less from classes and more from classmates.",
    "College isnt just about the books, its about the people you meet, the experiences you have, and the person you become.",
    "College is not a race, its a journey. Enjoy the ride.",
    "College is a time to find yourself, lose yourself, and find yourself again." ,
    "College is the time to make mistakes, to learn from them, and to grow.",
    "The only way to do great work is to love what you do.",
    "The future belongs to those who believe in the beauty of their dreams." ,
    "It does not matter how slowly you go as long as you do not stop." ,
    "The only thing that overcomes a difficult situation is perseverance.",
    "Your time is limited, so dont waste it living someone elses life." ,
    "The best way to predict the future is to create it." ,
    "The only way to do great work is to love what you do." ,
    "The future belongs to those who believe in the beauty of their dreams.",
]

const usedIndexes = new Set()
const quoteElement=document.getElementById("quote")

function generateQuote() {
    if (usedIndexes.size >= quotes.length) {
        usedIndexes.clear()
    }
    while (true) {
        const randomIdx=Math.floor(Math.random()*quotes.length)
    
        if (usedIndexes.has(randomIdx)) continue

        const quote = quotes[randomIdx]
        quoteElement.innerHTML=quote;
        usedIndexes.add(randomIdx)
        break
    }
    
}