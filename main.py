import uvicorn
from subprocess import run
from config.conf import settings


def main():
    """
    Main Function
    """
    if settings.mode_prod:
        run(f"gunicorn config.app:app -w {settings.workers} -b 0.0.0.0:8000 --worker-class uvicorn.workers.UvicornWorker".split(' '))
    else:
        uvicorn.run(
            "config.app:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
        )


if __name__ == "__main__":
    main()
