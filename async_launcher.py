"""
This testual module adheres the asynchronous conception.
There are three functions which do a whole
process of asynchronous web scraping.

"""
import asyncio
import aiohttp
from data_miner import DataFetcher as Df
from scraping_info import books


async def get_page(session, url):
	"""
	This function fetches the response data from the current page.
	"""
	async with session.get(url) as response:
		return await response.text()


async def collect_tasks_from_each_page(session):
	"""
	This function goes through each page and collects tasks to
	be performed asynchronously.
	"""

	# define a task bag
	tasks = []

	# define a number of pages to be processed
	num_of_pages = books['books-to-scrape']['pages_amount']

	# wade through the urls list
	for i in range(0, num_of_pages):
		# get the task
		n = i + 1
		url = books['books-to-scrape']['source'].format(n)
		task = asyncio.create_task(get_page(session, url))
		tasks.append(task)
	# gather all the tasks in one object corountine
	result = await asyncio.gather(*tasks)

	return result


async def main():
	"""
	This function performs these two above,
	giving a session object and initializing the web data.
	Returns a bunch of materials based on requests and enclosed
	as tasks to be performed asynchronously
	"""
	async with aiohttp.ClientSession() as session:
		# gather a list of responses
		data = await collect_tasks_from_each_page(session)

		return data


if __name__ == '__main__':

	# get the responses as tasks
	results = asyncio.run(main())

	# scrape the data in each task
	scraper = Df(results, 'books-to-scrape', books)

	content = scraper.fetch_content()

	books_list = scraper.structure_data(content)

	for book in books_list:
		for key, value in book.items():
			print(key + ':::' + str(value))
	else:
		print('\n\n')