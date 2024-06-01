import requests
from translate import Translator


class CommonFunction:
    # 通用函数
    @classmethod
    def chinese_translate(cls, string):
        if string:
            string = string.replace("'", ' ') or string.replace('"', ' ')
        translate_or = Translator(to_lang='chinese')
        translation = translate_or.translate(string)
        return translation

    @classmethod
    def msg(cls, code, msg=None, data=None, **kwargs):
        result = dict()
        result['code'] = int(code) if str(code).isdigit() else 50000
        result['mag'] = kwargs.get('remsg', None) or msg
        if data is not None:
            result['data'] = data
        return result

    @classmethod
    def headers(cls):
        headers = dict()
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 " \
                                "(KHTML, like Gecko) Chrome/96.0.4664.9 Safari/537.36"
        headers['Connection'] = "close"
        return headers

    @classmethod
    def content_image(cls, url):
        img_response = requests.get(url, headers=cls.headers())
        return img_response.content
