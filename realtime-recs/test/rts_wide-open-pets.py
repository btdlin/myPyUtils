import pytest
import recs_client.request as req
import bt_rts.thrift.gen.filters as recs_filter
from recs_client.client import RecommendationsClient

HOST = 'realtime-recs-k.magic.boomtrain.com'
#HOST = 'rts.aws.boomtrain.com'
#HOST = 'localhost'
PORT = 7070
TIMEOUT = 20000
BSIN = '18caa8db-842e-4391-b4c5-735b04b291aa'
RECSET_ID = 'fakedb0c-c5c6-4515-9bd1-5a06ddd676f6'
EMPTY_SEEDS =[]
EMPTY_EXCLUDES =["website|f85dddf3e1ca270e15fafca82f543513", "website|f85dddf3e1ca270e15fafca82f543513", "object|f4d313850813416f4b1444a53f6b38ba", "object|ac790f3d15859fc9010587b3fb4c9949", "object|6f7029df366501a7b891e302fb340344", "object|83f4fcfaf89d92c8c9e3bdd1eda79f8f", "article|3ac7a94e43f45d6c1edbbbb18fb76200", "article|e5a5fda951cd6d86e88efc9dd555fd77"]
TEST = True
GROUP_NAME = 'default'
COUNT1 = 1
COUNT2 = 15
CALLING_APP = 'test_client'

testdata = [
    ('wide-open-pets', 'wide-open-pets')
]

def test_rts():

    request = req.RecsRequest(site_id='wide-open-pets',
                              bsin=BSIN,
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(existence=None, and_=[recs_filter.TFilter(existence=None, and_=None, or_=None, recency=None, overlap=None, any=None, named='GLOBAL', range=None), recs_filter.TFilter(existence=None, and_=None, or_=None, recency=recs_filter.TRecencyFilter(range=recs_filter.TRange(min_=-518400.0, max_=None), field='pubDate'), overlap=None, any=None, named=None, range=None)], or_=None, recency=None, overlap=None, any=None, named=None, range=None)
    request.groups['featured'] = req.RecGroupRequest(count=COUNT1, metafilter=metafilter)

    metafilter = recs_filter.TFilter(existence=None, and_=None, or_=None, recency=None, overlap=None, any=None, named='GLOBAL', range=None)
    request.groups['articles'] = req.RecGroupRequest(count=COUNT2, metafilter=metafilter)


    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT1 + COUNT2
