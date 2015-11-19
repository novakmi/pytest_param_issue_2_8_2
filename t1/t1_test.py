import pytest
from utils import print_hello


class TestT1:
    def setup_method(self, method):
        print "==> setup_method (class %s)" % (self.__class__.__name__)
        print "<== setup_method (class %s)" % (self.__class__.__name__)

    def teardown_method(self, method):
        print "==> teardown_method (class %s)" % (self.__class__.__name__)
        print "<== teardown_method (class %s)" % (self.__class__.__name__)

    def test_t1(self):
        print "==>  test_t1"
        if not hasattr(pytest.config, "dryrun") or not pytest.config.dryrun:
            print_hello()
        print "<==  test_t1"

