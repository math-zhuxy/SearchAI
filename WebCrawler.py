import re
import requests
import bs4
import typing
def get_search_result(query: str) -> typing.Dict[int, str]:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4051.0 Safari/537.36 Edg/82.0.425.0'
        }
    
    baseUrl=f'http://cn.bing.com/search?q={query}'
    response = requests.post(baseUrl, headers=headers)
    if response.status_code != 200:
        print("There is a network problem")
        return {0: "网络有问题"}
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    ol_b_results = soup.find('ol', attrs={'id': 'b_results'})
    final_result: typing.Dict[int, str]  = {}
    if ol_b_results:
        p_tags = ol_b_results.find_all('p')
        if p_tags:
            for index, p_content in enumerate(p_tags):
                final_result[index+1] = p_content.text
        else:
            print("Failed to parse network data")
            return {0: "解析网络数据失败"}
    else:
        print("Failed to parse network data")
        return {0: "解析网络数据失败"}
    return final_result