import pytest


def pytest_addoption(parser):
    parser.addoption("--rts_host", action="store", default="realtime-recs-k.magic.boomtrain.com",
                     help="RTS host name")
    parser.addoption("--api_host", action="store", default="recommendations-g.magic.boomtrain.com",
                 help="API Recs host name")

@pytest.fixture
def rts_host(request):
    return request.config.getoption("--rts_host")

@pytest.fixture
def api_host(request):
    return request.config.getoption("--api_host")
