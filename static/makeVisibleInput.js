// @Author: Daniil Maslov (ComicSphinx)

var images = document.querySelectorAll('img');
images.forEach((item) => {
    item.addEventListener('mouseover', (event) => {
        inputImage = defineInputImageByParentClass(item);
        inputImage.style.visibility = 'visible';
    });

    item.addEventListener('mouseout', (event) => {
        inputImage = defineInputImageByParentClass(item);
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

function defineInputImageByParentClass(item) {
    var parentClass;
    var inputImage;
    
    try {
        parentClass = item.closest('.pic').className;
    } catch (err) {
        parentClass = item.closest('.block').className;
    }
    parentClass = document.getElementsByClassName(parentClass);
    inputImage = parentClass[0].querySelector('input');

    return inputImage;
}