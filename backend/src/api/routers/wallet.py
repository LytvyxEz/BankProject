from fastapi import APIRouter, Request

from schemas import Wallet, WalletResponse, CreateWalletRequest, bank
from uttils import try_except


wallet_router = APIRouter(prefix='/wallet')

@try_except
@wallet_router.post(path='/create')
def create_wallet(request: Request, wallet_request: CreateWalletRequest):
    wallet = bank.create_wallet(**dict(wallet_request))
    return wallet


@try_except
@wallet_router.get(path='/')
def wallet(request: Request):
    return 'ok'
