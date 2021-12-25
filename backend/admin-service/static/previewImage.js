var fileInput = document.querySelectorAll(".inputImage");

// TODO: надо будет зарефакторить эту функцию  (функция должна делать только одно действие)

// TODO: Если в блоке несколько изображений - оно подгоняет для последней. надо еще это учитывать

function readAndSetImage(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        // определить название класса (строка), из которого вызван input
        try {
            var parentClass = input.closest('.pic').className;
            // получить этот класс
            parentClass = document.getElementsByClassName(parentClass);
        } catch (err) {
            var parentClass = input.closest('.block').className;
            // получить этот класс
            parentClass = document.getElementsByClassName(parentClass);
        }
        
        // определить картинку, в которую будет загружаться изображение
        var image = parentClass[0].querySelector('img');
    
        reader.onload = function (e) {
            image.setAttribute("src", e.target.result);
        }
        
        reader.readAsDataURL(input.files[0]);
    }
}

fileInput.forEach((item) => {
    item.addEventListener('input', (event) => {
        readAndSetImage(item);
    })
});