# coding: utf-8

"""
    OOXML Automation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import presalytics_ooxml_automation
from presalytics_ooxml_automation.api.documents_api import DocumentsApi  # noqa: E501
from presalytics_ooxml_automation.rest import ApiException


class TestDocumentsApi(unittest.TestCase):
    """DocumentsApi unit test stubs"""

    def setUp(self):
        self.api = presalytics_ooxml_automation.api.documents_api.DocumentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_o_a_documents_download_document_id(self):
        """Test case for o_a_documents_download_document_id

        Link to download a user's document. Can only be accessed by the users who owns the document  # noqa: E501
        """
        pass

    def test_o_a_documents_get_id(self):
        """Test case for o_a_documents_get_id

        Get document information by document id  # noqa: E501
        """
        pass

    def test_o_a_documents_post(self):
        """Test case for o_a_documents_post

        Upload a file into the docAPI, returns a document ids  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
