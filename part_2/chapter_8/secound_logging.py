import logging,os

# create log and date format
log_format = '%(asctime)s %(message)s';
date_format = '%m/%d/%Y %I:%M:%S %p';

# configure logging
logging.basicConfig(format=log_format,datefmt=date_format);


# logging
logging.debug("This is debug log");
logging.info("This is info log");
logging.warning("This is warning log");
logging.error("This is error log");
