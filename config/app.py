import logging
from config.database import db
from config.conf import settings
from contextlib import asynccontextmanager
from starlette.middleware import Middleware
from starlette.applications import Starlette
from app.api.init_api import app as fastapi_app
from fastapi.middleware.cors import CORSMiddleware
from starlette_admin.contrib.mongoengine import Admin, ModelView
from starlette_admin import CustomView


# Models
from app.client.models import Client


@asynccontextmanager
async def app_lifespan(app):
    # code to execute when app is loading
    if settings.debug:
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(levelname)s %(message)s"
        )
    else:
        logging.basicConfig(
            level=logging.WARNING,
            format="%(asctime)s %(levelname)s %(message)s"
        )
    db.db_connect()
    yield
    # code to execute when app is shutting down
    db.db_disconnect()

origins: list = settings.allowed_hosts

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
]

app = Starlette(
    lifespan=app_lifespan,
    middleware=middleware
)

# Create admin
admin = Admin(title="KQueue")

# Add views


class UserView(ModelView):
    fields_default_sort = [(Client.name, True)]


# Views
admin.add_view(UserView(Client, icon="fa fa-users"))
# admin.add_view(UserView(Tag, icon="fa fa-users"))
admin.add_view(CustomView(
    label="Home",
    icon="fa fa-home",
    path="/home",
    template_path="home.html",
    add_to_menu=True,
))

# Mount admin to app
admin.mount_to(app)

# Mount fastapi to app
app.mount(path="/api/v1", app=fastapi_app)
