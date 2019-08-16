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


class TableTables(object):
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
        'name': 'str',
        'svg_blob_url': 'str',
        'has_style_part': 'bool',
        'style_part_outer_xml': 'str',
        'parent_graphic_id': 'int',
        'rows': 'str',
        'columns': 'str',
        'cells': 'str',
        'oo_xml_blob_url': 'str',
        'id': 'int',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'svg_blob_url': 'SvgBlobUrl',
        'has_style_part': 'HasStylePart',
        'style_part_outer_xml': 'StylePartOuterXml',
        'parent_graphic_id': 'ParentGraphicId',
        'rows': 'Rows',
        'columns': 'Columns',
        'cells': 'Cells',
        'oo_xml_blob_url': 'OoXmlBlobUrl',
        'id': 'Id',
        'date_created': 'DateCreated',
        'user_created': 'UserCreated',
        'date_modified': 'DateModified',
        'user_modified': 'UserModified'
    }

    def __init__(self, name=None, svg_blob_url=None, has_style_part=None, style_part_outer_xml=None, parent_graphic_id=None, rows=None, columns=None, cells=None, oo_xml_blob_url=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None):  # noqa: E501
        """TableTables - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._svg_blob_url = None
        self._has_style_part = None
        self._style_part_outer_xml = None
        self._parent_graphic_id = None
        self._rows = None
        self._columns = None
        self._cells = None
        self._oo_xml_blob_url = None
        self._id = None
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if svg_blob_url is not None:
            self.svg_blob_url = svg_blob_url
        if has_style_part is not None:
            self.has_style_part = has_style_part
        if style_part_outer_xml is not None:
            self.style_part_outer_xml = style_part_outer_xml
        if parent_graphic_id is not None:
            self.parent_graphic_id = parent_graphic_id
        if rows is not None:
            self.rows = rows
        if columns is not None:
            self.columns = columns
        if cells is not None:
            self.cells = cells
        if oo_xml_blob_url is not None:
            self.oo_xml_blob_url = oo_xml_blob_url
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
    def name(self):
        """Gets the name of this TableTables.  # noqa: E501


        :return: The name of this TableTables.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TableTables.


        :param name: The name of this TableTables.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def svg_blob_url(self):
        """Gets the svg_blob_url of this TableTables.  # noqa: E501


        :return: The svg_blob_url of this TableTables.  # noqa: E501
        :rtype: str
        """
        return self._svg_blob_url

    @svg_blob_url.setter
    def svg_blob_url(self, svg_blob_url):
        """Sets the svg_blob_url of this TableTables.


        :param svg_blob_url: The svg_blob_url of this TableTables.  # noqa: E501
        :type: str
        """

        self._svg_blob_url = svg_blob_url

    @property
    def has_style_part(self):
        """Gets the has_style_part of this TableTables.  # noqa: E501


        :return: The has_style_part of this TableTables.  # noqa: E501
        :rtype: bool
        """
        return self._has_style_part

    @has_style_part.setter
    def has_style_part(self, has_style_part):
        """Sets the has_style_part of this TableTables.


        :param has_style_part: The has_style_part of this TableTables.  # noqa: E501
        :type: bool
        """

        self._has_style_part = has_style_part

    @property
    def style_part_outer_xml(self):
        """Gets the style_part_outer_xml of this TableTables.  # noqa: E501


        :return: The style_part_outer_xml of this TableTables.  # noqa: E501
        :rtype: str
        """
        return self._style_part_outer_xml

    @style_part_outer_xml.setter
    def style_part_outer_xml(self, style_part_outer_xml):
        """Sets the style_part_outer_xml of this TableTables.


        :param style_part_outer_xml: The style_part_outer_xml of this TableTables.  # noqa: E501
        :type: str
        """

        self._style_part_outer_xml = style_part_outer_xml

    @property
    def parent_graphic_id(self):
        """Gets the parent_graphic_id of this TableTables.  # noqa: E501


        :return: The parent_graphic_id of this TableTables.  # noqa: E501
        :rtype: int
        """
        return self._parent_graphic_id

    @parent_graphic_id.setter
    def parent_graphic_id(self, parent_graphic_id):
        """Sets the parent_graphic_id of this TableTables.


        :param parent_graphic_id: The parent_graphic_id of this TableTables.  # noqa: E501
        :type: int
        """

        self._parent_graphic_id = parent_graphic_id

    @property
    def rows(self):
        """Gets the rows of this TableTables.  # noqa: E501


        :return: The rows of this TableTables.  # noqa: E501
        :rtype: str
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this TableTables.


        :param rows: The rows of this TableTables.  # noqa: E501
        :type: str
        """

        self._rows = rows

    @property
    def columns(self):
        """Gets the columns of this TableTables.  # noqa: E501


        :return: The columns of this TableTables.  # noqa: E501
        :rtype: str
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this TableTables.


        :param columns: The columns of this TableTables.  # noqa: E501
        :type: str
        """

        self._columns = columns

    @property
    def cells(self):
        """Gets the cells of this TableTables.  # noqa: E501


        :return: The cells of this TableTables.  # noqa: E501
        :rtype: str
        """
        return self._cells

    @cells.setter
    def cells(self, cells):
        """Sets the cells of this TableTables.


        :param cells: The cells of this TableTables.  # noqa: E501
        :type: str
        """

        self._cells = cells

    @property
    def oo_xml_blob_url(self):
        """Gets the oo_xml_blob_url of this TableTables.  # noqa: E501


        :return: The oo_xml_blob_url of this TableTables.  # noqa: E501
        :rtype: str
        """
        return self._oo_xml_blob_url

    @oo_xml_blob_url.setter
    def oo_xml_blob_url(self, oo_xml_blob_url):
        """Sets the oo_xml_blob_url of this TableTables.


        :param oo_xml_blob_url: The oo_xml_blob_url of this TableTables.  # noqa: E501
        :type: str
        """

        self._oo_xml_blob_url = oo_xml_blob_url

    @property
    def id(self):
        """Gets the id of this TableTables.  # noqa: E501


        :return: The id of this TableTables.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TableTables.


        :param id: The id of this TableTables.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this TableTables.  # noqa: E501


        :return: The date_created of this TableTables.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this TableTables.


        :param date_created: The date_created of this TableTables.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this TableTables.  # noqa: E501


        :return: The user_created of this TableTables.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this TableTables.


        :param user_created: The user_created of this TableTables.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this TableTables.  # noqa: E501


        :return: The date_modified of this TableTables.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this TableTables.


        :param date_modified: The date_modified of this TableTables.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this TableTables.  # noqa: E501


        :return: The user_modified of this TableTables.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this TableTables.


        :param user_modified: The user_modified of this TableTables.  # noqa: E501
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
        if not isinstance(other, TableTables):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
