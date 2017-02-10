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


def test_metafilter_resource_type_article_abs():
    COUNT = 15
    request = req.RecsRequest(site_id='wide-open-spaces',
                              bsin='97b61121-34bf-4c00-ab2e-57fcecba05f0',
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
                                                               values=['all']), any=None, recency=None,
                            named=None)], existence=None,
                                     overlap=None, any=None, recency=None, named=None)

    request.groups[GROUP_NAME] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)
    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT
