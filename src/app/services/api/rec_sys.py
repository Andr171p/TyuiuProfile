import json

from src.config import settings
from src.http.request import HTTPRequests
from src.app.schemas.request.rec_sys import RecSysRequestSchema
from src.app.schemas.response.rec_sys import RecSysResponseSchema


class RecSysAPI(HTTPRequests):
    async def get_recs(
        self, 
        data: RecSysRequestSchema
    ) -> RecSysResponseSchema:
        response = await self.post(
            url=f"{settings.rec_sys.url}{settings.rec_sys.endpoint}",
            json=data.model_dump()
        )
        response = json.loads(response)
        rec_sys_response = RecSysResponseSchema(**response)
        return rec_sys_response
        