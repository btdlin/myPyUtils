from bt_candidates.wiring import default_schema_factory, default_filter_factory as f
from bt_candidates.client import Client
from bt_candidates.sorting import SortStrategy
from bt_candidates.common import FieldType, AmountType, MatchType
import pytest

CLIENT = Client(host='candidates.aws.boomtrain.com', port=7070)

testdata = [
    ('Hubspot', 'hubspot-blog'),
    ('Atlanta Black Star', 'atlanta-black-star'),
    ('WireFly', '92d7386bbdaae2999f701aa2a614eaeb'),
    ('IEEE', 'fc09a30ba1a4b43d0cc9990be2df89bb'),
    ('Vogue', '9b69d8fc8b441b43d493d713e5703ada'),
    ('THG', 'fe3d1b4f09f60315d2bbfb27557a10e3'),
    ('Rappler', '1a1e951c0be6ac5f7a57c617f1160972'),
    ('Kellogg Insight', '2a9897b9f56088c2916bb3403cfff631'),
    ('YP Canada EN', '593964c3c0f76bc59c65b324f9dbf869'),
    ('Hubspot', 'hubspot-blog')
]

def test_yp_resource_type_lists_en():
    site_id = "593964c3c0f76bc59c65b324f9dbf869"
    filter = f.overlap_filter(field='resource-type', values=['lists_en'], min=1)
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter), limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) > 0

def test_yp_cityRegion_Toronto():
    site_id = "593964c3c0f76bc59c65b324f9dbf869"
    filter = f.overlap_filter(field='cityRegion', values=['Toronto'], min=1)
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter), limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) == 100 

def test_yp_resource_type_lists_en_cityRegion_Toronto():
    site_id = "593964c3c0f76bc59c65b324f9dbf869"
    filter_item_type = f.overlap_filter(field='resource-type', values={'lists_en'}, min=1, match_type=MatchType.CONTAINS)
    filter_city_region = f.overlap_filter(field='cityRegion', values={'toronto'}, min=1, match_type=MatchType.CONTAINS)
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter_item_type, filter_city_region), limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) == 100
    resource_ids = [candidate.resource_id for candidate in candidates]
    resources = CLIENT.get_resources(site_id=site_id, ids=resource_ids).resources
    city_regions = [resource.to_jsonobj()['fields']['cityRegion'] for resource in resources]
    for city_region in city_regions:
        assert ('toronto' in city_region) or ('Toronto' in city_region)

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_no_filter(customer_name, site_id):
    candidates = CLIENT.get_candidates(site_id, filter=None, limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) > 0

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_global_filter(customer_name, site_id):
    candidates = CLIENT.get_candidates(site_id, filter=f.named_filter('GLOBAL'), limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) > 0

testdata_metafilter_resource_type_article = [
    ('Hubspot', 'hubspot-blog'),
    ('Atlanta Black Star', 'atlanta-black-star'),
    ('WireFly', '92d7386bbdaae2999f701aa2a614eaeb'),
    ('IEEE', 'fc09a30ba1a4b43d0cc9990be2df89bb'),
    ('Vogue', '9b69d8fc8b441b43d493d713e5703ada'),
    ('Rappler', '1a1e951c0be6ac5f7a57c617f1160972'),
    ('Kellogg Insight', '2a9897b9f56088c2916bb3403cfff631'),
    ('Hubspot', 'hubspot-blog')
]
@pytest.mark.parametrize("customer_name, site_id", testdata_metafilter_resource_type_article)
def test_metafilter_resource_type_article(customer_name, site_id):
    filter = f.overlap_filter(field='resource-type', values=['article'], min=1)
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter), limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) > 0

testdata_metafilter_resource_type_news = [
    ('WireFly', '92d7386bbdaae2999f701aa2a614eaeb'),
    ('IEEE', 'fc09a30ba1a4b43d0cc9990be2df89bb'),
    ('Kellogg Insight', '2a9897b9f56088c2916bb3403cfff631')
]
@pytest.mark.parametrize("customer_name, site_id", testdata_metafilter_resource_type_news)
def test_metafilter_resource_type_news(customer_name, site_id):
    filter = f.overlap_filter(field='resource-type', values=['News'], min=1)
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter), limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) > 0

testdata_metafilter_module = [
    ('Hubspot', 'hubspot-blog'),
    ('Atlanta Black Star', 'atlanta-black-star'),
    ('WireFly', '92d7386bbdaae2999f701aa2a614eaeb'),
    ('Vogue', '9b69d8fc8b441b43d493d713e5703ada'),
    ('THG', 'fe3d1b4f09f60315d2bbfb27557a10e3'),
    ('Rappler', '1a1e951c0be6ac5f7a57c617f1160972'),
    ('Kellogg Insight', '2a9897b9f56088c2916bb3403cfff631'),
    ('YP Canada EN', '593964c3c0f76bc59c65b324f9dbf869'),
    ('Hubspot', 'hubspot-blog')
]
@pytest.mark.parametrize("customer_name, site_id", testdata_metafilter_module)
def test_metafilter_module(customer_name, site_id):
    filter = f.overlap_filter(field='module', values=['Sponsored'], min=1)
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter), limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) > 0

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_metafilter_module_not(customer_name, site_id):
    filter = f.overlap_filter(field='module', values=['Sponsored'], min=0, max=0)
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter), limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) > 0

testdata_metafilter_keywords = [
    ('Hubspot', 'hubspot-blog'),
    ('Rappler', '1a1e951c0be6ac5f7a57c617f1160972'),
    ('Kellogg Insight', '2a9897b9f56088c2916bb3403cfff631'),
    ('YP Canada EN', '593964c3c0f76bc59c65b324f9dbf869'),
    ('Hubspot', 'hubspot-blog')
]
#@pytest.mark.skip(reason="Not sure if this works for all customers")
@pytest.mark.parametrize("customer_name, site_id", testdata_metafilter_keywords)
def test_metafilter_keywords(customer_name, site_id):
    filter = f.overlap_filter(field='keywords', values=['Marketing'], min=1)
    #filter = f.overlap_filter(field='keywords', values=['Nokia', 'HMD Global'], min=1)
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter), limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) > 0
