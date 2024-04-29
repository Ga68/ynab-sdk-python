from ynab_sdk.api.models.responses.scheduled_transactions import (
    ScheduledTransactionsResponse
)
from ynab_sdk.utils.clients.base_client import BaseClient


class ScheduledTransactionsApi:
    def __init__(self, client: BaseClient):
        self.client = client

    def get_scheduled_transactions(
        self, budget_id: str
    ) -> ScheduledTransactionsResponse:
        response = self.client.get(f"/budgets/{budget_id}/scheduled_transactions")
        return ScheduledTransactionsResponse.from_dict(response)
