"""
1. Реализуйте асинхронный метод, который будет отправлять запросы в http://google.com по http
с ограничением не более 10 запросов в единицу времени.

2. Написать асинхронный код, который делает 50 get запросов к https://example.com/ .
Записать все статусы ответов в файл и убедиться, что количество запросов соответствует
заданному количеству. Необходимо учесть, чтобы одновременно выполнялось не больше
10 запросов. Для выполнения запросов использовать библиотеку aiohttp.
Все значения, количество запросов, лимит одновременно выполняемых запросов
и url должны передаваться как параметры.
"""

import asyncio
import aiohttp
import logging

from datetime import datetime
from typing import List, Union


logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s %(message)s')


async def fetch_data(session: aiohttp.ClientSession,
                     url: str,
                     semaphore: asyncio.Semaphore = None,
                     request_id: int = 1) -> Union[int, str]:
    """
    Запрашивает HTTP-ресурс через GET запрос и возвращает статус ответа в числовом формате.

    :param session: HTTP клиент
    :type session: aiohttp.ClientSession
    :param url: адрес запроса
    :type url: str
    :param semaphore: семафор
    :type semaphore: asyncio.Semaphore
    :param request_id: номер запроса, по умолчанию 1
    :type request_id: int

    :return: ответ запроса
    :rtype: Union[int, str]

    :raises aiohttp.ClientError: при ошибке запроса
    :raises asyncio.Timeout.Error: при таймауте запроса
    :raises Exception: при других ошибках
    """
    logging.info(f'Запрос №{request_id} дошел до семафора')
    async with semaphore:
        logging.info(f'Запрос №{request_id} делает запрос')
        await asyncio.sleep(3)                         # имитация длительного запроса

        try:
            async with session.get(url) as response:
                return response.status
        except aiohttp.ClientError as e:
            logging.exception(f'Ошибка при запросе №{request_id}: {e}')
            return f'Ошибка при запросе №{request_id}: {e}'
        except asyncio.TimeoutError:
            logging.exception(f'Таймаут при запросе №{request_id}')
            return f'Таймаут при запросе №{request_id}'
        except Exception as e:
            logging.exception(f'Неизвестная ошибка при запросе №{request_id}: {e}')
            return f'Неизвестная ошибка при запросе №{request_id}: {e}.'


def write_statuses_to_file(statuses: List[int]) -> None:
    """
    Записывает статусы ответов в файл.

    :param statuses: список статусов ответа
    :type statuses: List[str]

    :return: None
    :rtype: None
    """
    with open('statuses.txt', 'w') as file:
        file.writelines([str(status) + '\n' for status in statuses])


async def make_n_limited_get_requests(url: str, requests_count: int, requests_limit: int) -> None:
    """
    Делает множество GET-запросов с лимитом одновременно выполняемых запросов и записывает статусы ответов в файл.

    :param url: адрес запроса
    :type url: str
    :param requests_count: число запросов
    :type requests_count: int
    :param requests_limit: лимит одновременно выполняемых запросов
    :type requests_limit: int

    :return: None
    :rtype: None
    """
    async with aiohttp.ClientSession() as session:
        semaphore = asyncio.Semaphore(requests_limit)
        tasks = [asyncio.create_task(fetch_data(session, url, semaphore, i)) for i in range(1, requests_count + 1)]

        results = await asyncio.gather(*tasks)
        write_statuses_to_file(results)


if __name__ == '__main__':
    url = 'http://example.com'
    requests_count = 50
    requests_limit = 10
    asyncio.run(make_n_limited_get_requests(url, requests_count, requests_limit))