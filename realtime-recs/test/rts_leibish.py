import pytest
import recs_client.request as req
import bt_rts.thrift.gen.filters as recs_filter
from recs_client.client import RecommendationsClient

rts_host = 'realtime-recs-k.magic.boomtrain.com'
#rts_host = 'rts.aws.boomtrain.com'
#rts_host = 'localhost'
PORT = 7070
TIMEOUT = 20000
BSIN = '18e5cb36-3eca-45fb-a1d0-5cdc58c94a46'
RECSET_ID = 'fakedb0c-c5c6-4515-9bd1-5a06ddd676f6'
EMPTY_SEEDS =[]
EMPTY_EXCLUDES =["home_page|998c8eea5f4d7325b772a00d63dfae7e", "|2f6dfeaed24dc4db3a9ae80a6efc1d9d", "|f54ff3aa81e108897940e32fa82af533", "|ea6c06dd8e2c8b7ce643709c7584c0d6", "|4b722b38361e853b384aba9cf29c126a", "|d9991f15e6e5a4b83c3ed94d0f2ed057"]
TEST = True
GROUP_NAME = 'default'
COUNT = 5
CALLING_APP = 'test_client'

testdata = [
    ('Leibish', '8bf9fa832a2cf351cf1a19098038459d')
]

def test_rts(rts_host):

    request = req.RecsRequest(site_id='8bf9fa832a2cf351cf1a19098038459d',
                              bsin=BSIN,
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(existence=None, and_=[recs_filter.TFilter(existence=None, and_=None, or_=None, recency=None, overlap=None, any=None, named='GLOBAL', range=None), recs_filter.TFilter(existence=None, and_=None, or_=None, recency=recs_filter.TRecencyFilter(range=recs_filter.TRange(min_=-604800.0, max_=None), field='pubDate'), overlap=None, any=None, named=None, range=None), recs_filter.TFilter(existence=None, and_=None, or_=None, recency=None, overlap=recs_filter.TOverlapFilter(amount=recs_filter.TRange(min_=1.0, max_=None), values=['article_alist'], field='resource-type', match_type=0), any=None, named=None, range=None)], or_=None, recency=None, overlap=None, any=None, named=None, range=None)

    request.groups['articles'] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)

    config = {'host': rts_host, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT
