from bt_candidates.wiring import default_schema_factory, default_filter_factory as f
from bt_candidates.client import Client
from bt_candidates.sorting import SortStrategy
from bt_candidates.common import FieldType, AmountType, MatchType
import pytest
import time
from datetime import timedelta

CLIENT = Client(host='candidates.aws.boomtrain.com', port=7070)

def test_global_filter():
    candidates = CLIENT.get_candidates('snopes', filter=f.named_filter('GLOBAL'), limit=1000, sort_by=SortStrategy.POP_1D)
    #print(candidates)
    assert len(candidates) > 1000000

def test_metafilter_resource_type_article():
    filter = f.overlap_filter(field='resource-type', values=['article'], min=1)
    candidates = CLIENT.get_candidates('snopes', filter=f.and_filter(f.named_filter('GLOBAL'), filter), limit=1000, sort_by=SortStrategy.POP_1D)
    assert len(candidates) == 1000
