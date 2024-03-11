from django.contrib.sessions.models import Session


def get_session(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.save()
        session_key = request.session.session_key
    
    session = Session.objects.get(session_key=session_key)

    return session
