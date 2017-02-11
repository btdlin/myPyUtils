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
EMPTY_EXCLUDES = ['trending|166814', 'trending|167165', 'trending|167336', 'trending|166933', 'trending|167477',
                  'trending|167368', 'trending|167417', 'trending|167524', 'trending|167425',
                  '|2708816a3f1a36b0bb793c4e7ab83eab', 'trending|167433']
TEST = True
GROUP_NAME = 'default'
CALLING_APP = 'test_client'


def test_metafilter_resource_type_article_abs():
    COUNT = 5
    request = req.RecsRequest(site_id='75471913db291cdd62f3092709061407',
                              bsin='29c08e54-c44b-45d6-9f91-3f7597421442',
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(existence=None, and_=[
        recs_filter.TFilter(existence=None, and_=None, or_=None, recency=None, overlap=None, any=None, named='GLOBAL',
                            range=None),
        recs_filter.TFilter(existence=None, and_=None, or_=None, recency=None,
                            overlap=recs_filter.TOverlapFilter(amount=recs_filter.TRange(min_=1.0, max_=None),
                                                               values=['trending'], field='resource-type',
                                                               match_type=0), any=None, named=None, range=None)],
                                     or_=None, recency=None,
                                     overlap=None, any=None, named=None, range=None)

    request.groups['hotel'] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)
    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT
