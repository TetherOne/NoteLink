from contextlib import asynccontextmanager

from aiobotocore.session import get_session

from notelink.core.settings.config import settings


class S3Client:
    def __init__(
        self,
        access_key: str,
        secret_key: str,
        endpoint_url: str,
        bucket_name: str,
    ):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url,
        }
        self.bucket_name = bucket_name
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client(
            "s3",
            **self.config,
        ) as client:
            yield client

    async def upload_text(self, text: str, object_name: str) -> str:
        async with self.get_client() as client:
            await client.put_object(
                Bucket=self.bucket_name,
                Key=object_name,
                Body=text.encode("utf-8"),
            )
        return object_name

    async def get_text(self, object_name: str) -> str:
        async with self.get_client() as client:
            response = await client.get_object(
                Bucket=self.bucket_name,
                Key=object_name,
            )
            data = await response["Body"].read()
        return data.decode("utf-8")


s3_client = S3Client(
    access_key=settings.s3.access,
    secret_key=settings.s3.secret,
    endpoint_url=settings.s3.url,
    bucket_name=settings.s3.bucket_name,
)
