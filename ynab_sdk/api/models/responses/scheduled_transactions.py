from dataclasses import dataclass
from typing import Any, List, Optional

from ynab_sdk.utils import parsers


@dataclass
class Subscheduledtransaction:
    id: str
    scheduled_transaction_id: str
    amount: int
    memo: Optional[str]
    payee_id: Optional[str]
    category_id: Optional[str]
    transfer_account_id: Optional[str]
    deleted: bool

    @staticmethod
    def from_dict(obj: Any) -> "Subscheduledtransaction":
        assert isinstance(obj, dict)
        sub_transaction_id = parsers.from_str(obj.get("id"))
        scheduled_transaction_id = parsers.from_str(obj.get("scheduled_transaction_id"))
        amount = parsers.from_int(obj.get("amount"))
        memo = parsers.from_str(obj.get("memo"), True)
        payee_id = parsers.from_str(obj.get("payee_id"), True)
        category_id = parsers.from_str(obj.get("category_id"), True)
        transfer_account_id = parsers.from_str(obj.get("transfer_account_id"), True)
        deleted = parsers.from_bool(obj.get("deleted"))
        return Subscheduledtransaction(
            sub_transaction_id,
            scheduled_transaction_id,
            amount,
            memo,
            payee_id,
            category_id,
            transfer_account_id,
            deleted,
        )


@dataclass
class ScheduledTransaction:
    id: str
    date_first: str
    date_next: str
    frequency: str
    amount: int
    memo: Optional[str]
    flag_color: Optional[str]
    account_id: str
    payee_id: Optional[str]
    category_id: Optional[str]
    transfer_account_id: Optional[str]
    deleted: bool
    account_name: str
    payee_name: Optional[str]
    category_name: Optional[str]
    # their type is different from the Transaction's subtransaction; however, it's
    # named the same ("subtransactions") in the API response
    subtransactions: List[Subscheduledtransaction]

    @staticmethod
    def from_dict(obj: Any) -> "ScheduledTransaction":
        assert isinstance(obj, dict)
        scheduled_transaction_id = parsers.from_str(obj.get("id"))
        date_first = parsers.from_str(obj.get("date_first"))
        date_next = parsers.from_str(obj.get("date_next"))
        frequency = parsers.from_str(obj.get("frequency"))
        amount = parsers.from_int(obj.get("amount"))
        memo = parsers.from_str(obj.get("memo"), True)
        flag_color = parsers.from_str(obj.get("flag_color"), True)
        account_id = parsers.from_str(obj.get("account_id"))
        payee_id = parsers.from_str(obj.get("payee_id"), True)
        category_id = parsers.from_str(obj.get("category_id"), True)
        transfer_account_id = parsers.from_str(obj.get("transfer_account_id"), True)
        deleted = parsers.from_bool(obj.get("deleted"))
        account_name = parsers.from_str(obj.get("account_name"))
        payee_name = parsers.from_str(obj.get("payee_name"), True)
        category_name = parsers.from_str(obj.get("category_name"), True)
        subtransactions = parsers.from_list(
            Subscheduledtransaction.from_dict, obj.get("subtransactions")
        )
        return ScheduledTransaction(
            scheduled_transaction_id,
            date_first,
            date_next,
            frequency,
            amount,
            memo,
            flag_color,
            account_id,
            payee_id,
            category_id,
            transfer_account_id,
            deleted,
            account_name,
            payee_name,
            category_name,
            subtransactions,
        )


@dataclass
class Data:
    scheduled_transactions: List[ScheduledTransaction]
    server_knowledge: int

    @staticmethod
    def from_dict(obj: Any) -> "Data":
        assert isinstance(obj, dict)
        scheduled_transactions = parsers.from_list(
            ScheduledTransaction.from_dict, obj.get("scheduled_transactions")
        )
        server_knowledge = parsers.from_int(obj.get("server_knowledge"))
        return Data(scheduled_transactions, server_knowledge)


@dataclass
class ScheduledTransactionsResponse:
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> "ScheduledTransactionsResponse":
        assert isinstance(obj, dict)
        data = Data.from_dict(obj.get("data"))
        return ScheduledTransactionsResponse(data)
