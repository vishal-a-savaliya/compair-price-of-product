const PORT = process.env.PORT || 8000;
const express = require('express')
const axios = require('axios')
const cheerio = require('cheerio')
const app = express()


async function scarper(url){
    const { data } = await axios.get(url);

    const $ = cheerio.load(data);

    $("div .yuRUbf").each(() => {
        const link = $(this).find("a").attr('href');
        console.log(link);
    });
}


app.get('/', (req, res) => {
    res.json('Welcome to my compair')
})


app.get('/search/:q', (req, res) => {


    const query = req.params.q;

    query.replaceAll(" ", '-');

    const url = "https://www.google.com/search?q=" + query;

    console.log(url);


    scarper(url);
    // axios.get(url)
    //     .then(response => {
    //         const html = response.data
    //         const $ = cheerio.load(html)

    //         // console.log(html);

            const sites = []
            const products = [];

    //         // console.log();


    //         $("a", html).each(function () {

    //             // console.log(hii);

    //             // const a = $(this).children().filter('a');

    //             // 

    //             const title = $(this).text()
    //             const url = $(this).attr('href')

    //             console.log(url);

    //             // sitename = site[1];

    //             // sites.push({
    //             //     sitename
    //             // })
    //         })


    

    res.json({ sites, products });

    // }).catch(err => console.log(err))



})



app.listen(PORT, () => console.log(`server running on PORT ${PORT}`))


















