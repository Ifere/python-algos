def asteroidCollision(asteroids):
    stack = []

    if not asteroids:
        return None

    ast = asteroids
    i = 0

    while i < len(ast):

        if not stack:
            stack.append(ast[i])
            i += 1
            if i > len(ast) - 1: break;

        if ast[i] < 0 < stack[-1]:

            if abs(stack[-1]) < abs(ast[i]):
                stack.pop()


            elif abs(stack[-1]) > abs(ast[i]):
                i += 1
            else:
                stack.pop()
                i += 1
        else:
            stack.append(ast[i])
            i += 1

    return stack


print(asteroidCollision([-8, 8]))