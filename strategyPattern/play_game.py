from angry_birds import Red, Chuck
from fly_behaviors import FastFly

def main():
    red = Red()
    chuck = Chuck()
    red.do_fly()
    red.do_tweet()
    red.set_fly_behavior(FastFly())
    red.do_fly()
    chuck.do_fly()
    chuck.do_tweet()


if __name__ == '__main__':
    main()