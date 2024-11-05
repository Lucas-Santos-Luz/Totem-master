from .views import get_version

def version(request):
    return {'versão': get_version()}
