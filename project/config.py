import os


class BaseConfig:
    """Base configuration."""

    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious")
    print(SECRET_KEY)
    API_KEY = os.getenv("API_KEY", "jdjsdjkscsjdj")
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13

    RMQ_USER = os.getenv("RMQ_USER", "demo_user")
    RMQ_PASSWORD = os.getenv("RMQ_PASSWORD", "demo_password")
    RMQ_SERVER = os.getenv("RMQ_SERVER", "36.255.69.105")

    CREDIT_SERVICE = os.getenv("CREDIT_SERVICE", "http://localhost:8000")
    INVOICE_SERVICE = os.getenv("INVOICE_SERVICE", "http://localhost:7000")
    MAIL_SERVICE = os.getenv("MAIL_SERVICE", "http://localhost:6000")
    AUTH_SERVICE = os.getenv("AUTH_SERVICE", "http://localhost:4000")

    # CELERY_BROKER_URL = os.environ.get(
    #     "CELERY_BROKER_URL", f"amqp://{RMQ_USER}:{RMQ_PASSWORD}@{RMQ_SERVER}:5672"
    # )

    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://127.0.0.1:6379/0")

    CELERY_RESULT_BACKEND = os.environ.get(
        "CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379/0"
    )


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4


class ProductionConfig(BaseConfig):
    """Production configuration."""

    DEBUG = False
    BCRYPT_LOG_ROUNDS = 4
