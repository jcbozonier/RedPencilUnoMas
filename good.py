import datetime

class Good():
    def __init__(self):
        self.current_state = StableState()
    def reduce_price(self, by, effective=datetime.datetime.now()):
        self.current_state = self.current_state.reduce_price(by=by, effective=effective)
    def is_red_pencil_promotion_active(self):
        return self.current_state.is_red_pencil_promotion_active()

class StableState():
    def __init__(self):
        pass
    def reduce_price(self, by, effective):
        if by >= 0.05 and by <= 0.3:
            return RedPencilState(1.0-by, effective)
        else:
            return StabilizingState(by, effective)
    def is_red_pencil_promotion_active(self):
        return False

class StabilizingState():
    def __init__(self, by, effective):
        pass
    def reduce_price(self, by, effective):
        return self
    def is_red_pencil_promotion_active(self):
        return False

class RedPencilState():
    def __init__(self, promo, effective):
        self.promo_so_far = promo
        self.effective = effective
    def is_red_pencil_promotion_active(self):
        return True
    def reduce_price(self, by, effective):
        if self.promo_so_far * (1.0-by) < 0.70:
            return StableState()
        elif (effective - self.effective).days > 30:
            return RedPencilState(1.0-by, effective)
