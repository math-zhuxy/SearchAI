import re
import requests
import bs4
import set
def get_search_result(query: str) -> str:
    if len(set.web_search_cookie) <= 5:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4051.0 Safari/537.36 Edg/82.0.425.0'
        }
    else:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4051.0 Safari/537.36 Edg/82.0.425.0',
            'Cookie': set.web_search_cookie
        }
    baseUrl=f'https://cn.bing.com/search?q={query}'
    response = requests.get(baseUrl, headers=headers)
    if response.status_code != 200:
        print("There is a network problem")
        return "网络有问题"
    
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    ol_b_results = soup.find('ol', attrs={'id': 'b_results'})
    final_result: str  = ""
    if ol_b_results:
        # print(ol_b_results)
        p_tags = ol_b_results.find_all('p')
        if p_tags:
            for index, p_content in enumerate(p_tags):
                # final_result[index+1] = p_content.text
                final_result += f"第{index+1}条查询结果：{p_content.text}\n"
        else:
            return "解析网络数据失败"
    else:
        return "解析网络数据失败"
    
    if "Ref A" in final_result and not re.search(r'[\u4e00-\u9fff]', final_result):
        return "被 Bing 的反爬虫机制拦截"

    print("Get and parse bing data successfully")
    return final_result

