# This utility will estimate a person's ftp based on weight and gender
# Formula used:  weight*2-[(weight*2)(0.005(Age-35))]
#
import argparse
import sys

class FtpEst:

    HELP_TEXT = """
    This utility calculates an estimate of a person's FTP based on age and weight. Weight may be represented as
    pounds or kilograms.
    
    Syntax: ftpest.py <age> <weight>

    Examples:
    ftpest.py 35 180lb - 35 years old, 180 pounds
    ftpest.py 49 80kg - 49 years old, 80 kilograms
    """

    def __init__(self):
        self.weight_units = ['lb', 'kg']
        self.weight = 0
        self.age = 0

        # Parameters
        self.parser = argparse.ArgumentParser(description=self.HELP_TEXT)
        self.parser.add_argument('age', type=str, help='Biological age expressed in years')
        self.parser.add_argument('weight', type=str, help='Rider weight expressed as lb or kg')

    def _Pound2Kilogram(pounds):
        POUNDKG = 2.204623
        return pounds / POUNDKG

    def ProcessInput(self):
        self.args = self.parser.parse_args()

        if self.args.age:
            try:
                self.age = int(self.args.age)
            except:
                sys.exit("Please enter an integer between 1 and 150.")
            if self.age < 0 or self.age > 150:
                sys.exit("Please enter an integer between 1 and 150.")

    def CalcFTPEst(self):
        return (self.weight * 2) - ((self.weight * 2) * (0.005 * (self.age - 35)))

if __name__ == '__main__':
    ftp = FtpEst()
    ftp.ProcessInput()
    print(ftp.CalcFTPEst())