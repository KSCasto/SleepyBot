async def send_message(message,user_message) -> None:
    if not user_message:
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        # replace this with a call to the cardMaker API
        response = "Hello"
        await message.author.send(response) if is_private else message.channel.send(response)
    except Exception as error:
        print(error)