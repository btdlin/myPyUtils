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
EMPTY_EXCLUDES = ['article|d4eec3604fdc8d074acca588da415a5f', 'article|8c3fc7b9c25419e76b2dfb264ad34a2a',
                  'article|3cbc71a1038cb5c6b336adb4e7c8b669']
TEST = True
GROUP_NAME = 'default'
CALLING_APP = 'test_client'


def test_rts(rts_host):
    COUNT = 4
    request = req.RecsRequest(site_id='e0d1ed8756329211967755e409bfbfac',
                              bsin='150a2bcd-5f3d-44e7-94f0-b53d879a5360',
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(overlap=None, existence=None, recency=None, and_=[
        recs_filter.TFilter(overlap=None, existence=None, recency=None, and_=None, range=None, or_=None, any=None, named='GLOBAL'),
        recs_filter.TFilter(overlap=recs_filter.TOverlapFilter(values=['article'], field='resource-type', match_type=0,
                                       amount=recs_filter.TRange(max_=None, min_=1.0)), existence=None, recency=None, and_=None,
                range=None, or_=None, any=None, named=None)], range=None, or_=None, any=None, named=None)

    request.groups[GROUP_NAME] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)
    config = {'host': rts_host, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT
