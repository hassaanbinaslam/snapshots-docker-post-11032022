##
# app/src/hello.py

from datetime import datetime
import time
import commons.logger as logger


def main():
    # run for about 5 min: 300 sec
    for i in range(60):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        # prepare message
        msg = f"hello world at {dt_string}"

        # put message to stdout and logs
        print(msg)
        logger.logging.info(msg)

        # sleep for some seconds
        time.sleep(5)


if __name__ == "__main__":
    main()
