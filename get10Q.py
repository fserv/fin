import json
import sys
from api.sec_api import SEC_API  


def main(ticker_symbol):
    """
    Main function to download the 10-Q filing for a given ticker symbol

    """
    sec_api_client = SEC_API()
    
    # Query the 10-Q filings for the provided ticker symbol
    response = sec_api_client.query(ticker_symbol)
    
    # Convert the response from JSON to a Python dictionary
    response_dict = json.loads(response)
    
    # Check if filings are present
    if response_dict["total"]["value"] > 0:
        # Extract the filing details URL
        filing_url = response_dict["filings"][0]["linkToFilingDetails"]
        
        # Download the filing
        sec_api_client.download(filing_url, file_path=f"./downloaded_data/{ticker_symbol}_10Q.pdf", type="pdf")
        print(f"10-Q filing for {ticker_symbol} downloaded successfully.")
    else:
        print(f"No 10-Q filings found for {ticker_symbol}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get10q.py <ticker_symbol>")
    else:
        main(sys.argv[1])
