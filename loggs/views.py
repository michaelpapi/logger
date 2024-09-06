from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Logg, Loggs
from .forms import LoggForm, LogsForm

# Create your views here.

def index(request):
    """Home page for loggs."""
    return render(request, 'loggs/index.html')


def check_logg_owner(logg, user):
    if logg.owner != user:
        return Http404

@login_required
def loggs(request):
    """Shows all logs."""
    loggs = Logg.objects.filter(owner=request.user).order_by('date_added')
    # loggs = Logg.objects.order_by('date_added')
    context = {'loggs': loggs}
    return render(request, 'loggs/loggs.html', context)

@login_required
def logg(request, logg_id):
    logg = Logg.objects.get(id=logg_id)
    # Make sure the topic belongs to the current user.
    check_logg_owner(logg, request.user)
    

    logs = logg.logs.order_by("-date_added")
    context = {'logg': logg, 'logs': logs}
    return render(request, 'loggs/log.html', context)


@login_required
def new_logg(request):
    """Adds a new logg."""
    if request.method != 'POST':
        # No data has been sent, so create a new form
        form = LoggForm()

    else:
        # POST data has been submitted; so process and save.
        form = LoggForm(data=request.POST)
        if form.is_valid():
            new_logg = form.save(commit=False)
            new_logg.owner = request.user
            new_logg.save()
            return redirect('loggs:loggs')
        
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'loggs/new_logg.html', context)

@login_required
def new_log(request, logg_id):
    """Adds a new log under each Logg."""
    logg = Logg.objects.get(id=logg_id)

    if request.method != 'POST':
        # No data submitted, just creates blank page. 
        form = LogsForm()

    else:
        # POST data submitted; process data
        form = LogsForm(data=request.POST)
        if form.is_valid():
            new_log = form.save(commit=False)
            new_log.logg = logg
            new_log.save()
            return redirect('loggs:logg', logg_id=logg_id)
        
    # Display a blank or invalid form. 
    context = {'logg': logg, 'form': form}
    return render(request, 'loggs/new_log.html', context)


@login_required
def edit_log(request, log_id):
    """Edit an existing log."""
    log = Loggs.objects.get(id=log_id)
    logg = log.logg
    check_logg_owner(logg, request.user)
    

    if request.method != 'POST':
        # Initial request, prefill the form with the current entry.
        form = LogsForm(instance=log)
    
    else:
        # POST data submitted; process data.
        form = LogsForm(instance=log, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('loggs:logg', logg_id=logg.id)
        
    context = {'log': log, 'logg': logg, 'form': form}
    return render(request, 'loggs/edit_log.html', context)


@login_required
def delete_log(request, log_id):
    """Deletes a single log entry."""
    log = Loggs.objects.get(id=log_id)
    logg = log.logg
    check_logg_owner(logg, request.user)

    if request.method == 'POST':
        log.delete()
        return redirect('loggs:logg', logg_id=logg.id)
    else:
        return HttpResponseNotAllowed(['POST'])


@login_required
def delete_logg(request, logg_id):
    """Deletes an entire Logg and all its logs."""
    logg = Logg.objects.get(id=logg_id)
    check_logg_owner(logg, request.user)

    if request.method == 'POST':
        logg.delete()
        return redirect('loggs:loggs')
    else:
        return HttpResponseNotAllowed(['POST'])
