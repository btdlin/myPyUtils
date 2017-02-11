import pytest
import recs_client.request as req
import bt_rts.thrift.gen.filters as recs_filter
from recs_client.client import RecommendationsClient

#HOST = 'localhost'
HOST = 'realtime-recs-k.magic.boomtrain.com'
#HOST = 'rts.aws.boomtrain.com'
PORT = 7070
TIMEOUT = 20000
RECSET_ID = 'fakedb0c-c5c6-4515-9bd1-5a06ddd676f6'
EMPTY_SEEDS =[]
EMPTY_EXCLUDES =[]
TEST = True
GROUP_NAME = 'default'
COUNT = 6
CALLING_APP = 'test_client'

def test_metafilter_resource_type_article_abs():
    COUNT = 4
    request = req.RecsRequest(site_id='ae6897195848feb20f96c5beac08e41b',
                              bsin='265ded23-b7ed-480d-b283-9ae941d33ab4',
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
    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT

