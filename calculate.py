__author__ = 'Michael Lo'

# Filename of input text file
input_file = "input.txt"
output_file = "output.txt"


# Represents a business
class Business:
    def __init__(self, name, ratio, cap, custom_fields):
        self.name = name
        self.ratio = float(ratio)
        self.cap = int(cap)
        self.donation = 0
        self.custom_fields = custom_fields

    def set_donation(self, donation):
        self.donation = donation

    def get_name(self):
        return self.name

    def get_ratio(self):
        return self.ratio

    def get_cap(self):
        return self.cap

    def get_donation(self):
        return round(self.donation, 2)

    def get_custom_fields(self):
        return self.custom_fields


donation_pool = 0
business_donations = 0
businesses = []


def main():
    read_input()
    do_calculations()
    write_output()


def read_input():
    file = open(input_file, 'r')
    line_count = 0
    for line in file:
        line = line.rstrip()
        if not (line.startswith('#')):
            if line.isdigit():
                global donation_pool
                donation_pool = int(line)
                print(donation_pool)
            else:
                try:
                    split_line = line.split('_')
                    print(split_line)
                    business = Business(split_line.pop(0), split_line.pop(0), split_line.pop(0), split_line)
                    businesses.append(business)
                except TypeError:
                    print("Error in format of line: " + line_count)


def do_calculations():
    sum_of_caps = 0
    businesses_with_no_cap = 0

    for business in businesses:
        sum_of_caps += business.get_cap()

        if business.get_cap() == 0:
            businesses_with_no_cap += 1

    if sum_of_caps > donation_pool:
        for business in businesses:
            if business.get_cap() == 0:
                business.set_donation((donation_pool * business.get_ratio()))
            else:
                business.set_donation((business.get_cap() / sum_of_caps) * donation_pool)
    else:
        for business in businesses:
            if business.get_cap() == 0:
                business.set_donation((donation_pool * business.get_ratio()))
            else:
                business.set_donation(business.get_cap())


def write_output():
    file = open(output_file, 'w')
    file.write("Donation pool: " + str(donation_pool) + "\n")
    file.write("Total donated by businesses: " + str(business_donations) + "\n")
    file.write("Total donations: " + str(business_donations + donation_pool) + "\n")
    file.write("\n")

    file.write("Business | Donation | Cap | Remainder | Custom fields/notes\n")

    for business in businesses:
        custom_fields = ""

        if len(business.get_custom_fields()) > 0:
            for field in business.get_custom_fields()[0:-1]:
                custom_fields = custom_fields + field + " | "
            custom_fields = custom_fields + business.get_custom_fields()[-1]

        remainder = str(business.get_cap() - business.get_donation())
        if business.get_cap() == 0:
            remainder = "N/A"

        file.write(business.get_name() + " | " + str(business.get_donation()) + " | " + str(business.get_cap()) + " | "
                   + remainder + " | " + custom_fields + "\n")

if __name__ == '__main__':
    main()