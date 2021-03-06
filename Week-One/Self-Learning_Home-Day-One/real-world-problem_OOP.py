import datetime

class BlindDate(object):
    """A real world problem modelled using OOP"""
    
    """
   Evaluation code for applicants to join a dating site.
    """

    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, name, surname, gender, age, birthdate, marital_status, age_find, email, application_complete):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.birthdate = birthdate
        self.age_find = age_find
        self.email = email
        self.marital_status = marital_status
        self.application_complete = application_complete

    def fullname(self, title):
        if title not in self.TITLES:
            raise ValueError("Unrecognised title: '%s'" % title)

        return "%s %s %s" % (title, self.name, self.surname)

    def years_old(self):
        """This method calculates the person's age from the birthdate and the current date.

        :returns: int -- the person's age in years
        """
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age


    # check if application complete
    def join_application(self, age, application_complete):
        if application_complete == "Yes" and age >= 18:
            return "Application accepted! Welcome to Dating Site. You are Eligible for a blind date"
        elif application_complete == "Yes" and 18 > age > 0:
            return "Appliation rejected! Too Young to join dating site. Go play FIFA or something.. "
        else:
            return "Application for a blind date not Successful"

    # check the marital status of potential members and advice accordingly
    def match_maker(self, marital_status):
        if marital_status == 'Single':
            return "A potential soul mate is waiting to go on a date with you"
        elif marital_status == 'Married':
            return "We do not understand what you are doing here, but we hope you find whatever it is you are looking for. Also, We do not condone cheating. "
        elif marital_status == 'Divorced':
            return "Third time lucky is the charm"
        else:
            return "Yea, yea, we understand. Its complicated."

    # match user and partner depending on age preference
    def matchup(self, age, age_find):
        if age > 0 and age < 18:
            return "Sorry no minors on this site. You belong in jail Paedophile. "
        elif age - age_find <= 10:
            return "Potential Partner MatchUP"
        elif 10 < age - age_find <= 20:
            return "Mature Partner match up"
        elif age - age_find > 20:
            return "Sponsor Alert"
        else:
            return "Sorry but you entered an incorrect value for potential date partner"

    # confirm man settling bill
    def bill_payment(self, gender):
        if gender == 'Male':
            return "Please remember you will be footing the bill for the date"
        else:
            return "The date is paid for, all you have to do is turn up"


class Match(BlindDate):
    man = "Male"
    woman = "Female"

    def matchup(self, man, woman):
        return 'This is a match!'


class Login(BlindDate):
    complete = "Yes"
    years = 17

    def join_application(self, years, complete):
        return self.application_complete


class Marital_Status(BlindDate):
    status = 'single'

    def match_maker(self, status):
        return self.match_maker


user = BlindDate("Mike", "Makonde", "Male", 25, datetime.date(1990, 11, 22), "Single", 23, "mikem@gmail.com", "Yes")
print user.fullname('Mr')

if user.years_old() != user.age:
    raise RuntimeError('You lied about your age!!.')
else:
    print "Age Confirmed!!"

print user.application_complete
print user.age

print Login.years






