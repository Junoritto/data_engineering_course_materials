from extract import extract
from transform import transform
from load import load
from visualize import visualize_gdp_over_100b, visualize_region_avg_gdp
from utils import log_separator, log_message

def run_etl():
    try:
        log_separator()
        log_message("ETL 프로세스 시작")

        extract()
        transform()
        load()

        visualize_gdp_over_100b()
        visualize_region_avg_gdp()

        log_message("ETL 프로세스 완료")

    except Exception as e:
        log_message(f"ETL 프로세스 실패: {str(e)}")

if __name__ == '__main__':
    run_etl()