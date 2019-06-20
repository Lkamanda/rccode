'''
ce1.需求现在有一下几个日志记录需求:
    ce1)要求将所有日志都吸入磁盘文件中
    2)all.log文件中记录所有的日志信息,日志格式为:
    日期和时间 -日志级别 - 日志信息
    3)error.log文件中单独记录error及以上级别的日志信息
    日志格式为:日期和时间 -日志级别 - 文件名[:行号]  - 日志信息
    4)要求all.log在每天凌晨进行日志切割
2.分析
    ce1)要记录所有级别的日志因此日志的有效level需要设置为,
对低级别 --DEBUG
    2)日志需要发送到俩个不同的目的地,因此需要为日志设置俩个handler:
另外:俩个目的地都是磁盘文件,因此这俩个handler都是于filterhandler
    3)all.log要求按照时间进行日期切割,因此需要用logginghandlers.TimeRobatFilterHander
而error.log没有要求日志切割
    4)俩个日志文件的格式不同,因此需要对这俩个handler分别设置格式器
'''

import logging
import logging.handlers
import datetime

# 定义logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)


# 为不同的浏览器设置不同的handler
rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1,backupCount=7,atTime=datetime.time(0,0,0,0))
rf_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] -%(message)s'))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s -%(levelname)s -%(filename)s[:%(lineo)d] -%(message)s"))

#把不同的处理器装到logger上
logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logging.error('error message')
logging.critical('critical message')


