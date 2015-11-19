import ConfigParser
import re
import pytest
def pytest_addoption(parser):
    print "==> pytest_addoption"
    parser.addoption("--dry-run", action="store_true", dest="dryrun", default=False, help="Emulate running of tests (report can be still generated)")
    print "<== pytest_addoption"

def pytest_configure(config):
    print "==> pytest_configure"

#   --dry-run
    print "config.option.dryrun=%r" % config.option.dryrun
    config.dryrun = False
    if config.option.dryrun is not None:
        config.dryrun = config.option.dryrun
    print "config.dryrun=%r" % config.dryrun

