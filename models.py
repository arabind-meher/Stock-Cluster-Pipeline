from dataclasses import dataclass, asdict
from typing import Optional

from pandas import DataFrame


@dataclass
class Stock:
    symbol: Optional[str] = None
    company_name: Optional[str] = None
    market_cap_category: Optional[str] = None
    price: Optional[str] = None
    market_cap: Optional[str] = None
    revenue_ttm: Optional[str] = None
    net_income_ttm: Optional[str] = None
    shares_out: Optional[str] = None
    eps_ttm: Optional[str] = None
    pe_ratio: Optional[str] = None
    forward_pe: Optional[str] = None
    dividend: Optional[str] = None
    ex_dividend_date: Optional[str] = None
    volume: Optional[str] = None
    open: Optional[str] = None
    previous_close: Optional[str] = None
    days_range: Optional[str] = None
    fifty_two_week_range: Optional[str] = None
    beta: Optional[str] = None
    analysts: Optional[str] = None
    price_target: Optional[str] = None
    earnings_date: Optional[str] = None
    industry: Optional[str] = None
    sector: Optional[str] = None
    ipo_date: Optional[str] = None
    stock_exchange: Optional[str] = None

    def __getitem__(self, key):
        return asdict(self).get(key, None)

    def __setitem__(self, key, value):
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            raise KeyError(f"'{key}' is not a valid attribute of Stock")

    def to_dataframe(self):
        return DataFrame([asdict(self)])

    def to_dict(self):
        return asdict(self)
