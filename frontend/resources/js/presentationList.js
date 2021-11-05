// @Author: Daniil Maslov

const baseUrl = 'http://127.0.0.1:5000'

const router = new VueRouter({
    routes:
    [
        {
            path: '/presentationsList/'
        }
    ]
})

var app = new Vue({
    router,
    el: '.grid',
    data() {
        return {
            count: null,
            presentations: [
                {
                    ids: [],
                    images: []
                }
            ]
        }
    },
    mounted() {
        axios
            .get(baseUrl+'/presentationsList')
            .then(response => (
                // response.data. что дальше? узнать из ответа и надо будет как-то цикл сделать или тип того,
                // чтобы туда все id попали
                this.presentations.ids.push(response.data),
                // count тоже надо будет корректно заполниь
                this.count = response.count
            )),

            this.presentations.images.forEach(image => {
                this.presentation.ids.forEach(id => {
                    this.presentations.images.push(baseUrl+'/presentationImage/'+id+'mainImage')
                });
            });
    }
})