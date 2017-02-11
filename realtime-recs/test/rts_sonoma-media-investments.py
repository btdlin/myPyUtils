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
    COUNT = 7
    request = req.RecsRequest(site_id='sonoma-media-investments',
                              bsin='4f7bec79-45d9-48b0-8f9e-16fc9686bccc',
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(overlap=None, existence=None, recency=None, and_=[
        recs_filter.TFilter(overlap=None, existence=None, recency=None, and_=None, range=None, or_=None, any=None,
                            named='GLOBAL'),
        recs_filter.TFilter(overlap=None, existence=None,
                            recency=recs_filter.TRecencyFilter(range=recs_filter.TRange(max_=None, min_=-31536000.0),
                                                               field='pubDate'), and_=None,
                            range=None, or_=None, any=None, named=None), recs_filter.TFilter(
            overlap=recs_filter.TOverlapFilter(values=['article_pd'], field='resource-type', match_type=0,
                                               amount=recs_filter.TRange(max_=None, min_=1.0)), existence=None,
            recency=None, and_=None,
            range=None, or_=None, any=None, named=None)], range=None, or_=None, any=None, named=None)

    request.groups[GROUP_NAME] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)
    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT
