import requests
from urllib.parse import urlencode
import re

class News():
    def __init__(self):
        pass

    def weibo_hot(self):
        url = 'https://s.weibo.com/top/summary/'
        headers = {
            'Host':'s.weibo.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
        }

        result = requests.get(url, headers=headers)
        result_dict = dict()
        hot_word_list = re.findall('.*?<td class="td-02">.*?>(.*?)</a>', result.text, re.S)

        for word in hot_word_list:

            data = {
                'q':word,
                'Refer':'top'
            }

            result_url = 'https://s.weibo.com/weibo' + '?' + urlencode(data)
            result_dict[word] = result_url
        return result_dict

