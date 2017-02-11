import pytest
import recs_client.request as req
import bt_rts.thrift.gen.filters as recs_filter
from recs_client.client import RecommendationsClient

#HOST = 'localhost'
HOST = 'realtime-recs-k.magic.boomtrain.com'
#HOST = 'rts.aws.boomtrain.com'
PORT = 7070
TIMEOUT = 20000
BSIN = '35ae7c05-7d85-49f7-abb3-60e35651a397'
RECSET_ID = 'fakedb0c-c5c6-4515-9bd1-5a06ddd676f6'
EMPTY_SEEDS =[]
EMPTY_EXCLUDES =[]
TEST = True
GROUP_NAME = 'default'
COUNT = 4
CALLING_APP = 'test_client'

testdata = [
    ('Hubspot', 'hubspot-blog')
]

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_group_metafilter(customer_name, site_id):

    request = req.RecsRequest(site_id=site_id,
                              bsin=BSIN,
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(overlap=None, recency=None, and_=[
        recs_filter.TFilter(overlap=None, recency=None, and_=None, existence=None, or_=None, named='GLOBAL', range=None),
        recs_filter.TFilter(overlap=recs_filter.TOverlapFilter(values=['Marketing'], field='keywords', amount=recs_filter.TRange(min_=1.0, max_=None),
                                                               match_type=0), recency=None, and_=None, existence=None, or_=None, named=None, range=None)
    ], existence=None, or_=None, named=None, range=None)

    request.groups['default'] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)

    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == 4
