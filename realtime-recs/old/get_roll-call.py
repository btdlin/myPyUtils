from bt_candidates.wiring import default_schema_factory, default_filter_factory as f
from bt_candidates.client import Client
from bt_candidates.sorting import SortStrategy
from bt_candidates.common import FieldType, AmountType, MatchType
import pytest
import time
from datetime import timedelta

CLIENT = Client(host='candidates.aws.boomtrain.com', port=7070)

testdata = [
    ('roll-call', 'roll-call')
]

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_global_filter(customer_name, site_id):
    candidates = CLIENT.get_candidates(site_id, filter=f.named_filter('GLOBAL'), limit=1000, sort_by=SortStrategy.POP_1D)
#    print(candidates)
    for c in candidates:
        print(c)
    assert len(candidates) > 1000000

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_pubdate_8hr_after(customer_name, site_id):
    filter1 = f.recency_filter(
                        field = 'pubDate',
                        min = timedelta(hours=-8),
                        )
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter1), limit=100, sort_by=SortStrategy.POP_1D)
    for c in candidates:
        print(c)
    assert len(candidates) > 100000

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_pubdate_96hr_after(customer_name, site_id):
    filter1 = f.recency_filter(
                        field = 'pubDate',
                        min = timedelta(hours=-96),
                        )
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter1), limit=100, sort_by=SortStrategy.POP_1D)
    for c in candidates:
        print(c)
    assert len(candidates) > 100000

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_pubdate_48hr_after(customer_name, site_id):
    filter1 = f.recency_filter(
                        field = 'pubDate',
                        min = timedelta(hours=-48),
                        )
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter1), limit=100, sort_by=SortStrategy.POP_1D)
    for c in candidates:
        print(c)
    assert len(candidates) > 100000
@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_pubdate_19hr_after(customer_name, site_id):
    filter1 = f.recency_filter(
                        field = 'pubDate',
                        min = timedelta(hours=-19),
                        max = timedelta(hours=-8),
                        )
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter1), limit=100, sort_by=SortStrategy.POP_1D)
    for c in candidates:
        print(c)
    assert len(candidates) > 100000

#@pytest.mark.parametrize("customer_name, site_id", testdata)
#def test_pubdate_48hr_after(customer_name, site_id):
#    filter1 = f.recency_filter(
#                        field = 'pubDate',
#                        min = timedelta(hours=-48),
#                        max = timedelta(hours=-19),
#                        )
#    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter1), limit=100, sort_by=SortStrategy.POP_1D)
#    for c in candidates:
#        print(c)
#    assert len(candidates) > 100000
