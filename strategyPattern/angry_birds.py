from abc import ABC, abstractmethod
from fly_behaviors import StraightFly, FastFly
from tweet_behavior import WiiTweet, MuteTweet


class AngryBird(ABC):
    def __init__(self, fly_behavior, tweet_behavior):
        self._fly_behavior = fly_behavior
        self._tweet_behavior = tweet_behavior

    @abstractmethod
    def description(self):
        pass

    def do_fly(self):
        self._fly_behavior.fly()

    def do_tweet(self):
        self._tweet_behavior.tweet()

    def set_fly_behavior(self, fly_behavior):
        self._fly_behavior = fly_behavior

    def set_tweet_behavirt(self, tweet_behavior):
        self._tweet_behavior = tweet_behavior


class Red(AngryBird):
    def __init__(self):
        super().__init__(fly_behavior=StraightFly(), tweet_behavior=WiiTweet())

    def description(self):
        print('a bird name Red')

class Chuck(AngryBird):
    def __init__(self):
        super().__init__(fly_behavior=FastFly(), tweet_behavior=MuteTweet())

    def description(self):
        print('a bird name Chuck')
