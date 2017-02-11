from bt_candidates.client import Client
from bt_candidates.wiring import default_schema_factory as sf
from bt_candidates.wiring import default_filter_factory as ff
from bt_candidates.common import FieldType, AmountType, MatchType
from bt_candidates.resource_schema import SchemaField, ResourceSchema, DataFormat, DataLoader
from datetime import timedelta
from bt_candidates.sorting import SortStrategy

client = Client(host='candidates.aws.boomtrain.com', port=7070)

site_id = "e9cd7a8ae2406275f6afb01b679ebf69"
schema = client.get_schema(site_id)


def test_gazette():
    filter_resource_type = ff.overlap_filter(field='resource-type', values={'thegazette_sports'}, min=1, match_type=MatchType.CONTAINS)
    filter_meta_global = ff.and_filter(filter_resource_type, schema.named_filters['GLOBAL'])

    candidates = client.get_candidates(site_id=site_id, filter=filter_meta_global, limit=100, sort_by=SortStrategy.POP_1D)

    assert len(candidates) == 100

    resource_ids = [candidate.resource_id for candidate in candidates]
    resources = client.get_resources(site_id=site_id, ids=resource_ids).resources
    resource_types = [resource.to_jsonobj()['fields']['resource-type'] for resource in resources]
    for resource_type in resource_types:
        assert 'thegazette_sports' in resource_type
