from lesson_02.job1.dal.local_disk import save_to_disk
from lesson_02.job1.dal.sales_api import get_sales


def save_sales_to_local_disk(date: str, raw_dir: str) -> None:
    # 1. get data from the API
    data = get_sales(date)
    # 2. save data to disk
    save_to_disk(data, raw_dir)
