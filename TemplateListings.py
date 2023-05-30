from bs4 import BeautifulSoup
import re

class TemplateListings:
    def __init__(self, obj = None) -> None:
        if not obj:
            # declare as many attributes as necessary
            self.attr1 = None
            self.attr2 = None
            self.attr3 = None
        else:
            # extract_nums : useful for parsing money, year, etc.
            def extract_nums(string): # returns -1 if no numbers found
                temp = re.sub("[^0-9]", "", string)
                if temp:
                    return int(temp)
                else:
                    return -1
            
            soup = BeautifulSoup(obj, 'html.parser')
            # self.attr1 = some soup element
            # self.attr2 = some soup element
            # self.attr3 = some soup element

    def __str__(self) -> str:
        return f'{self.attr1}, {self.attr2}, {self.attr3}'

    def to_dict(self) -> dict:
        # make dictionary of all attributes
        return {
            "attribute 1": self.attr1,
            "attribute 2": self.attr2,
            "attribute 3": self.attr3
        }