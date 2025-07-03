
# Stock Cluster Pipeline

This project builds an **automated stock clustering pipeline** by scraping stock data from [stockanalysis.com](https://stockanalysis.com/) using **Selenium**, processing the data, generating features, and clustering stocks into meaningful groups based on financial characteristics.

## Overview
The pipeline automates the **end-to-end process**:
1. **Data Collection**: Scrapes live stock data from stockanalysis.com.
2. **Data Preprocessing**: Cleans and merges scraped data for analysis.
3. **Feature Engineering**: Generates financial features for clustering.
4. **Clustering**: Groups stocks based on performance and volatility characteristics.

## Web Scraping Details
- **Source Website:** [stockanalysis.com](https://stockanalysis.com/)
- **Technology Used:** Selenium with Firefox WebDriver
- **Data Collected:**
  - Stock Overview
  - Historical Price Data
  - Key Financial Metrics (e.g., P/E Ratio, Beta, Market Cap)

## Project Structure
```
├── data
│   ├── cleaned_merged_data.csv
│   ├── cluster_summary_with_5_clusters.csv
│   ├── feature_engineering_data.csv
│   └── merged_data.csv
├── extra
├── raw_data
│   ├── historical_data
│   │   ├── Large-Cap
│   │   ├── Mega-Cap
│   │   ├── Micro-Cap
│   │   ├── Mid-Cap
│   │   ├── Nano-Cap
│   │   └── Small-Cap
│   ├── large_cap_stocks.csv
│   ├── mega_cap_stocks.csv
│   ├── micro_cap_stocks.csv
│   ├── mid_cap_stocks.csv
│   ├── nano_cap_stocks.csv
│   └── small_cap_stocks.csv
├── source
├── utils
├── 01_data.ipynb
├── 02_data_preprocessing.ipynb
├── 03_feature_engineering.ipynb
├── 04_clustering.ipynb
├── logger.py
├── main.py
├── models.py
├── stock.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/arabind-meher/Stock-Cluster-Pipeline.git
cd Stock-Cluster-Pipeline
```

### 2. Set Up Environment
```bash
pip install -r requirements.txt
```

### 3. Start Scraping
```bash
python main.py
```
> This will scrape stock data from the provided Excel file and save it as CSV files.

### 4. Run the Notebooks Sequentially
- `01_data.ipynb` → Validate and explore scraped data.
- `02_data_preprocessing.ipynb` → Clean and structure datasets.
- `03_feature_engineering.ipynb` → Generate clustering features.
- `04_clustering.ipynb` → Perform clustering and visualize results.

## Clustering Summary
The project identifies **five distinct stock clusters** based on:
- Average adjusted close price
- Volatility
- Daily returns
- Trading volume
- Intraday range
- Beta (proxy)

Each cluster reflects unique stock behaviors:
- Growth-oriented stocks
- Stable, large-cap stocks
- High-risk, high-volatility assets
- Underperforming small-cap stocks

## Results

| Cluster | Key Characteristics | Market Cap Distribution |
|---------|---------------------|-------------------------|
| **0**   | Moderately priced, medium volatility, stable returns | Dominated by Large-Cap and Mega-Cap stocks |
| **1**   | Lower-priced, low volatility, strong cumulative returns | Balanced across all market caps |
| **2**   | Unique, high-priced stock with extremely high volatility | Likely a specialized outlier |
| **3**   | Highly volatile, highest daily and cumulative returns | Mostly Mega-Cap stocks |
| **4**   | Low-priced, low-volatility stocks with negative returns | Primarily Small-Cap and Micro-Cap stocks |

The clustering successfully segments stocks into meaningful, behavior-driven groups that can help investors differentiate between stable, growth, and high-risk assets.

## Author
**Arabind Meher**  
[LinkedIn](https://www.linkedin.com/in/arabind-meher) | [GitHub](https://github.com/arabind-meher)