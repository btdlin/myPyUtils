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
    COUNT = 5
    request = req.RecsRequest(site_id='patient-info-prod',
                              bsin='8a8a1d17-8029-491e-9ed6-e5ed659a4005',
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(or_=None, range=None, and_=[
        recs_filter.TFilter(or_=None, range=None, and_=None, existence=None, overlap=None, any=None, recency=None,
                            named='GLOBAL'),
        recs_filter.TFilter(or_=None, range=None, and_=None, existence=None,
                            overlap=recs_filter.TOverlapFilter(amount=recs_filter.TRange(max_=None, min_=1.0),
                                                               match_type=0, field='resource-type',
                                                               values=['Wellbeing']), any=None, recency=None,
                            named=None)], existence=None,
                                     overlap=None, any=None, recency=None, named=None)

    request.groups[GROUP_NAME] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)
    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT
