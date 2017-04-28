from bt_candidates.wiring import default_schema_factory, default_filter_factory as f
from bt_candidates.client import Client
from bt_candidates.sorting import SortStrategy

CLIENT = Client(host='candidates.aws.boomtrain.com', port=7070)

def test_global_filter():
#    candidates = CLIENT.get_candidates('9b69d8fc8b441b43d493d713e5703ada', filter=None, limit=100, sort_by=SortStrategy.POP_1D)
    candidates = CLIENT.get_candidates('9b69d8fc8b441b43d493d713e5703ada', filter=f.named_filter('GLOBAL'), limit=100, sort_by=SortStrategy.POP_1D)
    assert len(candidates) == 100

