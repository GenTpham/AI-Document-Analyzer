import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"Lỗi khi truy cập URL: {e}"

    soup = BeautifulSoup(response.text, 'html.parser')

    for tag in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
        tag.decompose()

    text = soup.get_text(separator=" ")
    lines = [line.strip() for line in text.splitlines()]
    text_cleaned =" ".join([line for line in lines if line])

    return text_cleaned