from django.http import HttpRequest
from django.urls import path

from core.api.schemas import PingResposnSchema
from core.api.v1.urls import router as v1_router

from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/ping", response=PingResposnSchema)
def ping(request: HttpRequest) -> PingResposnSchema:
    return PingResposnSchema(result=True)

api.add_router('v1/', v1_router)

urlpatterns = [
    path("", api.urls),
]