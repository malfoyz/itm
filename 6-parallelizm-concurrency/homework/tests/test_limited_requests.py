import asyncio
import os
from unittest.mock import AsyncMock, MagicMock, patch

import aiohttp
import pytest
import pytest_asyncio
from aiohttp import ClientSession

from homework.limited_requests import fetch_data, make_n_limited_get_requests, write_statuses_to_file


@pytest.fixture
def clearing_files():
    """Удаление созданного файла после тестов"""
    yield
    try:
        os.remove('statuses.txt')
    except FileNotFoundError:
        pass


@pytest.mark.parametrize('statuses, expected_result',
                         [([200, 200, 200], '200\n200\n200\n'),
                          ([400, 200], '400\n200\n'),
                          ([500, 503, 200, 404], '500\n503\n200\n404\n'),
                          ([], '')])
def test_write_statuses_to_file(statuses, expected_result, clearing_files):
    filename = 'statuses.txt'

    write_statuses_to_file(statuses)
    with open(filename, 'r') as file:
        result = file.read()

    assert result == expected_result


@pytest_asyncio.fixture
async def session():
    """Подготовка клиентской сессии."""
    with patch('aiohttp.ClientSession') as mock_session:
        mock_response = MagicMock()
        mock_response.status = 200

        mock_get = AsyncMock()

        # mock_get.__aenter__.return_value = mock_response
        #
        # mock_session.return_value.get.return_value = mock_get

        mock_get.return_value.__aenter__.return_value = mock_response

        mock_session.return_value.get = mock_get

        yield mock_session()


@pytest.mark.asyncio
async def test_fetch_data_success(session: ClientSession):
    url = "http://example.com"
    semaphore = asyncio.Semaphore(10)
    status = await fetch_data(session, url, semaphore=semaphore)

    assert status == 200


@pytest.mark.asyncio
async def test_make_n_limited_get_requests():
    url = 'http://example.com'
    requests_count = 5
    requests_limit = 5
    filename = 'statuses.txt'

    with patch('homework.limited_requests.fetch_data', return_value=200) as mock_fetch_data:
        await make_n_limited_get_requests(url, requests_count, requests_limit)
        assert mock_fetch_data.call_count == requests_count

        with open('statuses.txt', 'r') as file:
            statuses = file.readlines()

        expected_statuses = [str(200) + '\n' for i in range(requests_count)]
        assert statuses == expected_statuses