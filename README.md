Financial-GPT
by JaguarDB

HOW TO USE :

-Get SEC-API key off sec-api and put it into .env variable :
https://sec-api.io/
-Download requirements.txt in a conda env or whatever you choose 


Run:
python3 get10Q.py (TICKER_SYMBOL) to retreive 10-Q of that ticker symbol 


to understand more of SEC_API, look at methods of the api/sec_api.py 

Returned_data is the returned values of those methods, such as query and extract. 

-the main python3 get10Q.py uses the query and download to check if a ticker exists and then downloads the 10-Q filings of that ticker. 





