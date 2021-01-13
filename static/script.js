console.log("connected")

let correctButtons = document.querySelectorAll('.correct');

for (let button of correctButtons) {
    console.log("clicked")
    button.addEventListener('click', e => e.target.classList.toggle("correct_color"))
    
}


