# coding: utf-8

"""
    OOXML Automation

    This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.  # noqa: E501

    The version of the OpenAPI document: 0.1.0-no-tags
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from presalytics_ooxml_automation.configuration import Configuration


class OoxmlDTO(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'id': 'str',
        'open_office_xml': 'str'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'open_office_xml': 'openOfficeXml'
    }

    def __init__(self, type=None, id=None, open_office_xml=None, local_vars_configuration=None):  # noqa: E501
        """OoxmlDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._id = None
        self._open_office_xml = None
        self.discriminator = None

        self.type = type
        self.id = id
        self.open_office_xml = open_office_xml

    @property
    def type(self):
        """Gets the type of this OoxmlDTO.  # noqa: E501


        :return: The type of this OoxmlDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OoxmlDTO.


        :param type: The type of this OoxmlDTO.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this OoxmlDTO.  # noqa: E501


        :return: The id of this OoxmlDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OoxmlDTO.


        :param id: The id of this OoxmlDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def open_office_xml(self):
        """Gets the open_office_xml of this OoxmlDTO.  # noqa: E501


        :return: The open_office_xml of this OoxmlDTO.  # noqa: E501
        :rtype: str
        """
        return self._open_office_xml

    @open_office_xml.setter
    def open_office_xml(self, open_office_xml):
        """Sets the open_office_xml of this OoxmlDTO.


        :param open_office_xml: The open_office_xml of this OoxmlDTO.  # noqa: E501
        :type: str
        """

        self._open_office_xml = open_office_xml

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OoxmlDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OoxmlDTO):
            return True

        return self.to_dict() != other.to_dict()
