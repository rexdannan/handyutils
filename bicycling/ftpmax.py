# This utility will estimate a person's maxium ftp based on weight and gender
# Formula used:  weight*2-[(weight*2)(0.005(Age-35))]
# The weight needs to be represented as pounds for the formula.

import argparse
import sys

class FtpMax:
    # Constants
    POUNDKG = 2.204623
    HELP_TEXT = """
    This utility calculates an estimate of a person's maximum FTP based on age and weight. Weight may be represented as
    pounds or kilograms.
    
    Syntax: ftpest.py <age> <weight>

    Examples:
    ftpest.py 35 180lb male - 35 years old, 180 pounds, biological male
    ftpest.py 49 80kg female - 49 years old, 80 kilograms, biological female
    """

    def __init__(self):
        # Variables
        self.weight_units = ['lb', 'kg']
        self.gender = ['female', 'male']
        self.weight = 0
        self.age = 0
        self.gender_factor = 1

        # Parameters
        self.parser = argparse.ArgumentParser(description=self.HELP_TEXT)
        self.parser.add_argument('age', type=str, help='Biological age expressed in years')
        self.parser.add_argument('weight', type=str, help='Rider weight expressed as lb or kg')
        self.parser.add_argument('gender', type=str, help='Rider biological gender expressed as \"male\" or \"female\"')

    def ProcessInput(self):
        self.args = self.parser.parse_args()

        def _Kilogram2Pound(kilogram):
            return kilogram * self.POUNDKG

        if self.args.age:
            try:
                self.age = int(self.args.age)
            except:
                sys.exit("Please enter an integer between 1 and 150.")
            if self.age < 0 or self.age > 150:
                sys.exit("Please enter an integer between 1 and 150.")

        if self.args.weight:
            weight_unit = self.args.weight[-2:].lower()
            if weight_unit in self.weight_units:
                try:
                    self.weight = int(self.args.weight[:-2])
                    if weight_unit == "kg":
                        self.weight = _Kilogram2Pound(self.weight)
                except:
                    sys.exit("Please enter an integer between 1 and 300.")
                if self.weight < 1 or self.weight > 300:
                    sys.exit("Please enter an integer between 1 and 300.")
            else:
                sys.exit("Please provide a weight unit of LB, lb, KG, or kg.")

        if self.args.gender.lower().strip() in self.gender: 
            if self.args.gender.lower().strip() == "female":
                self.gender_factor = 0.9
        else:
            sys.exit("Please provide a biological gender of FEMALE, female, MALE, or male.")

    def CalcFTPEst(self):
        return ((self.weight * 2) - ((self.weight * 2) * (0.005 * (self.age - 35)))) * self.gender_factor

if __name__ == '__main__':
    ftp = FtpMax()
    ftp.ProcessInput()
    print(ftp.CalcFTPEst())