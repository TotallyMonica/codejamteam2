from front_end.code.entities.Entity import Entity


class Creature(Entity):
    health = 0

    def __init__(self, image_file):
        self.image = image_file
