from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.database import get_session
from backend.models import Brand
from backend.schemas import BrandList, BrandSchema, Message


router = APIRouter(prefix='/brands', tags=['brands'])


@router.post('/', response_model=BrandSchema, status_code=201)
def create_brand(brand: BrandSchema, session: Session = Depends(get_session)):
    db_brand = session.scalar(select(Brand).where(Brand.name == brand.name))

    if db_brand:
        raise HTTPException(status_code=400, detail='Brand already registered')

    db_brand = Brand(
        name=brand.name,
    )
    session.add(db_brand)
    session.commit()
    session.refresh(db_brand)

    return db_brand


@router.get('/', response_model=BrandList)
def read_brands(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    brands = session.scalars(select(Brand).offset(skip).limit(limit)).all()
    return {'brands': brands}


@router.put('/{brand_id}', response_model=BrandSchema)
def update_brand(
    brand_id: int, brand: BrandSchema, session: Session = Depends(get_session)
):

    db_brand = session.scalar(select(Brand).where(Brand.id == brand_id))
    if db_brand is None:
        raise HTTPException(status_code=404, detail='Brand not found')

    db_brand.name = brand.name

    session.commit()
    session.refresh(db_brand)

    return db_brand


@router.delete('/{brand_id}', response_model=Message)
def delete_brand(brand_id: int, session: Session = Depends(get_session)):
    db_brand = session.scalar(select(Brand).where(Brand.id == brand_id))

    if db_brand is None:
        raise HTTPException(status_code=404, detail='Brand not found')

    session.delete(db_brand)
    session.commit()

    return {'detail': 'Brand deleted'}
