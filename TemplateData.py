import json
import csv

class TemplateData:
    def __init__(self, jason = None) -> None:
        # takes in a .json file generated from dictionary of TemplateListings
        self.attr1s = []
        self.attr2s = []
        self.attr3s = []
        if not jason:
            return
        with open(jason, 'r') as f:
            self.data = json.load(f)
            for t in self.data:
                template = self.data[t]
                self.attr1s.append(template["attr1"])
                self.attr2s.append(template["attr2"])
                self.attr3s.append(template["attr3"])

    def generate_csv(self, name = None):
        if not name:
            name = "TemplateData.csv"
        if not name.endswith(".csv"):
            name += ".csv"
        
        with open(name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Attribute 1", "Attribute 2", "Attribute 3"])
            for i in range(len(self.attr1s)):
                writer.writerow([self.attr1s[i], self.attr2s[i], self.attr3s[i]])
        
        print(f"CSV file generated: {name}")