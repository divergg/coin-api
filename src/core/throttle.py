import time

from rest_framework.throttling import SimpleRateThrottle




class RewardsUserThrottle(SimpleRateThrottle):
    scope = 'create_rewards'
    block_seconds = 10  # Block user if they send repetitive requests in 10 seconds
    requests_to_block = 30

    def get_cache_key(self, request, view) -> str | None:
        if request.user and request.user.is_authenticated:
            return f'throttle_{self.scope}_{request.user.id}'
        return None

    def allow_request(self, request, view):
        result = super().allow_request(request, view)
        now = time.time()
        blocking_history = [timestamp for timestamp in self.history if timestamp > now - self.block_seconds]
        if len(blocking_history) > self.requests_to_block:
            request.user.is_blocked = True
            request.user.save()
            return self.throttle_failure()
        return result