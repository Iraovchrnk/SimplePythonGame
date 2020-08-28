
class Coords(object):
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def within_x(co1, co2):
    if (co2.x1 < co1.x1 < co2.x2) or (co2.x1 < co1.x2 < co2.x2) or (co1.x1 < co2.x1 < co1.x2 ) or (co1.x1 < co2.x2 < co1.x2):
        return True
    else:
        return False


def within_y(co1, co2):
    if (co2.y1 < co1.y1 < co2.y2) or (co2.y1 < co1.y2 < co2.y2) or (co1.y1 < co2.y1 < co1.y2) or (co1.y1 < co2.y2 < co1.y2):
        return True
    else:
        return False


def collided_left(co1, co2):
    if within_y(co1, co2):
        if co2.x1 <= co1.x1 <= co2.x2:
            return True
    return False


def collided_right(co1, co2):
    if within_y(co1, co2):
        if co2.x2 <= co1.x2 <= co2.x1:
            return True
    return False


def collided_top(co1, co2):
    if within_x(co1, co2):
        if co2.y1 <= co1.y1 <= co2.y2:
            return True
    return False


def collided_bottom(y, co1, co2):
    if within_x(co1, co2):
        y_calc = co1.y2 + y
        if co2.y1 <= y_calc <= co2.y2:    #check if stickman WILL collide platform rather than if it collided
            return True
    return False


'''
class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


def within_y(co1, co2):
    if (co2.y1 < co1.y1 < co2.y2) \
            or (co2.y1 < co1.y2 < co2.y2) \
            or (co1.y1 < co2.y1 < co1.y2) \
            or (co1.y1 < co2.y2 < co1.y2):
        return True
    else:
        return False


def within_x(co1, co2):
    if (co2.x1 < co1.x1 < co2.x2) or (co2.x1 < co1.x2 < co2.x2) or (co1.x1 < co2.x1 < co1.x2) or (co1.x1 < co2.x2 < co1.x2):
        return True
    else:
        return False


def collided_left(co1, co2):
    if within_y(co1, co2):
        if co2.x1 <= co1.x1 <= co2.x2:
            return True
    return False


def collided_right(co1, co2):
    if within_y(co1, co2):
        if co2.x2 <= co1.x2 <= co2.x1:
            return True
    return False


def collided_top(co1, co2):
    if within_x(co1, co2):
        if co2.y1 <= co1.y1 <= co2.y2:
            return True
    return False


def collided_bottom(co1, co2, y):
    if within_x(co1, co2):
        y_calc = co1.y2 + y
        if co2.y1 <= y_calc <= co2.y2:
            return True
    return False

'''