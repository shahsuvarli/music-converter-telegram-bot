from pytube import YouTube
import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)


# send songs
@bot.message_handler(func = lambda msg: True )
def start(message):

  yt = YouTube(str(message))
    
  # extract only audio
  video = yt.streams.filter(only_audio=True).first()

  
  # check for destination to save file
  destination = str(message.chat.id)
    
  # download the file
  out_file = video.download(output_path=destination)
  
  # save the file
  base, ext = os.path.splitext(out_file)
  new_file = base + '.mp3'
  os.rename(out_file, new_file)
    
  audio = open(new_file, 'rb')

  bot.send_audio(message.chat.id, audio)


bot.polling()