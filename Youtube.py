#pip install --upgrade google-api-python-client


from googleapiclient.discovery import build                                       
import requests                                                                   
import pandas as pd                                                               
api_key ='CHAVE DE API AQUI' #Sua chave de api do desenvoledor

youtube = build('youtube','v3', developerKey=api_key) #Criando objeto do youtube
next_page = None

video_comments = []
video_id ='5P3VO-8w-Xk'#Id do vídeo
#https://www.youtube.com/watch?v=ID DO VÍDEO


while True:
  r = youtube.commentThreads().list(part='snippet',videoId=video_id, pageToken=next_page).execute() #Pegando comentários
    
    
  video_comments += r['items']
  next_page = r.get('nextPageToken') #Atribuindo a próxima página

  if next_page is None:
    break


if video_comments is None:                          #Verificando se o vídeo tem comentários
    print('Este vídeo não tem comentários!')
else:
###################################################################################Criando tabela com comentários##########################################################################
  df = pd.json_normalize(video_comments)
  df = df[['snippet.topLevelComment.snippet.likeCount','snippet.topLevelComment.snippet.textDisplay','snippet.topLevelComment.snippet.authorDisplayName']]
  df = df.rename(columns= {'snippet.topLevelComment.snippet.likeCount':'Número de Likes','snippet.topLevelComment.snippet.textDisplay':'Comentário','snippet.topLevelComment.snippet.authorDisplayName':'Comentador'})
  df = df.sort_values(by='Número de Likes', ascending=False)
  
############################################################################################################################################################################################  

print(df[df['Comentário'].str.contains('\?')])#Filtrando comentários que contenham "?" em seu texto 
