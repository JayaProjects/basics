import logging
logging.basicConfig(filename='log1.txt',level=logging.DEBUG)

print("python logging demo")

logging.debug("This is debug message")
logging.info("This is infoinfo message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")

try:
    print(10/0)
except ZeroDivisionError as msg:
    print("cannot divide")
    logging.exception(msg)