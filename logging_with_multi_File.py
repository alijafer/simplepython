import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
import secrets
import os
import schedule
import time
import logging
import requests
import json
""" log_level=40
log_level = int(log_level)
logger = logging.getLogger('simple')
logger.setLevel(log_level)

logname = "my_app.log"
handler = TimedRotatingFileHandler(logname, when="midnight", interval=1)
handler.suffix = "%Y%m%d"
logger.addHandler(handler)
 """

url ="http://127.0.0.1:8000/"

def formata(self, record):
    print(record)
    record.message = record.getMessage()
    input_data = {}
    input_data['@timestamp'] = datetime.utcnow().isoformat()[:-3] + 'Z'
    input_data['level'] = record.levelname

    if record.message:
        input_data['message'] = record.message

    input_data.update(self.data)
    return json.dumps(input_data)

file ="D:/temp/"+  "error.log"
fmt=logging.Formatter('[%(levelname)s] %(asctime)s %(message)s\n')

fileinfo ="D:/temp/"+  "info.log"
fmtinfo=logging.Formatter('[%(levelname)s] %(asctime)s %(message)s')
fileexception ="D:/temp/"+  "exception.log"
fmtexception=logging.Formatter('[%(levelname)s] %(asctime)s %(message)s')



def setup_logger(name, log_file, level, fmta):
    """To setup as many loggers as you want"""
    
    #handler = logging.FileHandler(log_file, mode='a', encoding='utf-8') 
         
    #handler.setFormatter(fmta)
    #handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1, encoding='utf-8')
    handler = TimedRotatingFileHandler(log_file, when="M", interval=1, encoding='utf-8')
    handler.setFormatter(fmt=fmta) 
    handler.suffix = "%Y%m%d%Hh%Mm.log"
    handler.encoding  ='UTF-8'
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    
    


    return logger



# first file logger
loggererror = setup_logger('error', file, logging.ERROR, fmta=fmt)
loggerinfo = setup_logger('info', fileinfo, logging.INFO, fmtinfo)
loggerexception = setup_logger('exception', fileexception, logging.ERROR, fmtexception)


def job():
  try:

    x = requests.get(url)
  
    print(x.json())
    #loggerinfo.info(x.json())
  except Exception as e:
    # print(f"connot accsess{e}")
    # logger.error(e)
    loggerexception.exception(e)
  num = secrets.randbelow(255)
  loggerinfo.info(f"number علي {num}")
  


schedule.every(10).seconds.do(job)





## all your app logic here
def main():
  while True:
    schedule.run_pending()
    


if __name__ == "__main__":
   try:
    print("schedule run")
    main()
   except KeyboardInterrupt:
       print("bey")
       loggererror.error("exit")
    
      # do nothing here


