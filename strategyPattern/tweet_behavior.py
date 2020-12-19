from abc import ABC, abstractmethod


class TweetInterface(ABC):
    @abstractmethod
    def tweet(self):
        pass


class WiiTweet(TweetInterface):
    def tweet(self):
        print('wii~~')


class MuteTweet(TweetInterface):
    def tweet(self):
        print('silence')
