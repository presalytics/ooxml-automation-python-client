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


class SharedParagraph(object):
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
        'text_container_id': 'str',
        'text_container': 'object',
        'number': 'int',
        'text': 'object',
        'id': 'str',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'text_container_id': 'textContainerId',
        'text_container': 'textContainer',
        'number': 'number',
        'text': 'text',
        'id': 'id',
        'date_created': 'dateCreated',
        'user_created': 'userCreated',
        'date_modified': 'dateModified',
        'user_modified': 'userModified'
    }

    def __init__(self, text_container_id=None, text_container=None, number=None, text=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None, local_vars_configuration=None):  # noqa: E501
        """SharedParagraph - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._text_container_id = None
        self._text_container = None
        self._number = None
        self._text = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        self.text_container_id = text_container_id
        if text_container is not None:
            self.text_container = text_container
        if number is not None:
            self.number = number
        self.text = text
        if id is not None:
            self.id = id
        if date_created is not None:
            self.date_created = date_created
        if user_created is not None:
            self.user_created = user_created
        if date_modified is not None:
            self.date_modified = date_modified
        if user_modified is not None:
            self.user_modified = user_modified

    @property
    def text_container_id(self):
        """Gets the text_container_id of this SharedParagraph.  # noqa: E501


        :return: The text_container_id of this SharedParagraph.  # noqa: E501
        :rtype: str
        """
        return self._text_container_id

    @text_container_id.setter
    def text_container_id(self, text_container_id):
        """Sets the text_container_id of this SharedParagraph.


        :param text_container_id: The text_container_id of this SharedParagraph.  # noqa: E501
        :type: str
        """

        self._text_container_id = text_container_id

    @property
    def text_container(self):
        """Gets the text_container of this SharedParagraph.  # noqa: E501


        :return: The text_container of this SharedParagraph.  # noqa: E501
        :rtype: object
        """
        return self._text_container

    @text_container.setter
    def text_container(self, text_container):
        """Sets the text_container of this SharedParagraph.


        :param text_container: The text_container of this SharedParagraph.  # noqa: E501
        :type: object
        """

        self._text_container = text_container

    @property
    def number(self):
        """Gets the number of this SharedParagraph.  # noqa: E501


        :return: The number of this SharedParagraph.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this SharedParagraph.


        :param number: The number of this SharedParagraph.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def text(self):
        """Gets the text of this SharedParagraph.  # noqa: E501


        :return: The text of this SharedParagraph.  # noqa: E501
        :rtype: object
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SharedParagraph.


        :param text: The text of this SharedParagraph.  # noqa: E501
        :type: object
        """

        self._text = text

    @property
    def id(self):
        """Gets the id of this SharedParagraph.  # noqa: E501


        :return: The id of this SharedParagraph.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedParagraph.


        :param id: The id of this SharedParagraph.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this SharedParagraph.  # noqa: E501


        :return: The date_created of this SharedParagraph.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SharedParagraph.


        :param date_created: The date_created of this SharedParagraph.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this SharedParagraph.  # noqa: E501


        :return: The user_created of this SharedParagraph.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SharedParagraph.


        :param user_created: The user_created of this SharedParagraph.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SharedParagraph.  # noqa: E501


        :return: The date_modified of this SharedParagraph.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SharedParagraph.


        :param date_modified: The date_modified of this SharedParagraph.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this SharedParagraph.  # noqa: E501


        :return: The user_modified of this SharedParagraph.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SharedParagraph.


        :param user_modified: The user_modified of this SharedParagraph.  # noqa: E501
        :type: str
        """

        self._user_modified = user_modified

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
        if not isinstance(other, SharedParagraph):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedParagraph):
            return True

        return self.to_dict() != other.to_dict()
