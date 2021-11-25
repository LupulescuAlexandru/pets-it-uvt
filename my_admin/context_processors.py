from datetime import datetime, timedelta
#from .models import modificare_req
#from fisa.models import Fisa

def dates(request):
    todaydate = datetime.today()
    tomorrowdate = todaydate + timedelta(days=1)
    return {'todaydate': todaydate.strftime("%Y-%m-%d"),
            'tomorrowdate': tomorrowdate.strftime("%Y-%m-%d")}
            #'notification_counter': modificare_req.objects.all().count(),
            #'notification_user': Fisa.objects.filter(send_notification__in=[1,2]),
            #'notification_user_counter': Fisa.objects.filter(send_notification__in=[1,2]).count()}