from fastapi import Depends, HTTPException, status
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session
from auth.models import CategoryAccess, CreateCategoryRequest, Category, Topic, User
from auth.roles import Roles
from auth.token import get_current_user
from auth.database import get_db

def create_category(db: Session, category: CreateCategoryRequest,
                    current_user: User = Depends(get_current_user)):
    if current_user.role != Roles.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="The user is not authorized to create a category.")
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Category not found.")
    return category


def get_categories(db: Session,
               skip: int = 0,
               limit: int = 100,
               sort: str = None,
               search: str = None):
    categories = db.query(Category)
    if search:
        categories = categories.filter(Category.name.contains(search))
    if sort:
        if sort.lower() == "desc":
            categories = categories.order_by(desc(Category.id))
        elif sort.lower() == "asc":
            categories = categories.order_by(asc(Category.id))
    categories = categories.offset(skip).limit(limit).all()
    return categories


def get_topics_in_category(db: Session, category_id: int, skip: int = 0, limit: int = 100):
    topics = db.query(Topic).filter(Topic.category_id == category_id).offset(skip).limit(limit).all()
    if topics is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No topics found in the category.")
    return topics


def toggle_category_visibility(category_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.role == Roles.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can change category visibility."
        )

    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found."
        )

    category.is_private = not category.is_private
    db.commit()

    return {
        "message": f"Visibility for category '{category.name}' changed successfully to {'private' if category.is_private else 'public'}.",
        "category": {
            "id": category.id,
            "name": category.name,
            "is_private": category.is_private
        }
    }

# Privacy isn't included yet
# Also refactor into smaller functions eventually
def read_access(db: Session, category_id: int, user_id: int,
                current_user: User = Depends(get_current_user)):
    if current_user.role != Roles.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="The user is not authorized to give read access.")
    category = db.query(Category).filter_by(id=category_id).first()
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Category not found.")
    if not category.is_private:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="The category is public.")
    access_record = db.query(CategoryAccess).filter_by(category_id=category_id, user_id=user_id).first()
    if access_record is None:
        access_record = CategoryAccess(category_id=category_id, user_id=user_id, read_access=True)
        db.add(access_record)
    else:
        access_record.read_access = True
    db.commit()
    return {"message": "Read permission has been granted."}


# Privacy isn't included yet and user has to have read access to get write access
# Also refactor into smaller functions eventually
def write_access(db: Session, category_id: int, user_id: int,
                 current_user: User = Depends(get_current_user)):
    if current_user.role != Roles.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="The user is not authorized to give write access.")
    category = db.query(Category).filter_by(id=category_id).first()
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Category not found.")
    if not category.is_private:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="The category is public.")
    access_record = db.query(CategoryAccess).filter_by(category_id=category_id, user_id=user_id).first()
    if access_record is None:
        access_record = CategoryAccess(category_id=category_id, user_id=user_id, write_access=True)
        db.add(access_record)
    else:
        access_record.write_access = True
    db.commit()
    return {"message": "Write permission has been granted."}


def revoke_user_access():
    pass


def lock_category():
    pass