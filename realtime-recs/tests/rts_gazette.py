import pytest
import recs_client.request as req
import bt_rts.thrift.gen.filters as recs_filter
from recs_client.client import RecommendationsClient

HOST = 'realtime-recs-c.magic.boomtrain.com'
#HOST = 'rts.aws.boomtrain.com'
#HOST = 'localhost'
PORT = 7070
TIMEOUT = 20000
#BSIN = '24675829-e147-4f83-ae97-f69e2c38dd28'
BSIN = 'f7cd7674-2922-45e0-950e-3a7ce2c44d60'
RECSET_ID = 'fakedb0c-c5c6-4515-9bd1-5a06ddd676f6'
EMPTY_SEEDS =[]
EMPTY_EXCLUDES =['thegazette_default|7c491eccfe7846ab027a1edb667aae3a',
                 'thegazette_default|f6e5643c047044bba83e181c3832e4fa',
                 'thegazette_default|1cac764d7228097f49614d07ebb054f8',
                 'thegazette_default|f72849dc88231f4428c48fdeeb37951d',
                 'thegazette_default|ab50508da2cdca277caeda98995a0e42',
                 'thegazette_default|f9bbabd2e068318ef394d53fdeafc075']
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

#    metafilter = recs_filter.TFilter(overlap=None, recency=None, and_=[
#        recs_filter.TFilter(overlap=None, recency=None, and_=None, existence=None, or_=None, named='GLOBAL', range=None),
#        recs_filter.TFilter(overlap=recs_filter.TOverlapFilter(values=['thegazette_default'], field='resource-type', amount=recs_filter.TRange(min_=1.0, max_=None),
#                                                               match_type=0), recency=None, and_=None, existence=None, or_=None, named=None, range=None)
#    ], existence=None, or_=None, named=None, range=None)
#
#    request.groups['thegazette_default'] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)

    metafilter = recs_filter.TFilter(overlap=None, recency=None, and_=[
        recs_filter.TFilter(overlap=None, recency=None, and_=None, existence=None, or_=None, named='GLOBAL', range=None),
        recs_filter.TFilter(overlap=recs_filter.TOverlapFilter(values=['thegazette_sports'], field='resource-type', amount=recs_filter.TRange(min_=1.0, max_=None),
                                                               match_type=0), recency=None, and_=None, existence=None, or_=None, named=None, range=None)
    ], existence=None, or_=None, named=None, range=None)

    request.groups['thegazette_sports'] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)

    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT 
