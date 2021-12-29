// @Author: Daniil Maslov (ComicSphinx)

var images = document.querySelectorAll('img');
images.forEach((item) => {
    item.addEventListener('mouseover', (event) => {
        var parentClass = defineParentClass(item);
        var inputImage = parentClass[0].querySelector('input');
        inputImage.style.visibility = 'visible';
    });

    item.addEventListener('mouseout', (event) => {
        var parentClass = defineParentClass(item);
        var inputImage = parentClass[0].querySelector('input');
        inputImage.style.visibility = 'hidden';
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

function defineParentClass(item) {
    var parentClass;
    
    try {
        parentClass = item.closest('.pic').className;
    } catch (err) {
        parentClass = item.closest('.block').className;
    }
    parentClass = document.getElementsByClassName(parentClass);
    return parentClass;
}