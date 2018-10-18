import time

class Logger(object):
    @staticmethod
    def info(message):
        print("%s - %s\n" % (time.ctime(time.time()), message))

    @staticmethod
    def error(message):
        print("%s - Error: %s\n" % (time.ctime(time.time()), message))
