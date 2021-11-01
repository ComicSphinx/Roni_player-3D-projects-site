// @Author: Daniil Maslov (ComicSphinx)

var app = new Vue({
    el: '.grid',
    data() {
        return {
            presentationTitle: null,
            description: null,
            title: null
        };
    },
    mounted() {
        axios
            .get('http://127.0.0.1:5000/presentation/1')
            .then(response => (
                this.description = response.data.description,
                this.presentationTitle = response.data.presentationTitle,
                this.title = response.data.title
                ))
    }
});