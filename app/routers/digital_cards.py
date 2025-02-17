from fastapi import APIRouter

router = APIRouter(prefix="/card/digital", tags=["Digital Card"])


@router.post('/issue')
async def issue():
    return {"message": "Issue"}


@router.post('/top-up')
async def topUp():
    return {"message": "Top Up"}


@router.post('/cancel/url')
async def cancel_by_url():
    return {"message": "Cancel by url"}


@router.post('/cancel/code')
async def cancel_by_code():
    return {"message": "Cancel by code"}


@router.get('/reverse')
async def reverse():
    return {"message": "Reverse"}


@router.get('/stock')
async def stock():
    return {"message": "Check stock"}


@router.get('/balance')
async def balance():
    return {"message": "Balance"}


@router.post('/async/order')
async def order():
    return {"message": "Order"}


@router.get('/async/check')
async def check():
    return {"message": "Check"}
