def aceleradev_middlaware(get_response):

    def middlaware(request):
        response = get_response(request)
        return response

    return middlaware
