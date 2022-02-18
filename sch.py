from datetime import datetime
import secrets
import os
import schedule
import time
import logging



file ="c:/Users/ali29/python code/temp/"+ str(datetime.now().strftime('%d-%m-%Y %Hh%Mm'))+ ".log"
fmt='[%(levelname)s] %(asctime)s %(message)s'
# Create and configure logger
logging.basicConfig(filename=file,
                    format=fmt,
                    filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def job():
  num = secrets.randbelow(255)
  logger.info(f"number {num}")


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
       logger.warning("exit")
      # do nothing here
      