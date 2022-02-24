from stations.models import AD_Zones, UserSession, Favourite

def management(request):
    try:
        options = AD_Zones.objects.get(access_name="admin")
    except:
        options = None
    try:
        if not request.session.exists(request.session.session_key):
            request.session.create()
        session = UserSession.objects.filter(session=request.session.session_key)
        if session.exists():
            session = session[0]
            fav = Favourite.objects.filter(session=session)
        else:
            fav = None
    except:
        fav = None    
    

    return {
        'options': options,
        'fav' : fav
    }