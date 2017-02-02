from bt_candidates.wiring import default_schema_factory, default_filter_factory as f
from bt_candidates.client import Client
from bt_candidates.sorting import SortStrategy
from bt_candidates.common import FieldType, AmountType, MatchType
import pytest
import time
from datetime import timedelta

CLIENT = Client(host='candidates.aws.boomtrain.com', port=7070)

def test_upout_resource_type_nyc():
    site_id = "7a0f18a6274829b2e0710f57eea2b6d0"
    filter = f.overlap_filter(field='resource-type', values=['nyc'], min=1)
    candidates = CLIENT.get_candidates(site_id, filter=f.and_filter(f.named_filter('GLOBAL'), filter), limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) == 100

    for c in candidates:
        print(c)
        assert (c.event_counts is not None or c.base_score is not None)
        

