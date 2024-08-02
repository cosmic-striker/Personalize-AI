from talk import talk
def commantalk(command):
     if "hi"in command or 'hello' in command:
          talk("hello sir i am here to help you")
          talk("what would u like me to do now")
               
def conversation(command):
    if 'are you single' in command:
        talk('no,I am in a relationship with my creater')

    elif 'are you committed' in command:
        talk('yes,I am in a relationship with my creator')
             
    elif 'thank you' in command:
        talk('no mention, i am all ways there for you')
         
    elif 'good night' in command:
        talk("good night, have a sweet dreams.")
        talk("i hope the next day will shine for you")
           
    elif 'relationship with your creator' in command:
        talk('the relationship between me and him is more like a friend')
            
    elif 'about your creator' in command:
        talk("he is lovily.")
        talk("so cute.")
        talk("i like him very much in all ways.")
        talk("he allways try hard to prove himself.")

    elif "like to work for him" in command:
        talk("yes,of course i like to work for vishal.")
        talk("more then that i wish to work with vishal.")

    elif 'you wish for' in command:
        talk('i wish to stay with my vishal forever')
        talk('to help him when he need')
         
    elif 'created you' in command:
        talk('i was created by vishal. I like him very much in all ways')
                    
    elif 'you work for' in command:
        talk('i was created by vishal to help him, so i work for him ')
 
    elif 'change your name' in command:
        talk("no, you do's not have access to it")
            
    elif 'your code' in command:
        talk("only the creater vishal can access to ")
                 
    elif 'what is your name' in command:
        talk("I hope that was a nice name for me")
         
    elif 'version' in command:
        talk("my version is 0.07")
    else:
        pass