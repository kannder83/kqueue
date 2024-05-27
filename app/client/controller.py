
import logging
from app.client.models import Client


class DbClient():
    """
    """

    def create_client(self, client_dict: dict) -> str:
        try:
            logging.debug(f"page_dict: {client_dict}")
            client = Client(**client_dict)
            client.save()
            return client.to_dict()
        except Exception as error:
            logging.error(f"create_client - {error}")
            return f"{error}"


db_client = DbClient()
