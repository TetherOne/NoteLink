from celery import Celery

celery = Celery(
    "notelink",
    broker="amqp://guest:guest@rabbitmq:5672",
    include=[
        "notelink.api.notes.tasks",
    ],
)

celery.conf.update(
    result_backend="rpc://",
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    enable_utc=True,
)
