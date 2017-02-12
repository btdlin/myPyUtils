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
EMPTY_EXCLUDES = ['article|63', 'article|297', 'article|921507', 'article|2519', 'article|124798', 'article|174749',
                  'article|109128', 'article|920585', 'article|121448', 'website|919945', 'article|143557',
                  'article|204549', 'article|569091', 'article|132387', 'article|391663']
TEST = True
GROUP_NAME = 'default'
CALLING_APP = 'test_client'


def test_rts(rts_host):
    COUNT = 6
    request = req.RecsRequest(site_id='finder',
                              bsin='c5b7a9cf-7977-4da5-acaa-aa4ad3d03b69',
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(existence=None, and_=[
        recs_filter.TFilter(existence=None, and_=None, or_=None, recency=None, overlap=None, any=None, named='GLOBAL',
                            range=None),
        recs_filter.TFilter(existence=None, and_=None, or_=None,
                            recency=recs_filter.TRecencyFilter(range=recs_filter.TRange(min_=-604800.0, max_=None),
                                                               field='pubDate'), overlap=None,
                            any=None, named=None, range=None),
        recs_filter.TFilter(existence=None, and_=None, or_=None, recency=None,
                            overlap=recs_filter.TOverlapFilter(amount=recs_filter.TRange(min_=1.0, max_=None),
                                                               values=['top story', 'lead story'],
                                                               field='tag', match_type=0), any=None,
                            named=None, range=None),
        recs_filter.TFilter(existence=None, and_=None, or_=None, recency=None,
                            overlap=recs_filter.TOverlapFilter(amount=recs_filter.TRange(min_=1.0, max_=None),
                                                               values=['broadband plans', 'streaming',
                                                                       'music streaming', 'apps',
                                                                       'mobile plans', 'cheap phones', 'software',
                                                                       'gaming', 'wearables',
                                                                       'internet tv', 'virtual privacy network',
                                                                       'technology', 'mobile phones',
                                                                       'nbn tracker'], field='section', match_type=0),
                            any=None, named=None,
                            range=None)], or_=None, recency=None, overlap=None, any=None, named=None, range=None)

    request.groups['finder_tech'] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)

    config = {'host': rts_host, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT
