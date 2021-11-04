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
                firstImage:     baseUrl+'/presentationImage'+this.$route.path+'/firstImage',
                secondImage:    baseUrl+'/presentationImage'+this.$route.path+'/secondImage',
                thirdImage:     baseUrl+'/presentationImage'+this.$route.path+'/thirdImage',
                fourthImage:    baseUrl+'/presentationImage'+this.$route.path+'/fourthImage',
                fifthImage:     baseUrl+'/presentationImage'+this.$route.path+'/fifthImage',
                sixthImage:     baseUrl+'/presentationImage'+this.$route.path+'/sixthImage',
                seventhImage:   baseUrl+'/presentationImage'+this.$route.path+'/seventhImage',
                eightImage:     baseUrl+'/presentationImage'+this.$route.path+'/eightImage'
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