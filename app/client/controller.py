
import logging
from app.client.models import Page


class DbPage():
    """
    """

    def create_page(self, page_dict: dict) -> str:
        try:
            logging.debug(f"page_dict: {page_dict}")
            page = Page(**page_dict)
            page.save()
            return page.to_dict()
        except Exception as error:
            logging.error(f"create_page - {error}")
            return f"{error}"


db_page = DbPage()
