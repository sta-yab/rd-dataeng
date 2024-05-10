from dal.local_disk import save_to_disk
from dal.sales_api import get_sales


def save_sales_to_local_disk(date: str, raw_dir: str) -> None:
    # 1. get data from the API
    # 2. save data to disk
    data = get_sales(date)
    save_to_disk(data, raw_dir)
