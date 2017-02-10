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
EMPTY_EXCLUDES = ['website|a2d7084c7facc1d6af91e5d06918d733', 'website|b573e9d008d1489f0e4a0b9b86e038e6']
TEST = True
GROUP_NAME = 'default'
CALLING_APP = 'test_client'


def test_metafilter_resource_type_article_abs():
    COUNT = 11
    request = req.RecsRequest(site_id='abril-mdemulher',
                              bsin='20d29a65-858f-4d02-90a3-0fb91c6f730a',
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(overlap=None, existence=None, recency=None, and_=[
        recs_filter.TFilter(overlap=None, existence=None, recency=None, and_=None, range=None, or_=None, any=None, named='GLOBAL'),
        recs_filter.TFilter(overlap=recs_filter.TOverlapFilter(values=['article'], field='resource-type', match_type=0,
                                       amount=recs_filter.TRange(max_=None, min_=1.0)), existence=None, recency=None, and_=None,
                range=None, or_=None, any=None, named=None)], range=None, or_=None, any=None, named=None)

    request.groups[GROUP_NAME] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)
    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT
