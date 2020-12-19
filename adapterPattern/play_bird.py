from birds import RedBird
from ducks import Mallard
from adapters import DuckAdapter


def implement_bird_behavior(bird):
    bird.fly()
    bird.tweet()


def main():
    print('===play red bird===')
    red_bird = RedBird()
    implement_bird_behavior(red_bird)
    print('===play mallard duck===')
    duck_adapter = DuckAdapter(Mallard())
    implement_bird_behavior(duck_adapter)


if __name__ == '__main__':
    main()