import logging

class LogGen():
    @staticmethod
    def loggen():
        logging.basicConfig(filename='../Logs/automation.log', filemode= 'a',
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %P')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger

# import logging,mnn,n,m
# logger = logging.getLogger()
# fhandler = logging.FileHandler(filename='mylog.log', mode='a')
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fhandler.setFormatter(formatter)
# logger.addHandler(fhandler)
# logger.setLevel(logging.DEBUG)

