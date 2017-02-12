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
EMPTY_EXCLUDES = ['article|9257813cce8b2fed1630a8c47e409ad9', 'article|4697ea91e3e04b2730d9794088164c83',
                  'article|082a0f93e1aadae67d5aaf2aba2c9de8', 'article|7c1a152c1f49b9cf2823478fce6d65a6',
                  'website|4a741b31598b5c20089110cd2efc486e', 'article|adaea9e340a30bd0e8cda5038707d122',
                  'article|6df264902a4d3b45c802a8290f729b81', 'article|2e8aeeff27819080915bafc8c080ec2d']
TEST = True
GROUP_NAME = 'default'
CALLING_APP = 'test_client'


def test_rts(rts_host):
    COUNT = 4
    request = req.RecsRequest(site_id='f1c5057684a426566c7ac9984eae544b',
                              bsin='ca27b20d-7ca9-4643-ac02-843552f906f9',
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(existence=None, and_=None, or_=None, recency=None, overlap=None, any=None,
                                     named='GLOBAL', range=None)

    request.groups['all'] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)
    config = {'host': rts_host, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT
