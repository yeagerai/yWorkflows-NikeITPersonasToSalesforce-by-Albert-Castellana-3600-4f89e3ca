
# test_nike_it_personas_to_salesforce.py

import pytest
from pydantic import BaseModel
from typing import Optional
from your_module_path import NikeITPersonasToSalesforce, NikeITPersonasToSalesforceIn, NikeITPersonasToSalesforceOut

@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        # Test Case 1 - Success scenario
        (
            NikeITPersonasToSalesforceIn(Link="https://example.com/link1"),
            NikeITPersonasToSalesforceOut(Success=True, ErrorMessage=None),
        ),
        # Test Case 2 - Error scenario
        (
            NikeITPersonasToSalesforceIn(Link="https://example.com/link2"),
            NikeITPersonasToSalesforceOut(Success=False, ErrorMessage="Sample Error"),
        ),
        # Test Case 3 - Another success scenario
        (
            NikeITPersonasToSalesforceIn(Link="https://example.com/link3"),
            NikeITPersonasToSalesforceOut(Success=True, ErrorMessage=None),
        ),
    ],
)
async def test_transform(input_data: NikeITPersonasToSalesforceIn, expected_output: NikeITPersonasToSalesforceOut):
    # Instantiate the component
    nike_it_personas_to_salesforce = NikeITPersonasToSalesforce()

    # Call the transform method with mocked input data
    result = await nike_it_personas_to_salesforce.transform(input_data, callbacks=None)

    # Assert that the output matches the expected output
    assert result == expected_output
