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


class ChildObjectsDTO(object):
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
        'entity_id': 'str',
        'entity_name': 'str',
        'object_type': 'str',
        'parent_entity_id': 'str',
        'parent_object_type': 'str'
    }

    attribute_map = {
        'entity_id': 'entityId',
        'entity_name': 'entityName',
        'object_type': 'objectType',
        'parent_entity_id': 'parentEntityId',
        'parent_object_type': 'parentObjectType'
    }

    def __init__(self, entity_id=None, entity_name=None, object_type=None, parent_entity_id=None, parent_object_type=None, local_vars_configuration=None):  # noqa: E501
        """ChildObjectsDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._entity_id = None
        self._entity_name = None
        self._object_type = None
        self._parent_entity_id = None
        self._parent_object_type = None
        self.discriminator = None

        self.entity_id = entity_id
        self.entity_name = entity_name
        self.object_type = object_type
        self.parent_entity_id = parent_entity_id
        self.parent_object_type = parent_object_type

    @property
    def entity_id(self):
        """Gets the entity_id of this ChildObjectsDTO.  # noqa: E501


        :return: The entity_id of this ChildObjectsDTO.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this ChildObjectsDTO.


        :param entity_id: The entity_id of this ChildObjectsDTO.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_name(self):
        """Gets the entity_name of this ChildObjectsDTO.  # noqa: E501


        :return: The entity_name of this ChildObjectsDTO.  # noqa: E501
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """Sets the entity_name of this ChildObjectsDTO.


        :param entity_name: The entity_name of this ChildObjectsDTO.  # noqa: E501
        :type: str
        """

        self._entity_name = entity_name

    @property
    def object_type(self):
        """Gets the object_type of this ChildObjectsDTO.  # noqa: E501


        :return: The object_type of this ChildObjectsDTO.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this ChildObjectsDTO.


        :param object_type: The object_type of this ChildObjectsDTO.  # noqa: E501
        :type: str
        """

        self._object_type = object_type

    @property
    def parent_entity_id(self):
        """Gets the parent_entity_id of this ChildObjectsDTO.  # noqa: E501


        :return: The parent_entity_id of this ChildObjectsDTO.  # noqa: E501
        :rtype: str
        """
        return self._parent_entity_id

    @parent_entity_id.setter
    def parent_entity_id(self, parent_entity_id):
        """Sets the parent_entity_id of this ChildObjectsDTO.


        :param parent_entity_id: The parent_entity_id of this ChildObjectsDTO.  # noqa: E501
        :type: str
        """

        self._parent_entity_id = parent_entity_id

    @property
    def parent_object_type(self):
        """Gets the parent_object_type of this ChildObjectsDTO.  # noqa: E501


        :return: The parent_object_type of this ChildObjectsDTO.  # noqa: E501
        :rtype: str
        """
        return self._parent_object_type

    @parent_object_type.setter
    def parent_object_type(self, parent_object_type):
        """Sets the parent_object_type of this ChildObjectsDTO.


        :param parent_object_type: The parent_object_type of this ChildObjectsDTO.  # noqa: E501
        :type: str
        """

        self._parent_object_type = parent_object_type

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
        if not isinstance(other, ChildObjectsDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChildObjectsDTO):
            return True

        return self.to_dict() != other.to_dict()
