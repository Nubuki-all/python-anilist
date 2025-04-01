#!/usr/bin/env python3
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict

from .object import Object


class Title(Object):
    """Title object."""

    def __init__(
        self,
        *,
        **kwargs,
    ):
        self.__dict__.update(kwargs)

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return str(self) == str(other)
