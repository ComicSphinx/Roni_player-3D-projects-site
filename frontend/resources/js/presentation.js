// @Author: Daniil Maslov (ComicSphinx)

const getTextData = async () => {
    try { // в {id} надо будет динамически подставлять id презентации
        return await axios.get('http://127.0.0.1:5000/presentation')
    } catch (error) {
        console.error(error)
    }
}

const textData = getTextData()


var app = new Vue({
    el: '.grid',
    // потом сделать тут data: data (приравнять к переменной выше)
    data: {
        title: 'Title 1',
        presentationTitle: 'Presentation title',
        description: 'Few words about work another string about<br> work and something else<br>third string about description. Description end.',
        seen: false
    }
});