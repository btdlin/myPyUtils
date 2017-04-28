from bt_candidates.wiring import default_schema_factory, default_filter_factory as f
from bt_candidates.client import Client
from bt_candidates.sorting import SortStrategy
from bt_candidates.common import FieldType, AmountType, MatchType
import pytest
import time
from datetime import timedelta

CLIENT = Client(host='candidates.aws.boomtrain.com', port=7070)

def test_global_filter():
    candidates = CLIENT.get_candidates('sharecare', filter=f.named_filter('GLOBAL'), limit=1000, sort_by=SortStrategy.POP_1D)
    #print(candidates)
    assert len(candidates) > 1000000
