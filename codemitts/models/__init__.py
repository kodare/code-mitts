from mongoengine import connect
from mongoengine import signals
from datetime import datetime


def update_timestamp(sender, document, **kwargs):
    document.updated_at = datetime.utcnow()


def database_connect(database_name):
    signals.pre_save.connect(update_timestamp)
    connect(database_name)
