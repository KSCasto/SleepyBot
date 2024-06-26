async def send_message(message,user_message) -> None:
    if not user_message:
        return
    
    # := is the walrus operator, which assigns the result
    # of the right side to the left side, so is_private.
    # Here it checks if the first character of the message is '?'
    # by assigning it to is_private and comparing that to '?'
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        # replace this with desired functions as needed. Generally slash commands will work better though.
        response = "Hello"
        await message.author.send(response) if is_private else message.channel.send(response)
    except Exception as error:
        print(error)