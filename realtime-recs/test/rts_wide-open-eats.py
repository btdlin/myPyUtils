import pytest
import recs_client.request as req
import bt_rts.thrift.gen.filters as recs_filter
from recs_client.client import RecommendationsClient

# rts_host = 'localhost'
rts_host = 'realtime-recs-k.magic.boomtrain.com'
# rts_host = 'rts.aws.boomtrain.com'
PORT = 7070
TIMEOUT = 20000
RECSET_ID = 'fakedb0c-c5c6-4515-9bd1-5a06ddd676f6'
EMPTY_SEEDS = []
EMPTY_EXCLUDES = ['object|9d78e2d20379839e41b08824921f8f42', 'object|e619e93bdd09b5b3d61d729e73d57d15',
                  'website|6480a07edb1aaa64b115bb593368c071', 'object|6f5915fe0ba45cc0db3db9860e3b75be',
                  'article|75bd96a8810610d9128285917005392d', 'object|5c024e92e968b6967dad8b024c24846a',
                  'article|cda2c301b2618cf1aa88e2d115871b1c', 'article|c094989f3ccca0a0b0cc4fb6a4269874',
                  'article|437004c736172754a9dc64c6c62f9f7d', 'article|b39292aad969b0cea7164cd4fa4c398d',
                  'object|1e16c31836d171e41558f7e0a8bd5e74']
TEST = True
GROUP_NAME = 'default'
CALLING_APP = 'test_client'


def test_rts(rts_host):
    request = req.RecsRequest(site_id='wide-open-eats',
                              bsin='e29221c2-e1e5-4a8e-a28d-6a2f267552c6',
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    COUNT1 = 1
    metafilter = recs_filter.TFilter(overlap=None, existence=None, recency=None, and_=[
        recs_filter.TFilter(overlap=None, existence=None, recency=None, and_=None, range=None, or_=None, any=None,
                            named='GLOBAL'),
        recs_filter.TFilter(overlap=None, existence=None,
                            recency=recs_filter.TRecencyFilter(range=recs_filter.TRange(max_=None, min_=-518400.0),
                                                               field='pubDate'), and_=None, range=None,
                            or_=None, any=None, named=None)], range=None, or_=None, any=None, named=None)
    request.groups['featured'] = req.RecGroupRequest(count=COUNT1, metafilter=metafilter)

    COUNT2 = 15
    metafilter = recs_filter.TFilter(overlap=None, existence=None, recency=None, and_=None, range=None, or_=None,
                                     any=None, named='GLOBAL')
    request.groups['articles'] = req.RecGroupRequest(count=COUNT2, metafilter=metafilter)

    config = {'host': rts_host, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT1 + COUNT2
