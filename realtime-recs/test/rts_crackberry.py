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
    COUNT = 4
    request = req.RecsRequest(site_id='d14efd1c5848089137af10c7ee78252e',
                              bsin='19b0ed4f-eb3f-4d4c-a876-86ba86e2033d',
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
    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT
