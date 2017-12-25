from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse
from personal.backends.analyse import twitter_stream_api
from swe573 import settings
from django.http import HttpResponse
from core.models import Post
from core.forms import HomeForm

def index(request):
   return render(request, 'personal/home.html')


def contact(request):
   return render(request, 'personal/contact.html')


template_name = 'core/home.html'

@login_required
def analyse(request):
    posts = Post.objects.all()
    emotions = twitter_stream_api.DeepYou(request.user.username).give_analyse_result(posts)
    form = HomeForm()
   ##  twitter_stream_api.Result.show_graph(emotions)
  #  image_data = open("deepyou.png", "rb").read()
   # return HttpResponse(image_data, content_type="image/png")
   #  image_data = open(settings.BASE_DIR + settings.STATIC_URL + 'deepyou.png', "rb").read()
   #  deep_you = HttpResponse(image_data, content_type="image/png")
    args = {'form': form, 'posts':posts, 'deep_you':reverse('show_graph')}
    return render(request, template_name,
                  args)


def show_graph(request):
    image_data = open(settings.BASE_DIR + settings.STATIC_URL + 'deepyou.png', "rb").read()
    return HttpResponse(image_data, content_type="image/png")

        # return render(request, 'base.html',
    #               {'content': ['If you would like to contact me, please email me', 'selingungor01@gmail.com']})
    # image_data = open(settings.BASE_DIR + settings.STATIC_URL + 'deepyou.png', "rb").read()
#<div id="container">
#     <img src="something.jpg" alt="" />
# </div>
# # #
# #
# #
# #
# # def showimage(request):
# #     # Construct the graph
# #     t = arange(0.0, 2.0, 0.01)
# #     s = sin(2 * pi * t)
# #     plot(t, s, linewidth=1.0)
# #
# #     xlabel('time (s)')
# #     ylabel('voltage (mV)')
# #     title('About as simple as it gets, folks')
# #     grid(True)
# #
# #     # Store image in a string buffer
# #     buffer = StringIO.StringIO()
# #     canvas = pylab.get_current_fig_manager().canvas
# #     canvas.draw()
# #     pilImage = PIL.Image.fromstring("RGB", canvas.get_width_height(), canvas.tostring_rgb())
# #     pilImage.save(buffer, "PNG")
# #     pylab.close()
# #
# #     # Send buffer in a http response the the browser with the mime type image/png set
# #     return HttpResponse(buffer.getvalue(), mimetype="image/png")
