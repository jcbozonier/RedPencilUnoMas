class Good():
    def __init__(self):
        self.red_pencil_promotion_active = False
    def reduce_price(self, by):
        if by >= 0.05 and by <= 0.3:
            self.red_pencil_promotion_active = True
    def is_red_pencil_promotion_active(self):
        return self.red_pencil_promotion_active
