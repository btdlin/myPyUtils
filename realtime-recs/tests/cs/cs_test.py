from bt_candidates.wiring import default_schema_factory, default_filter_factory as f
from bt_candidates.client import Client
from bt_candidates.sorting import SortStrategy
import pytest

CLIENT = Client(host='candidates.aws.boomtrain.com', port=7070)

testdata = [
    ('WireFly', '92d7386bbdaae2999f701aa2a614eaeb'),
    ('IEEE', 'fc09a30ba1a4b43d0cc9990be2df89bb'),
    ('Vogue', '9b69d8fc8b441b43d493d713e5703ada'),
    ('THG', 'fe3d1b4f09f60315d2bbfb27557a10e3'),
    ('Rappler', '1a1e951c0be6ac5f7a57c617f1160972'),
    ('Kellogg Insight', '2a9897b9f56088c2916bb3403cfff631')
]

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_no_filter(customer_name, site_id):
    candidates = CLIENT.get_candidates(site_id, filter=None, limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) > 0

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_global_filter(customer_name, site_id):
    client = Client(host='candidates.aws.boomtrain.com', port=7070)
    candidates = client.get_candidates(site_id, filter=f.named_filter('GLOBAL'), limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) > 0

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_metafilter_resource_type_article(customer_name, site_id):
    filter = f.overlap_filter(field='resource-type', values=['article'], min=1)
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter), limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) > 0

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_metafilter_resource_type_news(customer_name, site_id):
    filter = f.overlap_filter(field='resource-type', values=['News'], min=1)
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter), limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) > 0

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_metafilter_module(customer_name, site_id):
    filter = f.overlap_filter(field='module', values=['Sponsored'], min=1)
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter), limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) > 0

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_metafilter_module_not(customer_name, site_id):
    filter = f.overlap_filter(field='module', values=['Sponsored'], min=0, max=0)
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter), limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) > 0

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_metafilter_keywords(customer_name, site_id):
    filter = f.overlap_filter(field='keywords', values=['Nokia', 'HMD Global'], min=1)
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter), limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) > 0
