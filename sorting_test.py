import random
import time
from trulz import sort

class TestSorting:
    def test_array_trick(self):
        input = [10, 2]
        output = sort(input)
        assert [2, 10] == output

    def test_out_of_range(self):
        input = [1000, -1]
        try:
            sort(input)
            assert False, 'should never get here'
        except RuntimeError as error:
            assert 'angst ugyldig verdi 1000' == str(error)

    def test_duplicates_are_kept(self):
        input = [2, 2, 1]
        output = sort(input)
        assert [1, 2, 2] == output

    def test_random_liste(self):
        input = random.choices(range(1000), k=10**6)
        begin = time.clock()
        output = sort(input)
        end = time.clock()

        fasit_begin = time.clock()
        fasit = sorted(input)
        fasit_end = time.clock()
        assert fasit == output

        print()
        print('sort took {}'.format(end - begin))
        print('sorted took {}'.format(fasit_end - fasit_begin))

    def test_random_liste_time(self):
        for each in range(32):
            input = random.choices(range(1000), k=10**each)
            begin = time.clock()
            output = sort(input)
            end = time.clock()
            
            fasit_begin = time.clock()
            fasit = sorted(input)
            fasit_end = time.clock()
            assert fasit == output
            
            print()
            print('input list len({})'.format(len(input))) 
            print('sort took {}'.format(end - begin))
            print('sorted took {}'.format(fasit_end - fasit_begin))
            if (fasit_end - fasit_begin) > 3:
                break
