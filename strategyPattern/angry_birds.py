from abc import ABC, abstractmethod
from fly_behaviors import StraightFly, FastFly
from tweet_behavior import WiiTweet, MuteTweet


class AngryBirds(ABC):
    def __init__(self, fly_behavior, tweet_behavior):
        self.fly_behavior = fly_behavior()
        self.tweet_behavior = tweet_behavior()

    def fly(self):
        self.fly_behavior.fly()

    def tweet(self):
        self.tweet_behavior.tweet()


class Red(AngryBirds):
    def __init__(self):
        super().__init__(fly_behavior=StraightFly, tweet_behavior=WiiTweet)


class Chuck(AngryBirds):
    def __init__(self):
        super().__init__(fly_behavior=FastFly, tweet_behavior=WiiTweet)
