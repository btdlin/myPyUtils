import pytest
import recs_client.request as req
import bt_rts.thrift.gen.filters as recs_filter
from recs_client.client import RecommendationsClient

HOST = 'realtime-recs-b.magic.boomtrain.com'
#HOST = 'rts.aws.boomtrain.com'
PORT = 7070
TIMEOUT = 20000
BSIN = '24675829-e147-4f83-ae97-f69e2c38dd28'
RECSET_ID = 'fakedb0c-c5c6-4515-9bd1-5a06ddd676f6'
EMPTY_SEEDS =[]
EMPTY_EXCLUDES =['website|a4564eeeac1a79fa5539044fb98f4185', 'thegazette_default|d73d63b3e436abc37a658e5837352f02']
TEST = True
GROUP_NAME = 'default'
COUNT = 4
CALLING_APP = 'test_client'

testdata = [
    ('Gazette', 'e9cd7a8ae2406275f6afb01b679ebf69')
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
        recs_filter.TFilter(overlap=recs_filter.TOverlapFilter(values=['thegazette_default'], field='resource-type', amount=recs_filter.TRange(min_=1.0, max_=None),
                                                               match_type=0), recency=None, and_=None, existence=None, or_=None, named=None, range=None)
    ], existence=None, or_=None, named=None, range=None)

    request.groups['thegazette_default'] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)

    metafilter = recs_filter.TFilter(overlap=None, recency=None, and_=[
        recs_filter.TFilter(overlap=None, recency=None, and_=None, existence=None, or_=None, named='GLOBAL', range=None),
        recs_filter.TFilter(overlap=recs_filter.TOverlapFilter(values=['thegazette_sports'], field='resource-type', amount=recs_filter.TRange(min_=1.0, max_=None),
                                                               match_type=0), recency=None, and_=None, existence=None, or_=None, named=None, range=None)
    ], existence=None, or_=None, named=None, range=None)

    request.groups['thegazette_sports'] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)

    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == 8
