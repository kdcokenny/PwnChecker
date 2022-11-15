from logscale_api import queryClient
from humiolib.HumioExceptions import HumioQueryJobExhaustedException, HumioHTTPException, HumioQueryJobExpiredException


def logscale_breach_list():
    breach_list = {}
    # queryjob = queryClient.create_queryjob("breach_info", is_live=False)
    # for poll_result in queryjob.poll_until_done(): #error on this line
    #     for event in poll_result.events:
    #         breach_name = event["breach_info.Name"]
    #         breach_date = event["breach_info.BreachDate"]
    #         breach_list[breach_name] = breach_date
    #     queryjob = queryClient.create_queryjob("breach_info", is_live=False)
    webStream = queryClient.streaming_query("breach_info", is_live=False)
    for event in webStream:
        breach_name = event["breach_info.Name"]
        breach_date = event["breach_info.BreachDate"]
        breach_list[breach_name] = breach_date
    return breach_list
