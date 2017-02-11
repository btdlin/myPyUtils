from bt_candidates.wiring import default_schema_factory, default_filter_factory as f
from bt_candidates.client import Client
from bt_candidates.sorting import SortStrategy
from bt_candidates.common import FieldType, AmountType, MatchType
import pytest
import time
from datetime import timedelta

CLIENT = Client(host='candidates.aws.boomtrain.com', port=7070)

def test_metafilter_resource_type_all():
    filter = f.overlap_filter(field='resource-type', values=['all'], min=1)
    candidates = CLIENT.get_candidates("wide-open-spaces", filter=f.and_filter(f.named_filter('GLOBAL'), filter), limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) > 0
