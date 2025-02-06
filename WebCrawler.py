import requests
import bs4
def get_search_result(query: str) -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4051.0 Safari/537.36 Edg/82.0.425.0'
        }
    
    baseUrl=f'https://cn.bing.com/search?q={query}'
    response = requests.get(baseUrl, headers=headers)
    if response.status_code != 200:
        print("There is a network problem")
        return {0: "网络有问题"}
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
    
    # print(final_result)
    print("Get and parse network data successfully")
    return final_result

