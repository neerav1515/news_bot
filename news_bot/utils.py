
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="bot.json"


import dialogflow_v2 as dialogflow 
d_s_c=dialogflow.SessionsClient()
idc="newsbot-bthgrv"

from gnewsclient import gnewsclient
client=gnewsclient.NewsClient()


def dtc(text,session_id,language_code='en'):
    session=d_s_c.session_path(idc,session_id)
    text_input=dialogflow.types.TextInput(text=text,language_code=language_code)
    query_input=dialogflow.types.QueryInput(text=text_input)
    response=d_s_c.detect_intent(session=session,query_input=query_input)
    return response.query_result


def get_reply(query,chat_id):
    response=dtc(query,chat_id)

    if response.intent.display_name=='get_news':
    	return "get_news",dict(response.parameters)
    else:
        return "small_talk",response.fulfillment_text	


def fetch_news(parameters):
   client.language=parameters.get('language')
   client.location=parameters.get('geo-country')
   #client.location=parameters.get('topic')
   t=str(parameters.get('topic').values[0])[14:]
   p=t[:-1]
   m=p[1:-1]
   client.topic=m

   return client.get_news()[:5]




topics_keyboard=[
  [ 'World', 'Nation'],
  [ 'Technology', 'Entertainmnet'],
  [ 'Science', 'health']
]   


topics_keyboard2=[
  ['Top Stories', 'World', 'Nation'],
  ['Business', 'Technology', 'Entertainmnet'],
  ['Sports', 'Science', 'Health']
]   

intro=(
    " This is a news and small talk bot made by Neerav Ganate(NIT hamirpur) "
    " this bot shows 8 news categories and can even respond to basic commands like hello,how are you,bye "
    "news categories: "
    "  1)WORLD  2)NATIONAL  3)BUSINESS  4)TECHNOLOGY  5)ENTERTAINMENT  6)SPORTS  7)SCIENCE  8)HEALTH   "
    " There are 6 news tabs "
    " in case any of the above tab does not work due to updates just type category_name,country_name,language "
    " also remaining 2 news_categories can we viewed in this manner "
    " you can see any country news in any language(default :usa and english) "
    " type /news to access news tab unlimited number of times "
    " type /help for any help "
)


helpo=(
    " the 8 categories are "
    "  1)WORLD  2)NATIONAL  3)BUSINESS  4)TECHNOLOGY  5)ENTERTAINMENT  6)SPORTS  7)SCIENCE  8)HEALTH   "
    " In case any tab does not work type category_name,country_name,language "
    " bot can also do small talks and greetings "
    " type /news for news tabs "

)