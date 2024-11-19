#assingment: creat function
message= input(">")
def emoji(message):
    dic_emoji = {
        "happy": ":)",
        "sad": ":("
    }
    output = ""
    for word in message.split():
        output += dic_emoji.get(word, word) + " "
    return output
print(emoji(message))
#make sence why we need function and how it works but i need to practise how i use it