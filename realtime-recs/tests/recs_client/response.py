import bt_rts.thrift.gen.recs as recs_thrift

class Recommendation(object):

    DEFAULT_GROUP_NAME = 'default'
    STR_TEMPLATE = '[Recommendation: {0}:{1}:{2} Resource: {3}; Score: {4}; Models Used: {5}]'

    def __init__(self, recset_id, group, position, resource, score,
                       models, recommender, experiment, recommendation_time,
                       test):
        self.recset_id = recset_id
        self.group = group
        self.position = position
        self.resource = resource
        self.score = score
        self.models = models or set()
        self.recommender = recommender
        self.experiment = experiment
        self.recommendation_time = recommendation_time
        self.test = test

        #for backwards compatibility:
        self.is_personalized = self.models and 'Popular' not in self.models
        try:
          self.resource_type = self.resource.split('|')[0]
          self.resource_id = self.resource.split('|')[1]
        except:
          self.resource_type = None
          self.resource_id = None

    def __str__(self):
        return Recommendation.STR_TEMPLATE.format( self.recset_id,
                                                   self.group,
                                                   self.position,
                                                   self.resource,
                                                   self.score,
                                                   self.models )

    @classmethod
    def from_thrift(cls, recommendation):
        params = recommendation.parameters or recs_thrift.TParameters()
        return cls(recset_id=recommendation.recset_id,
                   group=recommendation.group_name or Recommendation.DEFAULT_GROUP_NAME,
                   position=recommendation.recset_index,
                   resource=recommendation.resource,
                   score=recommendation.score,
                   models=params.models,
                   recommender=params.recommender,
                   experiment=params.experiment,
                   recommendation_time=params.recommendation_time,
                   test=recommendation.is_test or False)
