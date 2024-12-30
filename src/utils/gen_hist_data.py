import yfinance as yf
import pandas as pd

#  se va rula o singura data in development pentru a genera datele

tickers = [
    # Technology
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA", "ORCL", "ADBE", "CRM",
    "INTC", "AMD", "CSCO", "TXN", "QCOM", "IBM", "MU", "HPQ", "AVGO", "PYPL",
    "SHOP", "SQ", "SNOW", "NET", "SPOT", "ZM", "PLTR", "ASML", "SAP", "DOCU",

    # Financials
    "JPM", "BAC", "WFC", "C", "GS", "MS", "AXP", "USB", "PNC", "SCHW",
    "BK", "BLK", "TFC", "COF", "SPGI", "ICE", "MET", "AIG", "PRU", "CB",
    "V", "MA", "PAYX", "FIS", "FISV", "ALLY", "CME", "DFS", "MKTX", "NDAQ",

    # Healthcare
    "JNJ", "UNH", "PFE", "ABBV", "LLY", "MRK", "BMY", "TMO", "AMGN", "CVS",
    "DHR", "GILD", "ISRG", "MDT", "SYK", "ZTS", "BIIB", "HUM", "REGN", "CI",
    "VRTX", "RMD", "TDOC", "IQV", "LH", "EW", "GEHC", "HCA", "HOLX", "EXAS",

    # Consumer Discretionary
    "HD", "NKE", "LOW", "AMZN", "MCD", "SBUX", "TGT", "TJX", "DG", "F",
    "GM", "RCL", "CCL", "MAR", "HLT", "YUM", "DPZ", "ROST", "EBAY", "LVS",
    "TSCO", "W", "DASH", "PTON", "ETSY", "BKNG", "CHWY", "WING", "BLDR", "ULTA",

    # Consumer Staples
    "PG", "KO", "PEP", "WMT", "COST", "MO", "PM", "CL", "KMB", "WBA",
    "TAP", "GIS", "SYY", "KR", "MDLZ", "HSY", "CPB", "K", "STZ", "MKC",
    "TSN", "CAG", "BF.B", "LW", "HRL", "POST", "SAM", "UN", "UL", "ADM",

    # Energy
    "XOM", "CVX", "COP", "PSX", "SLB", "HAL", "MPC", "EOG", "OXY", "VLO",
    "HES", "PXD", "KMI", "WMB", "TRGP", "DVN", "FANG", "APA", "CHK", "AR",
    "BKR", "MUR", "CLR", "EQT", "CNQ", "SU", "IMO", "ENB", "TRP", "CVE",

    # Industrials
    "HON", "GE", "UPS", "BA", "RTX", "CAT", "DE", "MMM", "ETN", "ITW",
    "LMT", "NOC", "GD", "WM", "CSX", "NSC", "UNP", "FDX", "EXPD", "UAL",
    "DAL", "ALK", "AAL", "RSG", "WCN", "URI", "PCAR", "TXT", "DOV", "ROK",

    # Utilities
    "NEE", "DUK", "SO", "AEP", "D", "XEL", "SRE", "WEC", "ED", "ES",
    "PEG", "ETR", "PPL", "AWK", "CMS", "EVRG", "AEE", "CNP", "NRG", "FE",
    "EXC", "EIX", "AES", "PGE", "PNW", "NWN", "IDA", "OGE", "DTE", "NI",

    # Real Estate
    "AMT", "PLD", "DLR", "EQIX", "SPG", "PSA", "CCI", "O", "VTR", "WELL",
    "EQR", "AVB", "ARE", "ESS", "HST", "BXP", "IRM", "REG", "KIM", "SLG",
    "WY", "SBAC", "STOR", "NNN", "MAA", "CUBE", "EXR", "PEAK", "INVH", "EPR",

    # Materials
    "LIN", "APD", "SHW", "ECL", "FCX", "NEM", "BLL", "DD", "MLM", "IP",
    "VMC", "ALB", "CF", "LYB", "MOS", "PPG", "AVY", "WRK", "RPM", "CE",
    "ASIX", "CC", "EMN", "HUN", "KRO", "TROX", "WLK", "FMC", "NUE", "STLD",

    # Communication Services
    "GOOGL", "META", "DIS", "NFLX", "VZ", "T", "TMUS", "CMCSA", "CHTR", "EA",
    "TTWO", "FOX", "FOXA", "LYV", "NWS", "NWSA", "SIRI", "DISH", "TDS", "UONEK",

    # ETFs and Index Funds
    "ARKK", "SPY", "VOO", "QQQ", "DIA", "IVV", "XLK", "XLF", "XLY", "XLE"
]


def fetch_historical_data(ticker, period="5y"):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)
        if data.empty:
            print(f"No data found for ticker {ticker}.")
            return pd.DataFrame()
        
        # resetam indexul si adaugam coloana cu ticker-ul
        data.reset_index(inplace=True)
        data["Ticker"] = ticker
        
        # selectam numai coloanele care ne intereseaza
        return data[["Date", "Close", "Volume", "Ticker"]]
    except Exception as e:
        print(f"Error fetching data for ticker {ticker}: {e}")
        return pd.DataFrame()

def generate_historical_dataset(tickers, output_file="data/historical_data.csv", period="5y"):
    all_data = []
    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        data = fetch_historical_data(ticker, period=period)
        if not data.empty:
            all_data.append(data)
    
    # salvam datele in fisierul CSV
    if all_data:
        dataset = pd.concat(all_data, ignore_index=True)
        dataset.to_csv(output_file, index=False)
        print(f"Dataset saved to {output_file}")
    else:
        print("No data fetched. Dataset not created.")

if __name__ == "__main__":
    generate_historical_dataset(tickers, output_file="data/historical_data.csv", period="5y")
