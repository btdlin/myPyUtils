import pytest
import recs_client.request as req
import bt_rts.thrift.gen.filters as recs_filter
from recs_client.client import RecommendationsClient

# HOST = 'localhost'
HOST = 'realtime-recs-a.magic.boomtrain.com'
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
    ('WireFly', '92d7386bbdaae2999f701aa2a614eaeb'),
    ('IEEE', 'fc09a30ba1a4b43d0cc9990be2df89bb'),
    ('Vogue', '9b69d8fc8b441b43d493d713e5703ada'),
    ('THG', 'fe3d1b4f09f60315d2bbfb27557a10e3'),
    ('Rappler', '1a1e951c0be6ac5f7a57c617f1160972'),
    ('Kellogg Insight', '2a9897b9f56088c2916bb3403cfff631')
]



def test_metafilter_rappler():
    site_id = '1a1e951c0be6ac5f7a57c617f1160972'

    request = req.RecsRequest(site_id=site_id,
                              bsin=BSIN,
                              seeds=['article|156222'],
                              excludes=['article|156222'],
                              recset_id='7aa96f3a-c7a5-11e6-b95c-0e62f196a588',
                              test=False)

    metafilter = recs_filter.TFilter(overlap=None, recency=None, and_=[
        recs_filter.TFilter(overlap=None, recency=None, and_=None, existence=None, or_=None, named='GLOBAL', range=None),
        recs_filter.TFilter(overlap=recs_filter.TOverlapFilter(values=['Nigeria', 'Gombe'], field='keywords', amount=recs_filter.TRange(min_=1.0, max_=None),
                                       match_type=0), recency=None, and_=None, existence=None, or_=None, named=None,
                range=None)], existence=None, or_=None, named=None, range=None)

    request.groups[GROUP_NAME] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)
    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT
    for r in response:
        print(r)








@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_no_filter(customer_name, site_id):

    request = req.RecsRequest(site_id=site_id,
                              bsin=BSIN,
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    request.groups[GROUP_NAME] = req.RecGroupRequest(count=COUNT)
    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_global_filter(customer_name, site_id):

    request = req.RecsRequest(site_id=site_id,
                              bsin=BSIN,
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    filter = recs_filter.TFilter(and_=None, existence=None, range=None, recency=None,
                                 or_=None, named='GLOBAL', overlap=None)
    request.groups[GROUP_NAME] = req.RecGroupRequest(count=COUNT, metafilter=filter)
    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_metafilter(customer_name, site_id):

    request = req.RecsRequest(site_id=site_id,
                              bsin=BSIN,
                              seeds=EMPTY_SEEDS,
                              excludes=EMPTY_EXCLUDES,
                              recset_id=RECSET_ID,
                              test=TEST)

    metafilter = recs_filter.TFilter(overlap=None, recency=None, and_=[
        recs_filter.TFilter(overlap=None, recency=None, and_=None, existence=None, or_=None, named='GLOBAL', range=None),
        recs_filter.TFilter(overlap=recs_filter.TOverlapFilter(values=['NONE'], field='allowed_territories', amount=recs_filter.TRange(min_=1.0, max_=None),
                                       match_type=0), recency=None, and_=None, existence=None, or_=None, named=None,
                range=None),
        recs_filter.TFilter(overlap=recs_filter.TOverlapFilter(values=['DE'], field='resource-type', amount=recs_filter.TRange(min_=1.0, max_=None),
                                       match_type=0), recency=None, and_=None, existence=None, or_=None, named=None,
                range=None)], existence=None, or_=None, named=None, range=None)

    request.groups[GROUP_NAME] = req.RecGroupRequest(count=COUNT, metafilter=metafilter)
    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == COUNT

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
        recs_filter.TFilter(overlap=recs_filter.TOverlapFilter(values=['0'], field='closed', amount=recs_filter.TRange(min_=1.0, max_=None),
                                       match_type=0), recency=None, and_=None, existence=None, or_=None, named=None,
                range=None)], existence=None, or_=None, named=None, range=None)
    request.groups['pw_nofilter'] = req.RecGroupRequest(count=9, metafilter=metafilter)

    filter = recs_filter.TFilter(and_=None, existence=None, range=None, recency=None, or_=None, named='GLOBAL', overlap=None)
    request.groups['pw_watch_ind'] = req.RecGroupRequest(count=1, metafilter=filter)

    filter = recs_filter.TFilter(and_=None, existence=None, range=None, recency=None, or_=None, named='GLOBAL', overlap=None)
    request.groups['pw_watch_fam'] = req.RecGroupRequest(count=1, metafilter=filter)

    filter = recs_filter.TFilter(and_=None, existence=None, range=None, recency=None, or_=None, named='GLOBAL', overlap=None)
    request.groups['pw_bid_ind'] = req.RecGroupRequest(count=2, metafilter=filter)

    filter = recs_filter.TFilter(and_=None, existence=None, range=None, recency=None, or_=None, named='GLOBAL', overlap=None)
    request.groups['pw_bid_cat'] = req.RecGroupRequest(count=2, metafilter=filter)

    filter = recs_filter.TFilter(and_=None, existence=None, range=None, recency=None, or_=None, named='GLOBAL', overlap=None)
    request.groups['pw_watch_cat'] = req.RecGroupRequest(count=1, metafilter=filter)

    filter = recs_filter.TFilter(and_=None, existence=None, range=None, recency=None, or_=None, named='GLOBAL', overlap=None)
    request.groups['pw_bid_fam'] = req.RecGroupRequest(count=2, metafilter=filter)

    config = {'host': HOST, 'port': PORT, 'timeout': TIMEOUT}
    with RecommendationsClient(calling_app=CALLING_APP, **config) as client:
        response = client.get_recommendations(request)
    assert len(response) == 18
