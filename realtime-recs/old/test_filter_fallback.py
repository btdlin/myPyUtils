from bt_candidates.client import Client
from bt_candidates.wiring import default_filter_factory as ff
from bt_candidates.filters import MatchType
from bt_candidates.sorting import SortStrategy

client = Client('candidates.magic.boomtrain.com')
schema = client.get_schema('atlanta-black-star')

filt = ff.or_filter(
    ff.overlap_filter('title', ['Yohannes',  'IV'], match_type=MatchType.EXACT, min=2, max=2),
    ff.overlap_filter('title', ['Search', 'chicago'], match_type=MatchType.EXACT, min=2, max=2),
    ff.overlap_filter('title', ['african', 'history', 'month'], match_type=MatchType.EXACT, min=3, max=3)
)

candidates = client.get_candidates('atlanta-black-star', filt, limit=25)
print(len(candidates))
for c in candidates:
    print(c)

print('======================================================')

import itertools as it

def split_candidates(candidates, needed=10):
    to_score = []
    for _, grp in it.groupby(candidates, lambda c: c.sort_weight):
        grp = list(grp)
        if len(grp) > needed:
            to_score.extend(grp)
            return to_score
        else:
            to_score.extend(grp)

        needed -= len(grp)
    raise ValueError('too few candidates!', needed)


to_score = split_candidates(candidates, 5)
print(len(to_score))
for c in to_score:
    print(c)