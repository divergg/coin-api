from django.db.models.signals import post_save
from django.dispatch import receiver
from src.core.models import ScheduledReward
from src.core.tasks import create_user_reward
from django.utils.timezone import now

@receiver(post_save, sender=ScheduledReward)
def schedule_reward_task(sender, instance, created, **kwargs):
    if created:
        if instance.execute_at and instance.execute_at > now():
            create_user_reward.apply_async(
                kwargs={
                    'user_id': instance.user.id,
                    'amount': instance.amount,
                },
                eta=instance.execute_at,
            )
        else:
            create_user_reward.delay(user_id=instance.user.id, amount=instance.amount)
