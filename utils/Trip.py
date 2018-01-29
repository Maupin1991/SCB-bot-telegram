from models.SenseData import SensedData
import logging

def check_trip(timestamp=None):

    sense_data = SensedData().query().order(-SensedData.updated_at).fetch()
    print sense_data[0].updated_at
    last_sample = sense_data[0]

    period = (timestamp) - (last_sample.updated_at)
    minutes_sec = divmod(period.days * 86400 + period.seconds, 60)

    print minutes_sec
    logging.warning("Check_trip, minutes_sec: {}".format(timestamp))
    # "%02d-%02d-%02d_%02d:%02d:%02d", month, day, year, hour, minute, second


    return