from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)


def home(request):
     return render(request, 'index.html',{})

def chat(request):
     return render(request, 'chat.html',{})

class SendMessageView(View):
    def post(self, request, *args, **kwargs):
        message = request.POST.get('message', '')

        # Process the message as needed
        chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"keep the answer 3 sentences always /n {message}",
        }
    ],
    model="gpt-3.5-turbo",
)
        replygpt= (chat_completion.choices[0].message.content)
        replygpt=(f"Hi im probiz,  {replygpt} ")
 
    
        return JsonResponse({'status': 'success', 'replygpt': replygpt})