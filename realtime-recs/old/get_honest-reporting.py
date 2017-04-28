from bt_candidates.wiring import default_schema_factory, default_filter_factory as f
from bt_candidates.client import Client
from bt_candidates.sorting import SortStrategy
from bt_candidates.common import FieldType, AmountType, MatchType
import pytest
import time
from datetime import timedelta

CLIENT = Client(host='candidates.aws.boomtrain.com', port=7070)

testdata = [
    ('honest-reporting', 'honest-reporting')
]

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_global_filter(customer_name, site_id):
    candidates = CLIENT.get_candidates(site_id, filter=f.named_filter('GLOBAL'), limit=1000, sort_by=SortStrategy.POP_1D)
    assert len(candidates) == 1000

def test_long_beach_post_pubdate_after():
    site_id = 'long-beach-post'
    filter1 = f.recency_filter(
                        field = 'pubDate',
                        min = timedelta(days=-30),
                        )
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter1), limit=1000, sort_by=SortStrategy.POP_1D)
    assert len(candidates) == 1000
