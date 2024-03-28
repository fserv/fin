from sec_api.index import QueryApi,ExtractorApi
import json 
import os 
import dotenv
import requests

dotenv.load_dotenv()

class SEC_API:
    """
    A class representing the SEC API client.

    Attributes:
        api_key (str): The API key for accessing the SEC API.
        sec_api (QueryApi): An instance of the QueryApi class.

    Methods:
        get_10Q_filings: Retrieves the 10-Q filings for a given ticker symbol.

    """

    def __init__(self):
        """
        Initializes the SEC_API client.

        Retrieves the API key from the environment variables and sets it as the
        API key for the SEC API module.

        """
        self.api_key = os.environ['SEC_API_KEY']
        self.sec_api_query = QueryApi(api_key=self.api_key)
        self.sec_api_extract = ExtractorApi(api_key=self.api_key)
    
    def query(self, ticker_symbol):
        """
        Queries the filings for a given ticker symbol.

        Args:
            ticker_symbol (str): The ticker symbol of the company.
        """
        query = {
            "query": { "query_string": { 
                "query": f'formType:"10-Q" AND ticker:{ticker_symbol}', # only 10-Qs
            }},
            "from": "0", # start returning matches from position null, i.e. the first matching filing 
            "size": "1"  # return just one filing
        }

        response = self.sec_api_query.get_filings(query)

        pretty_response = json.dumps(response, indent=4)  
    
        return pretty_response 
    
    def extract(self, filing_url, item, type='text'):
        """
        Extracts the text content of a specific item from a 10-K, 10-Q or 8-K filing.

        Args:
            filing_url (str): The URL of the filing.
            item (str): The item to be extracted.
                10-K supported item codes: 1, 1A, 1B, 2, 3, 4, 5, 6, 7, 7A, 8, 9, 9A, 9B, 10, 11, 12, 13, 14, 15
                10-Q supported item codes: part1item1, part1item2, part1item3, part1item4, part2item1, part2item1a, part2item2, 
                    part2item3, part2item4, part2item5, part2item6
                8-K supported item codes: 1-1, 1-2, 1-3, 1-4, 1-5, 2-1, 2-2, 2-3, 2-4, 2-5, 2-6, 3-1, 3-2, 3-3, 4-1, 4-2, 5-1, 5-2, 
                    5-3, 5-4, 5-5, 5-6, 5-7, 5-8, 6-1, 6-2, 6-3, 6-4, 6-5, 6-6, 6-10, 7-1, 8-1, 9-1, signature
            type (str, optional): The return type of the item. Can be 'text' or 'html'. Defaults to 'text'.
        """
        extracted_text = self.sec_api_extract.get_section(filing_url, item, type)

        return extracted_text
    
    def download(self, filing_url, file_path = "./downloaded_data/filing.pdf", type="pdf"):
        """
        Downloads the filing document in HTML or PDF format.

        Args:
            filing_url (str): The URL of the filing.
            file_path (str): The path to save the downloaded filing document.
            type (str): The type of the file to download. Can be "html" or "pdf".
        """
        # Define the API endpoint
        url = "https://api.sec-api.io/filing-reader"

        # Define the parameters for the API request
        params = {
            "token": self.api_key,  # Replace with your actual API key
            "type": type,
            "url": filing_url
        }

        # Send a GET request to the API
        response = requests.get(url, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            # Open a file in write-binary mode and save the response content to it
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "wb") as f:
                f.write(response.content)
        else:
            print(f"Request failed with status code {response.status_code}")
    
    def pprint(text, line_length=100):
        """
        Pretty prints the text with a specified line length.

        Args:
            text (str): The text to be pretty printed.
            line_length (int): The maximum length of each line.

        """
        words = text.split(' ')
        lines = []
        current_line = ''
        for word in words:
            if len(current_line + ' ' + word) <= line_length:
                current_line += ' ' + word
            else:
                lines.append(current_line.strip())
                current_line = word
        if current_line:
            lines.append(current_line.strip())
        print('\n'.join(lines))

