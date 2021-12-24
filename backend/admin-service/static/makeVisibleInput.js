// TODO: Если в блоке несколько картинок, оно отображается для самой первой
// TODO: В square блоке инпуты почему-то стоят в отрыве от картинок. Как итог - при переходе на инпут, он пропадает

var images = document.querySelectorAll('img');
images.forEach((item) => {
    item.addEventListener('mouseover', (event) => {
        // определить название класса (строка), из которого вызван input
        try {
            var parentClass = item.closest('.pic').className;
            // Получить этот класс
            parentClass = document.getElementsByClassName(parentClass);
        } catch (err) {
            var parentClass = item.closest('.block').className;
            // Получить этот класс
            parentClass = document.getElementsByClassName(parentClass);
        }

        var inputImage = parentClass[0].querySelector('input');
        inputImage.style.visibility = 'visible';
    });

    item.addEventListener('mouseout', (event) => {
        try {
            // определить название класса (строка), из которого вызван input
            var parentClass = item.closest('.pic').className;
            // Получить этот класс
            parentClass = document.getElementsByClassName(parentClass);
        } catch (err) {
            // определить название класса (строка), из которого вызван input
            var parentClass = item.closest('.block').className;
            // Получить этот класс
            parentClass = document.getElementsByClassName(parentClass);
        }

        var inputImage = parentClass[0].querySelector('input');
        // TODO: УБРАТЬ ЭТУ ХНЮ ИЛИ ДОРАБОТАТЬ, ЧТОБЫ VISIBILITY НЕ ПРОПАДАЛ ПРИ НАВЕДЕНИИ НА ИНПУТ
        setTimeout(function() {inputImage.style.visibility = 'hidden'}, 300);
        
    });
})

var inputs = document.querySelectorAll("input");
inputs.forEach((item) => {
    item.addEventListener('mouseover', (event) => {
        item.style.visibility = 'visible';
    });
    
    item.addEventListener('mouseout', (event) => {
        item.style.visibility = 'hidden';
    });
})