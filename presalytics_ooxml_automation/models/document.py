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


class Document(object):
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
        'story_id': 'str',
        'filename': 'str',
        'owner_guid': 'str',
        'document_type_id': 'int',
        'blob_location': 'str',
        'table_styles_xml_blob_url': 'str',
        'title': 'str'
    }

    attribute_map = {
        'story_id': 'storyId',
        'filename': 'filename',
        'owner_guid': 'ownerGuid',
        'document_type_id': 'documentTypeId',
        'blob_location': 'blobLocation',
        'table_styles_xml_blob_url': 'tableStylesXmlBlobUrl',
        'title': 'title'
    }

    def __init__(self, story_id=None, filename=None, owner_guid=None, document_type_id=None, blob_location=None, table_styles_xml_blob_url=None, title=None, local_vars_configuration=None):  # noqa: E501
        """Document - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._story_id = None
        self._filename = None
        self._owner_guid = None
        self._document_type_id = None
        self._blob_location = None
        self._table_styles_xml_blob_url = None
        self._title = None
        self.discriminator = None

        if story_id is not None:
            self.story_id = story_id
        self.filename = filename
        if owner_guid is not None:
            self.owner_guid = owner_guid
        if document_type_id is not None:
            self.document_type_id = document_type_id
        self.blob_location = blob_location
        self.table_styles_xml_blob_url = table_styles_xml_blob_url
        self.title = title

    @property
    def story_id(self):
        """Gets the story_id of this Document.  # noqa: E501


        :return: The story_id of this Document.  # noqa: E501
        :rtype: str
        """
        return self._story_id

    @story_id.setter
    def story_id(self, story_id):
        """Sets the story_id of this Document.


        :param story_id: The story_id of this Document.  # noqa: E501
        :type: str
        """

        self._story_id = story_id

    @property
    def filename(self):
        """Gets the filename of this Document.  # noqa: E501


        :return: The filename of this Document.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this Document.


        :param filename: The filename of this Document.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def owner_guid(self):
        """Gets the owner_guid of this Document.  # noqa: E501


        :return: The owner_guid of this Document.  # noqa: E501
        :rtype: str
        """
        return self._owner_guid

    @owner_guid.setter
    def owner_guid(self, owner_guid):
        """Sets the owner_guid of this Document.


        :param owner_guid: The owner_guid of this Document.  # noqa: E501
        :type: str
        """

        self._owner_guid = owner_guid

    @property
    def document_type_id(self):
        """Gets the document_type_id of this Document.  # noqa: E501


        :return: The document_type_id of this Document.  # noqa: E501
        :rtype: int
        """
        return self._document_type_id

    @document_type_id.setter
    def document_type_id(self, document_type_id):
        """Sets the document_type_id of this Document.


        :param document_type_id: The document_type_id of this Document.  # noqa: E501
        :type: int
        """

        self._document_type_id = document_type_id

    @property
    def blob_location(self):
        """Gets the blob_location of this Document.  # noqa: E501


        :return: The blob_location of this Document.  # noqa: E501
        :rtype: str
        """
        return self._blob_location

    @blob_location.setter
    def blob_location(self, blob_location):
        """Sets the blob_location of this Document.


        :param blob_location: The blob_location of this Document.  # noqa: E501
        :type: str
        """

        self._blob_location = blob_location

    @property
    def table_styles_xml_blob_url(self):
        """Gets the table_styles_xml_blob_url of this Document.  # noqa: E501


        :return: The table_styles_xml_blob_url of this Document.  # noqa: E501
        :rtype: str
        """
        return self._table_styles_xml_blob_url

    @table_styles_xml_blob_url.setter
    def table_styles_xml_blob_url(self, table_styles_xml_blob_url):
        """Sets the table_styles_xml_blob_url of this Document.


        :param table_styles_xml_blob_url: The table_styles_xml_blob_url of this Document.  # noqa: E501
        :type: str
        """

        self._table_styles_xml_blob_url = table_styles_xml_blob_url

    @property
    def title(self):
        """Gets the title of this Document.  # noqa: E501


        :return: The title of this Document.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Document.


        :param title: The title of this Document.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if not isinstance(other, Document):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Document):
            return True

        return self.to_dict() != other.to_dict()
