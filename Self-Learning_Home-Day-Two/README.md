<b>Andela Boot Camp</b>
=======================

Home Study
==========

Day Two
-------


Lab One: max_min.py
-------------------
<b>Tests: </b>


    class MaxMinTest(TestCase):
                """docstring for MaxMinTest"""

                def test_find_max_min_four(self):
                    self.assertListEqual([1, 4],
                                         find_max_min([1, 2, 3, 4]),
                                         msg='should return [1,4] for [1, 2, 3, 4]')

                def test_find_max_min_one(self):
                    self.assertListEqual([4, 6],
                                         find_max_min([6, 4]),
                                         msg='should return [4, 6] for [6, 4]')

                def test_find_max_min_two(self):
                    self.assertListEqual([2, 78],
                                         find_max_min([4, 66, 6, 44, 7, 78, 8, 68, 2]),
                                         msg='should return [2, 78] for [4, 66, 6, 44, 7, 78, 8, 68, 2]')

                def test_find_max_min_three(self):
                    self.assertListEqual([1, 4],
                                         find_max_min([1, 2, 3, 4]),
                                         msg='should return [1,4] for [1, 2, 3, 4]')

                def test_find_max_min_identity(self):
                    self.assertListEqual([4],
                                         find_max_min([4, 4, 4, 4]),
                                         msg='Return the number of elements in the list in a new list if the `min` and `max` are equal')



Lab Two: word_count.py
-----------------------

<b>Tests: </b>

    class TestWordCounts(TestCase):

                """ Counts the occurrences or characters in a word"""

                def test_word_occurance1(self):
                    self.assertDictEqual(
                        {'word': 1},
                        words('word'),
                        msg='should count one word'
                    )

                def test_word_occurance2(self):
                    self.assertDictEqual(
                        {'one': 1, 'of': 1, 'each': 1},
                        words("one of each"),
                        msg='should count one of each'
                    )

                def test_word_occurance3(self):
                    self.assertDictEqual(
                        {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1},
                        words("one fish two fish red fish blue fish"),
                        msg='should count multiple occurrences'
                    )

                def test_word_occurance4(self):
                    self.assertDictEqual(
                        {'car': 1,
                            ":": 2,
                            'carpet': 1,
                            'as': 1,
                            'java': 1,
                            'javascript!!&@$%^&': 1
                         },
                        words('car : carpet as java : javascript!!&@$%^&'),
                        msg='should include punctuation'
                    )

                def test_word_occurance5(self):
                    self.assertDictEqual(
                        {'testing': 2, 1: 1, 2: 1},
                        words('testing 1 2 testing'),
                        msg='should include numbers'
                    )

                def test_word_occurance6(self):
                    self.assertDictEqual(
                        {'go': 1, 'Go': 1, 'GO': 1},
                        words('go Go GO'),
                        msg='should respect case'
                    )

                def test_word_occurance7(self):
                    self.assertDictEqual(
                        {"¡Hola!": 1, "¿Qué": 1, "tal?": 1, "Привет!": 1},
                        words('¡Hola! ¿Qué tal? Привет!'),
                        msg='should count international characters properly'
                    )

                def test_word_occurance8(self):
                    self.assertDictEqual(
                        {'hello': 1, 'world': 1},
                        words('hello\nworld'),
                        msg='should not count multilines'
                    )

                def test_word_occurance9(self):
                    self.assertDictEqual(
                        {'hello': 1, 'world': 1},
                        words('hello\tworld'),
                        msg='should not count tabs'
                    )

                def test_word_occurance0(self):
                    self.assertDictEqual(
                        {'hello': 1, 'world': 1},
                        words('hello  world'),
                        msg='should count multiple spaces as one'
                    )




HTTP & Web : cli_public-api.py
--------------------------------


<b>Question: </b>
   A Simple command line application that consumes a public api using a http client libraly 

<b>Answer: </b>
    This short program is a simple command line python application that takes the name of a country and prints out the  information  about countries via a RESTful API
    # It uses a RESTful API from https://restcountries.eu/     REST Countries
    
    The program takes country name as input and extracts single values from JSON response and prints the individual details from the returned country data including:
            The Capital City of that country
            The Region that that country lies in 
            The subregion that the country lies in
            The population of that country
            The Top level domain of that country
            The Calling code of the country
            The Languages spoken in that country
            The Currencies in use in that country
            The Codes of the countries bordering that country
            
          
