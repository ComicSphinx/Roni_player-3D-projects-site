var image = document.querySelectorAll("img");
var input = document.getElementsByClassName("chooseImage");

input[0].addEventListener('mouseover', (event) => {
    input[0].style.visibility = "visible";
});

input[0].addEventListener('mouseout', (event) => {
    input[0].style.visibility = "hidden";
})

image.forEach((item) => {
    item.addEventListener('mouseover', (event) => {
        input[0].style.visibility = "visible";
    });
    
    item.addEventListener('mouseout', (event) => {
        input[0].style.visibility = "hidden";
    });
});