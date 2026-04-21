from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from app.db.models import User, Ingredients
from app.schemas.onboarding import OnboardingPayload

async def get_or_create_user(db, device_id):
    result = await db.execute(select(User).where(User.device_id == device_id))
    user = result.scalar_one_or_none()
    if not user:
        user = User(device_id = device_id)
        db.add(user)
        await db.commit()
        await db.refresh(user)
    return user
    
async def save_onboarding(db, device_id, payload):
    await db.execute(
        update(User).where(User.device_id == device_id).values(dietary_restrictions = payload.dietary_restrictions, allergies = payload.allergies, pantry_staples = payload.pantry_staples, onboarding_complete = True)
    )
    await db.commit()
    
async def save_ingredients(db, device_id, ingredients):
    new_entry = Ingredients(device_id = device_id, ingredients = ingredients)
    db.add(new_entry)
    await db.commit()