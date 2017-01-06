from bt_candidates.wiring import default_schema_factory, default_filter_factory as f
from bt_candidates.client import Client
from bt_candidates.sorting import SortStrategy
from bt_candidates.common import FieldType, AmountType, MatchType
from datetime import timedelta

client = Client(host='candidates.aws.boomtrain.com', port=7070)
vogue = "9b69d8fc8b441b43d493d713e5703ada"
filter_two_days = f.recency_filter(
                        field = 'pubDate',
                        min = timedelta(days=-2),
                        max = timedelta(days=1),
                        )

filter_five_days = f.recency_filter(
                        field = 'pubDate',
                        min = timedelta(days=-5),
                        max = timedelta(days=1),
                        )

recency_fallback_filter = f.or_filter(filter_two_days, filter_five_days)
candidates_two_days = client.get_candidates(site_id=vogue, filter=filter_two_days, limit=100)
count1 = len(candidates_two_days)
print("Candidates applying two days filter : {}".format(count1))
fallback_candidates = client.get_candidates(site_id=vogue, filter=recency_fallback_filter, limit=100)
count2 = len(fallback_candidates)
print("Candidates applying the recency fallback to 5 days : {}".format(count2))
if(count1 < 100) and (count1 > count2):
    print("Error")
else:
    print("number of candidates added by fallback is {}".format(count2 - count1))
