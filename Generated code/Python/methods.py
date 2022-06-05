# This code in its entirety was generated and formatted automatically

import requests
from types import *

API_URL = 'https://api.telegram.org/bot{token}/{method}'
token = 'your_bot_token_here'
logger = None


def getUpdates(
        offset: int = None,
        limit: int = None,
        timeout: int = None,
        allowed_updates: list[str] = None) -> list[Update]:
    """Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned.
    :param offset: Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id. The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue. All previous updates will forgotten.
    :param limit: Limits the number of updates to be retrieved. Values between 1-100 are accepted. Defaults to 100.
    :param timeout: Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling. Should be positive, short polling should be used for testing purposes only.
    :param allowed_updates: A JSON-serialized list of the update types you want your bot to receive. For example, specify [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these types. See Update for a complete list of available update types. Specify an empty list to receive all update types except chat_member (default). If not specified, the previous setting will be used.Please note that this parameter doesn't affect updates created before the call to the getUpdates, so unwanted updates may be received for a short period of time."""
    request_params = {}
    request_params['offset'] = offset
    request_params['limit'] = limit
    request_params['timeout'] = timeout
    request_params['allowed_updates'] = allowed_updates

    response = requests.get(
        API_URL.format(
            token=token,
            method=getUpdates),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return [Update(item) for item in result]


def setWebhook() -> bool:
    """Use this method to specify a url and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified url, containing a JSON-serialized Update. In case of an unsuccessful request, we will give up after a reasonable amount of attempts. Returns True on success."""
    request_params = None

    response = requests.get(
        API_URL.format(
            token=token,
            method=setWebhook),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def deleteWebhook(drop_pending_updates: bool = None) -> bool:
    """Use this method to remove webhook integration if you decide to switch back to getUpdates. Returns True on success.
    :param drop_pending_updates: Pass True to drop all pending updates"""
    request_params = {}
    request_params['drop_pending_updates'] = drop_pending_updates

    response = requests.get(
        API_URL.format(
            token=token,
            method=deleteWebhook),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def getWebhookInfo() -> WebhookInfo:
    """Use this method to get current webhook status. Requires no parameters. On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty."""
    request_params = None

    response = requests.get(
        API_URL.format(
            token=token,
            method=getWebhookInfo),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return WebhookInfo(result)


def getMe() -> User:
    """A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a User object."""
    request_params = None

    response = requests.get(
        API_URL.format(
            token=token,
            method=getMe),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return User(result)


def logOut() -> bool:
    """Use this method to log out from the cloud Bot API server before launching the bot locally. You must log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns True on success. Requires no parameters."""
    request_params = None

    response = requests.get(
        API_URL.format(
            token=token,
            method=logOut),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def close() -> bool:
    """Use this method to close the bot instance before moving it from one local server to another. You need to delete the webhook before calling this method to ensure that the bot isn't launched again after server restart. The method will return error 429 in the first 10 minutes after the bot is launched. Returns True on success. Requires no parameters."""
    request_params = None

    response = requests.get(
        API_URL.format(
            token=token,
            method=close),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def sendMessage(
        chat_id: int | str,
        text: str,
        parse_mode: str = None,
        entities: list[MessageEntity] = None,
        disable_web_page_preview: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send text messages. On success, the sent Message is returned.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param text: Text of the message to be sent, 1-4096 characters after entities parsing
    :param parse_mode: Mode for parsing entities in the message text. See formatting options for more details.
    :param entities: A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode
    :param disable_web_page_preview: Disables link previews for links in this message
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the sent message from forwarding and saving
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['text'] = text
    request_params['parse_mode'] = parse_mode
    request_params['entities'] = [item.json for item in entities]
    request_params['disable_web_page_preview'] = disable_web_page_preview
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=sendMessage),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def forwardMessage(
        chat_id: int | str,
        from_chat_id: int | str,
        message_id: int,
        disable_notification: bool = None,
        protect_content: bool = None) -> Message:
    """Use this method to forward messages of any kind. Service messages can't be forwarded. On success, the sent Message is returned.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param from_chat_id: Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the forwarded message from forwarding and saving
    :param message_id: Message identifier in the chat specified in from_chat_id"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['from_chat_id'] = from_chat_id
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['message_id'] = message_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=forwardMessage),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def copyMessage(
        chat_id: int | str,
        from_chat_id: int | str,
        message_id: int,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: list[MessageEntity] = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> MessageId:
    """Use this method to copy messages of any kind. Service messages and invoice messages can't be copied. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param from_chat_id: Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
    :param message_id: Message identifier in the chat specified in from_chat_id
    :param caption: New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept
    :param parse_mode: Mode for parsing entities in the new caption. See formatting options for more details.
    :param caption_entities: A JSON-serialized list of special entities that appear in the new caption, which can be specified instead of parse_mode
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the sent message from forwarding and saving
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['from_chat_id'] = from_chat_id
    request_params['message_id'] = message_id
    request_params['caption'] = caption
    request_params['parse_mode'] = parse_mode
    request_params['caption_entities'] = [
        item.json for item in caption_entities]
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=copyMessage),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return MessageId(result)


def sendPhoto(
        chat_id: int | str,
        photo: InputFile | str,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: list[MessageEntity] = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send photos. On success, the sent Message is returned.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param photo: Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20. More info on Sending Files »
    :param caption: Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing
    :param parse_mode: Mode for parsing entities in the photo caption. See formatting options for more details.
    :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the sent message from forwarding and saving
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['photo'] = photo.json
    request_params['caption'] = caption
    request_params['parse_mode'] = parse_mode
    request_params['caption_entities'] = [
        item.json for item in caption_entities]
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=sendPhoto),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def sendAudio() -> Message:
    """Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future."""
    request_params = None

    response = requests.get(
        API_URL.format(
            token=token,
            method=sendAudio),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def sendDocument(
        chat_id: int | str,
        document: InputFile | str,
        thumb: InputFile | str = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: list[MessageEntity] = None,
        disable_content_type_detection: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send general files. On success, the sent Message is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param document: File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »
    :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    :param caption: Document caption (may also be used when resending documents by file_id), 0-1024 characters after entities parsing
    :param parse_mode: Mode for parsing entities in the document caption. See formatting options for more details.
    :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
    :param disable_content_type_detection: Disables automatic server-side content type detection for files uploaded using multipart/form-data
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the sent message from forwarding and saving
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['document'] = document.json
    request_params['thumb'] = thumb.json
    request_params['caption'] = caption
    request_params['parse_mode'] = parse_mode
    request_params['caption_entities'] = [
        item.json for item in caption_entities]
    request_params['disable_content_type_detection'] = disable_content_type_detection
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=sendDocument),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def sendVideo(
        chat_id: int | str,
        video: InputFile | str,
        duration: int = None,
        width: int = None,
        height: int = None,
        thumb: InputFile | str = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: list[MessageEntity] = None,
        supports_streaming: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param video: Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. More info on Sending Files »
    :param duration: Duration of sent video in seconds
    :param width: Video width
    :param height: Video height
    :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    :param caption: Video caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing
    :param parse_mode: Mode for parsing entities in the video caption. See formatting options for more details.
    :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
    :param supports_streaming: Pass True, if the uploaded video is suitable for streaming
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the sent message from forwarding and saving
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['video'] = video.json
    request_params['duration'] = duration
    request_params['width'] = width
    request_params['height'] = height
    request_params['thumb'] = thumb.json
    request_params['caption'] = caption
    request_params['parse_mode'] = parse_mode
    request_params['caption_entities'] = [
        item.json for item in caption_entities]
    request_params['supports_streaming'] = supports_streaming
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=sendVideo),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def sendAnimation(
        chat_id: int | str,
        animation: InputFile | str,
        duration: int = None,
        width: int = None,
        height: int = None,
        thumb: InputFile | str = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: list[MessageEntity] = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent Message is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param animation: Animation to send. Pass a file_id as String to send an animation that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data. More info on Sending Files »
    :param duration: Duration of sent animation in seconds
    :param width: Animation width
    :param height: Animation height
    :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    :param caption: Animation caption (may also be used when resending animation by file_id), 0-1024 characters after entities parsing
    :param parse_mode: Mode for parsing entities in the animation caption. See formatting options for more details.
    :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the sent message from forwarding and saving
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['animation'] = animation.json
    request_params['duration'] = duration
    request_params['width'] = width
    request_params['height'] = height
    request_params['thumb'] = thumb.json
    request_params['caption'] = caption
    request_params['parse_mode'] = parse_mode
    request_params['caption_entities'] = [
        item.json for item in caption_entities]
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=sendAnimation),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def sendVoice(
        chat_id: int | str,
        voice: InputFile | str,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: list[MessageEntity] = None,
        duration: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param voice: Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »
    :param caption: Voice message caption, 0-1024 characters after entities parsing
    :param parse_mode: Mode for parsing entities in the voice message caption. See formatting options for more details.
    :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
    :param duration: Duration of the voice message in seconds
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the sent message from forwarding and saving
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['voice'] = voice.json
    request_params['caption'] = caption
    request_params['parse_mode'] = parse_mode
    request_params['caption_entities'] = [
        item.json for item in caption_entities]
    request_params['duration'] = duration
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=sendVoice),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def sendVideoNote(
        chat_id: int | str,
        video_note: InputFile | str,
        duration: int = None,
        length: int = None,
        thumb: InputFile | str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """As of v.4.0, Telegram clients support rounded square mp4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent Message is returned.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param video_note: Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. More info on Sending Files ». Sending video notes by a URL is currently unsupported
    :param duration: Duration of sent video in seconds
    :param length: Video width and height, i.e. diameter of the video message
    :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the sent message from forwarding and saving
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['video_note'] = video_note.json
    request_params['duration'] = duration
    request_params['length'] = length
    request_params['thumb'] = thumb.json
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=sendVideoNote),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def sendMediaGroup(chat_id: int | str,
                   media: list[InputMediaAudio | InputMediaDocument | InputMediaPhoto | InputMediaVideo],
                   disable_notification: bool = None,
                   protect_content: bool = None,
                   reply_to_message_id: int = None,
                   allow_sending_without_reply: bool = None) -> list[Message]:
    """Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an array of Messages that were sent is returned.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param media: A JSON-serialized array describing messages to be sent, must include 2-10 items
    :param disable_notification: Sends messages silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the sent messages from forwarding and saving
    :param reply_to_message_id: If the messages are a reply, ID of the original message
    :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['media'] = [item.json for item in media]
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply

    response = requests.get(
        API_URL.format(
            token=token,
            method=sendMediaGroup),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return [Message(item) for item in result]


def sendLocation(
        chat_id: int | str,
        latitude: float,
        longitude: float,
        horizontal_accuracy: float = None,
        live_period: int = None,
        heading: int = None,
        proximity_alert_radius: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send point on the map. On success, the sent Message is returned.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param latitude: Latitude of the location
    :param longitude: Longitude of the location
    :param horizontal_accuracy: The radius of uncertainty for the location, measured in meters; 0-1500
    :param live_period: Period in seconds for which the location will be updated (see Live Locations, should be between 60 and 86400.
    :param heading: For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    :param proximity_alert_radius: For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the sent message from forwarding and saving
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['latitude'] = latitude
    request_params['longitude'] = longitude
    request_params['horizontal_accuracy'] = horizontal_accuracy
    request_params['live_period'] = live_period
    request_params['heading'] = heading
    request_params['proximity_alert_radius'] = proximity_alert_radius
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=sendLocation),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def editMessageLiveLocation(
        latitude: float,
        longitude: float,
        chat_id: int | str = None,
        message_id: int = None,
        inline_message_id: str = None,
        horizontal_accuracy: float = None,
        heading: int = None,
        proximity_alert_radius: int = None,
        reply_markup: InlineKeyboardMarkup = None) -> Message:
    """Use this method to edit live location messages. A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.
    :param chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param message_id: Required if inline_message_id is not specified. Identifier of the message to edit
    :param inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message
    :param latitude: Latitude of new location
    :param longitude: Longitude of new location
    :param horizontal_accuracy: The radius of uncertainty for the location, measured in meters; 0-1500
    :param heading: Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    :param proximity_alert_radius: Maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
    :param reply_markup: A JSON-serialized object for a new inline keyboard."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id
    request_params['inline_message_id'] = inline_message_id
    request_params['latitude'] = latitude
    request_params['longitude'] = longitude
    request_params['horizontal_accuracy'] = horizontal_accuracy
    request_params['heading'] = heading
    request_params['proximity_alert_radius'] = proximity_alert_radius
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=editMessageLiveLocation),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def stopMessageLiveLocation(
        chat_id: int | str = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None) -> Message:
    """Use this method to stop updating a live location message before live_period expires. On success, if the message is not an inline message, the edited Message is returned, otherwise True is returned.
    :param chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param message_id: Required if inline_message_id is not specified. Identifier of the message with live location to stop
    :param inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message
    :param reply_markup: A JSON-serialized object for a new inline keyboard."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id
    request_params['inline_message_id'] = inline_message_id
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=stopMessageLiveLocation),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def sendVenue(
        chat_id: int | str,
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        foursquare_id: str = None,
        foursquare_type: str = None,
        google_place_id: str = None,
        google_place_type: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send information about a venue. On success, the sent Message is returned.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param latitude: Latitude of the venue
    :param longitude: Longitude of the venue
    :param title: Name of the venue
    :param address: Address of the venue
    :param foursquare_id: Foursquare identifier of the venue
    :param foursquare_type: Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    :param google_place_id: Google Places identifier of the venue
    :param google_place_type: Google Places type of the venue. (See supported types.)
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the sent message from forwarding and saving
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['latitude'] = latitude
    request_params['longitude'] = longitude
    request_params['title'] = title
    request_params['address'] = address
    request_params['foursquare_id'] = foursquare_id
    request_params['foursquare_type'] = foursquare_type
    request_params['google_place_id'] = google_place_id
    request_params['google_place_type'] = google_place_type
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=sendVenue),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def sendContact(
        chat_id: int | str,
        phone_number: str,
        first_name: str,
        last_name: str = None,
        vcard: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send phone contacts. On success, the sent Message is returned.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param phone_number: Contact's phone number
    :param first_name: Contact's first name
    :param last_name: Contact's last name
    :param vcard: Additional data about the contact in the form of a vCard, 0-2048 bytes
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the sent message from forwarding and saving
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove keyboard or to force a reply from the user."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['phone_number'] = phone_number
    request_params['first_name'] = first_name
    request_params['last_name'] = last_name
    request_params['vcard'] = vcard
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=sendContact),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def sendPoll(
        chat_id: int | str,
        question: str,
        options: list[str],
        is_anonymous: bool = None,
        type: str = None,
        allows_multiple_answers: bool = None,
        correct_option_id: int = None,
        explanation: str = None,
        explanation_parse_mode: str = None,
        explanation_entities: list[MessageEntity] = None,
        open_period: int = None,
        close_date: int = None,
        is_closed: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send a native poll. On success, the sent Message is returned.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param question: Poll question, 1-300 characters
    :param options: A JSON-serialized list of answer options, 2-10 strings 1-100 characters each
    :param is_anonymous: True, if the poll needs to be anonymous, defaults to True
    :param type: Poll type, “quiz” or “regular”, defaults to “regular”
    :param allows_multiple_answers: True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False
    :param correct_option_id: 0-based identifier of the correct answer option, required for polls in quiz mode
    :param explanation: Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing
    :param explanation_parse_mode: Mode for parsing entities in the explanation. See formatting options for more details.
    :param explanation_entities: A JSON-serialized list of special entities that appear in the poll explanation, which can be specified instead of parse_mode
    :param open_period: Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close_date.
    :param close_date: Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can't be used together with open_period.
    :param is_closed: Pass True, if the poll needs to be immediately closed. This can be useful for poll preview.
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the sent message from forwarding and saving
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['question'] = question
    request_params['options'] = options
    request_params['is_anonymous'] = is_anonymous
    request_params['type'] = type
    request_params['allows_multiple_answers'] = allows_multiple_answers
    request_params['correct_option_id'] = correct_option_id
    request_params['explanation'] = explanation
    request_params['explanation_parse_mode'] = explanation_parse_mode
    request_params['explanation_entities'] = [
        item.json for item in explanation_entities]
    request_params['open_period'] = open_period
    request_params['close_date'] = close_date
    request_params['is_closed'] = is_closed
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=sendPoll),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def sendDice(
        chat_id: int | str,
        emoji: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send an animated emoji that will display a random value. On success, the sent Message is returned.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param emoji: Emoji on which the dice throw animation is based. Currently, must be one of “”, “”, “”, “”, “”, or “”. Dice can have values 1-6 for “”, “” and “”, values 1-5 for “” and “”, and values 1-64 for “”. Defaults to “”
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the sent message from forwarding
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['emoji'] = emoji
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=sendDice),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def sendChatAction() -> bool:
    """Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns True on success."""
    request_params = None

    response = requests.get(
        API_URL.format(
            token=token,
            method=sendChatAction),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def getUserProfilePhotos(
        user_id: int,
        offset: int = None,
        limit: int = None) -> UserProfilePhotos:
    """Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object.
    :param user_id: Unique identifier of the target user
    :param offset: Sequential number of the first photo to be returned. By default, all photos are returned.
    :param limit: Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100."""
    request_params = {}
    request_params['user_id'] = user_id
    request_params['offset'] = offset
    request_params['limit'] = limit

    response = requests.get(
        API_URL.format(
            token=token,
            method=getUserProfilePhotos),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return UserProfilePhotos(result)


def getFile(file_id: str) -> File:
    """Use this method to get basic info about a file and prepare it for downloading. For the moment, bots can download files of up to 20MB in size. On success, a File object is returned. The file can then be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>, where <file_path> is taken from the response. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile again.
    :param file_id: File identifier to get info about"""
    request_params = {}
    request_params['file_id'] = file_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=getFile),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return File(result)


def banChatMember(
        chat_id: int | str,
        user_id: int,
        until_date: int = None,
        revoke_messages: bool = None) -> bool:
    """Use this method to ban a user in a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless unbanned first. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.
    :param chat_id: Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername)
    :param user_id: Unique identifier of the target user
    :param until_date: Date when the user will be unbanned, unix time. If user is banned for more than 366 days or less than 30 seconds from the current time they are considered to be banned forever. Applied for supergroups and channels only.
    :param revoke_messages: Pass True to delete all messages from the chat for the user that is being removed. If False, the user will be able to see messages in the group that were sent before the user was removed. Always True for supergroups and channels."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['user_id'] = user_id
    request_params['until_date'] = until_date
    request_params['revoke_messages'] = revoke_messages

    response = requests.get(
        API_URL.format(
            token=token,
            method=banChatMember),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def unbanChatMember(
        chat_id: int | str,
        user_id: int,
        only_if_banned: bool = None) -> bool:
    """Use this method to unban a previously banned user in a supergroup or channel. The user will not return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be removed from the chat. If you don't want this, use the parameter only_if_banned. Returns True on success.
    :param chat_id: Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername)
    :param user_id: Unique identifier of the target user
    :param only_if_banned: Do nothing if the user is not banned"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['user_id'] = user_id
    request_params['only_if_banned'] = only_if_banned

    response = requests.get(
        API_URL.format(
            token=token,
            method=unbanChatMember),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def restrictChatMember(
        chat_id: int | str,
        user_id: int,
        permissions: ChatPermissions,
        until_date: int = None) -> bool:
    """Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass True for all permissions to lift restrictions from a user. Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    :param user_id: Unique identifier of the target user
    :param permissions: A JSON-serialized object for new user permissions
    :param until_date: Date when restrictions will be lifted for the user, unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['user_id'] = user_id
    request_params['permissions'] = permissions.json
    request_params['until_date'] = until_date

    response = requests.get(
        API_URL.format(
            token=token,
            method=restrictChatMember),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def promoteChatMember(
        chat_id: int | str,
        user_id: int,
        is_anonymous: bool = None,
        can_manage_chat: bool = None,
        can_post_messages: bool = None,
        can_edit_messages: bool = None,
        can_delete_messages: bool = None,
        can_manage_video_chats: bool = None,
        can_restrict_members: bool = None,
        can_promote_members: bool = None,
        can_change_info: bool = None,
        can_invite_users: bool = None,
        can_pin_messages: bool = None) -> bool:
    """Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass False for all boolean parameters to demote a user. Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param user_id: Unique identifier of the target user
    :param is_anonymous: Pass True, if the administrator's presence in the chat is hidden
    :param can_manage_chat: Pass True, if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege
    :param can_post_messages: Pass True, if the administrator can create channel posts, channels only
    :param can_edit_messages: Pass True, if the administrator can edit messages of other users and can pin messages, channels only
    :param can_delete_messages: Pass True, if the administrator can delete messages of other users
    :param can_manage_video_chats: Pass True, if the administrator can manage video chats
    :param can_restrict_members: Pass True, if the administrator can restrict, ban or unban chat members
    :param can_promote_members: Pass True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by him)
    :param can_change_info: Pass True, if the administrator can change chat title, photo and other settings
    :param can_invite_users: Pass True, if the administrator can invite new users to the chat
    :param can_pin_messages: Pass True, if the administrator can pin messages, supergroups only"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['user_id'] = user_id
    request_params['is_anonymous'] = is_anonymous
    request_params['can_manage_chat'] = can_manage_chat
    request_params['can_post_messages'] = can_post_messages
    request_params['can_edit_messages'] = can_edit_messages
    request_params['can_delete_messages'] = can_delete_messages
    request_params['can_manage_video_chats'] = can_manage_video_chats
    request_params['can_restrict_members'] = can_restrict_members
    request_params['can_promote_members'] = can_promote_members
    request_params['can_change_info'] = can_change_info
    request_params['can_invite_users'] = can_invite_users
    request_params['can_pin_messages'] = can_pin_messages

    response = requests.get(
        API_URL.format(
            token=token,
            method=promoteChatMember),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def setChatAdministratorCustomTitle(
        chat_id: int | str,
        user_id: int,
        custom_title: str) -> bool:
    """Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    :param user_id: Unique identifier of the target user
    :param custom_title: New custom title for the administrator; 0-16 characters, emoji are not allowed"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['user_id'] = user_id
    request_params['custom_title'] = custom_title

    response = requests.get(
        API_URL.format(
            token=token,
            method=setChatAdministratorCustomTitle),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def banChatSenderChat(chat_id: int | str, sender_chat_id: int) -> bool:
    """Use this method to ban a channel chat in a supergroup or a channel. Until the chat is unbanned, the owner of the banned chat won't be able to send messages on behalf of any of their channels. The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights. Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param sender_chat_id: Unique identifier of the target sender chat"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['sender_chat_id'] = sender_chat_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=banChatSenderChat),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def unbanChatSenderChat(chat_id: int | str, sender_chat_id: int) -> bool:
    """Use this method to unban a previously banned channel chat in a supergroup or channel. The bot must be an administrator for this to work and must have the appropriate administrator rights. Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param sender_chat_id: Unique identifier of the target sender chat"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['sender_chat_id'] = sender_chat_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=unbanChatSenderChat),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def setChatPermissions(
        chat_id: int | str,
        permissions: ChatPermissions) -> bool:
    """Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the can_restrict_members administrator rights. Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    :param permissions: A JSON-serialized object for new default chat permissions"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['permissions'] = permissions.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=setChatPermissions),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def exportChatInviteLink(chat_id: int | str) -> str:
    """Use this method to generate a new primary invite link for a chat; any previously generated primary link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the new invite link as String on success.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)"""
    request_params = {}
    request_params['chat_id'] = chat_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=exportChatInviteLink),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return str(result)


def createChatInviteLink(
        chat_id: int | str,
        name: str = None,
        expire_date: int = None,
        member_limit: int = None,
        creates_join_request: bool = None) -> ChatInviteLink:
    """Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. The link can be revoked using the method revokeChatInviteLink. Returns the new invite link as ChatInviteLink object.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param name: Invite link name; 0-32 characters
    :param expire_date: Point in time (Unix timestamp) when the link will expire
    :param member_limit: Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
    :param creates_join_request: True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can't be specified"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['name'] = name
    request_params['expire_date'] = expire_date
    request_params['member_limit'] = member_limit
    request_params['creates_join_request'] = creates_join_request

    response = requests.get(
        API_URL.format(
            token=token,
            method=createChatInviteLink),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return ChatInviteLink(result)


def editChatInviteLink(
        chat_id: int | str,
        invite_link: str,
        name: str = None,
        expire_date: int = None,
        member_limit: int = None,
        creates_join_request: bool = None) -> ChatInviteLink:
    """Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a ChatInviteLink object.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param invite_link: The invite link to edit
    :param name: Invite link name; 0-32 characters
    :param expire_date: Point in time (Unix timestamp) when the link will expire
    :param member_limit: Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
    :param creates_join_request: True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can't be specified"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['invite_link'] = invite_link
    request_params['name'] = name
    request_params['expire_date'] = expire_date
    request_params['member_limit'] = member_limit
    request_params['creates_join_request'] = creates_join_request

    response = requests.get(
        API_URL.format(
            token=token,
            method=editChatInviteLink),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return ChatInviteLink(result)


def revokeChatInviteLink(
        chat_id: int | str,
        invite_link: str) -> ChatInviteLink:
    """Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the revoked invite link as ChatInviteLink object.
    :param chat_id: Unique identifier of the target chat or username of the target channel (in the format @channelusername)
    :param invite_link: The invite link to revoke"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['invite_link'] = invite_link

    response = requests.get(
        API_URL.format(
            token=token,
            method=revokeChatInviteLink),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return ChatInviteLink(result)


def approveChatJoinRequest(chat_id: int | str, user_id: int) -> bool:
    """Use this method to approve a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param user_id: Unique identifier of the target user"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['user_id'] = user_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=approveChatJoinRequest),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def declineChatJoinRequest(chat_id: int | str, user_id: int) -> bool:
    """Use this method to decline a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param user_id: Unique identifier of the target user"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['user_id'] = user_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=declineChatJoinRequest),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def setChatPhoto(chat_id: int | str, photo: InputFile) -> bool:
    """Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param photo: New chat photo, uploaded using multipart/form-data"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['photo'] = photo.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=setChatPhoto),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def deleteChatPhoto(chat_id: int | str) -> bool:
    """Use this method to delete a chat photo. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)"""
    request_params = {}
    request_params['chat_id'] = chat_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=deleteChatPhoto),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def setChatTitle(chat_id: int | str, title: str) -> bool:
    """Use this method to change the title of a chat. Titles can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param title: New chat title, 1-255 characters"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['title'] = title

    response = requests.get(
        API_URL.format(
            token=token,
            method=setChatTitle),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def setChatDescription(chat_id: int | str, description: str = None) -> bool:
    """Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param description: New chat description, 0-255 characters"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['description'] = description

    response = requests.get(
        API_URL.format(
            token=token,
            method=setChatDescription),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def pinChatMessage(
        chat_id: int | str,
        message_id: int,
        disable_notification: bool = None) -> bool:
    """Use this method to add a message to the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param message_id: Identifier of a message to pin
    :param disable_notification: Pass True, if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels and private chats."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id
    request_params['disable_notification'] = disable_notification

    response = requests.get(
        API_URL.format(
            token=token,
            method=pinChatMessage),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def unpinChatMessage(chat_id: int | str, message_id: int = None) -> bool:
    """Use this method to remove a message from the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param message_id: Identifier of a message to unpin. If not specified, the most recent pinned message (by sending date) will be unpinned."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=unpinChatMessage),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def unpinAllChatMessages(chat_id: int | str) -> bool:
    """Use this method to clear the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)"""
    request_params = {}
    request_params['chat_id'] = chat_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=unpinAllChatMessages),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def leaveChat(chat_id: int | str) -> bool:
    """Use this method for your bot to leave a group, supergroup or channel. Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)"""
    request_params = {}
    request_params['chat_id'] = chat_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=leaveChat),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def getChat(chat_id: int | str) -> Chat:
    """Use this method to get up to date information about the chat (current name of the user for one-on-one conversations, current username of a user, group or channel, etc.). Returns a Chat object on success.
    :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)"""
    request_params = {}
    request_params['chat_id'] = chat_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=getChat),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Chat(result)


def getChatAdministrators(chat_id: int | str) -> list[ChatMember]:
    """Use this method to get a list of administrators in a chat. On success, returns an Array of ChatMember objects that contains information about all chat administrators except other bots. If the chat is a group or a supergroup and no administrators were appointed, only the creator will be returned.
    :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)"""
    request_params = {}
    request_params['chat_id'] = chat_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=getChatAdministrators),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return [ChatMember(item) for item in result]


def getChatMemberCount(chat_id: int | str) -> int:
    """Use this method to get the number of members in a chat. Returns Int on success.
    :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)"""
    request_params = {}
    request_params['chat_id'] = chat_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=getChatMemberCount),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return int(result)


def getChatMember(chat_id: int | str, user_id: int) -> ChatMember:
    """Use this method to get information about a member of a chat. Returns a ChatMember object on success.
    :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
    :param user_id: Unique identifier of the target user"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['user_id'] = user_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=getChatMember),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return ChatMember(result)


def setChatStickerSet(chat_id: int | str, sticker_set_name: str) -> bool:
    """Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    :param sticker_set_name: Name of the sticker set to be set as the group sticker set"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['sticker_set_name'] = sticker_set_name

    response = requests.get(
        API_URL.format(
            token=token,
            method=setChatStickerSet),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def deleteChatStickerSet(chat_id: int | str) -> bool:
    """Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)"""
    request_params = {}
    request_params['chat_id'] = chat_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=deleteChatStickerSet),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def answerCallbackQuery() -> bool:
    """Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned."""
    request_params = None

    response = requests.get(
        API_URL.format(
            token=token,
            method=answerCallbackQuery),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def setMyCommands(
        commands: list[BotCommand],
        scope: BotCommandScope = None,
        language_code: str = None) -> bool:
    """Use this method to change the list of the bot's commands. See https://core.telegram.org/bots#commands for more details about bot commands. Returns True on success.
    :param commands: A JSON-serialized list of bot commands to be set as the list of the bot's commands. At most 100 commands can be specified.
    :param scope: A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to BotCommandScopeDefault.
    :param language_code: A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands"""
    request_params = {}
    request_params['commands'] = [item.json for item in commands]
    request_params['scope'] = scope.json
    request_params['language_code'] = language_code

    response = requests.get(
        API_URL.format(
            token=token,
            method=setMyCommands),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def deleteMyCommands(
        scope: BotCommandScope = None,
        language_code: str = None) -> bool:
    """Use this method to delete the list of the bot's commands for the given scope and user language. After deletion, higher level commands will be shown to affected users. Returns True on success.
    :param scope: A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to BotCommandScopeDefault.
    :param language_code: A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands"""
    request_params = {}
    request_params['scope'] = scope.json
    request_params['language_code'] = language_code

    response = requests.get(
        API_URL.format(
            token=token,
            method=deleteMyCommands),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def getMyCommands(scope: BotCommandScope = None,
                  language_code: str = None) -> list[BotCommand]:
    """Use this method to get the current list of the bot's commands for the given scope and user language. Returns Array of BotCommand on success. If commands aren't set, an empty list is returned.
    :param scope: A JSON-serialized object, describing scope of users. Defaults to BotCommandScopeDefault.
    :param language_code: A two-letter ISO 639-1 language code or an empty string"""
    request_params = {}
    request_params['scope'] = scope.json
    request_params['language_code'] = language_code

    response = requests.get(
        API_URL.format(
            token=token,
            method=getMyCommands),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return [BotCommand(item) for item in result]


def setChatMenuButton(
        chat_id: int = None,
        menu_button: MenuButton = None) -> bool:
    """Use this method to change the bot's menu button in a private chat, or the default menu button. Returns True on success.
    :param chat_id: Unique identifier for the target private chat. If not specified, default bot's menu button will be changed
    :param menu_button: A JSON-serialized object for the bot's new menu button. Defaults to MenuButtonDefault"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['menu_button'] = menu_button.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=setChatMenuButton),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def getChatMenuButton(chat_id: int = None) -> MenuButton:
    """Use this method to get the current value of the bot's menu button in a private chat, or the default menu button. Returns MenuButton on success.
    :param chat_id: Unique identifier for the target private chat. If not specified, default bot's menu button will be returned"""
    request_params = {}
    request_params['chat_id'] = chat_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=getChatMenuButton),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return MenuButton(result)


def setMyDefaultAdministratorRights(
        rights: ChatAdministratorRights = None,
        for_channels: bool = None) -> bool:
    """Use this method to change the default administrator rights requested by the bot when it's added as an administrator to groups or channels. These rights will be suggested to users, but they are are free to modify the list before adding the bot. Returns True on success.
    :param rights: A JSON-serialized object describing new default administrator rights. If not specified, the default administrator rights will be cleared.
    :param for_channels: Pass True to change the default administrator rights of the bot in channels. Otherwise, the default administrator rights of the bot for groups and supergroups will be changed."""
    request_params = {}
    request_params['rights'] = rights.json
    request_params['for_channels'] = for_channels

    response = requests.get(
        API_URL.format(
            token=token,
            method=setMyDefaultAdministratorRights),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def getMyDefaultAdministratorRights(
        for_channels: bool = None) -> ChatAdministratorRights:
    """Use this method to get the current default administrator rights of the bot. Returns ChatAdministratorRights on success.
    :param for_channels: Pass True to get default administrator rights of the bot in channels. Otherwise, default administrator rights of the bot for groups and supergroups will be returned."""
    request_params = {}
    request_params['for_channels'] = for_channels

    response = requests.get(
        API_URL.format(
            token=token,
            method=getMyDefaultAdministratorRights),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return ChatAdministratorRights(result)


def editMessageText(
        text: str,
        chat_id: int | str = None,
        message_id: int = None,
        inline_message_id: str = None,
        parse_mode: str = None,
        entities: list[MessageEntity] = None,
        disable_web_page_preview: bool = None,
        reply_markup: InlineKeyboardMarkup = None) -> Message:
    """Use this method to edit text and game messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.
    :param chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param message_id: Required if inline_message_id is not specified. Identifier of the message to edit
    :param inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message
    :param text: New text of the message, 1-4096 characters after entities parsing
    :param parse_mode: Mode for parsing entities in the message text. See formatting options for more details.
    :param entities: A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode
    :param disable_web_page_preview: Disables link previews for links in this message
    :param reply_markup: A JSON-serialized object for an inline keyboard."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id
    request_params['inline_message_id'] = inline_message_id
    request_params['text'] = text
    request_params['parse_mode'] = parse_mode
    request_params['entities'] = [item.json for item in entities]
    request_params['disable_web_page_preview'] = disable_web_page_preview
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=editMessageText),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def editMessageCaption(
        chat_id: int | str = None,
        message_id: int = None,
        inline_message_id: str = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: list[MessageEntity] = None,
        reply_markup: InlineKeyboardMarkup = None) -> Message:
    """Use this method to edit captions of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.
    :param chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param message_id: Required if inline_message_id is not specified. Identifier of the message to edit
    :param inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message
    :param caption: New caption of the message, 0-1024 characters after entities parsing
    :param parse_mode: Mode for parsing entities in the message caption. See formatting options for more details.
    :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
    :param reply_markup: A JSON-serialized object for an inline keyboard."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id
    request_params['inline_message_id'] = inline_message_id
    request_params['caption'] = caption
    request_params['parse_mode'] = parse_mode
    request_params['caption_entities'] = [
        item.json for item in caption_entities]
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=editMessageCaption),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def editMessageMedia(
        media: InputMedia,
        chat_id: int | str = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None) -> Message:
    """Use this method to edit animation, audio, document, photo, or video messages. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo or a video otherwise. When an inline message is edited, a new file can't be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.
    :param chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param message_id: Required if inline_message_id is not specified. Identifier of the message to edit
    :param inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message
    :param media: A JSON-serialized object for a new media content of the message
    :param reply_markup: A JSON-serialized object for a new inline keyboard."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id
    request_params['inline_message_id'] = inline_message_id
    request_params['media'] = media.json
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=editMessageMedia),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def editMessageReplyMarkup(
        chat_id: int | str = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None) -> Message:
    """Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.
    :param chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param message_id: Required if inline_message_id is not specified. Identifier of the message to edit
    :param inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message
    :param reply_markup: A JSON-serialized object for an inline keyboard."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id
    request_params['inline_message_id'] = inline_message_id
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=editMessageReplyMarkup),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def stopPoll(chat_id: int | str, message_id: int,
             reply_markup: InlineKeyboardMarkup = None) -> Poll:
    """Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param message_id: Identifier of the original message with the poll
    :param reply_markup: A JSON-serialized object for a new message inline keyboard."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=stopPoll),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Poll(result)


def deleteMessage(chat_id: int | str, message_id: int) -> bool:
    """Use this method to delete a message, including service messages, with the following limitations:- A message can only be deleted if it was sent less than 48 hours ago.- A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.- Bots can delete outgoing messages in private chats, groups, and supergroups.- Bots can delete incoming messages in private chats.- Bots granted can_post_messages permissions can delete outgoing messages in channels.- If the bot is an administrator of a group, it can delete any message there.- If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.Returns True on success.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param message_id: Identifier of the message to delete"""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=deleteMessage),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def sendSticker(
        chat_id: int | str,
        sticker: InputFile | str,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers. On success, the sent Message is returned.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param sticker: Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the sent message from forwarding and saving
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['sticker'] = sticker.json
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=sendSticker),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def getStickerSet(name: str) -> StickerSet:
    """Use this method to get a sticker set. On success, a StickerSet object is returned.
    :param name: Name of the sticker set"""
    request_params = {}
    request_params['name'] = name

    response = requests.get(
        API_URL.format(
            token=token,
            method=getStickerSet),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return StickerSet(result)


def uploadStickerFile(user_id: int, png_sticker: InputFile) -> File:
    """Use this method to upload a .PNG file with a sticker for later use in createNewStickerSet and addStickerToSet methods (can be used multiple times). Returns the uploaded File on success.
    :param user_id: User identifier of sticker file owner
    :param png_sticker: PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. More info on Sending Files »"""
    request_params = {}
    request_params['user_id'] = user_id
    request_params['png_sticker'] = png_sticker.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=uploadStickerFile),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return File(result)


def createNewStickerSet(
        user_id: int,
        name: str,
        title: str,
        emojis: str,
        png_sticker: InputFile | str = None,
        tgs_sticker: InputFile = None,
        webm_sticker: InputFile = None,
        contains_masks: bool = None,
        mask_position: MaskPosition = None) -> bool:
    """Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. You must use exactly one of the fields png_sticker, tgs_sticker, or webm_sticker. Returns True on success.
    :param user_id: User identifier of created sticker set owner
    :param name: Short name of sticker set, to be used in t.me/addstickers/ URLs (e.g., animals). Can contain only english letters, digits and underscores. Must begin with a letter, can't contain consecutive underscores and must end in "_by_<bot_username>". <bot_username> is case insensitive. 1-64 characters.
    :param title: Sticker set title, 1-64 characters
    :param png_sticker: PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »
    :param tgs_sticker: TGS animation with the sticker, uploaded using multipart/form-data. See https://core.telegram.org/stickers#animated-sticker-requirements for technical requirements
    :param webm_sticker: WEBM video with the sticker, uploaded using multipart/form-data. See https://core.telegram.org/stickers#video-sticker-requirements for technical requirements
    :param emojis: One or more emoji corresponding to the sticker
    :param contains_masks: Pass True, if a set of mask stickers should be created
    :param mask_position: A JSON-serialized object for position where the mask should be placed on faces"""
    request_params = {}
    request_params['user_id'] = user_id
    request_params['name'] = name
    request_params['title'] = title
    request_params['png_sticker'] = png_sticker.json
    request_params['tgs_sticker'] = tgs_sticker.json
    request_params['webm_sticker'] = webm_sticker.json
    request_params['emojis'] = emojis
    request_params['contains_masks'] = contains_masks
    request_params['mask_position'] = mask_position.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=createNewStickerSet),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def addStickerToSet(
        user_id: int,
        name: str,
        emojis: str,
        png_sticker: InputFile | str = None,
        tgs_sticker: InputFile = None,
        webm_sticker: InputFile = None,
        mask_position: MaskPosition = None) -> bool:
    """Use this method to add a new sticker to a set created by the bot. You must use exactly one of the fields png_sticker, tgs_sticker, or webm_sticker. Animated stickers can be added to animated sticker sets and only to them. Animated sticker sets can have up to 50 stickers. Static sticker sets can have up to 120 stickers. Returns True on success.
    :param user_id: User identifier of sticker set owner
    :param name: Sticker set name
    :param png_sticker: PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »
    :param tgs_sticker: TGS animation with the sticker, uploaded using multipart/form-data. See https://core.telegram.org/stickers#animated-sticker-requirements for technical requirements
    :param webm_sticker: WEBM video with the sticker, uploaded using multipart/form-data. See https://core.telegram.org/stickers#video-sticker-requirements for technical requirements
    :param emojis: One or more emoji corresponding to the sticker
    :param mask_position: A JSON-serialized object for position where the mask should be placed on faces"""
    request_params = {}
    request_params['user_id'] = user_id
    request_params['name'] = name
    request_params['png_sticker'] = png_sticker.json
    request_params['tgs_sticker'] = tgs_sticker.json
    request_params['webm_sticker'] = webm_sticker.json
    request_params['emojis'] = emojis
    request_params['mask_position'] = mask_position.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=addStickerToSet),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def setStickerPositionInSet(sticker: str, position: int) -> bool:
    """Use this method to move a sticker in a set created by the bot to a specific position. Returns True on success.
    :param sticker: File identifier of the sticker
    :param position: New sticker position in the set, zero-based"""
    request_params = {}
    request_params['sticker'] = sticker
    request_params['position'] = position

    response = requests.get(
        API_URL.format(
            token=token,
            method=setStickerPositionInSet),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def deleteStickerFromSet(sticker: str) -> bool:
    """Use this method to delete a sticker from a set created by the bot. Returns True on success.
    :param sticker: File identifier of the sticker"""
    request_params = {}
    request_params['sticker'] = sticker

    response = requests.get(
        API_URL.format(
            token=token,
            method=deleteStickerFromSet),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def setStickerSetThumb(
        name: str,
        user_id: int,
        thumb: InputFile | str = None) -> bool:
    """Use this method to set the thumbnail of a sticker set. Animated thumbnails can be set for animated sticker sets only. Video thumbnails can be set only for video sticker sets only. Returns True on success.
    :param name: Sticker set name
    :param user_id: User identifier of the sticker set owner
    :param thumb: A PNG image with the thumbnail, must be up to 128 kilobytes in size and have width and height exactly 100px, or a TGS animation with the thumbnail up to 32 kilobytes in size; see https://core.telegram.org/stickers#animated-sticker-requirements for animated sticker technical requirements, or a WEBM video with the thumbnail up to 32 kilobytes in size; see https://core.telegram.org/stickers#video-sticker-requirements for video sticker technical requirements. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files ». Animated sticker set thumbnails can't be uploaded via HTTP URL."""
    request_params = {}
    request_params['name'] = name
    request_params['user_id'] = user_id
    request_params['thumb'] = thumb.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=setStickerSetThumb),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def answerInlineQuery(
        inline_query_id: str,
        results: list[InlineQueryResult],
        cache_time: int = None,
        is_personal: bool = None,
        next_offset: str = None,
        switch_pm_text: str = None,
        switch_pm_parameter: str = None) -> bool:
    """Use this method to send answers to an inline query. On success, True is returned.No more than 50 results per query are allowed.
    :param inline_query_id: Unique identifier for the answered query
    :param results: A JSON-serialized array of results for the inline query
    :param cache_time: The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300.
    :param is_personal: Pass True, if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query
    :param next_offset: Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don't support pagination. Offset length can't exceed 64 bytes.
    :param switch_pm_text: If passed, clients will display a button with specified text that switches the user to a private chat with the bot and sends the bot a start message with the parameter switch_pm_parameter
    :param switch_pm_parameter: Deep-linking parameter for the /start message sent to the bot when user presses the switch button. 1-64 characters, only A-Z, a-z, 0-9, _ and - are allowed.Example: An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube account to adapt search results accordingly. To do this, it displays a 'Connect your YouTube account' button above the results, or even before showing any. The user presses the button, switches to a private chat with the bot and, in doing so, passes a start parameter that instructs the bot to return an OAuth link. Once done, the bot can offer a switch_inline button so that the user can easily return to the chat where they wanted to use the bot's inline capabilities."""
    request_params = {}
    request_params['inline_query_id'] = inline_query_id
    request_params['results'] = [item.json for item in results]
    request_params['cache_time'] = cache_time
    request_params['is_personal'] = is_personal
    request_params['next_offset'] = next_offset
    request_params['switch_pm_text'] = switch_pm_text
    request_params['switch_pm_parameter'] = switch_pm_parameter

    response = requests.get(
        API_URL.format(
            token=token,
            method=answerInlineQuery),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def answerWebAppQuery(
        web_app_query_id: str,
        result: InlineQueryResult) -> SentWebAppMessage:
    """Use this method to set the result of an interaction with a Web App and send a corresponding message on behalf of the user to the chat from which the query originated. On success, a SentWebAppMessage object is returned.
    :param web_app_query_id: Unique identifier for the query to be answered
    :param result: A JSON-serialized object describing the message to be sent"""
    request_params = {}
    request_params['web_app_query_id'] = web_app_query_id
    request_params['result'] = result.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=answerWebAppQuery),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return SentWebAppMessage(result)


def sendInvoice(
        chat_id: int | str,
        title: str,
        description: str,
        payload: str,
        provider_token: str,
        currency: str,
        prices: list[LabeledPrice],
        max_tip_amount: int = None,
        suggested_tip_amounts: list[int] = None,
        start_parameter: str = None,
        provider_data: str = None,
        photo_url: str = None,
        photo_size: int = None,
        photo_width: int = None,
        photo_height: int = None,
        need_name: bool = None,
        need_phone_number: bool = None,
        need_email: bool = None,
        need_shipping_address: bool = None,
        send_phone_number_to_provider: bool = None,
        send_email_to_provider: bool = None,
        is_flexible: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup = None) -> Message:
    """Use this method to send invoices. On success, the sent Message is returned.
    :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    :param title: Product name, 1-32 characters
    :param description: Product description, 1-255 characters
    :param payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
    :param provider_token: Payments provider token, obtained via Botfather
    :param currency: Three-letter ISO 4217 currency code, see more on currencies
    :param prices: Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
    :param max_tip_amount: The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0
    :param suggested_tip_amounts: A JSON-serialized array of suggested amounts of tips in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
    :param start_parameter: Unique deep-linking parameter. If left empty, forwarded copies of the sent message will have a Pay button, allowing multiple users to pay directly from the forwarded message, using the same invoice. If non-empty, forwarded copies of the sent message will have a URL button with a deep link to the bot (instead of a Pay button), with the value used as the start parameter
    :param provider_data: A JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.
    :param photo_url: URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.
    :param photo_size: Photo size
    :param photo_width: Photo width
    :param photo_height: Photo height
    :param need_name: Pass True, if you require the user's full name to complete the order
    :param need_phone_number: Pass True, if you require the user's phone number to complete the order
    :param need_email: Pass True, if you require the user's email address to complete the order
    :param need_shipping_address: Pass True, if you require the user's shipping address to complete the order
    :param send_phone_number_to_provider: Pass True, if user's phone number should be sent to provider
    :param send_email_to_provider: Pass True, if user's email address should be sent to provider
    :param is_flexible: Pass True, if the final price depends on the shipping method
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the sent message from forwarding and saving
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
    :param reply_markup: A JSON-serialized object for an inline keyboard. If empty, one 'Pay total price' button will be shown. If not empty, the first button must be a Pay button."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['title'] = title
    request_params['description'] = description
    request_params['payload'] = payload
    request_params['provider_token'] = provider_token
    request_params['currency'] = currency
    request_params['prices'] = [item.json for item in prices]
    request_params['max_tip_amount'] = max_tip_amount
    request_params['suggested_tip_amounts'] = suggested_tip_amounts
    request_params['start_parameter'] = start_parameter
    request_params['provider_data'] = provider_data
    request_params['photo_url'] = photo_url
    request_params['photo_size'] = photo_size
    request_params['photo_width'] = photo_width
    request_params['photo_height'] = photo_height
    request_params['need_name'] = need_name
    request_params['need_phone_number'] = need_phone_number
    request_params['need_email'] = need_email
    request_params['need_shipping_address'] = need_shipping_address
    request_params['send_phone_number_to_provider'] = send_phone_number_to_provider
    request_params['send_email_to_provider'] = send_email_to_provider
    request_params['is_flexible'] = is_flexible
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=sendInvoice),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def answerShippingQuery(
        shipping_query_id: str,
        ok: bool,
        shipping_options: list[ShippingOption] = None,
        error_message: str = None) -> bool:
    """If you sent an invoice requesting a shipping address and the parameter is_flexible was specified, the Bot API will send an Update with a shipping_query field to the bot. Use this method to reply to shipping queries. On success, True is returned.
    :param shipping_query_id: Unique identifier for the query to be answered
    :param ok: Specify True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible)
    :param shipping_options: Required if ok is True. A JSON-serialized array of available shipping options.
    :param error_message: Required if ok is False. Error message in human readable form that explains why it is impossible to complete the order (e.g. "Sorry, delivery to your desired address is unavailable'). Telegram will display this message to the user."""
    request_params = {}
    request_params['shipping_query_id'] = shipping_query_id
    request_params['ok'] = ok
    request_params['shipping_options'] = [
        item.json for item in shipping_options]
    request_params['error_message'] = error_message

    response = requests.get(
        API_URL.format(
            token=token,
            method=answerShippingQuery),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def answerPreCheckoutQuery(
        pre_checkout_query_id: str,
        ok: bool,
        error_message: str = None) -> bool:
    """Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an Update with the field pre_checkout_query. Use this method to respond to such pre-checkout queries. On success, True is returned. Note: The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.
    :param pre_checkout_query_id: Unique identifier for the query to be answered
    :param ok: Specify True if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use False if there are any problems.
    :param error_message: Required if ok is False. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. "Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!"). Telegram will display this message to the user."""
    request_params = {}
    request_params['pre_checkout_query_id'] = pre_checkout_query_id
    request_params['ok'] = ok
    request_params['error_message'] = error_message

    response = requests.get(
        API_URL.format(
            token=token,
            method=answerPreCheckoutQuery),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def setPassportDataErrors() -> bool:
    """Informs a user that some of the Telegram Passport elements they provided contains errors. The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change). Returns True on success."""
    request_params = None

    response = requests.get(
        API_URL.format(
            token=token,
            method=setPassportDataErrors),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return bool(result)


def sendGame(
        chat_id: int,
        game_short_name: str,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup = None) -> Message:
    """Use this method to send a game. On success, the sent Message is returned.
    :param chat_id: Unique identifier for the target chat
    :param game_short_name: Short name of the game, serves as the unique identifier for the game. Set up your games via Botfather.
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param protect_content: Protects the contents of the sent message from forwarding and saving
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
    :param reply_markup: A JSON-serialized object for an inline keyboard. If empty, one 'Play game_title' button will be shown. If not empty, the first button must launch the game."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['game_short_name'] = game_short_name
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(
        API_URL.format(
            token=token,
            method=sendGame),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def setGameScore(
        user_id: int,
        score: int,
        force: bool = None,
        disable_edit_message: bool = None,
        chat_id: int = None,
        message_id: int = None,
        inline_message_id: str = None) -> Message:
    """Use this method to set the score of the specified user in a game message. On success, if the message is not an inline message, the Message is returned, otherwise True is returned. Returns an error, if the new score is not greater than the user's current score in the chat and force is False.
    :param user_id: User identifier
    :param score: New score, must be non-negative
    :param force: Pass True, if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters
    :param disable_edit_message: Pass True, if the game message should not be automatically edited to include the current scoreboard
    :param chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat
    :param message_id: Required if inline_message_id is not specified. Identifier of the sent message
    :param inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message"""
    request_params = {}
    request_params['user_id'] = user_id
    request_params['score'] = score
    request_params['force'] = force
    request_params['disable_edit_message'] = disable_edit_message
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id
    request_params['inline_message_id'] = inline_message_id

    response = requests.get(
        API_URL.format(
            token=token,
            method=setGameScore),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return Message(result)


def getGameHighScores() -> list[GameHighScore]:
    """Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. On success, returns an Array of GameHighScore objects."""
    request_params = None

    response = requests.get(
        API_URL.format(
            token=token,
            method=getGameHighScores),
        params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException(
            'Error {errno}: {error}'.format(
                errno=response['error_code'],
                error=response['description']))
    result = response['result']

    return [GameHighScore(item) for item in result]
