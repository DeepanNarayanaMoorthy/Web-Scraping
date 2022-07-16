function sleep(milliseconds) {
	const date = Date.now();
	let currentDate = null;
	do {
		currentDate = Date.now();
	} while (currentDate - date < milliseconds);
}

const express = require('express');
const app = express();

const puppeteer = require('puppeteer-extra')
const StealthPlugin = require('puppeteer-extra-plugin-stealth')

puppeteer.use(StealthPlugin())

const AdblockerPlugin = require('puppeteer-extra-plugin-adblocker')
puppeteer.use(AdblockerPlugin({ blockTrackers: true }))

app.get('/socialblade', (req, res) => {
    let instaid=req.query.instaid ;

	puppeteer.launch({ headless: true }).then(async browser => {
		const page = await browser.newPage()
		await page.setViewport({
			width: 1920,
			height: 1080,
		});
		console.log(`Testing adblocker plugin..`)
		await page.goto('https://socialblade.com/login')
		await page.waitForTimeout(1000)
		await page.type("#admin-login > div:nth-child(2) > input.dashboard-form", 'yyxx0610@gmail.com', { delay: 20 })
		await page.type("#admin-login > div:nth-child(4) > input", 'deepan2000', { delay: 20 })
		await page.click('input[value="LOGIN"]')
		console.log("sleeping")
		// sleep(2000);
		await page.waitForTimeout()
		await page.goto('https://socialblade.com/instagram/user/'+instaid)
		await page.waitForTimeout()
		await page.screenshot({ 'path': '2.png' });
	
		var info1={};
	
		let FOLLOWERS_RANK="#socialblade-user-content > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > p"
		let FOLLOWING_RANK="#socialblade-user-content > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > p"
		let ENGAGEMENT_RANK="#socialblade-user-content > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > p"
		let MEDIA_RANK="#socialblade-user-content > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > p"
		
		await page.waitForSelector(FOLLOWERS_RANK)
		let element = await page.$(FOLLOWERS_RANK)
		FOLLOWERS_RANK = await page.evaluate(el => el.textContent, element)
		info1["FOLLOWERS_RANK"]=String(FOLLOWERS_RANK).replace(/\D/g, "")
	
		await page.waitForSelector(FOLLOWING_RANK)
		element = await page.$(FOLLOWING_RANK)
		FOLLOWING_RANK = await page.evaluate(el => el.textContent, element)
		info1["FOLLOWING_RANK"]=String(FOLLOWING_RANK).replace(/\D/g, "")
	
		await page.waitForSelector(ENGAGEMENT_RANK)
		element = await page.$(ENGAGEMENT_RANK)
		ENGAGEMENT_RANK = await page.evaluate(el => el.textContent, element)
		info1["ENGAGEMENT_RANK"]=String(ENGAGEMENT_RANK).replace(/\D/g, "")
		console.log(ENGAGEMENT_RANK);
	
		await page.waitForSelector(MEDIA_RANK)
		element = await page.$(MEDIA_RANK)
		MEDIA_RANK = await page.evaluate(el => el.textContent, element)
		info1["MEDIA_RANK"]=String(MEDIA_RANK).replace(/\D/g, "")
	
		var linkTexts = await page.$$eval(".YouTubeUserTopInfo",
					elements=> elements.map(item=>String(item.textContent).replace(/\D/g, "")))
	
		let graphs = await page.evaluate(async () => { 
			return await new Promise(resolve => {
				let vall=Highcharts.chartCount
				var dict = {};
				for (let i = 0; i < vall; i++) {
					dict[Highcharts.charts[i].title.textStr] = Highcharts.charts[i].options.series[0].data;
				}
				resolve(dict)
			})
		})
	
	
		// console.log(graphs)
		// console.log(info1)
		// console.log(linkTexts)
		res.json([graphs, info1, linkTexts]);
	
		await browser.close()
	})

})

var server = app.listen(8081, function () {
	var host = server.address().address
	var port = server.address().port
	
	console.log("Example app listening at http://%s:%s", host, port)
 })



