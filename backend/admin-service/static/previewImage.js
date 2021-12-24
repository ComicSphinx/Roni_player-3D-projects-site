var firstImage = document.querySelectorAll("#firstImg");
var fileInput = document.querySelectorAll(".chooseImage");

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            image[0].setAttribute("src", e.target.result);
        }
        
        reader.readAsDataURL(input.files[0]);
    }
}

fileInput.forEach((item) => {
    item.addEventListener('input', (event) => {
        readURL(item);
    })
});

console.log(fileInput[0].getAttribute('class'));