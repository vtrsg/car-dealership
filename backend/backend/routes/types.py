from fastapi import APIRouter, Depends, HTTPException  # FastAPI,
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.database import get_session
from backend.models import ModelType
from backend.schemas import Message, ModelTypeList, ModelTypeSchema

router = APIRouter(prefix='/types', tags=['types'])


@router.post('/', response_model=ModelTypeSchema, status_code=201)
def create_type(
    type: ModelTypeSchema, session: Session = Depends(get_session)
):
    db_type = session.scalar(
        select(ModelType).where(ModelType.name == type.name)
    )

    if db_type:
        raise HTTPException(status_code=400, detail='Type already registered')

    db_type = ModelType(
        name=type.name,
    )
    session.add(db_type)
    session.commit()
    session.refresh(db_type)

    return db_type


@router.get('/', response_model=ModelTypeList)
def read_types(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    types = session.scalars(select(ModelType).offset(skip).limit(limit)).all()
    return {'types': types}


@router.put('/{type_id}', response_model=ModelTypeSchema)
def update_type(
    type_id: int,
    type: ModelTypeSchema,
    session: Session = Depends(get_session),
):

    db_type = session.scalar(select(ModelType).where(ModelType.id == type_id))
    if db_type is None:
        raise HTTPException(status_code=404, detail='Type not found')

    db_type.name = type.name

    session.commit()
    session.refresh(db_type)

    return db_type


@router.delete('/{type_id}', response_model=Message)
def delete_type(type_id: int, session: Session = Depends(get_session)):
    db_type = session.scalar(select(ModelType).where(ModelType.id == type_id))

    if db_type is None:
        raise HTTPException(status_code=404, detail='Type not found')

    session.delete(db_type)
    session.commit()

    return {'detail': 'Type deleted'}
