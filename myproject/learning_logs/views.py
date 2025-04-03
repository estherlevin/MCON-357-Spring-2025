from django.shortcuts import render

# Create your views here.
from learning_logs.models import Topic

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    # get all topics sorted by date_created
    topic_list = Topic.objects.order_by('date_created')
    context = {'topics': topic_list}
    """Show all topics."""
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    a_topic = Topic.objects.get(id=topic_id)
    entries = a_topic.entry_set.order_by('-date_created')
    context = {'topic': a_topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)