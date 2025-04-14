import datetime

from django.utils import timezone

from django.db.models import QuerySet

from src.core.models import User, RewardLog, ScheduledReward




class RewardService:

    @staticmethod
    def retrieve_user_rewards(user: User) -> QuerySet[RewardLog]:
        rewards = RewardLog.objects.filter(user=User)
        return rewards


    @staticmethod
    def request_reward_for_user(user: User, amount: int):
        now = timezone.now()
        execute_at = now + datetime.timedelta(minutes=5)
        return ScheduledReward.objects.create(execute_at=execute_at, user=user, amount=amount)


    @staticmethod
    def create_scheduled_reward(user_id: int, amount: int):
        return RewardLog.objects.create(user_id=user_id, amount=amount)