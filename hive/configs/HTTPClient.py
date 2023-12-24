import httpx


async def get_http_connection():
    http_client = httpx.AsyncClient()
    try:
        yield http_client
    finally:
        await http_client.aclose()

