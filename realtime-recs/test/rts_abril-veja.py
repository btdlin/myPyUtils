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
EMPTY_EXCLUDES = ['website|e52fa2c5958c48b8bc232c4c189f48c0', 'website|1a559720fc9f6e4e584a4f952897b4a1']
TEST = True
GROUP_NAME = 'default'
CALLING_APP = 'test_client'


def test_rts():
    COUNT = 5
    request = req.RecsRequest(site_id='f941f7fb036fb2836f08d8fff561b60d',
                              bsin='efba175f-3704-4ce1-870e-cf90f5331ff0',
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(or_=None, range=None, and_=[
        recs_filter.TFilter(or_=None, range=None, and_=None, existence=None, overlap=None, any=None, recency=None, named='GLOBAL'),
        recs_filter.TFilter(or_=None, range=None, and_=None, existence=None,
                overlap=recs_filter.TOverlapFilter(amount=recs_filter.TRange(max_=None, min_=1.0), match_type=0, field='resource-type',
                                       values=['article']), any=None, recency=None, named=None)], existence=None,
                                     overlap=None, any=None, recency=None, named=None)

    request.groups[GROUP_NAME] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)
    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT
