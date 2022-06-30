from importlib.resources import path
from itertools import product
from django.shortcuts import render
from django.contrib import messages
from django.http.response import JsonResponse

# import Entities
from wha_products.models import Audios
from wha_products.models import Company
from wha_products.models import Products

# import speech to text
import speech_recognition as sr
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
from textblob import TextBlob

# Create your views here.

def audio_recorder(request):

    if request.method == "POST":

        try:
            # Get audio Properties
            print("Audio sent to the server correctly!")
            audio_file = request.FILES.get('recorded_audio')
            
            # Get Foreignkey products
            product_id = Products.objects.get(name_product="sentiment_analysis")
            
            # Create Audio object 
            record = Audios.objects.create(audio_path = audio_file, 
                                           product=product_id,
                                           user_company=request.user)
            print("product_id", product_id)
            #speech to text
            audio_path = record.audio_path
            
            audio_text = speech_to_text_google(audio_path)

            # append text to the audio object
            record.audio_text = audio_text 

            # Save into Database 
            record.save()
            messages.success(request, 'Audio recorded, successfully added!')
            
            response = {}
            response['status'] = "success"
            response['data'] = {
                                    "body" : {
                                        "audio_text" : audio_text,
                                        "message" : "Audio recorded, successfully added!"
                                    }
                                }                       
            
            return JsonResponse(response)
                
        except Exception as e:
            # ... PRINT THE ERROR MESSAGE ... #
            print(e)
            response = {}
            response['status'] = "success"
            response['message'] = "Unable to record the audio"
            return JsonResponse(response)
    
    if request.method == "GET":
        template = 'sentiment_analysis/audio_recorder.html'
        
        # Get name of company
        company = {}
        if Company.objects.filter(user_company=request.user):
            company = Company.objects.filter(user_company=request.user)[0]
        
        # Get Recorded audios
        records = Audios.objects.filter(user_company=request.user)
        print(company)
        print(records)
        return render(request, template, {"company" : company,
                                          "records": records})

# create a speech recognition object
r = sr.Recognizer()

def speech_to_text_google(path):
    
    input_audio = "./media/" + str(path)
    ffmpeg_extract_audio(input_audio, "./media/records/output.wav")
    with sr.AudioFile("./media/records/output.wav") as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
    
    return text


def sentiment_analysis(request):
        
    """
        Sentiment analysis using textblob
    """
    # get id audio from ajax post
    id_audio = request.POST.get('id_audio', None)

    # get text from correspondent audio id
    records = Audios.objects.get(id = id_audio)
    text = records.audio_text
    print("text: ", text)

    # create blob object 
    blob = TextBlob(text)
    print("tags", blob.tags)
    print("noun_phrases", blob.noun_phrases)

    response_sentiment_analysis = 0
    for sentence in blob.sentences:
        response_sentiment_analysis = sentence.sentiment.polarity
        
    print(response_sentiment_analysis)
    # save score entiment analysis in the database
    records.score_text = response_sentiment_analysis
    records.save()

    response = {}
    response['status'] = "success"
    response['data'] = {
                                "body" : {
                                    "score" : response_sentiment_analysis,
                                    "message" : "Audio recorded, successfully added!"
                                }
                            }  
    
    return JsonResponse(response)

def audio_delete(request):
    """
        Delete audio recorded
    """
    
    # get id audio from ajax post
    id_audio = request.POST.get('id_audio', None)

    try:
        # get text from correspondent audio id
        record = Audios.objects.get(id = id_audio)
        record.delete()
        messages.success(request, "Record deleted successfully!")

        response = {}
        response["status"] = "success"
        response["data"] = {
                                "body" : {
                                    "message" : "Record deleted successfully!"
                                }
                            }  
        return JsonResponse(response)
 

    except Exception as e:
        # ... PRINT THE ERROR MESSAGE ... #
        print(e)
        response = {}
        response['status'] = "success"
        response['message'] = "Record doesn't exists"
        return JsonResponse(response)



