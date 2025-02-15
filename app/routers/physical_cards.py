from fastapi import APIRouter

router = APIRouter(prefix="/card/physical", tags=["Physical Card"])


@router.post("/activate", )
async def activate():
    return {"message": "Activated"}


@router.post("/deactivate")
async def deactivate():
    return {"message": "Deactivated"}


@router.post("/withdraw")
async def activate():
    return {"message": "Withdrawn"}


@router.post("/top-up")
async def topUp():
    return {"message": "Top Up"}


@router.post("/refund")
async def activate():
    return {"message": "Deactivated"}


@router.post("/order")
async def order():
    return {"message": "Ordered"}


@router.get("/status")
async def status():
    return {"message": "Status"}


@router.post("/fulfill")
async def fulfill():
    return {"message": "Fulfilled"}


@router.get("/balance")
async def balance():
    return {"message": "Balance"}
