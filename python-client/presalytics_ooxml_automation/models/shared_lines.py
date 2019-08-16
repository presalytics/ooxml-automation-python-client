# coding: utf-8

"""
    OOXML Automation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SharedLines(object):
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
        'solid_fills_id': 'int',
        'dash_type_id': 'int',
        'head_end_type_id': 'int',
        'tail_end_type_id': 'int',
        'weight': 'int',
        'head_end_height_id': 'int',
        'head_end_width_id': 'int',
        'tail_end_height_id': 'int',
        'tail_end_width_id': 'int',
        'id': 'int',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'solid_fills_id': 'SolidFillsId',
        'dash_type_id': 'DashTypeId',
        'head_end_type_id': 'HeadEndTypeId',
        'tail_end_type_id': 'TailEndTypeId',
        'weight': 'Weight',
        'head_end_height_id': 'HeadEndHeightId',
        'head_end_width_id': 'HeadEndWidthId',
        'tail_end_height_id': 'TailEndHeightId',
        'tail_end_width_id': 'TailEndWidthId',
        'id': 'Id',
        'date_created': 'DateCreated',
        'user_created': 'UserCreated',
        'date_modified': 'DateModified',
        'user_modified': 'UserModified'
    }

    def __init__(self, solid_fills_id=None, dash_type_id=None, head_end_type_id=None, tail_end_type_id=None, weight=None, head_end_height_id=None, head_end_width_id=None, tail_end_height_id=None, tail_end_width_id=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """SharedLines - a model defined in OpenAPI"""  # noqa: E501

        self._solid_fills_id = None
        self._dash_type_id = None
        self._head_end_type_id = None
        self._tail_end_type_id = None
        self._weight = None
        self._head_end_height_id = None
        self._head_end_width_id = None
        self._tail_end_height_id = None
        self._tail_end_width_id = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        if solid_fills_id is not None:
            self.solid_fills_id = solid_fills_id
        if dash_type_id is not None:
            self.dash_type_id = dash_type_id
        if head_end_type_id is not None:
            self.head_end_type_id = head_end_type_id
        if tail_end_type_id is not None:
            self.tail_end_type_id = tail_end_type_id
        if weight is not None:
            self.weight = weight
        if head_end_height_id is not None:
            self.head_end_height_id = head_end_height_id
        if head_end_width_id is not None:
            self.head_end_width_id = head_end_width_id
        if tail_end_height_id is not None:
            self.tail_end_height_id = tail_end_height_id
        if tail_end_width_id is not None:
            self.tail_end_width_id = tail_end_width_id
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
    def solid_fills_id(self):
        """Gets the solid_fills_id of this SharedLines.  # noqa: E501


        :return: The solid_fills_id of this SharedLines.  # noqa: E501
        :rtype: int
        """
        return self._solid_fills_id

    @solid_fills_id.setter
    def solid_fills_id(self, solid_fills_id):
        """Sets the solid_fills_id of this SharedLines.


        :param solid_fills_id: The solid_fills_id of this SharedLines.  # noqa: E501
        :type: int
        """

        self._solid_fills_id = solid_fills_id

    @property
    def dash_type_id(self):
        """Gets the dash_type_id of this SharedLines.  # noqa: E501


        :return: The dash_type_id of this SharedLines.  # noqa: E501
        :rtype: int
        """
        return self._dash_type_id

    @dash_type_id.setter
    def dash_type_id(self, dash_type_id):
        """Sets the dash_type_id of this SharedLines.


        :param dash_type_id: The dash_type_id of this SharedLines.  # noqa: E501
        :type: int
        """

        self._dash_type_id = dash_type_id

    @property
    def head_end_type_id(self):
        """Gets the head_end_type_id of this SharedLines.  # noqa: E501


        :return: The head_end_type_id of this SharedLines.  # noqa: E501
        :rtype: int
        """
        return self._head_end_type_id

    @head_end_type_id.setter
    def head_end_type_id(self, head_end_type_id):
        """Sets the head_end_type_id of this SharedLines.


        :param head_end_type_id: The head_end_type_id of this SharedLines.  # noqa: E501
        :type: int
        """

        self._head_end_type_id = head_end_type_id

    @property
    def tail_end_type_id(self):
        """Gets the tail_end_type_id of this SharedLines.  # noqa: E501


        :return: The tail_end_type_id of this SharedLines.  # noqa: E501
        :rtype: int
        """
        return self._tail_end_type_id

    @tail_end_type_id.setter
    def tail_end_type_id(self, tail_end_type_id):
        """Sets the tail_end_type_id of this SharedLines.


        :param tail_end_type_id: The tail_end_type_id of this SharedLines.  # noqa: E501
        :type: int
        """

        self._tail_end_type_id = tail_end_type_id

    @property
    def weight(self):
        """Gets the weight of this SharedLines.  # noqa: E501


        :return: The weight of this SharedLines.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this SharedLines.


        :param weight: The weight of this SharedLines.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def head_end_height_id(self):
        """Gets the head_end_height_id of this SharedLines.  # noqa: E501


        :return: The head_end_height_id of this SharedLines.  # noqa: E501
        :rtype: int
        """
        return self._head_end_height_id

    @head_end_height_id.setter
    def head_end_height_id(self, head_end_height_id):
        """Sets the head_end_height_id of this SharedLines.


        :param head_end_height_id: The head_end_height_id of this SharedLines.  # noqa: E501
        :type: int
        """

        self._head_end_height_id = head_end_height_id

    @property
    def head_end_width_id(self):
        """Gets the head_end_width_id of this SharedLines.  # noqa: E501


        :return: The head_end_width_id of this SharedLines.  # noqa: E501
        :rtype: int
        """
        return self._head_end_width_id

    @head_end_width_id.setter
    def head_end_width_id(self, head_end_width_id):
        """Sets the head_end_width_id of this SharedLines.


        :param head_end_width_id: The head_end_width_id of this SharedLines.  # noqa: E501
        :type: int
        """

        self._head_end_width_id = head_end_width_id

    @property
    def tail_end_height_id(self):
        """Gets the tail_end_height_id of this SharedLines.  # noqa: E501


        :return: The tail_end_height_id of this SharedLines.  # noqa: E501
        :rtype: int
        """
        return self._tail_end_height_id

    @tail_end_height_id.setter
    def tail_end_height_id(self, tail_end_height_id):
        """Sets the tail_end_height_id of this SharedLines.


        :param tail_end_height_id: The tail_end_height_id of this SharedLines.  # noqa: E501
        :type: int
        """

        self._tail_end_height_id = tail_end_height_id

    @property
    def tail_end_width_id(self):
        """Gets the tail_end_width_id of this SharedLines.  # noqa: E501


        :return: The tail_end_width_id of this SharedLines.  # noqa: E501
        :rtype: int
        """
        return self._tail_end_width_id

    @tail_end_width_id.setter
    def tail_end_width_id(self, tail_end_width_id):
        """Sets the tail_end_width_id of this SharedLines.


        :param tail_end_width_id: The tail_end_width_id of this SharedLines.  # noqa: E501
        :type: int
        """

        self._tail_end_width_id = tail_end_width_id

    @property
    def id(self):
        """Gets the id of this SharedLines.  # noqa: E501


        :return: The id of this SharedLines.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedLines.


        :param id: The id of this SharedLines.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this SharedLines.  # noqa: E501


        :return: The date_created of this SharedLines.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SharedLines.


        :param date_created: The date_created of this SharedLines.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this SharedLines.  # noqa: E501


        :return: The user_created of this SharedLines.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SharedLines.


        :param user_created: The user_created of this SharedLines.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SharedLines.  # noqa: E501


        :return: The date_modified of this SharedLines.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SharedLines.


        :param date_modified: The date_modified of this SharedLines.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this SharedLines.  # noqa: E501


        :return: The user_modified of this SharedLines.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SharedLines.


        :param user_modified: The user_modified of this SharedLines.  # noqa: E501
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
        if not isinstance(other, SharedLines):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
