from requests import get
from bs4 import BeautifulSoup as bs
from pprint import pprint
from fake_headers import Headers
from fake_user_agent import user_agent

url = "https://browser-info.ru/"
header = Headers().generate()


def main():
    response = get(url=url, headers=header).text
    # soup = bs(response, "lxml")
    # # pprint(soup.text)
    # block = soup.find("div", id="javascript_check")
    # # pprint(block)
    # find_status_js = block.find_all("span")
    # pprint(f"----------{find_status_js[0].text} ------------------- {find_status_js[1].text}.")

    browser_data = {}
    soup = bs(response, "lxml")
    block = soup.find("div", id="tool_padding")
    block_items = block.find_all("div", id)
    # pprint((block_items))
    browser_data[block_items[0].text] = block_items[2].text
    browser_data[block_items[4].text[:10]] = block_items[4].text[-9:]
    browser_data[block_items[5].text[:6]] = block_items[5].text[-8:]
    browser_data[block_items[6].text[:5]] = block_items[6].text[-20:]
    browser_data[block_items[9].text[:10]] = block_items[9].text[12:]
    pprint(browser_data)


if __name__ == "__main__":
    main()
