books = {
	'books-to-scrape': {
		'source': 'http://books.toscrape.com/catalogue/page-{}.html',
		'object': {'tag': 'li', 'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'},
		'title': {'tag': 'h3'},
		'integer': {'tag': 'p', 'class': 'price_color'},
		'link': {'tag': 'a', 'attribute': 'src'},
		'image': {'tag': 'img', 'attribute': 'src'},
		'obj_components': ['titles', 'integers', 'links', 'images'],
		'pages_amount': 1
	}
}