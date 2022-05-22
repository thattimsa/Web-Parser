# ვაიმპორტებ საჭირო მოდულებს
import requests
from bs4 import BeautifulSoup
import csv


# აქ შემოვიღე კონსტანტები
URL = 'https://xiaomi.com.ge/product-category/smart-device/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36', 'accept': '*/*'}
FILE = 'products.csv'

# ლინკის დასამუშავებელი ფუნქცია
def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

# ფუნქცია, რომელიც ითვლის გვერდებს
def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('a', class_='page-numbers')
    if pagination:
        return int(pagination[-2].get_text())  # აქ მივუთითე '-2', რადგან ლინკში გვერდის ნომერი ბოლოდან მეორე სიმბოლოა
    else:
        return 1 # იმ შემთხვევებისთვის, თუ სულ ერთი გვერდი იქნება

# მონაცემების მიმღები ფუნქცია
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='product-wrapper')

    products = []
    for item in items:
        products.append({
            'title': item.find('h3', class_='product-title').get_text(strip=True),
            'price': item.find('span', class_='price').get_text(strip=True)
        })
    return products

# მონაცემთა CSV-ში შემნახავი ფუნქცია
def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['დასახელება', 'ფასი'])
        for item in items:
            writer.writerow([item['title'], item['price']])

# მთავარი ფუნქცია, სადაც ვიძახებთ დამხმარე ფუნქციებს
def parse():
    html = get_html(URL)
    if html.status_code == 200:
        items = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f'მიმდინარეობს გვერდის პარსინგი - გვერდი {page}/{pages_count}...')
            html = get_html(URL, params={'page': page})
            items.extend(get_content(html.text))
        save_file(items, FILE)
        print(f'^^^ მიღებულია {len(items)} პროდუქტი ^^^')
        print(f'^^^ ფაილი შეიქმნა და მიღებული ინფორმაცია შენახულია ^^^')
    else:
        print('შეცდომა: კავშირი სერვერთან ვერ დამყარდა')

parse()