from requests import get
from bs4 import BeautifulSoup as bs
from pprint import pprint
from fake_headers import Headers
from fake_user_agent import user_agent

url = "https://browser-info.ru/"
header = Headers().generate()


def main():
    response = get(url=url, headers=header).text
    # pprint(response)
    soup = bs(response, "lxml")
    # pprint(soup.text)
    block = soup.find("div", id="javascript_check")
    # pprint(block)
    find_status_js = block.find_all("span")
    pprint(f"----------{find_status_js[0].text} ------------------- {find_status_js[1].text}.")

if __name__ == "__main__":
    main()
