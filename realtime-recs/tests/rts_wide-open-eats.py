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
EMPTY_EXCLUDES = ['website|b4c6d99eaab70be4d88550facb324cf8']
TEST = True
GROUP_NAME = 'default'
CALLING_APP = 'test_client'


def test_metafilter_resource_type_article_abs():
    COUNT = 5
    request = req.RecsRequest(site_id='wide-open-eats',
                              bsin='e29221c2-e1e5-4a8e-a28d-6a2f267552c6',
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(existence=None, and_=[
        recs_filter.TFilter(existence=None, and_=None, or_=None, recency=None, overlap=None, any=None, named='GLOBAL', range=None),
        recs_filter.TFilter(existence=None, and_=None, or_=None,
                recency=recs_filter.TRecencyFilter(range=recs_filter.TRange(min_=-86400.0, max_=None), field='pubDate'), overlap=None, any=None,
                named=None, range=None)], or_=None, recency=None, overlap=None, any=None, named=None, range=None)

    request.groups['lbpost'] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)
    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT
