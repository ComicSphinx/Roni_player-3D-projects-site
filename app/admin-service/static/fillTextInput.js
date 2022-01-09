// @Author: Daniil Maslov (ComicSphinx)
var inputTitle = document.getElementById('inputTitle');
var inputDescription = document.getElementById('inputDescription');
var title = document.getElementsByTagName('h1');
var description = document.getElementsByTagName('p');

title[0].addEventListener('input', (event) => {
    inputTitle.setAttribute('value', title[0].textContent);
});

description[0].addEventListener('input', (event) => {
    inputDescription.setAttribute('value', description[0].textContent);
});