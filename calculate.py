__author__ = 'Michael Lo'

import os

# Filename of input text file
input_file = "input.txt"


# Represents a business
class Business:
    def __init__(self, name, ratio, cap, custom_fields):
        self.name = name
        self.ratio = ratio
        self.cap = cap
        self.custom_fields = custom_fields

    def get_name(self):
        return self.name

    def get_ratio(self):
        return self.ratio

    def get_cap(self):
        return self.cap

    def get_custom_fields(self):
        return self.custom_fields


# Represents all businesses with donation caps.
# Contributions up to the sum of the caps will be split equally by these businesses.
class RegularBusinesses:
    def __init__(self):
        self.businesses = []

    def get_businesses(self):
        return self.businesses

    def get_business(self, name):
        for business in self.businesses:
            if business.get_name() == name:
                return business

    def add_business(self, business):
        self.businesses.append(business)


# Represents all businesses with donation caps.
# Contributions above the sum of the caps will be split equally by these businesses.
class NoCapBusinesses:
    def __init__(self):
        self.businesses = []

    def get_businesses(self):
        return self.businesses

    def get_business(self, name):
        for business in self.businesses:
            if business.get_name() == name:
                return business

    def add_business(self, business):
        self.businesses.append(business)

regularBusinesses = RegularBusinesses()
noCapBusinesses = NoCapBusinesses()


def main():
    directory = os.path.dirname(os.getcwd())
    os.chdir(directory)
    read_input(input_file)
    do_calculations()
    write_output()


def read_input():
    pass
    # Read in file
    # For each line in file:
        # Create Business object representing it


def do_calculations():
    pass
    # Sum caps
    # If cap lower than total donation pool:
        # All regular businesses pay an equal proportion (same percentage of their cap)
    # Else:
        # All regular businesses pay their cap
        # All no cap businesses pay an equal share of (total donated - aggregate cap)


def write_output():
    pass
    # Print total donation pool
    # Print total donated by businesses
    # Print total donations (people and businesses)
    # For each business:
        # Print out name, amount to pay, unpaid amount remaining in cap, custom fields

if __name__ == '__main__':
    main()