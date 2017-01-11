import pytest
import recs_client.request as req
import bt_rts.thrift.gen.filters as recs_filter
from recs_client.client import RecommendationsClient

HOST = 'realtime-recs-b.magic.boomtrain.com'
#HOST = 'rts.aws.boomtrain.com'
PORT = 7070
TIMEOUT = 20000
BSIN = 'ec5e00d4-6386-4cf7-a1d1-ea0e4f7d8a8c'
RECSET_ID = 'fakedb0c-c5c6-4515-9bd1-5a06ddd676f6'
EMPTY_SEEDS =[]
EMPTY_EXCLUDES =[]
TEST = True
GROUP_NAME = 'default'
COUNT = 2
CALLING_APP = 'test_client'

testdata = [
    ('Kellogg Insight', '2a9897b9f56088c2916bb3403cfff631')
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
        recs_filter.TFilter(overlap=None, recency=None, and_=None, existence=None, or_=None, named='GLOBAL', range=None)
                ], existence=None, or_=None, named=None, range=None)

    request.groups[GROUP_NAME] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)
    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT

