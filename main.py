import requests
import json


def make_response_file(response, method):
    with open('response_' + method + '.txt', 'w', encoding='utf-8') as file:
        file.write(f'Код ответа сервера: {response.status_code}\n\n')
        dictionary = dict(response.headers)
        content_length = int(dictionary['Content-Length'])
        file.write(f'Заголовки ответа:\n{json.dumps(dictionary, indent=4)}')
        if content_length != 0:
            file.write(f'\n\nТело ответа:\n{response.text}')


make_response_file(requests.options('https://httpbin.org/'), 'options')
make_response_file(requests.get('https://httpbin.org/'), 'get')
make_response_file(requests.post('https://httpbin.org/'), 'post')
