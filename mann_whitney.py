class RowUnit:
    value = None
    index = None
    rank = None

    def __init__(self, value = None, index = None, rank = None):
        self.value = value
        self.index = index
        self.rank = rank

    def __it__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

class MannWhitney(object):
    sample_list = [[1,2,3,4,6,11,321,-4], [321,312,12,-1321,1321], [3123,12312,3123321,123,-1321]]

    _merged_row = []
    _rank_sums = {}
    _max_rank_sum = None
    _sample_sizes = []
    _max_sample_size = None
    _criterion_value = None

    def __init__(self):
        pass


    def _generate_merged_row(self):
        index = 1
        for sample in self.sample_list:
            for unit in sample:
                self._merged_row.append(RowUnit(unit, index))
            index += 1

    def _define_ranks(self):
        self._merged_row.sort()
        previous_unit = None
        for unit in self._merged_row:
            if previous_unit == None:
                previous_unit = unit
                previous_unit.rank = 1
            else:
                if unit.value == previous_unit.value:
                    unit.rank = previous_unit.rank
                else:
                    unit.rank = previous_unit.rank + 1
            previous_unit = unit

    def _calculate_rank_sums(self):
        for unit in self._merged_row:
            if self._rank_sums.get(unit.index) == None:
                self._rank_sums[unit.index] = unit.rank
            else:
                self._rank_sums[unit.index] += unit.rank

    def _define_max_rank_sum(self):
        for current_value in self._rank_sums.values():
            if self._max_rank_sum == None:
                self._max_rank_sum = current_value
            elif current_value > self._max_rank_sum:
                self._max_rank_sum = current_value

    def _define_sample_sizes(self):
        for sample in self.sample_list:
            self._sample_sizes.append(len(sample))

    def _define_max_sample_size(self):
        for current_size in self._sample_sizes:
            if self._max_sample_size == None:
                self._max_sample_size = current_size
            elif current_size > self._max_sample_size:
                self._max_sample_size = current_size

    def _calculate_criterion_value(self):
         sample_sizes_product = 1
         for sample_size in self._sample_sizes:
             sample_sizes_product *= sample_size
         self._criterion_value = sample_sizes_product + self._max_sample_size*(self._max_sample_size + 1)/2 - self._max_rank_sum 

    def extract_the_criterion(self, sample_list = None):
        if sample_list != None:
            self.sample_list = sample_list
        self._generate_merged_row()
        self._define_ranks()
        self._calculate_rank_sums()
        self._define_max_rank_sum()
        self._define_sample_sizes()
        self._define_max_sample_size()
        self._calculate_criterion_value()
        #for unit in self._merged_row:
        #    print("\nvalue: {};\nindex: {};\nrank: {};\n".format(unit.value, unit.index, unit.rank))
        print(self._rank_sums)
        print(self._max_rank_sum)
        print(self._sample_sizes)
        print(self._max_sample_size)
        print(self._criterion_value)
        


test = MannWhitney()
test.extract_the_criterion()
