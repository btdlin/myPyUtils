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
CALLING_APP = 'test_client'

def test_metafilter_resource_type_article_abs():
    COUNT = 4
    request = req.RecsRequest(site_id='roll-call',
                              bsin='de2fb381-767f-4b73-a519-eb66013dbfbe',
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(overlap=None, recency=None, and_=[
        recs_filter.TFilter(overlap=None, recency=None, and_=None, existence=None, or_=None, named='GLOBAL', range=None)
                ], existence=None, or_=None, named=None, range=None)

    request.groups[GROUP_NAME] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)
    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT

