from bt_candidates.wiring import default_schema_factory, default_filter_factory as f
from bt_candidates.client import Client
from bt_candidates.sorting import SortStrategy
from bt_candidates.common import FieldType, AmountType, MatchType
import pytest
import time
from datetime import timedelta

CLIENT = Client(host='candidates.aws.boomtrain.com', port=7070)

testdata = [
    ('gamespot', '0eddb34d4eb4be1df2b4160ec047aa73')
]

@pytest.mark.parametrize("customer_name, site_id", testdata)
def test_global_filter(customer_name, site_id):
    candidates = CLIENT.get_candidates(site_id, filter=f.named_filter('GLOBAL'), limit=1000, sort_by=SortStrategy.POP_1D)
    print(candidates)
    assert len(candidates) > 1000000

