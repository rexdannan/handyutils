# This utility will estimate a person's actual ftp based on wattage and time
# Formula used: wattage * factor based on duration of test

import sys
import argparse

class FtpAct:

    # Constants
    HELP_TEXT = """
    This utility calculates a person's ftp based on wattage output and test duration.
    
    Syntax: ftpact.py <watts> <durationinminutes>

    Examples:
    ftpact.py 270 3 - 270 watts, 3 minutes
    ftpact.py 220 60 - 220 watts, 60 minutes
    """

    # Definition data
    time_factor = { 1:.7, 3:.8, 5:.85, 20:.95, 60:1}

    def __init__(self):
        self.avg_watts=0
        self.duration=0
        self.duration_factor=0

        # Parameters
        self.parser = argparse.ArgumentParser(description=self.HELP_TEXT)
        self.parser.add_argument('avg_watts', type=str, help='Average watts achieved during the test')
        self.parser.add_argument('duration', type=str, help='Duration of the test expressed in minutes')
    
    def ProcessInput(self):
        self.args = self.parser.parse_args()

        if self.args.avg_watts:
            try:
                self.avg_watts = int(self.args.avg_watts)
            except:
                sys.exit("Please enter wattage of 1 or greater.")
            if self.avg_watts < 1:
                sys.exit("Please enter wattage of 1 of greater.")

        if self.args.duration:
            try:
                self.duration = int(self.args.duration)
            except:
                sys.exit("Please enter a duration of 1, 3, 5, 20, or 60 minutes.")
            try:
                self.duration_factor = self.time_factor[self.duration]
            except:
                sys.exit("Please enter a duration of 1, 3, 5, 20, or 60 minutes.")

    def CalcFTPAct(self):
        return self.duration_factor * self.avg_watts

if __name__ == '__main__':
    ftp = FtpAct()
    ftp.ProcessInput()
    print(ftp.CalcFTPAct())