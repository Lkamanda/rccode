import logging
# 自定义日志格式
LOG_FORMAT = "%(asctime)s=====%(levelname)s++++++%(message)s"


# 设置存放日志路径,以及异常显示级别
logging.basicConfig(filename="xiaolin2.log", level=logging.DEBUG, format=LOG_FORMAT)
# format 格式
# datefmt时间格式
# level级别
logging.debug("this is a debug log.")
logging.info("this is a info log.")
logging.warning("this is warning log.")
logging.error("this is error log")
logging.critical("this is a critical log.")

logging.log(logging.DEBUG,"this a debug log")
logging.log(logging.INFO,"INFO")
logging.log(logging.WARNING,"WARNING")
logging.log(logging.ERROR,"ERROR")
logging.log(logging.CRITICAL,"CRITICAL")
