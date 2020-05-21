import pytz
from datetime import datetime


def timezone_2_country_name(timezone):
    try:
        return([ pytz.country_names[k]  for k, v in pytz.country_timezones.items() if v[0] == str(timezone)][0] )
    except:
        return None

def country_with_common_timezone():
    now = datetime.now(pytz.utc)
    common_offset=list(set([now.astimezone(tz).utcoffset() for tz in map(pytz.timezone, pytz.all_timezones_set)]))
    result={}
    for w in common_offset:
        if (w.total_seconds()/ 3600)>0:
            utc='UTC' +"+" +str((w.total_seconds()/ 3600))
            print( utc,[timezone_2_country_name(tz.zone)  for tz in map(pytz.timezone, pytz.all_timezones_set) if now.astimezone(tz).utcoffset() == w if timezone_2_country_name(tz.zone)!=None ]
        )
            result[utc]=[timezone_2_country_name(tz.zone)  for tz in map(pytz.timezone, pytz.all_timezones_set) if now.astimezone(tz).utcoffset() == w if timezone_2_country_name(tz.zone)!=None ]
        else:
            utc='UTC' +str((w.total_seconds()/ 3600))
            result[utc]=[timezone_2_country_name(tz.zone)  for tz in map(pytz.timezone, pytz.all_timezones_set) if now.astimezone(tz).utcoffset() == w if timezone_2_country_name(tz.zone)!=None ]
            print( utc,[timezone_2_country_name(tz.zone) for tz in map(pytz.timezone, pytz.all_timezones_set) if
             now.astimezone(tz).utcoffset() == w if timezone_2_country_name(tz.zone) != None])

    return result



country_with_common_timezone()






