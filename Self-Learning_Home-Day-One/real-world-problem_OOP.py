
class BlindDate(object):
    """
   Evaluation code for applicants to join a dating site.
    """

    def __init__(self, name, gender, age, marital_status, age_find, application_complete):
        self.name = name
        self.gender = gender
        self.age = age
        self.age_find = age_find
        self.marital_status = marital_status
        self.application_complete = application_complete

    def join_application(self, age, application_complete):
        if application_complete == "Yes" and age >= 18:
            return "Application accepted! Welcome to Dating Site. You are Eligible for a blind date"
        elif application_complete == "Yes" and 18 > age > 0:
            return "Appliation rejected! Too Young to join dating site. Go play FIFA or something.. "
        else:
            return "Application for a blind date not Successful"

    def match_maker(self, marital_status):
        if marital_status == 'Single':
            return "A potential soul mate is waiting to go on a date with you"
        elif marital_status == 'Married':
            return "We do not understand what you are doing here, but we hope you find whatever it is you are looking for. Also, We do not condone cheating. "
        elif marital_status == 'Divorced':
            return "Third time lucky is the charm"
        else:
            return "Yea, yea, we understand. Its complicated."

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


user = BlindDate("Mike", "Male", 25, "Single", 23, "Yes")
print user.application_complete
print user.age
print Login.years

