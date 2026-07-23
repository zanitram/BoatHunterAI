from .base_provider import Provider
from .autotrader import AutoTraderProvider
from .boats_com import BoatsComProvider
from .castanet import CastanetProvider
from .craigslist import CraigslistProvider
from .used_ca import UsedCaProvider

__all__ = [
    "Provider",
    "AutoTraderProvider",
    "BoatsComProvider",
    "CastanetProvider",
    "CraigslistProvider",
    "UsedCaProvider",
]
