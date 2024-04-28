# from pymongo import MongoClient
import logging
from config.conf import settings
from mongoengine import connect, Document, disconnect


class Database():

    def __init__(self):
        self.db_name = "kqueue"
        self.host = settings.database_hostname
        self.port = settings.database_port

    def db_connect(self):
        if settings.mode_prod:
            logging.info("Connecting to MongoDB Production")
            connect(host=f"mongodb://{self.host}:{self.port}/{self.db_name}")
        else:
            logging.info("Connecting to MongoDB DEV")
            connect(host=f"mongodb://{self.host}:{self.port}/{self.db_name}")

    def db_disconnect(self):
        logging.info("Disconnecting to MongoDB")
        disconnect()


db = Database()
