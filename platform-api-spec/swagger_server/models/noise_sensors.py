# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.noise_sensor import NoiseSensor
from swagger_server import util


class NoiseSensors(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, sensors: List[NoiseSensor]=None):  # noqa: E501
        """NoiseSensors - a model defined in Swagger

        :param sensors: The sensors of this NoiseSensors.  # noqa: E501
        :type sensors: List[NoiseSensor]
        """
        self.swagger_types = {
            'sensors': List[NoiseSensor]
        }

        self.attribute_map = {
            'sensors': 'sensors'
        }

        self._sensors = sensors

    @classmethod
    def from_dict(cls, dikt) -> 'NoiseSensors':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NoiseSensors of this NoiseSensors.  # noqa: E501
        :rtype: NoiseSensors
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sensors(self) -> List[NoiseSensor]:
        """Gets the sensors of this NoiseSensors.


        :return: The sensors of this NoiseSensors.
        :rtype: List[NoiseSensor]
        """
        return self._sensors

    @sensors.setter
    def sensors(self, sensors: List[NoiseSensor]):
        """Sets the sensors of this NoiseSensors.


        :param sensors: The sensors of this NoiseSensors.
        :type sensors: List[NoiseSensor]
        """
        if sensors is None:
            raise ValueError("Invalid value for `sensors`, must not be `None`")  # noqa: E501

        self._sensors = sensors
