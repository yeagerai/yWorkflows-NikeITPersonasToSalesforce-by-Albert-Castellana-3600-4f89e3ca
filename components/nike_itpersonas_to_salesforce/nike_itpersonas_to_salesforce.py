
import typing
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from core.workflows.abstract_workflow import AbstractWorkflow

class NikeITPersonasToSalesforceIn(BaseModel):
    Link: str

class NikeITPersonasToSalesforceOut(BaseModel):
    Success: bool
    ErrorMessage: Optional[str]

class NikeITPersonasToSalesforce(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: NikeITPersonasToSalesforceIn, callbacks: typing.Any
    ) -> NikeITPersonasToSalesforceOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)

        success = results_dict["Success"]
        error_message = results_dict.get("ErrorMessage")

        out = NikeITPersonasToSalesforceOut(
            Success=success,
            ErrorMessage=error_message,
        )
        return out

load_dotenv()
nike_it_personas_to_salesforce_app = FastAPI()

@nike_it_personas_to_salesforce_app.post("/transform/")
async def transform(
    args: NikeITPersonasToSalesforceIn,
) -> NikeITPersonasToSalesforceOut:
    nike_it_personas_to_salesforce = NikeITPersonasToSalesforce()
    return await nike_it_personas_to_salesforce.transform(args, callbacks=None)
