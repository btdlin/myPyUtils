import pytest
import recs_client.request as req
import bt_rts.thrift.gen.filters as recs_filter
from recs_client.client import RecommendationsClient

#rts_host = 'localhost'
rts_host = 'realtime-recs-k.magic.boomtrain.com'
#rts_host = 'rts.aws.boomtrain.com'
PORT = 7070
TIMEOUT = 20000
BSIN = '35ae7c05-7d85-49f7-abb3-60e35651a397'
RECSET_ID = 'fakedb0c-c5c6-4515-9bd1-5a06ddd676f6'
EMPTY_SEEDS =[]
EMPTY_EXCLUDES =[]
TEST = True
GROUP_NAME = 'default'
COUNT = 4
CALLING_APP = 'test_client'

testdata = [
    ('Hubspot', 'hubspot-blog')
]

def test_rts(rts_host):

    request = req.RecsRequest(site_id='hubspot-blog',
                              bsin=BSIN,
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(overlap=None, recency=None, and_=[
        recs_filter.TFilter(overlap=None, recency=None, and_=None, existence=None, or_=None, named='GLOBAL', range=None),
        recs_filter.TFilter(overlap=recs_filter.TOverlapFilter(values=['Marketing'], field='keywords', amount=recs_filter.TRange(min_=1.0, max_=None),
                                                               match_type=0), recency=None, and_=None, existence=None, or_=None, named=None, range=None)
    ], existence=None, or_=None, named=None, range=None)

    request.groups['default'] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)

    config = {'host': rts_host, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == 4
