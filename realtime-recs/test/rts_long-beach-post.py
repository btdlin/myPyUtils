import pytest
import recs_client.request as req
import bt_rts.thrift.gen.filters as recs_filter
from recs_client.client import RecommendationsClient

# rts_host = 'localhost'
rts_host = 'realtime-recs-k.magic.boomtrain.com'
# rts_host = 'rts.aws.boomtrain.com'
PORT = 7070
TIMEOUT = 20000
RECSET_ID = 'fakedb0c-c5c6-4515-9bd1-5a06ddd676f6'
EMPTY_SEEDS = []
EMPTY_EXCLUDES = ['website|b4c6d99eaab70be4d88550facb324cf8']
TEST = True
GROUP_NAME = 'default'
CALLING_APP = 'test_client'


def test_rts(rts_host):
    request = req.RecsRequest(site_id='long-beach-post',
                              bsin='e1fb9080-f54f-47cd-923a-ae6d6d9342a0',
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    COUNT1 = 10
    metafilter = recs_filter.TFilter(overlap=None, existence=None, recency=None, and_=[
        recs_filter.TFilter(overlap=None, existence=None, recency=None, and_=None, range=None, or_=None, any=None, named='GLOBAL'),
        recs_filter.TFilter(overlap=None, existence=None,
                recency=recs_filter.TRecencyFilter(range=recs_filter.TRange(max_=None, min_=-86400.0), field='pubDate'), and_=None, range=None,
                or_=None, any=None, named=None)], range=None, or_=None, any=None, named=None)
    request.groups['featured'] = req.RecGroupRequest(count=COUNT1, metafilter=metafilter)

    config = {'host': rts_host, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT1
