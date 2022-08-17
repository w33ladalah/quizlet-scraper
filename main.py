import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = False
# options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options)
total_pages = 108
with open('./books.csv', 'a', encoding='UTF8') as f:
	# create the csv writer
	writer = csv.writer(f)
	# writer.writerow(['Title', 'Author', '# of Solutions'])

	for i in range(52, total_pages+1):
		print('Page: ' + str(i))
		# driver.implicitly_wait(1)
		driver.get('https://quizlet.com/subjects/arts-and-humanities/history-textbook-solutions?page=' + str(i))

		# if total_pages == 0:
		# 	total_pages = int(driver.find_element(By.CSS_SELECTOR, '.Pagination-paginationText').text.split(' of ')[-1])

		books = driver.find_elements(By.CSS_SELECTOR, value='div.TextbookCard')
		for book in books:
			title = book.find_element(By.CSS_SELECTOR, 'h4 a.AssemblyLink--title span').text
			author = book.find_element(By.CSS_SELECTOR, '.TextbookCard-Details > span:nth-child(3)').text
			try:
				solutions = book.find_element(By.CSS_SELECTOR, 'span.AssemblyPillText').text.strip(' solutions').replace(',', '')
				solutions = 0 if solutions == 'Verified' else solutions
			except:
				solutions = 0
			row = [
				title,
				author,
				solutions
			]

			# write a row to the csv file
			writer.writerow(row)

driver.quit()

# title, authors, and  # of solutions.
