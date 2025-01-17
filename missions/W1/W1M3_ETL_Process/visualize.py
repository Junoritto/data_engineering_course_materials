import pandas as pd
import sqlite3
from utils import log_message
from tabulate import tabulate

DB_FILE = 'sqliteDB/World_Economies.db'
PLOT_PATH = 'results/plots/'

def visualize_gdp_over_100b():
    query = """
    SELECT Country, GDP_USD_billion, Year
    FROM Countries_by_GDP
    WHERE GDP_USD_billion >= 100
    ORDER BY GDP_USD_billion DESC;
    """
    
    with sqlite3.connect(DB_FILE) as conn:
        df = pd.read_sql(query, conn)
    
    df.index = range(1, len(df) + 1)
    # 콘솔에 표 출력
    print("\n🌍 GDP 100B USD 이상 국가 목록:")
    print(tabulate(df, headers='keys', tablefmt='grid'))
    
    log_message("GDP 100B USD 이상 국가 데이터를 콘솔에 출력 완료.")


def visualize_region_avg_gdp():
    query = """
    SELECT Region, ROUND(AVG(GDP_USD_billion), 2) AS Avg_GDP
    FROM (
        SELECT Country, Region, GDP_USD_billion,
               ROW_NUMBER() OVER (PARTITION BY Region ORDER BY GDP_USD_billion DESC) AS rank
        FROM Countries_by_GDP
    )
    WHERE rank <= 5
    GROUP BY Region
    ORDER BY Avg_GDP DESC;
    """
    
    with sqlite3.connect(DB_FILE) as conn:
        df = pd.read_sql(query, conn)

    df.index = range(1, len(df) + 1)
    # 콘솔에 표 출력
    print("\n📊 Region별 상위 5개 국가의 GDP 평균:")
    print(tabulate(df, headers='keys', tablefmt='grid'))
    
    log_message("Region별 상위 5개 국가의 평균 GDP 데이터를 콘솔에 출력 완료.")


if __name__ == '__main__':
    visualize_gdp_over_100b()
    visualize_region_avg_gdp()