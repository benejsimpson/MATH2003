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
   
    @property
    def requested_hours_unallocated(self):
        '''
        returns the number of hours requested minus the number of hours allocated. Returns None if no hours have been allocated
        '''
        if self.allocated_hours is None:
            return None
        return self.requested_hours - self.allocated_hours

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

    def __str__(self):
        res = f'{self.name}\n\tMembership : {self.membership}\n\tRequested : {self.requested_hours} | Allocated : {self.allocated_hours} | Unallocated : {self.requested_hours_unallocated}'
        return res

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
        return sum(soc.requested_hours for soc in self.societies)
        
    def order_by_membership(self, descending = True):
        '''
        orders by membership
        '''
        return sorted(
            self.societies,
            key = lambda soc : soc.membership,
            reverse = descending
        )

    def order_by_requests(self, descending = True):
        '''
        orders by number of requests
        '''
        return sorted(
            self.societies,
            key = lambda soc : soc.requested_hours,
            reverse = descending
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

    def generate_random_data(
            self,
            rand_seed = 2003,
            membership_bounds = [50,200],
            requested_hours_bounds = [7,20]
        ):
        '''
        generates random data for each society.
        50 <= membership <= 200
        7 <= preferred_practice_time <= 20
        '''
        # set RNG seed
        rng = r.Random(rand_seed)

        for soc in self.societies:
            # generate random values
            rand_membership = rng.randint(membership_bounds[0],membership_bounds[1])    # 50 <= membership <= 200
            rand_requested_hours = rng.randint(requested_hours_bounds[0],requested_hours_bounds[1]) # 7 <= preferred_practice_time <= 20

            # update soc with new values
            soc.update_membership(rand_membership)
            soc.update_requested_hours(rand_requested_hours)

        self.reset_allocated_times()

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
        print('=-=-=-= Allocation by Society =-=-=-=')
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
        print('=-=-=-= Allocation by Membership =-=-=-=')
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

        self.allocate_remaining(algorithm = 'm', descending = True)

    def allocate_by_requests(self):
        '''
        allocates by requests
        '''
        print('=-=-=-= Allocation by Requests =-=-=-=')
        for soc in self.societies:
            proportion_of_total_requests = soc.requested_hours / self.total_requests
            allocated = floor(proportion_of_total_requests * self.allocatable_hours)
            soc.update_allocated_hours(
                min(
                    allocated,
                    soc.requested_hours
                )
            )
        self.allocate_remaining(algorithm = 'r', descending = True)

    def allocate_remaining_v1(self, algorithm, descending =  True):
        '''
        allocates remaining hours after floor function
        '''
        if algorithm.lower() in ['membership','m']:
            ordered = self.order_by_membership(descending)
        elif algorithm.lower() in ['requests','r']:
            ordered = self.order_by_requests(descending)
        else:
            print('ERROR: algorithm not recognised')
            ordered = self.societies

        while True:
            for soc in ordered:
                if self.unallocated_hours == 0:
                    break
                if soc.requested_hours_unallocated != 0:
                    soc.update_allocated_hours(soc.allocated_hours + 1)
            if self.unallocated_hours == 0 or sum(soc.requested_hours_unallocated for soc in self.societies) == 0:
                break

    def allocate_remaining(self):
        '''
        New allocation Algo!\n
        This one is going to give the extra hours to the soc with the highest remainders
        '''
        ordered = self.societies
        
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
        


list_of_societies = [
    Society(name, membership, requested)
    for name, membership, requested in zip(
        SOCIETIES,
        MEMBERSHIP,
        PREFERRED_PRACTICE_TIME
    )
]

def allocator_algorithms():
    allocator = AllocateHours(list_of_societies)    # initialise allocator
    allocator.generate_random_data()                # generate random data
    
    allocator.allocate_by_membership()              # allocate by membership
    print(allocator)                                # print membership results
    
    allocator.reset_allocated_times()               # reset allocated times
    
    allocator.allocate_by_society()                 # allocate by society
    print(allocator)                                # print society results

    allocator.reset_allocated_times()               # reset allocated times

    allocator.allocate_by_requests()                # allocate by requests
    print(allocator)                                # print requests results

    allocator.reset_allocated_times()               # reset


allocator_algorithms()
