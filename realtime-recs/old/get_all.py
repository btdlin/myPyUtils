from bt_candidates.wiring import default_schema_factory, default_filter_factory as f
from bt_candidates.client import Client
from bt_candidates.sorting import SortStrategy
from bt_candidates.common import FieldType, AmountType, MatchType
import pytest
import time
from datetime import timedelta

CLIENT = Client(host='candidates.aws.boomtrain.com', port=7070)

def test_global_filter():

    file = open('customer_list.txt', 'r')
    site_ids = [s.rstrip() for s in file if not s.startswith('#')]
    #print(site_ids)
    print('\n')

    for site_id in site_ids:
        candidates = CLIENT.get_candidates(site_id, filter=f.named_filter('GLOBAL'), limit=1000, sort_by=SortStrategy.POP_1D)
        if len(candidates) <= 20:
            print(site_id + ' has ' + str(len(candidates)) + ' resources.')
