// @Author: Daniil Maslov (ComicSphinx)

const baseUrl = 'http://127.0.0.1:5000'

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
            title: null,
            images: {
                firstImage: '',
                secondImage: '',
                thirdImage: '',
                fourthImage: '',
                fifthImage: '',
                sixthImage: '',
                seventhImage: '',
                eightImage: ''
            }
        };
    },
    // Загрузка данных
    mounted() {
        axios
            .get(baseUrl+'/presentationText'+this.$route.path)
            .then(response => (
                this.description = response.data.description,
                this.presentationTitle = response.data.presentationTitle,
                this.title = response.data.title
                ));
        axios
            .get(baseUrl+'/presentationImages'+this.$route.path)
            .then(response => (
                this.firstImage = response.data,
                this.secondImage = response.data,
                this.thirdImage = response.data,
                this.fourthImage = response.data,
                this.fifthImage = response.data,
                this.sixthImage = response.data,
                this.seventhImage = response.data,
                this.eightImage = response.data
            ));
    }
});