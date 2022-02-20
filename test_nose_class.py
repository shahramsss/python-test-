import unit_test

class Test_cal:
    def test_sum(self):
        assert unit_test.sum(3 , 9 ) == 12

    def test_subtract(self):
        assert unit_test.subtract(10 ,2) ==8

    def test_multiply(self):
        assert unit_test.multiply(4,5) == 20 