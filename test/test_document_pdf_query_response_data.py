# coding: utf-8

"""
    Samsara API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import samsara
from samsara.models.document_pdf_query_response_data import DocumentPdfQueryResponseData  # noqa: E501
from samsara.rest import ApiException

class TestDocumentPdfQueryResponseData(unittest.TestCase):
    """DocumentPdfQueryResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DocumentPdfQueryResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.document_pdf_query_response_data.DocumentPdfQueryResponseData()  # noqa: E501
        if include_optional :
            return DocumentPdfQueryResponseData(
                completed_at_time = '2020-01-02T15:04:06+07:00', 
                document_id = '6c8c0c01-206a-41a4-9d21-15b9978d04cb', 
                download_document_pdf_url = 'https://samsara-driver-document-pdfs.s3.us-west-2.amazonaws.com/org/38487/42a4cffc-409d-4ddf-ba1c-5e3bbb961cba?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASI...&X-Amz-Date=20200423T162507Z&X-Amz-Expires=86400&X-Amz-Security-Token=IQoJ...-Amz-SignedHeaders=host&response-expires=2020-04-24T16%3A25%3A07Z&X-Amz-Signature=1c6fe87...', 
                id = '5c8c0c01-206a-41a4-9d21-15b9978d04cb', 
                job_status = 'Completed', 
                requested_at_time = '2020-01-02T15:04:05+07:00'
            )
        else :
            return DocumentPdfQueryResponseData(
        )

    def testDocumentPdfQueryResponseData(self):
        """Test DocumentPdfQueryResponseData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
