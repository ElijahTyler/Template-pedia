# Template-pedia

a Python-based web scraper / compiler framework for Windows and Linux

## Installation

0. Ensure you have Firefox installed to the default location
1. Download and extract the .zip at <https://github.com/ElijahTyler/Template-pedia.git>
2. Open Terminal in the project directory and type `python -m pip install -r requirements.txt`

## Setup

1. main.py : Anywhere you see the word "template" is where you add your own URL, class name, variable name etc.
2. TemplateListings.py : You can declare as many attributes as you see fit for whatever data you're scraping. The file comes preloaded with three slots.
3. TemplateData.py : Make sure that your attributes in TemplateListings.py are all accounted for when creating a TemplateData object.

## Usage

IMPORTANT: Open `main.py` and add your personal website search URLs (example is in the file), otherwise nothing will happen once you run the file.

Open Terminal in the project directory and type `python main.py`. This will open an automated Firefox window that will scrape your given webpage for all listings of your chosen element. Then, a TemplateListing object is created for each listing it finds. Lastly, `listings.json` will be created, a dictionary of all listings found.

TemplateData.py is used to create a .csv file with all of your listings. To do so, open Python in your terminal with `/bin/python3` and run the following commands:

```python
from TemplateData import TemplateData
t = TemplateData('listings.json')
t.generate_csv()
```

This, by default, will generate a .csv file named `TemplateData.csv`. You can pass in whatever name you like to generate_csv().
