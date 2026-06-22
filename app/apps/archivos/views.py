from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def my_files(request):
    docs = request.user.documents.all()
    return render(
        request, "archivos/list.html", {"active": "files", "docs": docs}
    )
