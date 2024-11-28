from fastapi import APIRouter, HTTPException

from schemas import CreateProduct, Product

router = APIRouter(prefix="/prodact", tags=["Products"])

db_products = []


@router.get("/all_products", response_model=list[Product])  
async def get_all_products():
    return db_products

@router.post("/create", response_model=Product) 
async def create_product(product: CreateProduct):
    new_item = {"id": len(db_products),
                "name": product.name,
                "category_id": product.category_id,
                "description": product.description,
                "price": product.price,
                "image_url": product.image_url,
                "stock": product.stock
                }
    db_products.append(new_item)
    return new_item

@router.put("/update_prodact", response_model=Product)
async def update_product(product_id: int, product: CreateProduct):
    for item in db_products:
        if item["id"] == product_id:
            item["name"] = product.name
            item["category_id"] = product.category_id
            item["description"] = product.description
            item["price"] = product.price
            item["image_url"] = product.image_url
            item["stock"] = product.stock
            return item
    raise HTTPException(status_code=404, detail=f"product {product_id} not found")

@router.delete("/delete/{product_id}")
async def delete_product(product_id: int):
    global db_products
    db_products = [item for item in db_products if item["id"] != product_id]
    return {"message": f"Product {product_id} deleted"}