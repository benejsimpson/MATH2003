import csv
import pandas as pd
import random as r
import tkinter as tk
from tkinter import filedialog
from math import floor
from math import ceil
import matplotlib.pyplot as plt

MEMBERSHIP_MIN = 50
MEMBERSHIP_MAX = 200
REQUESTS_MIN = 7
REQUESTS_MAX = 20

SOCIETIES = [
    'Aerobics',
    'Basketball',
    'Cricket',
    'Dancing',
    'Egg & Spoon Racing',
    'Fencing',
    'Gymnastics',
    'Handball',
    'Indoor Hockey',
    'Judo'
]
MEMBERSHIPS = [67, 51, 69, 58, 82, 155, 141, 110, 196, 53]
REQUESTS = [15, 8, 8, 10, 8, 18, 20, 8, 13, 16]
ALLOCATABLE_HOURS = 70

r.seed(2003)

# ==================
# Society data
# ==================

class Society():
    '''
    holds data about a specific society
    '''
    def __init__(
            self,
            name,
            membership,
            requested_hours
        ):
        self.name = name
        self.membership = membership
        self.requested_hours = requested_hours

        self.allocated_hours = 0
        self.remainder = None

    @property
    def satisfaction(self):
        '''
        satisfaction of a society is the proportion of its allocated hours to its requested hours
        '''
        if self.allocated_hours is None:
            print('ERROR: No hours allocated for satifaction')
            return 0
        return self.allocated_hours / self.requested_hours

    @property
    def requested_hours_unallocated(self):
        '''
        returns the number of hours requested minus the number of hours allocated. Returns None if no hours have been allocated
        '''
        if self.allocated_hours is None:
            return None
        return self.requested_hours - self.allocated_hours

    @property
    def data_output_format(self):
        '''
        is the data out version
        '''
        return {
            'm' : self.membership,
            'd' : self.requested_hours,
            'x' : self.allocated_hours
            }

    @property
    def requests_per_member(self):
        return self.membership / self.requested_hours

    def update_membership(self, new_membership):
        '''
        updates membership for specific society
        '''
        self.membership = new_membership

    def update_requested_hours(self, new_requested_hours):
        '''
        updates the requested hours for specific society
        '''
        self.requested_hours = new_requested_hours

    def update_allocated_hours(self, hours):
        '''
        updates allocated hours for specific society
        '''
        self.allocated_hours = hours

    def update_remainder_allocation(self, remainder):
        '''
        updates a new variable self.remainder
        '''
        self.remainder = remainder

    def __str__(self):
        res = f'{self.name}\n\tMembership : {self.membership}\n\tRequested : {self.requested_hours} | Allocated : {self.allocated_hours} | Unallocated : {self.requested_hours_unallocated}\n\tSatisfaction : {round(self.satisfaction,4)}'
        return res


# ==================
# Society list
# ==================

class SocietyList():
    '''
    data storage for societies
    '''
    def __init__(self, societies : list[Society]):
        self.societies = societies

    def __str__(self):
        '''
        prints list of society data
        '''
        res = '===============================================================================\n'
        for soc in self.societies:
            res += str(soc)
            res += '\n'
        res += '===============================================================================\n'
        return res

    @property
    def total_membership(self):
        '''
        returns total membership across all societies
        '''
        return sum([soc.membership for soc in self.societies])

    @property
    def num_societies(self):
        '''
        returns the number of societies
        '''
        return len(self.societies)

    @property
    def total_requests(self):
        '''
        gets the total requests made by all socs
        '''
        return sum(soc.requested_hours for soc in self.societies)

    @property
    def lowest_satisfaction_soc(self):
        '''
        returns society object with lowest satisfaction score
        '''
        lowest = self.get_lowest_satisfaction()
        if lowest.satisfaction == 0:
            print('Lowest satisfaction is 0')
            print(f'{lowest.name}\n\tRequests : {lowest.requested_hours} | Allocated : {lowest.allocated_hours}')
        return lowest

    @property
    def lowest_satisfaction_score(self):
        '''
        returns the lowest satisfaction score
        '''
        return self.lowest_satisfaction_soc.satisfaction
        
    def order_by_membership(self):
        '''
        returns a dict of socs ordered by membership - does not mutate
        '''
        return sorted(
            self.societies,
            key = lambda soc : soc.membership,
            reverse = True
        )

    def order_by_requests(self):
        '''
        returns a dict of socs ordered by requests - does not mutate
        '''
        return sorted(
            self.societies,
            key = lambda soc : soc.requested_hours,
            reverse = True
        )

    def order_by_remainder(self):
        '''
        returns a dict of socs ordered by remainder values [0,1] - does not mutate
        '''
        return sorted(
            self.societies,
            key = lambda soc : soc.remainder,
            reverse= True
        )

    def order_by_membership_weighted_utility(self):
        '''
        returns a dict of socs ordered by membership weighted utility (high -> low) - does not mutate
        '''
        return sorted(
            self.societies,
            key = lambda soc : soc.requests_per_member,
            reverse = True
        )

    def order_by_satisfaction(self):
        '''
        returns a dict of socs ordered by satisfaction (low to high) - does not mutate
        '''
        return sorted(
            self.societies,
            key = lambda soc : soc.satisfaction,
            reverse = False
        )

    def get_lowest_satisfaction(self):
        '''
        returns the soc with the lowest satisfaction
        '''
        return self.order_by_satisfaction()[0]

    def reset_allocated_times(self):
        '''
        resets allocated times for all societies
        '''
        for soc in self.societies:
            soc.update_allocated_hours(0)

    def update_allocated_times(self, allocated_times : list[int]):
        '''
        updates allocated times for all societies
        '''
        if len(allocated_times) != len(self.societies):
            print('ERROR: List sizes do not match')
            return

        for soc, hours in zip(self.societies, allocated_times):
            soc.update_allocated_hours(hours)

    def generate_random_data(
            self,
            member_min = MEMBERSHIP_MIN,
            member_max = MEMBERSHIP_MAX,
            request_min = REQUESTS_MIN,
            request_max = REQUESTS_MAX
            ):
        '''
        generates random data for each society.\n
        Default Values: \n
        50 <= membership <= 200\n
        7 <= preferred_practice_time <= 20
        '''

        for soc in self.societies:
            # generate random values
            rand_membership = r.randint(member_min,member_max)
            rand_requested_hours = r.randint(request_min,request_max)

            # update soc with new values
            soc.update_membership(rand_membership)
            soc.update_requested_hours(rand_requested_hours)

        self.reset_allocated_times()

    def output_format(self, algoname = ''):
        '''
        output format of societies data
        '''
        res = []
        if algoname != '':
            res = [algoname]
        res.extend([soc.data_output_format for soc in self.societies])
        return res

# ==================
# Allocation algorithms
# ==================

class AllocateHours(SocietyList):
    '''
    allocates hours
    '''
    def __init__(
            self,
            societies : list[Society],
            allocatable_hours = 70
    ):
        super().__init__(societies)
        self.allocatable_hours = allocatable_hours

    @property
    def unallocated_hours(self):
        '''
        unallocated hours
        '''
        allocated = sum(
            soc.allocated_hours or 0
            for soc in self.societies
        )
        return self.allocatable_hours - allocated

    def allocate_by_satisfaction(self):
        '''
        allocated hours to lowest satisfaction until all hours have been used\n
        returns the minimum satisfaction
        '''
        self.reset_allocated_times()

        while self.unallocated_hours > 0:

            # find eligible socs that require hours
            eligible = [
                soc for soc in self.societies
                if soc.allocated_hours < soc.requested_hours
            ]
            # if all societies have their allocated hours, break
            if not eligible:
                break
            
            # find soc with lowest satisfaction
            lowest = min(eligible, key=lambda soc: soc.satisfaction)

            # give it an hour
            lowest.update_allocated_hours(lowest.allocated_hours + 1)

        # return the min satisfaction guaranteed to all socs
        return min(soc.satisfaction for soc in self.societies)

    def allocate_all_societies_to_minimum_satisfaction(self):
        '''
        finds t* - the minimum satisfaction guaranteed to each society\n
        clears all allocations\n
        reallocates hours to each society until s_i >= t*\n
        distributes remaining hours to societies using membership utility
        '''
        # gets guaranteed satisfaction
        guaranteed_satisfaction = self.allocate_by_satisfaction()

        # resets allocations
        self.reset_allocated_times()

        # give each soc enough hours to reach minimum satisfaction
        for soc in self.societies:
            while soc.satisfaction < guaranteed_satisfaction:
                soc.update_allocated_hours(soc.allocated_hours + 1)

        return self.unallocated_hours

    def allocate_remaining_hours(self):
        '''
        allocates remaining hours from guaranteed minimum\n
        gets societies with lowest satisfaction\n
        gives an hour to the society with the highest membership\n
        repeats until all hours given out
        '''
        while self.unallocated_hours > 0:
            min_satisfaction = self.lowest_satisfaction_score
            socs_with_min_satisfaction = [
                soc for soc in self.societies
                if soc.satisfaction == min_satisfaction
                ]
            highest_membership = max(
                socs_with_min_satisfaction,
                key = lambda soc : soc.membership
                )
            highest_membership.update_allocated_hours(highest_membership.allocated_hours + 1)

    def allocate_by_society(self):
        '''
        Allocates each society the same number of hours. \n
        If a society requests less than they are provisionally allocated, they are allocated their requested hours 
        (this shouldn't happen for the 70 allocatable hours, 10 societies, and requests in [7,20])
        '''
        hours_per_soc = self.allocatable_hours // self.num_societies

        for soc in self.societies:
            allocated = min(
                hours_per_soc,
                soc.requested_hours
                )
            soc.update_allocated_hours(allocated)

    def allocate_by_membership(self):
        '''
        Allocates each society a number of hours proportional to their membership, 
        relative to the total membership of all societies. \n
        Non-integer results are rounded down and all remaining hours are allocated to the societies with the greatest memberships. 
        If a society requests less than their proportionally allocated hours, they will recieve their requested hours. 
        What remains will be allocated to societies with largest memberships.
        '''
        # allocate times proportional to each society membership
        for soc in self.societies:
            proportion_of_total_membership = soc.membership / self.total_membership
            allocated = floor(proportion_of_total_membership * self.allocatable_hours)
            soc.update_allocated_hours(
                min(
                    allocated,
                    soc.requested_hours
                )
            )

    def allocate_by_requests(self, integer = True):
        '''
        allocates by requests
        '''

        for soc in self.societies:
            proportion_of_total_requests = soc.requested_hours / self.total_requests
            
            if integer:
                allocated = floor(proportion_of_total_requests * self.allocatable_hours)
            else:
                allocated = proportion_of_total_requests * self.allocatable_hours
            
            soc.update_allocated_hours(
                min(
                    allocated,
                    soc.requested_hours
                )
            )

    def allocate_remainders(self):
        '''
        New allocation Algo!\n
        This one is going to give the extra hours to the soc with the highest remainders
        '''
        ordered = self.get_remainders()
        while True:
            for soc in ordered:
                if self.unallocated_hours == 0:
                    break
                if soc.requested_hours_unallocated != 0:
                    soc.update_allocated_hours(soc.allocated_hours + 1)
            if self.unallocated_hours == 0 or sum(soc.requested_hours_unallocated for soc in self.societies) == 0:
                break

    def get_remainders(self):
        '''
        does what it says on the tin - I don't like the squiggles
        '''
        for soc in self.societies:
            proportion_of_total_membership = soc.membership / self.total_membership
            allocated = floor(proportion_of_total_membership * self.allocatable_hours)
            remainder = allocated % 1
            soc.update_remainder_allocation(remainder)
        return self.order_by_remainder()

    @property
    def satisfaction_data(self):
        return [soc.satisfaction for soc in self.societies]


def compare_allocation_methods_plot(soc_list):
    plt.figure('MATH2003_Plot')
    plt.title('Ordered Satisfaction Curves')
    plt.xlabel('Society rank (lowest to highest satisfaction)')
    plt.ylabel('Satisfaction')
    plt.xlim(0.75,len(soc_list) + 0.25)

    xs = [i+1 for i in range(len(soc_list))]

    allocator = AllocateHours(soc_list)

    allocator.reset_allocated_times()
    allocator.allocate_by_society()
    ys0 = sorted([soc.satisfaction for soc in allocator.societies])
    plt.plot(xs,ys0,'o-g')

    allocator.reset_allocated_times()
    allocator.allocate_by_membership()
    ys1 = sorted([soc.satisfaction for soc in allocator.societies]).copy()
    plt.plot(xs,ys1,'o-b')

    allocator.reset_allocated_times()
    allocator.allocate_remaining_hours()
    ys2 = sorted([soc.satisfaction for soc in allocator.societies]).copy()
    plt.plot(xs,ys2,'o-r')
    for soc in allocator.societies:
        print(soc)
    
    print(allocator.total_requests)

    plt.legend(['Equal', 'Membership', 'Proposed Method'], loc = 'lower right')

    plt.show()

# ==================
# Create societies objects
# ==================

list_of_societies = [
    Society(name, mems, reqs)
    for name,mems,reqs in zip(
        SOCIETIES,
        MEMBERSHIPS,
        REQUESTS
    )
]

def import_soc_info():
    root = tk.Tk()
    root.withdraw() # hide empty window

    try:
        filepath = filedialog.askopenfilename(
            title="Select society data",
            filetypes=[("CSV files", "*.csv")],
        )
    finally:
        root.destroy()

    if not filepath: # user cancelled file selection
        return None

    socinfo = []
    required_headers = {"SocName", "SocMembers", "SocRequests"}

    try:
        with open(filepath, newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            if set(reader.fieldnames or []) != required_headers:
                raise ValueError(
                    "CSV headers must be : SocName, SocMembers, SocRequests."
                )

            for row_number, row in enumerate(reader, start=2):
                if None in row or any(value is None for value in row.values()):
                    raise ValueError(
                        f"Row {row_number}: incorrect number of columns."
                    )

                name = row["SocName"].strip()

                if not name:
                    raise ValueError(
                        f"Row {row_number}: society name cannot be empty."
                    )

                try:
                    members = int(row["SocMembers"])
                    requested = float(row["SocRequests"])
                    requests = ceil(requested)
                except (ValueError, OverflowError):
                    raise ValueError(
                        f"Row {row_number}: invalid members or requested hours."
                    ) from None

                if not 50 <= members <= 200:
                    raise ValueError(
                        f"Row {row_number}: members must be between 50 and 200."
                    )

                if requested < 0:
                    raise ValueError(
                        f"Row {row_number}: requested hours cannot be negative."
                    )

                socinfo.append([name, members, requests])

        if not socinfo:
            raise ValueError("The CSV contains no society data.")

    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        print(f"Import failed: {error}")
        return None

    return socinfo


def read_number(prompt, convert, is_valid):
    while True:
        value = input(prompt).strip()

        if not value:
            while True:
                choice = input(
                    "\t- S : Finish with collected entries\n"
                    "\t- D : Use default\n"
                    "\t- X : Cancel\n"
                    "\t- C : Continue entering data\n\t"
                ).strip().upper()

                if choice in ['S', 'X', 'D']:
                    return None, choice
                if choice == 'C':
                    break
            continue

        try:
            number = convert(value)
        except (ValueError, OverflowError):
            print("Rejected: enter a valid number.")
            continue

        if not is_valid(number):
            print("Rejected: number outside the allowed range.")
            continue

        return number, None

def get_soc_info(usr_input_names=False):
    socinfo = []

    while True:
        if usr_input_names:
            socname = input("Name:\n\t").strip()
            if not socname:
                print("Please enter a name.")
                continue
        else:
            cycle, index = divmod(len(socinfo), len(SOCIETIES))
            socname = SOCIETIES[index]
            if cycle:
                socname += f" {cycle + 1}"

        socmemb, action = read_number(
            "Enter number of members (50 – 200):\n\t",
            int,
            lambda number: 50 <= number <= 200,
        )

        if action:
            return socinfo if action == "S" else None

        socreqs, action = read_number(
            "Enter requested hours (0 or more, rounded up):\n\t",
            lambda value: ceil(float(value)),
            lambda number: number >= 0,
        )

        if action:
            return socinfo if action == "S" else None

        socinfo.append([socname, socmemb, socreqs])


def run():
    num_hours_available = ALLOCATABLE_HOURS
    while True:
        choice = input(
            "Choose option:\n"
            "\t- X: without names\n"
            "\t- E: with names\n"
            "\t- I: import from files\n"
            "\t- R: random (coming soon...)\n\t"
        ).strip().lower()

        if choice in ['x', 'e','i','r']:
            break
        else:
            print('Please choose X, E, I, or R.')

    if choice == 'i':
        soclist = import_soc_info()
    elif choice == 'r':
        num_iters, action = read_number(
            prompt = 'How many random societies would you like to generate?\n\t',
            convert = int,
            is_valid = lambda number : 0 <= number <= 100_000,
        )
        if action:
            return None
        num_hours_available, action = read_number(
            prompt = "Number of hours available for allocation (default : 70)\n\t",
            convert = int,
            is_valid = lambda number : 0 <= number <= 1_000,
        )
        if action:
            if action == 'D':
                print('Using Default : 70')
                num_hours_available = 70
            else:
                return None
            
        members_min, action = read_number(
            prompt = "Minimum number of members (default : 50)\n\t",
            convert = int,
            is_valid = lambda number : 0 <= number <= 1_000,
        )
        if action:
            if action == 'D':
                print('Using Default : 50')
                members_min = 50
            else:
                return None
        members_max, action = read_number(
            prompt = "Maximum number of members (default : 200)\n\t",
            convert = int,
            is_valid = lambda number : members_min <= number <= 10_000,
        )
        if action:
            if action == 'D':
                print('Using Default : 200')
                members_max = 200
            else:
                return None
        requests_min, action = read_number(
            prompt = "Minimum number of requested hours (default : 7)\n\t",
            convert = int,
            is_valid = lambda number : 0 <= number <= 1_000,
        )
        if action:
            if action == 'D':
                print('Using Default : 7')
                requests_min = 7
            else:
                return None
        requests_max, action = read_number(
            prompt = "Maximum number of requested hours (default : 20)\n\t",
            convert = int,
            is_valid = lambda number : requests_min <= number <= 10_000,
        )
        if action:
            if action == 'D':
                print('Using Default : 20')
                requests_max = 20
            else:
                return None
        
        soclist = []
        for _ in range(num_iters):
            cycle, index = divmod(len(soclist), len(SOCIETIES))
            socname = SOCIETIES[index]
            if cycle:
                socname += f" {cycle + 1}"

            socmembers = r.randint(members_min, members_max)
            socrequests = r.randint(requests_min, requests_max)
            soclist.append([socname, socmembers,socrequests])
    
    else:
        soclist = get_soc_info(usr_input_names = (choice == "e"))

    if not soclist:
        print("No data to allocate.")
        return

    allocator = AllocateHours(societies = [
    Society(name, mems, reqs)
    for name,mems,reqs in soclist
    ],
    allocatable_hours= num_hours_available)
    
    print("\n--- Data Loaded ---")
    for society in allocator.societies:
        print(society)

    algorithms = {
        "1": allocator.allocate_remaining_hours,
        "2": allocator.allocate_by_membership,
        "3": allocator.allocate_by_society,
    }

    while True:
        print('Would you like to see a plot comparing the different allocation methods?')
        if input("Y/N").upper() == 'Y':
            compare_allocation_methods_plot([Society(name,mems,reqs) for name,mems,reqs in soclist])
        choice = input(
            "\nChoose Algorithm:\n"
            "\t1. Proposed\n"
            "\t2. Membership\n"
            "\t3. Equal\n\t"
        ).strip()

        if choice in algorithms:
            break

        print("Please choose a number from 1 to 3.")

    allocator.reset_allocated_times()
    algorithms[choice]()

    for society in allocator.societies:
        print(society)

if __name__ == "__main__":
    run()