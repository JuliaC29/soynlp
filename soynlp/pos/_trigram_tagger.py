from collections import OrderedDict
from collections import namedtuple

from ._dictionary import Dictionary
from ._evaluator import BaseEvaluator
from ._template import BaseTemplateMatcher

default_profile= OrderedDict([
        # ('cohesion_l', 0.5), ... 
])

ScoreTable = namedtuple('ScoreTable', list(default_profile))

class TrigramEvaluator(BaseEvaluator):

    def __init__(self, profile):
        self.profile = profile if profile else default_profile

    def evaluate(self, candidates, preference=None):
        scores = []
        for c in candidates:
            score = self._evaluate(c)
            # if preference:
                # add preference score
            scores.append((c, score))
        return sorted(scores, key=lambda x:-x[-1])

    def make_scoretable(self, args):
        # return ScoreTable(*args)
        raise NotImplemented

    def _evaluate(self, scoretable):
        return sum(score * self.profile.get(field, 0) for field, score in scoretable._asdict().items())

class TrigramTemplateMatcher(BaseTemplateMatcher):

    def __init__(self, dictionary, templates=None):
        self.dictionary = dictionary
        self.templates = templates if teamplates else []

    def generate(self, sentence):
        raise NotImplemented