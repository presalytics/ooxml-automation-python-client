# coding: utf-8

"""
    OOXML Automation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0-no-tags
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class TableBorders(object):
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
        'top_id': 'str',
        'top': 'SharedLines',
        'bottom_id': 'str',
        'bottom': 'SharedLines',
        'right_id': 'str',
        'right': 'SharedLines',
        'left_id': 'str',
        'left': 'SharedLines',
        't_lto_br_id': 'str',
        't_lto_br': 'SharedLines',
        'b_lto_tr_id': 'str',
        'b_lto_tr': 'SharedLines',
        'id': 'str',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'top_id': 'topId',
        'top': 'top',
        'bottom_id': 'bottomId',
        'bottom': 'bottom',
        'right_id': 'rightId',
        'right': 'right',
        'left_id': 'leftId',
        'left': 'left',
        't_lto_br_id': 'tLtoBRId',
        't_lto_br': 'tLtoBR',
        'b_lto_tr_id': 'bLtoTRId',
        'b_lto_tr': 'bLtoTR',
        'id': 'id',
        'date_created': 'dateCreated',
        'user_created': 'userCreated',
        'date_modified': 'dateModified',
        'user_modified': 'userModified'
    }

    def __init__(self, top_id=None, top=None, bottom_id=None, bottom=None, right_id=None, right=None, left_id=None, left=None, t_lto_br_id=None, t_lto_br=None, b_lto_tr_id=None, b_lto_tr=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """TableBorders - a model defined in OpenAPI"""  # noqa: E501

        self._top_id = None
        self._top = None
        self._bottom_id = None
        self._bottom = None
        self._right_id = None
        self._right = None
        self._left_id = None
        self._left = None
        self._t_lto_br_id = None
        self._t_lto_br = None
        self._b_lto_tr_id = None
        self._b_lto_tr = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        self.top_id = top_id
        if top is not None:
            self.top = top
        self.bottom_id = bottom_id
        if bottom is not None:
            self.bottom = bottom
        self.right_id = right_id
        if right is not None:
            self.right = right
        self.left_id = left_id
        if left is not None:
            self.left = left
        self.t_lto_br_id = t_lto_br_id
        if t_lto_br is not None:
            self.t_lto_br = t_lto_br
        self.b_lto_tr_id = b_lto_tr_id
        if b_lto_tr is not None:
            self.b_lto_tr = b_lto_tr
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
    def top_id(self):
        """Gets the top_id of this TableBorders.  # noqa: E501


        :return: The top_id of this TableBorders.  # noqa: E501
        :rtype: str
        """
        return self._top_id

    @top_id.setter
    def top_id(self, top_id):
        """Sets the top_id of this TableBorders.


        :param top_id: The top_id of this TableBorders.  # noqa: E501
        :type: str
        """

        self._top_id = top_id

    @property
    def top(self):
        """Gets the top of this TableBorders.  # noqa: E501


        :return: The top of this TableBorders.  # noqa: E501
        :rtype: SharedLines
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this TableBorders.


        :param top: The top of this TableBorders.  # noqa: E501
        :type: SharedLines
        """

        self._top = top

    @property
    def bottom_id(self):
        """Gets the bottom_id of this TableBorders.  # noqa: E501


        :return: The bottom_id of this TableBorders.  # noqa: E501
        :rtype: str
        """
        return self._bottom_id

    @bottom_id.setter
    def bottom_id(self, bottom_id):
        """Sets the bottom_id of this TableBorders.


        :param bottom_id: The bottom_id of this TableBorders.  # noqa: E501
        :type: str
        """

        self._bottom_id = bottom_id

    @property
    def bottom(self):
        """Gets the bottom of this TableBorders.  # noqa: E501


        :return: The bottom of this TableBorders.  # noqa: E501
        :rtype: SharedLines
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        """Sets the bottom of this TableBorders.


        :param bottom: The bottom of this TableBorders.  # noqa: E501
        :type: SharedLines
        """

        self._bottom = bottom

    @property
    def right_id(self):
        """Gets the right_id of this TableBorders.  # noqa: E501


        :return: The right_id of this TableBorders.  # noqa: E501
        :rtype: str
        """
        return self._right_id

    @right_id.setter
    def right_id(self, right_id):
        """Sets the right_id of this TableBorders.


        :param right_id: The right_id of this TableBorders.  # noqa: E501
        :type: str
        """

        self._right_id = right_id

    @property
    def right(self):
        """Gets the right of this TableBorders.  # noqa: E501


        :return: The right of this TableBorders.  # noqa: E501
        :rtype: SharedLines
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this TableBorders.


        :param right: The right of this TableBorders.  # noqa: E501
        :type: SharedLines
        """

        self._right = right

    @property
    def left_id(self):
        """Gets the left_id of this TableBorders.  # noqa: E501


        :return: The left_id of this TableBorders.  # noqa: E501
        :rtype: str
        """
        return self._left_id

    @left_id.setter
    def left_id(self, left_id):
        """Sets the left_id of this TableBorders.


        :param left_id: The left_id of this TableBorders.  # noqa: E501
        :type: str
        """

        self._left_id = left_id

    @property
    def left(self):
        """Gets the left of this TableBorders.  # noqa: E501


        :return: The left of this TableBorders.  # noqa: E501
        :rtype: SharedLines
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this TableBorders.


        :param left: The left of this TableBorders.  # noqa: E501
        :type: SharedLines
        """

        self._left = left

    @property
    def t_lto_br_id(self):
        """Gets the t_lto_br_id of this TableBorders.  # noqa: E501


        :return: The t_lto_br_id of this TableBorders.  # noqa: E501
        :rtype: str
        """
        return self._t_lto_br_id

    @t_lto_br_id.setter
    def t_lto_br_id(self, t_lto_br_id):
        """Sets the t_lto_br_id of this TableBorders.


        :param t_lto_br_id: The t_lto_br_id of this TableBorders.  # noqa: E501
        :type: str
        """

        self._t_lto_br_id = t_lto_br_id

    @property
    def t_lto_br(self):
        """Gets the t_lto_br of this TableBorders.  # noqa: E501


        :return: The t_lto_br of this TableBorders.  # noqa: E501
        :rtype: SharedLines
        """
        return self._t_lto_br

    @t_lto_br.setter
    def t_lto_br(self, t_lto_br):
        """Sets the t_lto_br of this TableBorders.


        :param t_lto_br: The t_lto_br of this TableBorders.  # noqa: E501
        :type: SharedLines
        """

        self._t_lto_br = t_lto_br

    @property
    def b_lto_tr_id(self):
        """Gets the b_lto_tr_id of this TableBorders.  # noqa: E501


        :return: The b_lto_tr_id of this TableBorders.  # noqa: E501
        :rtype: str
        """
        return self._b_lto_tr_id

    @b_lto_tr_id.setter
    def b_lto_tr_id(self, b_lto_tr_id):
        """Sets the b_lto_tr_id of this TableBorders.


        :param b_lto_tr_id: The b_lto_tr_id of this TableBorders.  # noqa: E501
        :type: str
        """

        self._b_lto_tr_id = b_lto_tr_id

    @property
    def b_lto_tr(self):
        """Gets the b_lto_tr of this TableBorders.  # noqa: E501


        :return: The b_lto_tr of this TableBorders.  # noqa: E501
        :rtype: SharedLines
        """
        return self._b_lto_tr

    @b_lto_tr.setter
    def b_lto_tr(self, b_lto_tr):
        """Sets the b_lto_tr of this TableBorders.


        :param b_lto_tr: The b_lto_tr of this TableBorders.  # noqa: E501
        :type: SharedLines
        """

        self._b_lto_tr = b_lto_tr

    @property
    def id(self):
        """Gets the id of this TableBorders.  # noqa: E501


        :return: The id of this TableBorders.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TableBorders.


        :param id: The id of this TableBorders.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this TableBorders.  # noqa: E501


        :return: The date_created of this TableBorders.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this TableBorders.


        :param date_created: The date_created of this TableBorders.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this TableBorders.  # noqa: E501


        :return: The user_created of this TableBorders.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this TableBorders.


        :param user_created: The user_created of this TableBorders.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this TableBorders.  # noqa: E501


        :return: The date_modified of this TableBorders.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this TableBorders.


        :param date_modified: The date_modified of this TableBorders.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this TableBorders.  # noqa: E501


        :return: The user_modified of this TableBorders.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this TableBorders.


        :param user_modified: The user_modified of this TableBorders.  # noqa: E501
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
        if not isinstance(other, TableBorders):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
