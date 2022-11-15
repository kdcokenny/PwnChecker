from humiolib.HumioClient import HumioIngestClient, HumioClient
from config import HUMIO_BASE_URL, HUMIO_INGEST_TOKEN, HUMIO_REPOSITORY, HUMIO_USER_TOKEN

client = HumioIngestClient(
    base_url=HUMIO_BASE_URL,
    ingest_token=HUMIO_INGEST_TOKEN,
)

queryClient = HumioClient(
    base_url=HUMIO_BASE_URL,
    repository=HUMIO_REPOSITORY,
    user_token=HUMIO_USER_TOKEN
)
