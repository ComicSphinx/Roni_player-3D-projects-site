// @Author: Daniil Maslov (ComicSphinx)

const router = new VueRouter({
    routes: 
    [
        {
            // Тут еще можно связать с темплейтами (позволяет переиспользовать компонент в любом месте)
            path: '/presentation/:id',
            props: true,
            required: true
        }
    ]
})

var app = new Vue({
    router,
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
            .get('http://127.0.0.1:5000/presentation'+this.$route.path)
            .then(response => (
                this.description = response.data.description,
                this.presentationTitle = response.data.presentationTitle,
                this.title = response.data.title
                ))
    }
});