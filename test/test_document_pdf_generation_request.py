# coding: utf-8

"""
    Samsara API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2020-06-15
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import samsara
from samsara.models.document_pdf_generation_request import DocumentPdfGenerationRequest  # noqa: E501
from samsara.rest import ApiException

class TestDocumentPdfGenerationRequest(unittest.TestCase):
    """DocumentPdfGenerationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DocumentPdfGenerationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.document_pdf_generation_request.DocumentPdfGenerationRequest()  # noqa: E501
        if include_optional :
            return DocumentPdfGenerationRequest(
                document_id = '6c8c0c01-206a-41a4-9d21-15b9978d04cb'
            )
        else :
            return DocumentPdfGenerationRequest(
                document_id = '6c8c0c01-206a-41a4-9d21-15b9978d04cb',
        )

    def testDocumentPdfGenerationRequest(self):
        """Test DocumentPdfGenerationRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
