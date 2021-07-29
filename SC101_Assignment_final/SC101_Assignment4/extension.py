"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    d_data = {}
    for year in ['2010s', '2000s', '1990s']:
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        ##################
        response = requests.get(url)
        html_text = response.text
        soup = BeautifulSoup(html_text, features="html.parser")
        targets = soup.find('tbody', {'class':'titleColumn'}) # larget is a list
        male = 0
        female = 0
        count = 0
        for i in targets:
            target = i.td
            male += target[2]
            female += target[4]
            count += 1
            if count > 200:
                break
        d_data[year] = {'male' : male, 'female' : female}
        ##################
    for key, value in d_data.items():
        print("-----------------------------")
        print(key + 's')
        print("Male Number: " + str(value.get('male')))
        print("Female Number: " + str(value.get('female')))


if __name__ == '__main__':
    main()
