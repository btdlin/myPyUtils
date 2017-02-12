import pytest
import recs_client.request as req
import bt_rts.thrift.gen.filters as recs_filter
from recs_client.client import RecommendationsClient

#rts_host = 'localhost'
rts_host = 'realtime-recs-k.magic.boomtrain.com'
#rts_host = 'rts.aws.boomtrain.com'
PORT = 7070
TIMEOUT = 20000
BSIN = '9d62d431-3c4d-4eff-aacb-c77643f97b9f'
RECSET_ID = 'fakedb0c-c5c6-4515-9bd1-5a06ddd676f6'
EMPTY_SEEDS =[]
EMPTY_EXCLUDES =["website_alist|44224", "website_alist|23013", "website_alist|23012", "website_alist|44224"]
TEST = True
GROUP_NAME = 'default'
COUNT = 5
CALLING_APP = 'test_client'

testdata = [
    ('alistdaily', '883617d0eb6793113323ba5e36470778')
]

def test_rts(rts_host):

    request = req.RecsRequest(site_id='883617d0eb6793113323ba5e36470778',
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
