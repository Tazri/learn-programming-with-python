import logging,os

try :
    os.mkdir('log');
except FileExistsError :
    print(">>> Directory Alread Exist <<<");

logging.basicConfig(filename='./log/test.log',level=logging.DEBUG);

logging.debug("This is debug log");
logging.info("This is info log");
logging.warning("This is warning log");
logging.error("This is error log");
logging.critical("This is critical log");