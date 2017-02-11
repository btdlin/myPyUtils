import pytest
import recs_client.request as req
import bt_rts.thrift.gen.filters as recs_filter
from recs_client.client import RecommendationsClient

# HOST = 'localhost'
HOST = 'realtime-recs-k.magic.boomtrain.com'
# HOST = 'rts.aws.boomtrain.com'
PORT = 7070
TIMEOUT = 20000
RECSET_ID = 'fakedb0c-c5c6-4515-9bd1-5a06ddd676f6'
EMPTY_SEEDS = []
EMPTY_EXCLUDES = []
TEST = True
GROUP_NAME = 'default'
CALLING_APP = 'test_client'


def test_rts():
    COUNT1 = 5
    COUNT2 = 1
    request = req.RecsRequest(site_id='honest-reporting',
                              bsin='ca297fe2-7390-4a70-9778-19c63b2cb3be',
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(overlap=None, existence=None, recency=None, and_=None, range=None, or_=None,
                                     any=None, named='GLOBAL')
    request.groups['hr_all'] = req.RecGroupRequest(count=COUNT1, metafilter=metafilter)

    metafilter = recs_filter.TFilter(overlap=None, existence=None, recency=None, and_=[
        recs_filter.TFilter(overlap=None, existence=None, recency=None, and_=None, range=None, or_=None, any=None, named='GLOBAL'),
        recs_filter.TFilter(overlap=None, existence=None,
                recency=recs_filter.TRecencyFilter(range=recs_filter.TRange(max_=None, min_=-172800.0), field='pubDate'), and_=None, range=None,
                or_=None, any=None, named=None)], range=None, or_=None, any=None, named=None)
    request.groups['hr_recent'] = req.RecGroupRequest(count=COUNT2, metafilter=metafilter)

    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT1 + COUNT2
