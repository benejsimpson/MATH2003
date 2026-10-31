import random as r
from math import floor

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
PREFERRED_PRACTICE_TIME = [
    16,
    14,
    15,
    7,
    19,
    15,
    17,
    11,
    9,
    7
]
MEMBERSHIP = [
    152,
    87,
    193,
    64,
    178,
    134,
    199,
    73,
    158,
    121
]
ALLOCATABLE_HOURS = 70

# ==================

# ==================

class Society():
    '''
    holds data about a specific society
    '''
    def __init__(
            self,
            name,
            membership,
            preferred_practice_time
        ):
        self.name = name
        self.membership = membership
        self.requested_hours = preferred_practice_time

        self.allocated_hours = None
        self.remainder = None
   
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
        res = f'{self.name}\n\tMembership : {self.membership}\n\tRequested : {self.requested_hours} | Allocated : {self.allocated_hours} | Unallocated : {self.requested_hours_unallocated}'
        return res


# ==================

# ==================

class SocietyList():
    '''
    data storage for societies
    '''
    def __init__(self, societies : list[Society]):
        self.societies = societies

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
        
    def order_by_membership(self):
        '''
        orders by membership
        '''
        return sorted(
            self.societies,
            key = lambda soc : soc.membership,
            reverse = True
        )

    def order_by_requests(self):
        '''
        orders by number of requests
        '''
        return sorted(
            self.societies,
            key = lambda soc : soc.requested_hours,
            reverse = True
        )

    def order_by_remainder(self):
        '''
        orders socs in their remainder values [0,1]
        '''
        return sorted(
            self.societies,
            key = lambda soc : soc.remainder,
            reverse= True
        )

    def reset_allocated_times(self):
        '''
        resets allocated times for all societies
        '''
        for soc in self.societies:
            soc.update_allocated_hours(None)

    def update_allocated_times(self, allocated_times : list[int]):
        '''
        updates allocated times for all societies
        '''
        if len(allocated_times) != len(self.societies):
            print('ERROR: List sizes do not match')
            return
        
        for soc, hours in zip(self.societies, allocated_times):
            soc.update_allocated_hours(hours)

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

    def generate_random_data(self):
        '''
        generates random data for each society.
        50 <= membership <= 200
        7 <= preferred_practice_time <= 20
        '''

        for soc in self.societies:
            # generate random values
            rand_membership = r.randint(50,200)    # 50 <= membership <= 200
            rand_requested_hours = r.randint(7,20) # 7 <= preferred_practice_time <= 20

            # update soc with new values
            soc.update_membership(rand_membership)
            soc.update_requested_hours(rand_requested_hours)

        self.reset_allocated_times()

    def output_format(self, algoname = ''):
        res = []
        if algoname != '':
            res = [algoname]
        res.extend([soc.data_output_format for soc in self.societies])
        return res

# ==================

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

    def allocate_by_requests(self):
        '''
        allocates by requests
        '''

        for soc in self.societies:
            proportion_of_total_requests = soc.requested_hours / self.total_requests
            allocated = floor(proportion_of_total_requests * self.allocatable_hours)
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


class ResultsStorage:
    '''

    '''
    def __init__(
            self,
            start_dist,

        ):
        self.start_dist = None



    

# ==================

# ==================

list_of_societies = [
    Society(name, membership, requested)
    for name, membership, requested in zip(
        SOCIETIES,
        MEMBERSHIP,
        PREFERRED_PRACTICE_TIME
    )
]

# ==================

# ==================

def run_algorithms(list_of_societies):
    '''
    the big one
    '''
    res = {}
    allocator = AllocateHours(list_of_societies)
    allocator.generate_random_data()

    res['None'] = (allocator.output_format(algoname='None'))

    allocator.allocate_by_society()
    res['s1'] = (allocator.output_format('society1'))
    allocator.get_remainders()
    res['s2'] = (allocator.output_format('society2'))

    allocator.reset_allocated_times()

    allocator.allocate_by_membership()
    res['m1'] = (allocator.output_format('membership1'))
    allocator.get_remainders()
    res['m2'] = (allocator.output_format('membership2'))

    allocator.reset_allocated_times()

    allocator.allocate_by_requests()
    res['r1'] = (allocator.output_format('requests1'))
    allocator.get_remainders()
    res['r2'] = (allocator.output_format('requests2'))

    allocator.reset_allocated_times()

    return res

# bigres = []
# for _ in range(10):
#     bigres.append(run_algorithms(list_of_societies=list_of_societies))

# print('\nthis is about to get mental...\n')
# for i,res in enumerate(bigres):
#     print(f'trial {i+1}')
#     for a,b in res.items():
#         print(a)
#         print(b)


def run_sim(iters):
    res = {
        'society' : [],
        'membership' : [],
        'requests' : [],
        }
    allocator = AllocateHours(list_of_societies)
    for _ in range(iters):
        allocator.generate_random_data()                            # generate random data for trial

        allocator.allocate_by_society()                             # apply allocation algorithm
        allocator.get_remainders()                                  # allocate remainders

        res['society'].append(allocator.output_format())            # store output data

        allocator.reset_allocated_times()                           # reset allocated times

        allocator.allocate_by_membership()                          # apply allocation algorithm
        allocator.get_remainders()                                  # allocate remainders

        res['membership'].append(allocator.output_format())         # store output data

        allocator.reset_allocated_times()                           # reset allocated times

        allocator.allocate_by_requests()                            # apply allocation algorithm
        allocator.get_remainders()                                  # allocate remainders

        res['requests'].append(allocator.output_format())           # store output data

        allocator.reset_allocated_times()                           # reset allocated times
    return res

res = run_sim(50)



for algo_name,algo_results in res.items():
    print(f'\t=-=-=-=-= Algo Applied = {algo_name} =-=-=-=-=\n')
    for i,trial_results_for_algo in enumerate(algo_results):
        print(f' Trial {i+1} :')
        for soc_results in trial_results_for_algo:
            print(f'\t{soc_results}')
        print()

    print()
