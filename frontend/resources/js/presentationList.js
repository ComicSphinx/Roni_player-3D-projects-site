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
                    page: null,
                    image: null
                }
                // {
                //     page: "presentation.html#/1",
                //     image: baseUrl+"/presentationImage/1"+"/mainImage"
                // },
                // {
                //     page: "presentation.html#/2",
                //     image: baseUrl+"/presentationImage/2"+"/mainImage"
                // }
            ]
        }
    },
    mounted() {
        axios
            .get(baseUrl+'/presentationsList/')
            .then(response => (
                // TODO: На первой итерации в page, image подается id - 2, на второй - undefined (хотя, по console.log в 42 стр видно, что идет 1, затем 2)

                response.data.presentationIds.forEach(element => {
                    console.log(element),
                    page = response.data.presentationIds[element],
                    image = baseUrl+"/presentationImage/"+response.data.presentationIds[element]+"/mainImage"
                    
                    this.presentations.push({
                        page, 
                        image
                    })
                })
            ))
    }
    // mounted() {
    //     axios
    //         .get(baseUrl+'/presentationsList/')
    //         .then(response => (
    //             // хз, принимает ли он такой формат? 0: 1 ; 1: 2 или просто через запятую надо? 1, 2
    //             // this.presentations.page += response.data.presentationId
    //             // this.presentations.page += 1
                
    //             // попробую собирать изображение уже на месте
    //             // this.presentation.image = baseUrl+"'/presentationImage/'"+this.presentation.id+"'/mainImage'"
    //             // console.log(this.presentations.images[0])
    //             // // this.presentations.ids.forEach(id => {
    //             // //     this.presentations.images[id] = ("baseUrl+'/presentationImage/'"+this.presentations.ids[id]+"'/mainImage'")
    //             // // }),
    //             // // console.log(this.presentations.images)
    //         ))
    // }
})