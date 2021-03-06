import pytest
import recs_client.request as req
import bt_rts.thrift.gen.filters as recs_filter
from recs_client.client import RecommendationsClient

#HOST = 'realtime-recs-e.magic.boomtrain.com'
HOST = 'localhost'
#HOST = 'realtime-recs-b.magic.boomtrain.com'
PORT = 7070
TIMEOUT = 20000
BSIN = 'f6cb11da-3342-4849-a098-2efe94f8e80e'
RECSET_ID = 'fakedb0c-c5c6-4515-9bd1-5a06ddd676f6'
EMPTY_SEEDS =[]
EMPTY_EXCLUDES =[]
TEST = True
GROUP_NAME = 'default'
COUNT = 2
CALLING_APP = 'test_client'

testdata = [
    ('Atlanta Black Star', 'atlanta-black-star')
]

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_metafilter_resource_type_article(customer_name, site_id):

    request = req.RecsRequest(site_id=site_id,
                              bsin=BSIN,
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(overlap=None, recency=None, and_=[
        recs_filter.TFilter(overlap=None, recency=None, and_=None, existence=None, or_=None, named='GLOBAL', range=None),
        #recs_filter.TFilter(overlap=recs_filter.TOverlapFilter(values=['文章'], field='resource-type', amount=recs_filter.TRange(min_=1.0, max_=None),
        recs_filter.TFilter(overlap=recs_filter.TOverlapFilter(values=['article'], field='resource-type', amount=recs_filter.TRange(min_=1.0, max_=None),
                                       match_type=0), recency=None, and_=None, existence=None, or_=None, named=None,
                range=None)], existence=None, or_=None, named=None, range=None)

    request.groups[GROUP_NAME] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)
    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT

