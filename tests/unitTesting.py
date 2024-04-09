import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.sec_api import SEC_API

class TestSEC_API(unittest.TestCase):
    def setUp(self):
        self.api = SEC_API()
    

    """
    Test the download method of the SEC_API class.

    The download method should download the filing document in PDF Format.
    -This method should return something called filing.pdf, the link currently links to Amazon 10-Q filing.
    """
    def test_download(self):
        url = 'https://www.sec.gov/Archives/edgar/data/1018724/000144530513002495/amzn-20130930x10q.htm'
        result = self.api.download(url)
        # Add assertions here based on what you expect the result to be
        # For example, if download returns the content of the file, you might check if result is not empty
        
        print("RESULT: " , result)
        self.assertIsNotNone(result)



    """
    Test the extract method of the SEC_API class.

    The extract method should extract the text of a specific item from the filing document.
    -This method should return the text of a specific item from the filing document.

    -look into extracted.txt in returnedData for the expected output
    
    """
    def test_extract(self):
        # Add your test code here
        link = "https://www.sec.gov/Archives/edgar/data/1018724/000144530513002495/amzn-20130930x10q.htm"

        # Use the extract method with the given link
        data = self.api.extract(link, "part1item1")
        print("data: " , data)



    """
    Test the query method of the SEC_API class.

    The query method should query for a given ticker symbol given a ticker

    -Look into query.txt for expected output 
    
    """

    def test_query (self):
        # Retrieve the 10-Q filings for a given ticker symbol
        ticker_symbol = 'AMZN'

        filings = self.api.query(ticker_symbol)
        print("filings", filings)     
