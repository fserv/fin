import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.sec_api import SEC_API

class TestSEC_API(unittest.TestCase):
    def setUp(self):
        self.api = SEC_API()

    def test_download(self):
        url = 'https://www.sec.gov/Archives/edgar/data/1018724/000144530513002495/amzn-20130930x10q.htm'
        result = self.api.download(url)
        # Add assertions here based on what you expect the result to be
        # For example, if download returns the content of the file, you might check if result is not empty
        self.assertIsNotNone(result)

    def test_extract(self):
        # Add your test code here
        link = "https://www.sec.gov/Archives/edgar/data/1018724/000144530513002495/amzn-20130930x10q.htm"

        # Use the extract method with the given link
        data = self.api.extract(link, "part1item1")

        print(data)

    def test_query (self):
        # Retrieve the 10-Q filings for a given ticker symbol
        ticker_symbol = 'AMZN'

        filings = self.api.query(ticker_symbol)
        print(filings)     
