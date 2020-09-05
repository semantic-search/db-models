import mongoengine
import config


def global_init():
    mongoengine.register_connection(
        db=config.DB,
        host=config.MONGO_HOST,
        port=int(config.PORT),
        alias='core',
        authentication_source=config.DB,
        username=config.MONGO_USER,
        password=config.MONGO_PASSWORD
    )
    mongoengine.connect(
        db=config.DB,
        host=config.MONGO_HOST,
        port=int(config.PORT),
        username=config.MONGO_USER,
        password=config.MONGO_PASSWORD
    )

