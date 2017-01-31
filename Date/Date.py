# -*- coding: utf-8 -*-
import datetime
from dateutil import parser
import time
import unicodedata
import locale
# Choose your local time
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

class Date(object):

    frenchMonths = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "decembre"]


    # Get timestamp in im miliseconds
    @staticmethod
    def getTimestamp():
        return int(round(time.time() * 1000))


    # Return a string from a date with a format
    @staticmethod
    def dateFormat(date, format="%d/%m/%Y"):
        return date.strftime(format)



    # Return conversion of a date (from a string or not) in date
    @staticmethod
    def convertToDate(date):
        if isinstance(date, basestring):
            return parser.parse(date, dayfirst=True).date()

        else:
            return date



    # Return conversion of a datetime (from a string or not) in datetime
    @staticmethod
    def convertToDatetime(date):
        if isinstance(date, basestring):
            return parser.parse(date, dayfirst=True)

        else:
            return date


    # Return conversion of a timestamp in datetime
    @staticmethod
    def convertTimestampToDatetime(timestamp):
        return datetime.datetime.fromtimestamp(int(timestamp))


    # Get a date from a string date with month name
    @staticmethod
    def getDateWithMonthNameForComment(date):
        nfkd_form = unicodedata.normalize('NFKD', date.lower())
        dateInASCII = nfkd_form.encode('ASCII', 'ignore').\
                                                        strip().\
                                                        replace("  ", " ").\
        for key, month in enumerate(Date.frenchMonths):
            if month in dateInASCII:
                return Date.getDatetimeOfComment(Date.convertToDatetime(dateInASCII.replace(month, str(key+1))))


    # Return a date from a comment (general string)
    @staticmethod
    def getDatetimeOfComment(date):
        return Date.dateFormat(Date.convertToDatetime(date), '%Y-%m-%d %H:%M:%S')


    # Add some days to a date (1 by default)
    @staticmethod
    def addDays(date, daysNumber=1):
        date += datetime.timedelta(days=daysNumber)
        return date


    # Substract some days to a date (1 by default)
    @staticmethod
    def lessDays(date, daysNumber=1):
        date -= datetime.timedelta(days=daysNumber)
        return date