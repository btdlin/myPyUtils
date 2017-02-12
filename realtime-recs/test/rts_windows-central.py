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
EMPTY_EXCLUDES = []
TEST = True
GROUP_NAME = 'default'
CALLING_APP = 'test_client'


def test_rts(rts_host):
    COUNT = 4
    request = req.RecsRequest(site_id='5d29921c2b8b2d6fb309bcf08c26f9f9',
                              bsin='cd0c1b08-2b94-4bf5-ad21-4d3d259cf870',
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(existence=None, and_=[
        recs_filter.TFilter(existence=None, and_=None, or_=None, recency=None, overlap=None, any=None, named='GLOBAL',
                            range=None),
        recs_filter.TFilter(existence=None, and_=None, or_=None, recency=None,
                            overlap=recs_filter.TOverlapFilter(amount=recs_filter.TRange(min_=None, max_=0.0),
                                                               values=['game'],
                                                               field='model',
                                                               match_type=0), any=None, named=None, range=None)],
                                     or_=None, recency=None,
                                     overlap=None, any=None, named=None, range=None)

    request.groups[GROUP_NAME] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)
    config = {'host': rts_host, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT
