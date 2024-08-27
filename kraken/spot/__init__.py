#!/usr/bin/env python
# Copyright (C) 2023 Benjamin Thomas Schwertfeger
# GitHub: https://github.com/btschwertfeger
# pylint: disable=unused-import,cyclic-import

"""Module that provides the Spot REST clients."""

from reinforcement.crypto.time_series.kraken_202406_ws.base_api import SpotAsyncClient, SpotClient
from reinforcement.crypto.time_series.kraken_202406_ws.spot.earn import Earn
from reinforcement.crypto.time_series.kraken_202406_ws.spot.funding import Funding
from reinforcement.crypto.time_series.kraken_202406_ws.spot.market import Market
from reinforcement.crypto.time_series.kraken_202406_ws.spot.orderbook import SpotOrderBookClient
from reinforcement.crypto.time_series.kraken_202406_ws.spot.trade import Trade
from reinforcement.crypto.time_series.kraken_202406_ws.spot.user import User
from reinforcement.crypto.time_series.kraken_202406_ws.spot.ws_client import SpotWSClient

__all__ = [
    "Earn",
    "Funding",
    "SpotWSClient",
    "Market",
    "SpotOrderBookClient",
    "SpotClient",
    "SpotAsyncClient",
    "Trade",
    "User",
]
