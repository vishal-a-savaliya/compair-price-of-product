const PORT = process.env.PORT || 8000;
const express = require('express')
const axios = require('axios')
const cheerio = require('cheerio')
const app = express()




app.get('/', (req, res) => {
    res.json('Welcome to my compair')
})


app.get('/search/:q', (req, res) => {


    const query = req.params.q;

    query.replaceAll(" ", '-');

    const url = "https://www.google.com/search?q=" + query;

    console.log(url);

    setTimeout(() => {
        axios.get(url)
            .then(response => {
                const html = response.data
                const $ = cheerio.load(html)

                // console.log(html);

                const sites = []
                const products = [];

                // console.log();


                $("h3", html).each(function () {

                    const title = $(this).text()

                    const site = title.split("-");

                    sitename = site[1];

                    sites.push({
                        sitename
                    })
                })





                sites.forEach(site => {
                    switch (site) {
                        case 'Amazon.in':

                            url = "https://www.amazon.in/s?k=mi+band+6";
                            axios.get(url)
                                .then(res => {
                                    const $ = cheerio.load(res.data);

                                    $(".a-section").each(function () {
                                        const div = $(this).children();
                                        console.log(div);
                                    })

                                })

                            break;
                        case 'Flipkart.com':

                            break;
                        case 'Tata CLiQ':

                            break;
                        // case Amazon.in:

                        //     break;
                        // case Amazon.in:

                        // break;

                        default:
                            break;
                    }



                })

                res.json({ sites, products });

            }).catch(err => console.log(err))
    }, 3000);


})



app.listen(PORT, () => console.log(`server running on PORT ${PORT}`))


















