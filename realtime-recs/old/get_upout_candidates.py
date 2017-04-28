from bt_candidates.wiring import default_schema_factory, default_filter_factory as f
from bt_candidates.client import Client
from bt_candidates.sorting import SortStrategy
from bt_candidates.common import FieldType, AmountType, MatchType
import pytest

CLIENT = Client(host='candidates.aws.boomtrain.com', port=7070)

testdata = [
    ('upout', '7a0f18a6274829b2e0710f57eea2b6d0')
]

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_global_filter(customer_name, site_id):
    candidates = CLIENT.get_candidates(site_id, filter=f.named_filter('GLOBAL'), limit=100, sort_by=SortStrategy.POP_1D)
    for c in candidates:
        print(c)
        assert c.event_counts is not None or c.base_score is not None


@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_global_filter_and_resource_type(customer_name, site_id):
    filter = f.overlap_filter(field='resource-type', values=['nyc'], min=1)
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter), limit=100,
                                       sort_by=SortStrategy.POP_1D)
    for c in candidates:
        print(c)
        assert c.event_counts is not None or c.base_score is not None
