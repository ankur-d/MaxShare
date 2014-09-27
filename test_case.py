"""
    Created By: Ankur Dulwani
    Created At: 27th Sep' 2014 3:42 PM
"""

import unittest
import random
import os
import csv
import MaxShare
from collections import namedtuple

class TestCase(unittest.TestCase):
    
    #creating a input CSV with random values
    def setUp(self):
        self.years = range(random.randint(1990, 2004), random.randint(2005, 2014))
        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 
                       'July', 'August', 'September', 'October', 'November', 'December']
        self.no_companies = random.randint(1, 20)
        self.share_price = range(100, 1000)
        self.no_entries = len(self.years) * 12
        self.headers = ['Year', 'Month']
        self.csv_input = 'unit_test.csv'
        self.dict_data = {}

        # Construct the data of CSV file
        company_tuple = namedtuple('tup', 
                                    ['price', 'year', 'month']
                                   )
        
        #creating a dictionary with default values for a company
        for i in range(self.no_companies):
            self.headers.append('Company %s' % str(i + 1))
            self.dict_data['Company %s' % str(i + 1)] = company_tuple(0, 'year', 'month')
        with open('unit_test.csv', 'wb') as data_file:
            data_writer = csv.writer(data_file, csv.excel)
            data_writer.writerow(self.headers)

            for year in self.years:
                for i in self.months:
                    data_row = [year, i]
                    for j in range(self.no_companies):
                        share_val = random.choice(self.share_price)
                        data_row.append(share_val)
                        #logic to get highest price in a dictionary
                        if self.dict_data['Company %s' % str(j + 1)].price < share_val:
                            self.dict_data['Company %s' % str(j + 1)] = company_tuple(share_val, year, i)
                    data_writer.writerow(data_row)
                year += 1

        #till here we have input CSV created and dict_data which contains the actual output


class ValidateResult(TestCase):
    #Test Output Result for each Company
    def test_results(self):
        ret_val = MaxShare.get_max_share_price(self.csv_input)
        for company_info in ret_val.split('\n')[1:]:
            if company_info:
                company_name, price, year, month = company_info.split('\t')
                #check results from original program with this test case
                self.assertEqual(str(year), str(self.dict_data[company_name].year))
                self.assertEqual(str(month), str(self.dict_data[company_name].month))
                self.assertEqual(str(price), str(self.dict_data[company_name].price))



if __name__ == "__main__":
    unittest.main()