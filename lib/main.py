import math

def angles_summ(a, b):
    return (a - b) % 360

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.points = list()

    def render(self):
        self.points = list()
        for i in range(360):
            x = math.ceil(self.x + self.radius * math.cos(i * math.pi/180))
            y = math.ceil(self.y + self.radius * math.sin(i * math.pi/180))
            self.points.append({"x":x, "y":y})
            #map2d[y][x] = 1

class CircleLens:
    def __init__(self, x, y, radius, rotation):
        self.x = x
        self.y = y
        self.radius = radius
        self.rotation = rotation
        self.points = list()

    def render(self):
        self.points = list()
        for i in range(360):
            rotation = self.rotation + i
            if rotation < 360:
                x1 = self.x
                y1 = self.y
                x2 = math.ceil(self.x + self.radius * math.cos(rotation * math.pi/180))
                y2 = math.ceil(self.y + self.radius * math.sin(rotation * math.pi/180))
                x3 = self.x
                y3 = self.radius + self.y
                self.points.append({"x":x2, "y":y2})

            # angle = math.atan2(y3 - y1, x3 - x1) - math.atan2(y2 - y1, x2 - x1)
            # angle = angle * 180 / math.pi
            # if angle > 0 and angle < 180 + self.rotation:
            #     #map2d[x2][y2] = 1
            #     self.points.append({"x":x2, "y":y2})

    def pygame_points(self):
        points = list()
        for point in self.points:
            points.append([point["x"], point["y"]])
        return points
class Rect:
    def __init__(self, x, y, w, h, rotation):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rotation = rotation
        self.points = list()

    def render(self):
        self.points = list()
        for i in range(4):
            x = self.x
            y = self.y
            if i == 1:
                x = x + self.w
            elif i == 2:
                x = x + self.w
                y = y + self.h
            elif i == 3:
                y = y + self.h

            x1 = self.x + self.w / 2 # center
            y1 = self.y + self.h / 2

            x3 = self.x + self.w / 2
            y3 = self.y

            angle = math.atan2(y3 - y1, x3 - x1) - math.atan2(y - y1, x - x1)
            angle = angle * 180 / math.pi

            rotation = angles_summ(angle, self.rotation)

            radius = math.sqrt((x1 - x)**2 + (y1 - y)**2)

            x2 = math.ceil(self.x + radius * math.cos(rotation * math.pi/180))
            y2 = math.ceil(self.y + radius * math.sin(rotation * math.pi/180))

            self.points.append({"x":x2, "y":y2})

    def pygame_points(self):
        points = list()
        for point in self.points:
            points.append([point["x"], point["y"]])
        return points


def hello():
    return "Hello, wekoptics!"

# def pixel_gen(x, y):
#     radius = 100
#     center_x = 250
#     center_y = 250
#     distance = math.sqrt((center_x-x) ** 2 + (center_y-y) ** 2)
#     if distance < radius and distance > radius - 1.5:
#         return 1
#     else:
#         return 0

def empty_map_gen():
    map2d = list()
    for x in range(500):
        map2d.append(list())
        for y in range(500):
            map2d[x].append(0)
    return map2d

def render_objects(map2d, objects, swap_axes):
    for obj in objects:
        for point in obj.points:
            if swap_axes == False:
                map2d[point["x"]][point["y"]] = 1
            else:
                map2d[point["y"]][point["x"]] = 1
    return map2d


def pygame_render_objects(objects):
    objs = list()
    for obj in objects:
        points = list()
        for point in obj.points:
            points.append([point["x"], point["y"]])
        objs.append(points)
    return objs

def gen_pygame():
    circle = CircleLens(x=250, y=250, radius=100, rotation=90)
    circle.render()
    rect = Rect(x=400, y=50, w=80, h=40, rotation=45)
    rect.render()
    objs = [circle, rect]
    return pygame_render_objects(objs)

def gen(swap_axes):
    map2d = empty_map_gen()

    circle = CircleLens(x=250, y=250, radius=100, rotation=180)
    circle.render()
    objs = [circle]
    map2d = render_objects(map2d, objs, swap_axes)

    # for x in range(500):
    #     for y in range(500):
    #         pixel = pixel_gen(x, y)
    #         if swap_axes == True:
    #             map2d[y][x] = pixel
    #         else:
    #             map2d[x][y] = pixel
    return map2d