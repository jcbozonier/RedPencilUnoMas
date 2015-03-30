class Good():
    def __init__(self):
        self.current_state = StableState()
    def reduce_price(self, by):
        self.current_state = self.current_state.reduce_price(by=by)
    def is_red_pencil_promotion_active(self):
        return self.current_state.is_red_pencil_promotion_active()

class StableState():
    def __init__(self):
        pass
    def reduce_price(self, by):
        if by >= 0.05 and by <= 0.3:
            return RedPencilState(by)
        else:
            return self
    def is_red_pencil_promotion_active(self):
        return False

class RedPencilState():
    def __init__(self, promo):
        self.promo_so_far = promo
    def is_red_pencil_promotion_active(self):
        return True
    def reduce_price(self, by):
        if self.promo_so_far * (1.0-by) < 0.70:
            return StableState()
