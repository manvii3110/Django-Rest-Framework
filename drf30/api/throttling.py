from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class JackRateThrottle(UserRateThrottle):
    scope='jack'