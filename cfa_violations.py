"""
Author: Spencer Hitchcock
Date: 24/06/2016

A brief program written in Python to summarize a simple dataset. SUMMARIZEVIOLATIONS calculates the number of violations in each category, and the earliest and latest violation date for each category given this comma-delimited data file representing building code violations: 

http://forever.codeforamerica.org/fellowship-2015-tech-interview/Violations-2012.csv

Usage:
    python cfa_violations.py
"""

import csv
import urllib2

defaultURL = "http://forever.codeforamerica.org/fellowship-2015-tech-interview/Violations-2012.csv"

def summarizeViolations(url=defaultURL):
    # Create a dictionary called RESULTS_DICT in which to store calculated results.
    results_dict = {}

    # Use the URLLIB2 library to parse string from url, store as RESPONSE.
    response = urllib2.urlopen(url)

    # Use the CSV library to parse the string as a .csv, store as CSVFILE.
    csvfile = csv.DictReader(response)

    # For each ENTRY in CSVFILE try find the corresponding entry for its CATEGORY
    # in RESULTS_DICT. 
    for entry in csvfile:
        category = entry['violation_category']
        date = entry['violation_date'] 
        try:
            # Increase current count of violations by 1
            results_dict[category]['count'] += 1

            # Compare this ENTRY's time to the CURRENT_EARLIEST and replace if necessary
            current_earliest = results_dict[category]['earliest']
            results_dict[category]['earliest'] = min(date, current_earliest)

            # Compare this ENTRY's time to the CURRENT_LATEST and replace if necessary
            current_latest = results_dict[category]['latest']
            results_dict[category]['latest'] = max(date, current_latest)

        #If the corresponding entry in RESULTS_DICT does not exist handle
        # the KeyError by creating an entry for that CATEGORY. 
        except KeyError:
            results_dict[category] = {'count':1 , 'earliest': date, 'latest': date}

    # For each CATEGORY in RESULTS_DICT, print number of violations,
    # earliest and latest violation with nice formaating.
    for category in results_dict:
        print(category.center(29))
        for item in results_dict[category]:
            print('{0:8} ==> {1:8}'.format(item,results_dict[category][item]))

summarizeViolations()
