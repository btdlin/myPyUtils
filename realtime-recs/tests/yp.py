from bt_candidates.client import Client
from bt_candidates.wiring import default_schema_factory as sf
from bt_candidates.wiring import default_filter_factory as ff
from bt_candidates.common import FieldType, AmountType, MatchType
from bt_candidates.resource_schema import SchemaField, ResourceSchema, DataFormat, DataLoader
from datetime import timedelta

client = Client(host='candidates.aws.boomtrain.com', port=7070)

# yellow pages.
site_id = "593964c3c0f76bc59c65b324f9dbf869"
schema = client.get_schema(site_id)

filter_item_type = ff.overlap_filter(field='itemType', values={'lists_en'}, min=1, match_type=MatchType.CONTAINS)
filter_city_region = ff.overlap_filter(field='cityRegion', values={'toronto'}, min=1, match_type=MatchType.CONTAINS)
filter_meta = ff.and_filter(filter_item_type,filter_city_region)
filter_meta_global = ff.and_filter(filter_item_type, filter_city_region, schema.named_filters['GLOBAL'])

candidates_meta = client.get_candidates(site_id=site_id, filter=filter_meta, limit=100)
candidates_meta_global = client.get_candidates(site_id=site_id, filter=filter_meta_global, limit=100)

if(len(candidates_meta) < 100):
    assert('Less than 100 candidates found for itemtype and city_region filter')

if(len(candidates_meta_global) < 100):
    assert('Less than 100 candidates found for item_type and city_region filter which also pass the GLOBAL filter')

def test_city_regions(candidates):
    resource_ids = [candidate.resource_id for candidate in candidates]
    resources = client.get_resources(site_id=site_id, ids=resource_ids).resources
    city_regions = [resource.to_jsonobj()['fields']['cityRegion'] for resource in resources]
    for city_region in city_regions:
        if ('toronto' not in city_region) and ('Toronto' not in city_region):
            assert('This resource is incorrect!!!')

    print("Successfully passed the city_region test")

test_city_regions(candidates_meta)
test_city_regions(candidates_meta_global)
