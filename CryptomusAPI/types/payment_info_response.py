from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class ConvertInfo:
    to_currency: str
    commission: float
    rate: float
    amount: float

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> ConvertInfo:
        return cls(
            to_currency=data.get("to_currency"),
            commission=float(data.get("commission", 0)),
            rate=float(data.get("rate", 0)),
            amount=float(data.get("amount", 0))
        )


@dataclass
class PaymentInfoResponse:
    state: int
    uuid: str
    order_id: str
    amount: float
    payment_status: str
    url: str
    expired_at: int
    status: str
    is_final: bool
    created_at: datetime
    updated_at: datetime
    commission: float
    payment_amount: float | None = None
    payment_amount_usd: float | None = None
    payer_amount: float | None = None
    additional_data: str | None = None
    payer_amount_exchange_rate: float | None = None
    discount_percent: float | None = None
    discount: float | None = None
    payer_currency: str | None = None
    currency: str | None = None
    comments: str | None = None
    merchant_amount: float | None = None
    network: str | None = None
    address: str | None = None
    address_qr_code: str | None = None
    from_: str | None = None
    txid: str | None = None
    convert: ConvertInfo | None = None

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> PaymentInfoResponse:
        from_ = data["result"].pop("from", None)
        convert_data = data["result"].pop("convert", None)
        convert = ConvertInfo.from_json(convert_data) if convert_data else None
        return cls(state=data["state"], from_=from_, convert=convert, **data["result"])