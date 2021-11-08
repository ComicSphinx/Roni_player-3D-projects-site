// @Author: Daniil Maslov (ComicSphinx)

const baseUrl = 'http://127.0.0.1:5000'
const presentationPage = 'presentation.html#/'

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
            ]
        }
    },
    mounted() {
        axios
            .get(baseUrl+'/presentationsList/')
            .then(response => (
                response.data.presentationIds.forEach(element => {
                    page = presentationPage + response.data.presentationIds[element-1],
                    image = baseUrl + "/presentationImage/" + response.data.presentationIds[element-1] + "/mainImage"
                    
                    this.presentations.push({
                        page, 
                        image
                    })
                })
            ))
    }
})