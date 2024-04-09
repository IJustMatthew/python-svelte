from bs4 import BeautifulSoup
from selenium import webdriver


def scrape_website(category):
    """Scrape Etsy website for products based on category."""
    data_list = list()

    driver = webdriver.Chrome()
    driver.get("https://www.etsy.com/search?q=" + category + "&ref=pagination&page=1")
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    items = soup.find_all(class_="listing-link")

    # Extract the text content of an element
    for item in items:
        try:
            title = item.find("h3").text.strip()
            image = item.find("img")["src"]
            currency = item.find("span", class_="currency-symbol").text
            price = (
                item.find("p", class_="lc-price")
                .find("span", class_="currency-value")
                .text
            )

            try:
                original_price = (
                    item.find("p", class_="search-collage-promotion-price")
                    .find("span", class_="currency-value")
                    .text
                )
            except AttributeError:
                original_price = ""

            try:
                rating_info = item.find(
                    "div",
                    class_="flex-direction-row-xs",
                ).text
            except AttributeError:
                rating_info = ""

            url = item["href"]
            data_list.append(
                {
                    "title": title,
                    "thumbnail": image,
                    "price": price,
                    "original_price": original_price,
                    "currency": currency,
                    "rating_info": rating_info,
                    "url": url,
                }
            )
        except AttributeError:
            title = None

    return data_list
