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


class DocumentType(object):
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
        'type_id': 'int',
        'name': 'str',
        'file_extension': 'str',
        'description': 'str',
        'mime_type': 'str',
        'ooxml_package_type': 'str',
        'id': 'str'
    }

    attribute_map = {
        'type_id': 'typeId',
        'name': 'name',
        'file_extension': 'fileExtension',
        'description': 'description',
        'mime_type': 'mimeType',
        'ooxml_package_type': 'ooxmlPackageType',
        'id': 'id'
    }

    def __init__(self, type_id=None, name=None, file_extension=None, description=None, mime_type=None, ooxml_package_type=None, id=None, local_vars_configuration=None):  # noqa: E501
        """DocumentType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type_id = None
        self._name = None
        self._file_extension = None
        self._description = None
        self._mime_type = None
        self._ooxml_package_type = None
        self._id = None
        self.discriminator = None

        if type_id is not None:
            self.type_id = type_id
        self.name = name
        self.file_extension = file_extension
        self.description = description
        self.mime_type = mime_type
        self.ooxml_package_type = ooxml_package_type
        if id is not None:
            self.id = id

    @property
    def type_id(self):
        """Gets the type_id of this DocumentType.  # noqa: E501


        :return: The type_id of this DocumentType.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this DocumentType.


        :param type_id: The type_id of this DocumentType.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

    @property
    def name(self):
        """Gets the name of this DocumentType.  # noqa: E501


        :return: The name of this DocumentType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentType.


        :param name: The name of this DocumentType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def file_extension(self):
        """Gets the file_extension of this DocumentType.  # noqa: E501


        :return: The file_extension of this DocumentType.  # noqa: E501
        :rtype: str
        """
        return self._file_extension

    @file_extension.setter
    def file_extension(self, file_extension):
        """Sets the file_extension of this DocumentType.


        :param file_extension: The file_extension of this DocumentType.  # noqa: E501
        :type: str
        """

        self._file_extension = file_extension

    @property
    def description(self):
        """Gets the description of this DocumentType.  # noqa: E501


        :return: The description of this DocumentType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DocumentType.


        :param description: The description of this DocumentType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def mime_type(self):
        """Gets the mime_type of this DocumentType.  # noqa: E501


        :return: The mime_type of this DocumentType.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this DocumentType.


        :param mime_type: The mime_type of this DocumentType.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

    @property
    def ooxml_package_type(self):
        """Gets the ooxml_package_type of this DocumentType.  # noqa: E501


        :return: The ooxml_package_type of this DocumentType.  # noqa: E501
        :rtype: str
        """
        return self._ooxml_package_type

    @ooxml_package_type.setter
    def ooxml_package_type(self, ooxml_package_type):
        """Sets the ooxml_package_type of this DocumentType.


        :param ooxml_package_type: The ooxml_package_type of this DocumentType.  # noqa: E501
        :type: str
        """

        self._ooxml_package_type = ooxml_package_type

    @property
    def id(self):
        """Gets the id of this DocumentType.  # noqa: E501


        :return: The id of this DocumentType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentType.


        :param id: The id of this DocumentType.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, DocumentType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentType):
            return True

        return self.to_dict() != other.to_dict()
