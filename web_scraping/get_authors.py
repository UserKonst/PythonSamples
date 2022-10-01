import requests
import bs4
import lxml

page_num = 1
base_url = 'http://quotes.toscrape.com/page/{}'
has_data_to_srap = True
authors = set()

while has_data_to_srap:
    response = requests.get(base_url.format(page_num))
    soup = bs4.BeautifulSoup(response.text, 'lxml')

    author_tags = soup.select(".author")
    if not author_tags:
        break

    # map(lambda tag: tag.text, author_tags)

    for auth_tag in author_tags:
        authors.add(auth_tag.text)

    print(f'page {page_num}, unique authors found: {len(authors)}')
    page_num += 1

print(f'total unique authors: {len(authors)}')
