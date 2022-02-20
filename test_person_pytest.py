
from person import Person
import pytest
import time


class TestPeson:
    @pytest.fixture
    def setup(self):
        self.p1 = Person('sss', 'shah')
        self.p2 = Person('s2', 'sh2')
        yield "setup"
        time.sleep(2)

    

    def test_fullname(self , setup):
        assert self.p1.fullname() == 'sss shah'
        assert self.p2.fullname() == 's2 sh2'

    def test_email(self , setup):
        assert self.p1.email() == 'sss@gmail.com'
        assert self.p2.email() == 's2@gmail.com'


