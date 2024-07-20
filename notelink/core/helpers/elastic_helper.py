from elasticsearch import AsyncElasticsearch


class ElasticsearchClient:
    def __init__(
        self,
        host: str = "notelink-elasticsearch",
        port: int = 9200,
        scheme: str = "http",
    ):
        self.client = AsyncElasticsearch(
            hosts=[{"host": host, "port": port, "scheme": scheme}]
        )

    async def create_index(self, index_name: str, body: dict):
        await self.client.indices.create(index=index_name, body=body, ignore=400)

    async def index_document(self, index_name: str, document_id: str, document: dict):
        await self.client.index(index=index_name, id=document_id, document=document)

    async def search(self, index_name: str, query: dict):
        return await self.client.search(index=index_name, body=query)

    async def close(self):
        await self.client.close()


es_client = ElasticsearchClient()
