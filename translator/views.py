from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from translator.models import Translation
from translator.serializers import TranslationSerializer

# Create your views here.

class FrenchSpanishTranslationViewSet(APIView):

    def get(self, request):
        import google.generativeai as genai

        api_key = ""

        prompt = """
        Traduis "castor" en serbe. La réponse ne doit contenir que la traduction.
        """

        genai.configure(api_key=api_key)

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        return Response(data={"result": response.text}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response(data={}, status=None)

    def put(self, request, pk):
        return Response(data={}, status=None)

    def delete(self, request, pk):
        return Response(data={}, status=None)

class FrenchEnglishTranslationViewSet(APIView):

    def get(self, request):
        return Response(data={}, status=None)

    def post(self, request):
        return Response(data={}, status=None)

    def put(self, request, pk):
        return Response(data={}, status=None)

    def delete(self, request, pk):
        return Response(data={}, status=None)

class AllTranslation(APIView):

    def get(self, request):

        data = Translation.objects.all() # SELECT * FROM TRANSLATION
        serialized_data = TranslationSerializer(data, many=True) # Formater nos données

        return Response(data=serialized_data.data, status=None) # Affichage des données de la réponse sous json



def index(request):
    return render(request, 'index.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})
