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
                firstImage:     baseUrl+'/presentationImages'+this.$route.path+'/first_image',
                secondImage:    baseUrl+'/presentationImages'+this.$route.path+'/second_image',
                thirdImage:     baseUrl+'/presentationImages'+this.$route.path+'/third_image',
                fourthImage:    baseUrl+'/presentationImages'+this.$route.path+'/fourth_image',
                fifthImage:     baseUrl+'/presentationImages'+this.$route.path+'/fifth_image',
                sixthImage:     baseUrl+'/presentationImages'+this.$route.path+'/sixth_image',
                seventhImage:   baseUrl+'/presentationImages'+this.$route.path+'/seventh_image',
                eightImage:     baseUrl+'/presentationImages'+this.$route.path+'/eight_image'
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
    }
});