#!/usr/bin/env python
# Copyright (C) 2023 Benjamin Thomas Schwertfeger
# GitHub: https://github.com/btschwertfeger
# pylint: disable=unused-import

"""This module provides the Kraken Futures clients"""

from reinforcement.crypto.time_series.kraken_202406_ws.base_api import FuturesAsyncClient
from reinforcement.crypto.time_series.kraken_202406_ws.futures.funding import Funding
from reinforcement.crypto.time_series.kraken_202406_ws.futures.market import Market
from reinforcement.crypto.time_series.kraken_202406_ws.futures.trade import Trade
from reinforcement.crypto.time_series.kraken_202406_ws.futures.user import User
from reinforcement.crypto.time_series.kraken_202406_ws.futures.ws_client import FuturesWSClient

__all__ = [
    "Funding",
    "FuturesAsyncClient",
    "FuturesWSClient",
    "Market",
    "Trade",
    "User",
]
