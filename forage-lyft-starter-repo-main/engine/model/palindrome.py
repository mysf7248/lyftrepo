from datetime import datetime

from engine.sternman_engine import SternmanEngine


class Palindrome(SternmanEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date > datetime.yesterday().date() or self.engine_should_be_serviced():
            return True
        else:
            print('Service not due')
            return False
