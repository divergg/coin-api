from celery_singleton import Singleton
from config.celery import app as celery_app

@celery_app.task(name='create_user_reward', base=Singleton)
def create_user_reward(user_id: int, amount: int) -> None:
    from src.core.services import RewardService
    RewardService.create_scheduled_reward(user_id=user_id, amount=amount)
