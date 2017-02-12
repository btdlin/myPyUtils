import pytest
import recs_client.request as req
import bt_rts.thrift.gen.filters as recs_filter
from recs_client.client import RecommendationsClient

#rts_host = 'localhost'
rts_host = 'realtime-recs-k.magic.boomtrain.com'
#rts_host = 'rts.aws.boomtrain.com'
PORT = 7070
TIMEOUT = 20000
RECSET_ID = 'fakedb0c-c5c6-4515-9bd1-5a06ddd676f6'
EMPTY_SEEDS =[]
EMPTY_EXCLUDES =[]
TEST = True
GROUP_NAME = 'default'
COUNT = 2
CALLING_APP = 'test_client'

def test_rts(rts_host):
    COUNT = 4
    request = req.RecsRequest(site_id='4e95f0debe3619d4e92b1b9828f17942',
                              bsin='4deef5a5-d5c9-4b9e-94f6-f67e394405cd',
                              #bsin='19620e18-7694-4772-a743-992e99ac1c92',
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(overlap=None, recency=None, and_=[
        recs_filter.TFilter(overlap=None, recency=None, and_=None, existence=None, or_=None, named='GLOBAL', range=None),
        recs_filter.TFilter(overlap=recs_filter.TOverlapFilter(values=['article'], field='resource-type', amount=recs_filter.TRange(min_=1.0, max_=None),
                                       match_type=0), recency=None, and_=None, existence=None, or_=None, named=None,
                range=None)], existence=None, or_=None, named=None, range=None)

    request.groups[GROUP_NAME] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)
    config = {'host': rts_host, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT

