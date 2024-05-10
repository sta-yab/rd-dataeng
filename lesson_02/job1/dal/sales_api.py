from typing import List, Dict, Any, Tuple
import requests
import os

API_URL = 'https://fake-api-vycpfa6oca-uc.a.run.app/'
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')


def get_sales(date: str) -> List[Dict[str, Any]]:
    """
    Get data from sales API for specified date.

    :param date: data retrieve the data from
    :return: list of records
    """
    page = 1
    result = []
    while True:
        data, status_code = _get_data_page(date, page)
        print(date, page, status_code)
        if status_code == 200:
            result += data
            page += 1
        elif page == 1 and status_code == 404:
            # no data for specified date
            return []
        elif page > 1 and status_code == 404:
            return result
        elif status_code == 403:
            # forbidden error
            return []


def _get_data_page(date: str, page: int) -> Tuple[Dict[str, Any], int]:
    response = requests.get(
        url=os.path.join(API_URL, 'sales'),
        params={'date': date, 'page': page},
        headers={'Authorization': AUTH_TOKEN},
    )
    return response.json(), response.status_code
