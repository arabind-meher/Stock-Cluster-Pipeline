import os

import pandas as pd

from stock import StockScraper


def get_stock_data_excel(path: str, sheet: str):
    modify_str = lambda x: x.strip().lower().replace(" ", "_")

    stock_df = pd.read_excel(path, sheet_name=sheet).sample(5)
    stock_df.columns = list(map(modify_str, stock_df.columns))
    stock_df["market_cap_category"] = sheet.strip()

    return stock_df["links"].tolist(), stock_df[
        ["symbol", "company_name", "market_cap_category"]
    ].to_dict(orient="records")


if __name__ == "__main__":
    file = "stock_urls.xlsx"
    path = os.path.join("source", file)
    sheet_name = "Mega Cap"
    urls, meta = get_stock_data_excel(path, sheet_name)

    directory = "data"

    stock_scraper = StockScraper(directory)
    stock_scraper.initialize_driver()
    stock_scraper.scrape_urls(urls, meta, file=str(sheet_name + ".csv"))

    stock_scraper.close()

# stock_scraper.scrape_url(
#         "https://stockanalysis.com/stocks/aapl/",
#         meta={
#             "symbol": "AAPL",
#             "company_name": "Apple Inc.",
#             "market_cap_category": "Mega Cap",
#         },
#     )
