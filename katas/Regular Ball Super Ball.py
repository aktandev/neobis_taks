class Ball(object):
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


    def __str__(self):
        return self.ball_type









ball1 = Ball()
ball2 = Ball("super")
