// @Author: Daniil Maslov (ComicSphinx)
var inputTitle = document.getElementById('inputTitle');
var inputDescription = document.getElementById('inputDescription');
var h1Title = document.getElementsByTagName('h1');
var pDescription = document.getElementsByTagName('p');

h1Title[0].addEventListener('input', (event) => {
    inputTitle.setAttribute('value', h1Title[0].textContent);
});

pDescription[0].addEventListener('input', (event) => {
    inputDescription.setAttribute('value', pDescription[0].textContent);
});