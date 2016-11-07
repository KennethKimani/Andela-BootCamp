<b> Andela Boot Camp </b>
=========================
Home Study
==========
Day One
--------




Lab 1: fizz_buzz.py
-------------------

<b>Question: </b>
Create a function fizz_buzz to return 'Fizz', 'Buzz', 'FizzBuzz', or the argument it receives, all depending on the argument of the function, a number that is divisible by, 3, 5, or both 3 and 5, respectively.

When the number is not divisible by 3 or 5, the number itself should be returned.

<b>Tests:</b>

    class FizzBuzzClassTest(TestCase):
        """docstring for FizzBuzz"""

        def test_fizz_1(self):
            self.assertEqual(fizz_buzz(3), 'Fizz', msg='should return `Fizz` for number divisible by 3')

        def test_fizz_2(self):
            self.assertEqual(fizz_buzz(33), 'Fizz', msg='should return `Fizz` for number divisible by 3')

        def test_buzz_1(self):
            self.assertEqual(fizz_buzz(5), 'Buzz', msg='should return `Buzz` for number divisible by 5')

        def test_buzz_2(self):
            self.assertEqual(fizz_buzz(25), 'Buzz', msg='should return `Buzz` for number divisible by 5')

        def test_fizz_buzz_1(self):
            self.assertEqual(fizz_buzz(15), 'FizzBuzz', msg='should return `FizzBuzz` for number divisible by 3 and 5')

        def test_fizz_buzz_2(self):
            self.assertEqual(fizz_buzz(105), 'FizzBuzz', msg='should return `FizzBuzz` for number divisible by 3 and 5')

        def test_indivisible_1(self):
            self.assertEqual(fizz_buzz(101), 101, msg='should return the number if its in divisible by neither 3 or 5')

        def test_indivisible_2(self):
            self.assertEqual(fizz_buzz(8), 8, msg='should return the number if its in divisible by neither 3 or 5')


        
        
        
Lab 2: data_type.py
-------------------

<b>Question: </b>
Define a function called data_type, to take one argument. Compare and return results, based on the argument supplied to the function. Complete the test to produce the perfect function that accounts for all expectations.

For strings, return its length.
For None return string 'no value'
For booleans return the boolean
For integers return a string showing how it compares to hundred e.g. For 67 return 'less than 100' for 4034 return 'more than 100' or equal to 100 as the case may be
For lists return the 3rd item, or None if it doesn't exist

<b>Tests:</b>
       
       class DataTypeTestCase(TestCase):

          def test_none_type(self):
            self.assertEqual('no value', data_type(None))

          def test_array_type(self):
            self.assertEqual(3, data_type([1, 2, 3]))

          def test_small_array_type(self):
            self.assertEqual(None, data_type([1, 2]))

          def test_small_booleans_type(self):
            self.assertEqual(True, data_type(True))

          def test_small_integer_type(self):
            self.assertEqual('less than 100', data_type(3))

          def test_large_integer_type(self):
            self.assertEqual('more than 100', data_type(200))

          def test_str_type(self):
            self.assertEqual(6, data_type('andela'))





    
  
Lab 3: fizz_buzz.py
-------------------

<b>Question: </b>
You are to create a Car class that can be used to instantiate various vehicles.

It takes in arguments that depict the type, model, and name of the vehicle, provided they are set.

Let the test guide you to building your Car boiler-plate.

<b>Tests: </b>
      
      class CarClassTest(TestCase):
            """docstring for CarClassTest"""

            def test_car_instance(self):
                honda = Car('Honda')
                self.assertIsInstance(honda, Car, msg='The object should be an instance of the `Car` class')

            def test_object_type(self):
                honda = Car('Honda')
                self.assertTrue((type(honda) is Car), msg='The object should be a type of `Car`')

            def test_default_car_name(self):
                gm = Car()
                self.assertEqual('General', gm.name,
                                 msg='The car should be called `General` if no name was passed as an argument')

            def test_default_car_model(self):
                gm = Car()
                self.assertEqual('GM', gm.model, msg="The car's model should be called `GM` if no model was passed as an argument")

            def test_car_properties(self):
                toyota = Car('Toyota', 'Corolla')
                self.assertListEqual(['Toyota', 'Corolla'],
                                     [toyota.name, toyota.model],
                                     msg='The car name and model should be a property of the car')

            def test_car_doors(self):
                opel = Car('Opel', 'Omega 3')
                porshe = Car('Porshe', '911 Turbo')
                self.assertListEqual([opel.num_of_doors,
                                     porshe.num_of_doors,
                                     Car('Koenigsegg', 'Agera R').num_of_doors],
                                     [4, 2, 2],
                                     msg='The car shoud have four (4) doors except its a Porshe or Koenigsegg')

            def test_car_wheels(self):
                man = Car('MAN', 'Truck', 'trailer')
                koenigsegg = Car('Koenigsegg', 'Agera R')
                self.assertEqual([8, 4], [man.num_of_wheels, koenigsegg.num_of_wheels],
                                 msg='The car shoud have four (4) wheels except its a type of trailer')

            def test_car_type(self):
                koenigsegg = Car('Koenigsegg', 'Agera R')
                self.assertTrue(koenigsegg.is_saloon(),
                                msg='The car type should be saloon if it is not a trailer')

            def test_car_speed(self):
                man = Car('MAN', 'Truck', 'trailer')
                parked_speed = man.speed
                moving_speed = man.drive(7).speed

                self.assertListEqual([parked_speed, moving_speed],
                                     [0, 77],
                                     msg='The Trailer should have speed 0 km/h until you put `the pedal to the metal`')

            def test_car_speed2(self):
                man = Car('Mercedes', 'SLR500')
                parked_speed = man.speed
                moving_speed = man.drive(3).speed

                self.assertListEqual([parked_speed, moving_speed],
                                     [0, 1000],
                                     msg='The Mercedes should have speed 0 km/h until you put `the pedal to the metal`')

            def test_drive_car(self):
                man = Car('MAN', 'Truck', 'trailer')
                moving_man = man.drive(7)
                moving_man_instance = isinstance(moving_man, Car)
                moving_man_type = type(moving_man) is Car
                self.assertListEqual([True, True, man.speed],
                                     [moving_man_instance, moving_man_type, moving_man.speed],
                                     msg='The car drive function should return the instance of the Car class')


                             
                           
                           
                           
                           
                      
OOP: real-world-problem_OOP.py
------------------------------

<b>Question:</b>
Github repo containing a real world problem modelled using OOP while taking advantage of inheriatnce, encapsulation, polymorphism and the other OOP concepts.

<b>Answer: </b>
The code is an Evaluation code for applicants to join a dating site. 

    It takes in the details of the applicant including the name, gender, age, marital_status, age_find, application_complete to           check their elligibity and to try to match the applicants to potential partners in order to set them up for a blind date. 
