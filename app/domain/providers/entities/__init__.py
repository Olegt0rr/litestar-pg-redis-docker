from starlite import Provide, Router

from app.constants import Paths

from .controller import Controller
from .service import Service

__all__ = ["Controller", "Service", "router"]

router = Router(
    path=Paths.PROVIDER_ENTITIES,
    route_handlers=[Controller],
    dependencies={"service": Provide(Service.new)},
)
