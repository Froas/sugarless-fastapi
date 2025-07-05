from fastapi import APIRouter, status, Response
from models.products import Product
from config.database import collection
from schema.schemas import list_serial, individual_serial, random_serial
from bson import ObjectId
import redis.asyncio as redis
import json


router = APIRouter()

# r = redis.from_url("redis://localhost")

def serialize(doc):
    doc.pop("_id", None)
    return doc

@router.get("/")
async def get_product():
    products = list_serial(collection.find())
    return products

@router.post("/")
async def post_product(product: Product):
    collection.insert_one(product.dict())

@router.delete("/delete/{id}")
async def delete_product(id: str):
    collection.find_one_and_delete({"_id": ObjectId(id)})

@router.get("/random")
async def get_random():
    # cached = await r.get("random_pool")

    # if cached:
    #     print("Cache is used")
    #     pool = json.loads(cached)
    #     return random_serial(pool)
    
    products = list(collection.find())

    cleaned = [serialize(product) for product in products]

    # await r.set("random_pool", json.dumps(cleaned))
    product = random_serial(cleaned)
    return product


@router.get("/status")
async def get_status(response: Response):
    response.status_code = status.HTTP_200_OK