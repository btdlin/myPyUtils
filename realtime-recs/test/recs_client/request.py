
import bt_rts.thrift.gen.recs as recs_thrift

from collections import defaultdict

class DeduplicationInstructions(object):

    def __init__(self, excludes, score_diff):
        self.score_diff = score_diff
        self.excludes = set(excludes or [])

    def to_thrift(self):
        return recs_thrift.TDeduplication(min_score_difference=self.score_diff,
                                          excludes=self.excludes)

class RecGroupRequest(object):

    def __init__(self, count, metafilter=None, types=None):
        self.count = count
        self.metafilter = metafilter
        self.types = set(types or [])

    def to_thrift(self):
        return recs_thrift.TRecGroupRequest(count=self.count,
                                            metafilter=self.metafilter)

class RecsRequest(object):
    def __init__(self, site_id, bsin, seeds, excludes, recset_id, test):
        self.site_id = site_id
        self.bsin = bsin
        self.seeds = list(seeds or [])
        self.excludes = excludes
        self.test = test

        self.groups = defaultdict(RecGroupRequest)
        self.deduplication = DeduplicationInstructions(excludes=excludes, score_diff=None)
        self.id = recset_id

    @property
    def count(self):
        return sum( group.count for group in self.groups.values() )

    def to_thrift(self):
        return recs_thrift.TRecsRequest( site_id=self.site_id,
                                         bsin=self.bsin,
                                         recset_id=self.id,
                                         groups={ k: v.to_thrift() for k, v in self.groups.items() },
                                         deduplication=self.deduplication.to_thrift(),
                                         seeds=self.seeds,
                                         request_features=recs_thrift.TRequestFeatures(is_test=self.test) )
