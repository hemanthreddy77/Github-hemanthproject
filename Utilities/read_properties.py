# import configparser
from configparser import ConfigParser

configur = ConfigParser()
configur.read('../Configurations/config.ini')

class read_config:
    @staticmethod
    def get_baseurl():
        url = configur.get('common login data','admin_pageurl')
        return url
    @staticmethod
    def get_user_email():
        username = configur.get('common login data','username')
        return username
    @staticmethod
    def get_user_password():
        password = configur.get('common login data', 'password')
        return password

