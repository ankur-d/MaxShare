"""
    Created By: Ankur Dulwani
    Created On: 26th Sep' 2014 9:25 PM
    
"""
import os
import os.path
import csv
from collections import OrderedDict, namedtuple

def get_max_share_price(filePath=None):
    #check if file path is given or not
    if not filePath:
        filePath = raw_input("Please enter the file path\n")
    fileName, fileExtension = os.path.splitext(filePath)
    
    #check for proper file format
    if fileExtension != '.csv':
        print "Incorrect file Format (only CSV)"
        get_max_share_price()
    else:
        
        #check if file exists or not and is readable
        if os.path.isfile(filePath) and os.access(filePath, os.R_OK):
            with open(filePath,'rb') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                company_list = csv_reader.fieldnames[2:]                #get all company
                company_tuple = namedtuple('tup',                       #define named tuple with properties of company 
                                            ['price', 'year', 'month']
                                           )
                dict_data = OrderedDict()
                
                #create dictionary with default values for each company
                for company in company_list:
                    dict_data[company] = company_tuple(0, 'year', 'month')
                
                for row in csv_reader:
                    year, month = row['Year'], row['Month']
                    
                    #get share price for each company in a list
                    company_data = map(int, [row[co] for co in company_list])
                    
                    #check for the price of each company, replace with greater one
                    for company, price in zip(company_list, company_data):
                        if dict_data[company].price < price:
                            dict_data[company] = company_tuple(price, year, month)
                
                print "\nCompany Name \t Max Price \t Year \t Month\n"
                result = "Company Name\tMax Price\tYear\tMonth\n"
                for company in company_list:
                    print "%s \t %.2f \t %s \t %s \n"%(
                                          company, 
                                          dict_data[company].price, 
                                          dict_data[company].year, 
                                          dict_data[company].month)
                    
                    #need result for unit_test file
                    result = result+"%s\t%s\t%s\t%s\n"%(
                                          company, 
                                          dict_data[company].price, 
                                          dict_data[company].year, 
                                          dict_data[company].month)
                return result
        else:
            print "Either file is missing or is not readable"
            get_max_share_price()



if __name__ == "__main__":
    get_max_share_price()