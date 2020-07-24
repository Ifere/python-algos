isPossible = False


def points(sx, sy, tx, ty):
    if tx < sx or ty < sy:
        return False

    elif tx == sx:
        if (ty - sy) % sx == 0:
            return True
        else:
            return False

    elif ty == sy:
        if (tx - sx) % sy == 0:
            return True
        else:
            return False

    else:
        return points(sx, sy, tx - ty, ty) or points(sx, sy, tx, ty - tx)


def canReach(x1, y1, x2, y2):
    # Write your code here

    if points(x1, y1, x2, y2):
        return 'Yes'
    else:
        return 'No'