
# NikeITPersonasToSalesforce

This component is part of a workflow that transfers Nike IT Personas information to Salesforce. It receives a link to the source data as input and outputs a Success status (boolean) and an optional ErrorMessage (string) in case of errors.

## Initial generation prompt
description: 'IOs - Inputs:

  - Link: str

  Outputs:

  - Success: bool

  - ErrorMessage: Optional[str]

  '
name: NikeITPersonasToSalesforce


## Transformer breakdown
- Execute the transform of the AbstractWorkflow
- Prepare the Output BaseModel

## Parameters
[]

        