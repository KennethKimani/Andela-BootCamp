class Car(object):

    """
    A car class that instantiates various vehicles.
    It takes in arguments that depict the type, model,
    and name of the vehicle, provided they are set.
    """

    # Defaults to General and GM if no arguments are provided
    def __init__(self, name='General', model='GM', car_type='saloon'):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.speed = 0

        # Number of doors check
        if (self.name == 'Porshe' or self.name == 'Koenigsegg'):
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        # Number of Wheels check
        if (self.car_type == 'trailer'):
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    # Saloon Car check
    def is_saloon(self):
        if self.car_type == 'saloon':
            return True
        else:
            return False

    # Car Speed  test
    def drive(self, desired_speed):
        if (self.car_type == 'trailer'):
            self.speed = desired_speed * 11
            return self
        else:
            if(desired_speed !=0):
                self.speed = 10 ** desired_speed
            else:
                self.speed = 10 * desired_speed
            return self
