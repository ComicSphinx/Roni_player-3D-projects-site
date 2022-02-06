// @Author: Daniil Maslov (ComicSphinx)

var fileInput = document.querySelectorAll(".inputImage");

function getParentClassOfInput(input) {
    // Определить название класса (строка), в котором лежит input (.pic или .block)
    var parentClass;
    try {
        parentClass = input.closest('.pic').className;
    } catch (err) {
        parentClass = input.closest('.block').className;
    }
    // Получить класс, как объект и вернуть его
    parentClass = document.getElementsByClassName(parentClass);
    return parentClass;
}

function setClassImage(image, input) {
    var file = input.files[0]
    var reader = new FileReader();

    // Задать изображение
    reader.onloadend = function () {
        image.setAttribute("src", reader.result);
    }

    // Если файл успешно получен
    if (file) {
        reader.readAsDataURL(file);
    }
}

fileInput.forEach((input) => {
    input.addEventListener('input', (event) => {
        // Определить картинку, в которую будет загружаться изображение
        var parentClass = getParentClassOfInput(input);
        var image = parentClass[0].querySelector('img');
        
        // Задать изображение этой картинке
        setClassImage(image, input);
    })
});