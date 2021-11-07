// @Author: Daniil Maslov

const baseUrl = 'http://127.0.0.1:5000'

const router = new VueRouter({
    routes:
    [
        {
            path: '/presentationsList'
        }
    ]
})

var app = new Vue({
    router,
    el: '.list',
    data() {
        return {
            presentations: [
                {
                    id: "haha"
                },
                {
                    id: "lol"
                }
            ]
        }
    },
    mounted() {
        axios
            .get(baseUrl+'/presentationsList/')
            .then(response => (
                // хз, принимает ли он такой формат? 0: 1 ; 1: 2 или просто через запятую надо? 1, 2
                this.presentations.id = response.data.presentationId
                
                // попробую собирать изображение уже на месте
                // this.presentation.image = baseUrl+"'/presentationImage/'"+this.presentation.id+"'/mainImage'"
                // console.log(this.presentations.images[0])
                // // this.presentations.ids.forEach(id => {
                // //     this.presentations.images[id] = ("baseUrl+'/presentationImage/'"+this.presentations.ids[id]+"'/mainImage'")
                // // }),
                // // console.log(this.presentations.images)
            ))
    }
})