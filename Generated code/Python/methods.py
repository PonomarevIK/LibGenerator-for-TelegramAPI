import requests
from types import *

API_URL = 'https://api.telegram.org/bot{token}/{method}'
token = 'your_bot_token_here'


def getUpdates(
        offset: int = None,
        limit: int = None,
        timeout: int = None,
        allowed_updates: list[str] = None) -> list[Update]:
    """Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned."""
    payload = {}
    if offset is not None:
        payload['offset'] = offset
    if limit is not None:
        payload['limit'] = limit
    if timeout is not None:
        payload['timeout'] = timeout
    if allowed_updates is not None:
        payload['allowed_updates'] = allowed_updates

    result = requests.get(
        API_URL.format(
            token=token,
            method=getUpdates),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def setWebhook() -> bool:
    """Use this method to specify a url and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified url, containing a JSON-serialized Update. In case of an unsuccessful request, we will give up after a reasonable amount of attempts. Returns True on success."""
    payload = {}

    result = requests.get(
        API_URL.format(
            token=token,
            method=setWebhook),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def deleteWebhook(drop_pending_updates: bool = None) -> bool:
    """Use this method to remove webhook integration if you decide to switch back to getUpdates. Returns True on success."""
    payload = {}
    if drop_pending_updates is not None:
        payload['drop_pending_updates'] = drop_pending_updates

    result = requests.get(
        API_URL.format(
            token=token,
            method=deleteWebhook),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def getWebhookInfo() -> WebhookInfo:
    """Use this method to get current webhook status. Requires no parameters. On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty."""
    payload = {}

    result = requests.get(
        API_URL.format(
            token=token,
            method=getWebhookInfo),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def getMe() -> User:
    """A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a User object."""
    payload = {}

    result = requests.get(
        API_URL.format(
            token=token,
            method=getMe),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def logOut() -> bool:
    """Use this method to log out from the cloud Bot API server before launching the bot locally. You must log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns True on success. Requires no parameters."""
    payload = {}

    result = requests.get(
        API_URL.format(
            token=token,
            method=logOut),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def close() -> bool:
    """Use this method to close the bot instance before moving it from one local server to another. You need to delete the webhook before calling this method to ensure that the bot isn't launched again after server restart. The method will return error 429 in the first 10 minutes after the bot is launched. Returns True on success. Requires no parameters."""
    payload = {}

    result = requests.get(
        API_URL.format(
            token=token,
            method=close),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


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
    """Use this method to send text messages. On success, the sent Message is returned."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['text'] = text
    if parse_mode is not None:
        payload['parse_mode'] = parse_mode
    if entities is not None:
        payload['entities'] = entities
    if disable_web_page_preview is not None:
        payload['disable_web_page_preview'] = disable_web_page_preview
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if protect_content is not None:
        payload['protect_content'] = protect_content
    if reply_to_message_id is not None:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=sendMessage),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def forwardMessage(
        chat_id: int | str,
        from_chat_id: int | str,
        message_id: int,
        disable_notification: bool = None,
        protect_content: bool = None) -> Message:
    """Use this method to forward messages of any kind. Service messages can't be forwarded. On success, the sent Message is returned."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['from_chat_id'] = from_chat_id
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if protect_content is not None:
        payload['protect_content'] = protect_content
    payload['message_id'] = message_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=forwardMessage),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


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
    """Use this method to copy messages of any kind. Service messages and invoice messages can't be copied. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['from_chat_id'] = from_chat_id
    payload['message_id'] = message_id
    if caption is not None:
        payload['caption'] = caption
    if parse_mode is not None:
        payload['parse_mode'] = parse_mode
    if caption_entities is not None:
        payload['caption_entities'] = caption_entities
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if protect_content is not None:
        payload['protect_content'] = protect_content
    if reply_to_message_id is not None:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=copyMessage),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


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
    """Use this method to send photos. On success, the sent Message is returned."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['photo'] = photo
    if caption is not None:
        payload['caption'] = caption
    if parse_mode is not None:
        payload['parse_mode'] = parse_mode
    if caption_entities is not None:
        payload['caption_entities'] = caption_entities
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if protect_content is not None:
        payload['protect_content'] = protect_content
    if reply_to_message_id is not None:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=sendPhoto),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def sendAudio() -> Message:
    """Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future."""
    payload = {}

    result = requests.get(
        API_URL.format(
            token=token,
            method=sendAudio),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


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
    """Use this method to send general files. On success, the sent Message is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['document'] = document
    if thumb is not None:
        payload['thumb'] = thumb
    if caption is not None:
        payload['caption'] = caption
    if parse_mode is not None:
        payload['parse_mode'] = parse_mode
    if caption_entities is not None:
        payload['caption_entities'] = caption_entities
    if disable_content_type_detection is not None:
        payload['disable_content_type_detection'] = disable_content_type_detection
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if protect_content is not None:
        payload['protect_content'] = protect_content
    if reply_to_message_id is not None:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=sendDocument),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


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
    """Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['video'] = video
    if duration is not None:
        payload['duration'] = duration
    if width is not None:
        payload['width'] = width
    if height is not None:
        payload['height'] = height
    if thumb is not None:
        payload['thumb'] = thumb
    if caption is not None:
        payload['caption'] = caption
    if parse_mode is not None:
        payload['parse_mode'] = parse_mode
    if caption_entities is not None:
        payload['caption_entities'] = caption_entities
    if supports_streaming is not None:
        payload['supports_streaming'] = supports_streaming
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if protect_content is not None:
        payload['protect_content'] = protect_content
    if reply_to_message_id is not None:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=sendVideo),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


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
    """Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent Message is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['animation'] = animation
    if duration is not None:
        payload['duration'] = duration
    if width is not None:
        payload['width'] = width
    if height is not None:
        payload['height'] = height
    if thumb is not None:
        payload['thumb'] = thumb
    if caption is not None:
        payload['caption'] = caption
    if parse_mode is not None:
        payload['parse_mode'] = parse_mode
    if caption_entities is not None:
        payload['caption_entities'] = caption_entities
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if protect_content is not None:
        payload['protect_content'] = protect_content
    if reply_to_message_id is not None:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=sendAnimation),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


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
    """Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['voice'] = voice
    if caption is not None:
        payload['caption'] = caption
    if parse_mode is not None:
        payload['parse_mode'] = parse_mode
    if caption_entities is not None:
        payload['caption_entities'] = caption_entities
    if duration is not None:
        payload['duration'] = duration
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if protect_content is not None:
        payload['protect_content'] = protect_content
    if reply_to_message_id is not None:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=sendVoice),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


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
    """As of v.4.0, Telegram clients support rounded square mp4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent Message is returned."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['video_note'] = video_note
    if duration is not None:
        payload['duration'] = duration
    if length is not None:
        payload['length'] = length
    if thumb is not None:
        payload['thumb'] = thumb
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if protect_content is not None:
        payload['protect_content'] = protect_content
    if reply_to_message_id is not None:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=sendVideoNote),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def sendMediaGroup(chat_id: int | str,
                   media: list[InputMediaAudio | InputMediaDocument | InputMediaPhoto | InputMediaVideo],
                   disable_notification: bool = None,
                   protect_content: bool = None,
                   reply_to_message_id: int = None,
                   allow_sending_without_reply: bool = None) -> list[Message]:
    """Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an array of Messages that were sent is returned."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['media'] = media
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if protect_content is not None:
        payload['protect_content'] = protect_content
    if reply_to_message_id is not None:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply

    result = requests.get(
        API_URL.format(
            token=token,
            method=sendMediaGroup),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


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
    """Use this method to send point on the map. On success, the sent Message is returned."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['latitude'] = latitude
    payload['longitude'] = longitude
    if horizontal_accuracy is not None:
        payload['horizontal_accuracy'] = horizontal_accuracy
    if live_period is not None:
        payload['live_period'] = live_period
    if heading is not None:
        payload['heading'] = heading
    if proximity_alert_radius is not None:
        payload['proximity_alert_radius'] = proximity_alert_radius
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if protect_content is not None:
        payload['protect_content'] = protect_content
    if reply_to_message_id is not None:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=sendLocation),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def editMessageLiveLocation(
        latitude: float,
        longitude: float,
        chat_id: int | str = None,
        message_id: int = None,
        inline_message_id: str = None,
        horizontal_accuracy: float = None,
        heading: int = None,
        proximity_alert_radius: int = None,
        reply_markup: InlineKeyboardMarkup = None) -> Message | bool:
    """Use this method to edit live location messages. A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""
    payload = {}
    if chat_id is not None:
        payload['chat_id'] = chat_id
    if message_id is not None:
        payload['message_id'] = message_id
    if inline_message_id is not None:
        payload['inline_message_id'] = inline_message_id
    payload['latitude'] = latitude
    payload['longitude'] = longitude
    if horizontal_accuracy is not None:
        payload['horizontal_accuracy'] = horizontal_accuracy
    if heading is not None:
        payload['heading'] = heading
    if proximity_alert_radius is not None:
        payload['proximity_alert_radius'] = proximity_alert_radius
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=editMessageLiveLocation),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def stopMessageLiveLocation(
        chat_id: int | str = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None) -> Message | bool:
    """Use this method to stop updating a live location message before live_period expires. On success, if the message is not an inline message, the edited Message is returned, otherwise True is returned."""
    payload = {}
    if chat_id is not None:
        payload['chat_id'] = chat_id
    if message_id is not None:
        payload['message_id'] = message_id
    if inline_message_id is not None:
        payload['inline_message_id'] = inline_message_id
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=stopMessageLiveLocation),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


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
    """Use this method to send information about a venue. On success, the sent Message is returned."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['latitude'] = latitude
    payload['longitude'] = longitude
    payload['title'] = title
    payload['address'] = address
    if foursquare_id is not None:
        payload['foursquare_id'] = foursquare_id
    if foursquare_type is not None:
        payload['foursquare_type'] = foursquare_type
    if google_place_id is not None:
        payload['google_place_id'] = google_place_id
    if google_place_type is not None:
        payload['google_place_type'] = google_place_type
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if protect_content is not None:
        payload['protect_content'] = protect_content
    if reply_to_message_id is not None:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=sendVenue),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


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
    """Use this method to send phone contacts. On success, the sent Message is returned."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['phone_number'] = phone_number
    payload['first_name'] = first_name
    if last_name is not None:
        payload['last_name'] = last_name
    if vcard is not None:
        payload['vcard'] = vcard
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if protect_content is not None:
        payload['protect_content'] = protect_content
    if reply_to_message_id is not None:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=sendContact),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


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
    """Use this method to send a native poll. On success, the sent Message is returned."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['question'] = question
    payload['options'] = options
    if is_anonymous is not None:
        payload['is_anonymous'] = is_anonymous
    if type is not None:
        payload['type'] = type
    if allows_multiple_answers is not None:
        payload['allows_multiple_answers'] = allows_multiple_answers
    if correct_option_id is not None:
        payload['correct_option_id'] = correct_option_id
    if explanation is not None:
        payload['explanation'] = explanation
    if explanation_parse_mode is not None:
        payload['explanation_parse_mode'] = explanation_parse_mode
    if explanation_entities is not None:
        payload['explanation_entities'] = explanation_entities
    if open_period is not None:
        payload['open_period'] = open_period
    if close_date is not None:
        payload['close_date'] = close_date
    if is_closed is not None:
        payload['is_closed'] = is_closed
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if protect_content is not None:
        payload['protect_content'] = protect_content
    if reply_to_message_id is not None:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=sendPoll),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def sendDice(
        chat_id: int | str,
        emoji: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send an animated emoji that will display a random value. On success, the sent Message is returned."""
    payload = {}
    payload['chat_id'] = chat_id
    if emoji is not None:
        payload['emoji'] = emoji
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if protect_content is not None:
        payload['protect_content'] = protect_content
    if reply_to_message_id is not None:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=sendDice),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def sendChatAction() -> bool:
    """Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns True on success."""
    payload = {}

    result = requests.get(
        API_URL.format(
            token=token,
            method=sendChatAction),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def getUserProfilePhotos(
        user_id: int,
        offset: int = None,
        limit: int = None) -> UserProfilePhotos:
    """Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object."""
    payload = {}
    payload['user_id'] = user_id
    if offset is not None:
        payload['offset'] = offset
    if limit is not None:
        payload['limit'] = limit

    result = requests.get(
        API_URL.format(
            token=token,
            method=getUserProfilePhotos),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def getFile(file_id: str) -> File:
    """Use this method to get basic info about a file and prepare it for downloading. For the moment, bots can download files of up to 20MB in size. On success, a File object is returned. The file can then be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>, where <file_path> is taken from the response. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile again."""
    payload = {}
    payload['file_id'] = file_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=getFile),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def banChatMember(
        chat_id: int | str,
        user_id: int,
        until_date: int = None,
        revoke_messages: bool = None) -> bool:
    """Use this method to ban a user in a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless unbanned first. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['user_id'] = user_id
    if until_date is not None:
        payload['until_date'] = until_date
    if revoke_messages is not None:
        payload['revoke_messages'] = revoke_messages

    result = requests.get(
        API_URL.format(
            token=token,
            method=banChatMember),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def unbanChatMember(
        chat_id: int | str,
        user_id: int,
        only_if_banned: bool = None) -> bool:
    """Use this method to unban a previously banned user in a supergroup or channel. The user will not return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be removed from the chat. If you don't want this, use the parameter only_if_banned. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['user_id'] = user_id
    if only_if_banned is not None:
        payload['only_if_banned'] = only_if_banned

    result = requests.get(
        API_URL.format(
            token=token,
            method=unbanChatMember),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def restrictChatMember(
        chat_id: int | str,
        user_id: int,
        permissions: ChatPermissions,
        until_date: int = None) -> bool:
    """Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass True for all permissions to lift restrictions from a user. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['user_id'] = user_id
    payload['permissions'] = permissions
    if until_date is not None:
        payload['until_date'] = until_date

    result = requests.get(
        API_URL.format(
            token=token,
            method=restrictChatMember),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


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
    """Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass False for all boolean parameters to demote a user. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['user_id'] = user_id
    if is_anonymous is not None:
        payload['is_anonymous'] = is_anonymous
    if can_manage_chat is not None:
        payload['can_manage_chat'] = can_manage_chat
    if can_post_messages is not None:
        payload['can_post_messages'] = can_post_messages
    if can_edit_messages is not None:
        payload['can_edit_messages'] = can_edit_messages
    if can_delete_messages is not None:
        payload['can_delete_messages'] = can_delete_messages
    if can_manage_video_chats is not None:
        payload['can_manage_video_chats'] = can_manage_video_chats
    if can_restrict_members is not None:
        payload['can_restrict_members'] = can_restrict_members
    if can_promote_members is not None:
        payload['can_promote_members'] = can_promote_members
    if can_change_info is not None:
        payload['can_change_info'] = can_change_info
    if can_invite_users is not None:
        payload['can_invite_users'] = can_invite_users
    if can_pin_messages is not None:
        payload['can_pin_messages'] = can_pin_messages

    result = requests.get(
        API_URL.format(
            token=token,
            method=promoteChatMember),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def setChatAdministratorCustomTitle(
        chat_id: int | str,
        user_id: int,
        custom_title: str) -> bool:
    """Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['user_id'] = user_id
    payload['custom_title'] = custom_title

    result = requests.get(
        API_URL.format(
            token=token,
            method=setChatAdministratorCustomTitle),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def banChatSenderChat(chat_id: int | str, sender_chat_id: int) -> bool:
    """Use this method to ban a channel chat in a supergroup or a channel. Until the chat is unbanned, the owner of the banned chat won't be able to send messages on behalf of any of their channels. The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['sender_chat_id'] = sender_chat_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=banChatSenderChat),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def unbanChatSenderChat(chat_id: int | str, sender_chat_id: int) -> bool:
    """Use this method to unban a previously banned channel chat in a supergroup or channel. The bot must be an administrator for this to work and must have the appropriate administrator rights. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['sender_chat_id'] = sender_chat_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=unbanChatSenderChat),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def setChatPermissions(
        chat_id: int | str,
        permissions: ChatPermissions) -> bool:
    """Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the can_restrict_members administrator rights. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['permissions'] = permissions

    result = requests.get(
        API_URL.format(
            token=token,
            method=setChatPermissions),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def exportChatInviteLink(chat_id: int | str) -> str:
    """Use this method to generate a new primary invite link for a chat; any previously generated primary link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the new invite link as String on success."""
    payload = {}
    payload['chat_id'] = chat_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=exportChatInviteLink),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def createChatInviteLink(
        chat_id: int | str,
        name: str = None,
        expire_date: int = None,
        member_limit: int = None,
        creates_join_request: bool = None) -> ChatInviteLink:
    """Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. The link can be revoked using the method revokeChatInviteLink. Returns the new invite link as ChatInviteLink object."""
    payload = {}
    payload['chat_id'] = chat_id
    if name is not None:
        payload['name'] = name
    if expire_date is not None:
        payload['expire_date'] = expire_date
    if member_limit is not None:
        payload['member_limit'] = member_limit
    if creates_join_request is not None:
        payload['creates_join_request'] = creates_join_request

    result = requests.get(
        API_URL.format(
            token=token,
            method=createChatInviteLink),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def editChatInviteLink(
        chat_id: int | str,
        invite_link: str,
        name: str = None,
        expire_date: int = None,
        member_limit: int = None,
        creates_join_request: bool = None) -> ChatInviteLink:
    """Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a ChatInviteLink object."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['invite_link'] = invite_link
    if name is not None:
        payload['name'] = name
    if expire_date is not None:
        payload['expire_date'] = expire_date
    if member_limit is not None:
        payload['member_limit'] = member_limit
    if creates_join_request is not None:
        payload['creates_join_request'] = creates_join_request

    result = requests.get(
        API_URL.format(
            token=token,
            method=editChatInviteLink),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def revokeChatInviteLink(
        chat_id: int | str,
        invite_link: str) -> ChatInviteLink:
    """Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the revoked invite link as ChatInviteLink object."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['invite_link'] = invite_link

    result = requests.get(
        API_URL.format(
            token=token,
            method=revokeChatInviteLink),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def approveChatJoinRequest(chat_id: int | str, user_id: int) -> bool:
    """Use this method to approve a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['user_id'] = user_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=approveChatJoinRequest),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def declineChatJoinRequest(chat_id: int | str, user_id: int) -> bool:
    """Use this method to decline a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['user_id'] = user_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=declineChatJoinRequest),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def setChatPhoto(chat_id: int | str, photo: InputFile) -> bool:
    """Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['photo'] = photo

    result = requests.get(
        API_URL.format(
            token=token,
            method=setChatPhoto),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def deleteChatPhoto(chat_id: int | str) -> bool:
    """Use this method to delete a chat photo. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=deleteChatPhoto),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def setChatTitle(chat_id: int | str, title: str) -> bool:
    """Use this method to change the title of a chat. Titles can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['title'] = title

    result = requests.get(
        API_URL.format(
            token=token,
            method=setChatTitle),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def setChatDescription(chat_id: int | str, description: str = None) -> bool:
    """Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id
    if description is not None:
        payload['description'] = description

    result = requests.get(
        API_URL.format(
            token=token,
            method=setChatDescription),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def pinChatMessage(
        chat_id: int | str,
        message_id: int,
        disable_notification: bool = None) -> bool:
    """Use this method to add a message to the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['message_id'] = message_id
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification

    result = requests.get(
        API_URL.format(
            token=token,
            method=pinChatMessage),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def unpinChatMessage(chat_id: int | str, message_id: int = None) -> bool:
    """Use this method to remove a message from the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id
    if message_id is not None:
        payload['message_id'] = message_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=unpinChatMessage),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def unpinAllChatMessages(chat_id: int | str) -> bool:
    """Use this method to clear the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=unpinAllChatMessages),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def leaveChat(chat_id: int | str) -> bool:
    """Use this method for your bot to leave a group, supergroup or channel. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=leaveChat),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def getChat(chat_id: int | str) -> Chat:
    """Use this method to get up to date information about the chat (current name of the user for one-on-one conversations, current username of a user, group or channel, etc.). Returns a Chat object on success."""
    payload = {}
    payload['chat_id'] = chat_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=getChat),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def getChatAdministrators(chat_id: int | str) -> list[ChatMember]:
    """Use this method to get a list of administrators in a chat. On success, returns an Array of ChatMember objects that contains information about all chat administrators except other bots. If the chat is a group or a supergroup and no administrators were appointed, only the creator will be returned."""
    payload = {}
    payload['chat_id'] = chat_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=getChatAdministrators),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def getChatMemberCount(chat_id: int | str) -> int:
    """Use this method to get the number of members in a chat. Returns Int on success."""
    payload = {}
    payload['chat_id'] = chat_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=getChatMemberCount),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def getChatMember(chat_id: int | str, user_id: int) -> ChatMember:
    """Use this method to get information about a member of a chat. Returns a ChatMember object on success."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['user_id'] = user_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=getChatMember),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def setChatStickerSet(chat_id: int | str, sticker_set_name: str) -> bool:
    """Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['sticker_set_name'] = sticker_set_name

    result = requests.get(
        API_URL.format(
            token=token,
            method=setChatStickerSet),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def deleteChatStickerSet(chat_id: int | str) -> bool:
    """Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=deleteChatStickerSet),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def answerCallbackQuery() -> bool:
    """Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned."""
    payload = {}

    result = requests.get(
        API_URL.format(
            token=token,
            method=answerCallbackQuery),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def setMyCommands(
        commands: list[BotCommand],
        scope: BotCommandScope = None,
        language_code: str = None) -> bool:
    """Use this method to change the list of the bot's commands. See https://core.telegram.org/bots#commands for more details about bot commands. Returns True on success."""
    payload = {}
    payload['commands'] = commands
    if scope is not None:
        payload['scope'] = scope
    if language_code is not None:
        payload['language_code'] = language_code

    result = requests.get(
        API_URL.format(
            token=token,
            method=setMyCommands),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def deleteMyCommands(
        scope: BotCommandScope = None,
        language_code: str = None) -> bool:
    """Use this method to delete the list of the bot's commands for the given scope and user language. After deletion, higher level commands will be shown to affected users. Returns True on success."""
    payload = {}
    if scope is not None:
        payload['scope'] = scope
    if language_code is not None:
        payload['language_code'] = language_code

    result = requests.get(
        API_URL.format(
            token=token,
            method=deleteMyCommands),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def getMyCommands(scope: BotCommandScope = None,
                  language_code: str = None) -> list[BotCommand]:
    """Use this method to get the current list of the bot's commands for the given scope and user language. Returns Array of BotCommand on success. If commands aren't set, an empty list is returned."""
    payload = {}
    if scope is not None:
        payload['scope'] = scope
    if language_code is not None:
        payload['language_code'] = language_code

    result = requests.get(
        API_URL.format(
            token=token,
            method=getMyCommands),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def setChatMenuButton(
        chat_id: int = None,
        menu_button: MenuButton = None) -> bool:
    """Use this method to change the bot's menu button in a private chat, or the default menu button. Returns True on success."""
    payload = {}
    if chat_id is not None:
        payload['chat_id'] = chat_id
    if menu_button is not None:
        payload['menu_button'] = menu_button

    result = requests.get(
        API_URL.format(
            token=token,
            method=setChatMenuButton),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def getChatMenuButton(chat_id: int = None) -> MenuButton:
    """Use this method to get the current value of the bot's menu button in a private chat, or the default menu button. Returns MenuButton on success."""
    payload = {}
    if chat_id is not None:
        payload['chat_id'] = chat_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=getChatMenuButton),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def setMyDefaultAdministratorRights(
        rights: ChatAdministratorRights = None,
        for_channels: bool = None) -> bool:
    """Use this method to change the default administrator rights requested by the bot when it's added as an administrator to groups or channels. These rights will be suggested to users, but they are are free to modify the list before adding the bot. Returns True on success."""
    payload = {}
    if rights is not None:
        payload['rights'] = rights
    if for_channels is not None:
        payload['for_channels'] = for_channels

    result = requests.get(
        API_URL.format(
            token=token,
            method=setMyDefaultAdministratorRights),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def getMyDefaultAdministratorRights(
        for_channels: bool = None) -> ChatAdministratorRights:
    """Use this method to get the current default administrator rights of the bot. Returns ChatAdministratorRights on success."""
    payload = {}
    if for_channels is not None:
        payload['for_channels'] = for_channels

    result = requests.get(
        API_URL.format(
            token=token,
            method=getMyDefaultAdministratorRights),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def editMessageText(
        text: str,
        chat_id: int | str = None,
        message_id: int = None,
        inline_message_id: str = None,
        parse_mode: str = None,
        entities: list[MessageEntity] = None,
        disable_web_page_preview: bool = None,
        reply_markup: InlineKeyboardMarkup = None) -> Message | bool:
    """Use this method to edit text and game messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""
    payload = {}
    if chat_id is not None:
        payload['chat_id'] = chat_id
    if message_id is not None:
        payload['message_id'] = message_id
    if inline_message_id is not None:
        payload['inline_message_id'] = inline_message_id
    payload['text'] = text
    if parse_mode is not None:
        payload['parse_mode'] = parse_mode
    if entities is not None:
        payload['entities'] = entities
    if disable_web_page_preview is not None:
        payload['disable_web_page_preview'] = disable_web_page_preview
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=editMessageText),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def editMessageCaption(
        chat_id: int | str = None,
        message_id: int = None,
        inline_message_id: str = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: list[MessageEntity] = None,
        reply_markup: InlineKeyboardMarkup = None) -> Message | bool:
    """Use this method to edit captions of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""
    payload = {}
    if chat_id is not None:
        payload['chat_id'] = chat_id
    if message_id is not None:
        payload['message_id'] = message_id
    if inline_message_id is not None:
        payload['inline_message_id'] = inline_message_id
    if caption is not None:
        payload['caption'] = caption
    if parse_mode is not None:
        payload['parse_mode'] = parse_mode
    if caption_entities is not None:
        payload['caption_entities'] = caption_entities
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=editMessageCaption),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def editMessageMedia(
        media: InputMedia,
        chat_id: int | str = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None) -> Message | bool:
    """Use this method to edit animation, audio, document, photo, or video messages. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo or a video otherwise. When an inline message is edited, a new file can't be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""
    payload = {}
    if chat_id is not None:
        payload['chat_id'] = chat_id
    if message_id is not None:
        payload['message_id'] = message_id
    if inline_message_id is not None:
        payload['inline_message_id'] = inline_message_id
    payload['media'] = media
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=editMessageMedia),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def editMessageReplyMarkup(
        chat_id: int | str = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None) -> Message | bool:
    """Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""
    payload = {}
    if chat_id is not None:
        payload['chat_id'] = chat_id
    if message_id is not None:
        payload['message_id'] = message_id
    if inline_message_id is not None:
        payload['inline_message_id'] = inline_message_id
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=editMessageReplyMarkup),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def stopPoll(chat_id: int | str, message_id: int,
             reply_markup: InlineKeyboardMarkup = None) -> Poll:
    """Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['message_id'] = message_id
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=stopPoll),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def deleteMessage(chat_id: int | str, message_id: int) -> bool:
    """Use this method to delete a message, including service messages, with the following limitations:
          - A message can only be deleted if it was sent less than 48 hours ago.
          - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.
          - Bots can delete outgoing messages in private chats, groups, and supergroups.
          - Bots can delete incoming messages in private chats.
          - Bots granted can_post_messages permissions can delete outgoing messages in channels.
          - If the bot is an administrator of a group, it can delete any message there.
          - If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.
          Returns True on success."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['message_id'] = message_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=deleteMessage),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def sendSticker(
        chat_id: int | str,
        sticker: InputFile | str,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers. On success, the sent Message is returned."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['sticker'] = sticker
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if protect_content is not None:
        payload['protect_content'] = protect_content
    if reply_to_message_id is not None:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=sendSticker),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def getStickerSet(name: str) -> StickerSet:
    """Use this method to get a sticker set. On success, a StickerSet object is returned."""
    payload = {}
    payload['name'] = name

    result = requests.get(
        API_URL.format(
            token=token,
            method=getStickerSet),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def uploadStickerFile(user_id: int, png_sticker: InputFile) -> File:
    """Use this method to upload a .PNG file with a sticker for later use in createNewStickerSet and addStickerToSet methods (can be used multiple times). Returns the uploaded File on success."""
    payload = {}
    payload['user_id'] = user_id
    payload['png_sticker'] = png_sticker

    result = requests.get(
        API_URL.format(
            token=token,
            method=uploadStickerFile),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


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
    """Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. You must use exactly one of the fields png_sticker, tgs_sticker, or webm_sticker. Returns True on success."""
    payload = {}
    payload['user_id'] = user_id
    payload['name'] = name
    payload['title'] = title
    if png_sticker is not None:
        payload['png_sticker'] = png_sticker
    if tgs_sticker is not None:
        payload['tgs_sticker'] = tgs_sticker
    if webm_sticker is not None:
        payload['webm_sticker'] = webm_sticker
    payload['emojis'] = emojis
    if contains_masks is not None:
        payload['contains_masks'] = contains_masks
    if mask_position is not None:
        payload['mask_position'] = mask_position

    result = requests.get(
        API_URL.format(
            token=token,
            method=createNewStickerSet),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def addStickerToSet(
        user_id: int,
        name: str,
        emojis: str,
        png_sticker: InputFile | str = None,
        tgs_sticker: InputFile = None,
        webm_sticker: InputFile = None,
        mask_position: MaskPosition = None) -> bool:
    """Use this method to add a new sticker to a set created by the bot. You must use exactly one of the fields png_sticker, tgs_sticker, or webm_sticker. Animated stickers can be added to animated sticker sets and only to them. Animated sticker sets can have up to 50 stickers. Static sticker sets can have up to 120 stickers. Returns True on success."""
    payload = {}
    payload['user_id'] = user_id
    payload['name'] = name
    if png_sticker is not None:
        payload['png_sticker'] = png_sticker
    if tgs_sticker is not None:
        payload['tgs_sticker'] = tgs_sticker
    if webm_sticker is not None:
        payload['webm_sticker'] = webm_sticker
    payload['emojis'] = emojis
    if mask_position is not None:
        payload['mask_position'] = mask_position

    result = requests.get(
        API_URL.format(
            token=token,
            method=addStickerToSet),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def setStickerPositionInSet(sticker: str, position: int) -> bool:
    """Use this method to move a sticker in a set created by the bot to a specific position. Returns True on success."""
    payload = {}
    payload['sticker'] = sticker
    payload['position'] = position

    result = requests.get(
        API_URL.format(
            token=token,
            method=setStickerPositionInSet),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def deleteStickerFromSet(sticker: str) -> bool:
    """Use this method to delete a sticker from a set created by the bot. Returns True on success."""
    payload = {}
    payload['sticker'] = sticker

    result = requests.get(
        API_URL.format(
            token=token,
            method=deleteStickerFromSet),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def setStickerSetThumb(
        name: str,
        user_id: int,
        thumb: InputFile | str = None) -> bool:
    """Use this method to set the thumbnail of a sticker set. Animated thumbnails can be set for animated sticker sets only. Video thumbnails can be set only for video sticker sets only. Returns True on success."""
    payload = {}
    payload['name'] = name
    payload['user_id'] = user_id
    if thumb is not None:
        payload['thumb'] = thumb

    result = requests.get(
        API_URL.format(
            token=token,
            method=setStickerSetThumb),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def answerInlineQuery(
        inline_query_id: str,
        results: list[InlineQueryResult],
        cache_time: int = None,
        is_personal: bool = None,
        next_offset: str = None,
        switch_pm_text: str = None,
        switch_pm_parameter: str = None) -> bool:
    """Use this method to send answers to an inline query. On success, True is returned.
          No more than 50 results per query are allowed."""
    payload = {}
    payload['inline_query_id'] = inline_query_id
    payload['results'] = results
    if cache_time is not None:
        payload['cache_time'] = cache_time
    if is_personal is not None:
        payload['is_personal'] = is_personal
    if next_offset is not None:
        payload['next_offset'] = next_offset
    if switch_pm_text is not None:
        payload['switch_pm_text'] = switch_pm_text
    if switch_pm_parameter is not None:
        payload['switch_pm_parameter'] = switch_pm_parameter

    result = requests.get(
        API_URL.format(
            token=token,
            method=answerInlineQuery),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def answerWebAppQuery(
        web_app_query_id: str,
        result: InlineQueryResult) -> SentWebAppMessage:
    """Use this method to set the result of an interaction with a Web App and send a corresponding message on behalf of the user to the chat from which the query originated. On success, a SentWebAppMessage object is returned."""
    payload = {}
    payload['web_app_query_id'] = web_app_query_id
    payload['result'] = result

    result = requests.get(
        API_URL.format(
            token=token,
            method=answerWebAppQuery),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


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
    """Use this method to send invoices. On success, the sent Message is returned."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['title'] = title
    payload['description'] = description
    payload['payload'] = payload
    payload['provider_token'] = provider_token
    payload['currency'] = currency
    payload['prices'] = prices
    if max_tip_amount is not None:
        payload['max_tip_amount'] = max_tip_amount
    if suggested_tip_amounts is not None:
        payload['suggested_tip_amounts'] = suggested_tip_amounts
    if start_parameter is not None:
        payload['start_parameter'] = start_parameter
    if provider_data is not None:
        payload['provider_data'] = provider_data
    if photo_url is not None:
        payload['photo_url'] = photo_url
    if photo_size is not None:
        payload['photo_size'] = photo_size
    if photo_width is not None:
        payload['photo_width'] = photo_width
    if photo_height is not None:
        payload['photo_height'] = photo_height
    if need_name is not None:
        payload['need_name'] = need_name
    if need_phone_number is not None:
        payload['need_phone_number'] = need_phone_number
    if need_email is not None:
        payload['need_email'] = need_email
    if need_shipping_address is not None:
        payload['need_shipping_address'] = need_shipping_address
    if send_phone_number_to_provider is not None:
        payload['send_phone_number_to_provider'] = send_phone_number_to_provider
    if send_email_to_provider is not None:
        payload['send_email_to_provider'] = send_email_to_provider
    if is_flexible is not None:
        payload['is_flexible'] = is_flexible
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if protect_content is not None:
        payload['protect_content'] = protect_content
    if reply_to_message_id is not None:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=sendInvoice),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def answerShippingQuery(
        shipping_query_id: str,
        ok: bool,
        shipping_options: list[ShippingOption] = None,
        error_message: str = None) -> bool:
    """If you sent an invoice requesting a shipping address and the parameter is_flexible was specified, the Bot API will send an Update with a shipping_query field to the bot. Use this method to reply to shipping queries. On success, True is returned."""
    payload = {}
    payload['shipping_query_id'] = shipping_query_id
    payload['ok'] = ok
    if shipping_options is not None:
        payload['shipping_options'] = shipping_options
    if error_message is not None:
        payload['error_message'] = error_message

    result = requests.get(
        API_URL.format(
            token=token,
            method=answerShippingQuery),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def answerPreCheckoutQuery(
        pre_checkout_query_id: str,
        ok: bool,
        error_message: str = None) -> bool:
    """Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an Update with the field pre_checkout_query. Use this method to respond to such pre-checkout queries. On success, True is returned. Note: The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent."""
    payload = {}
    payload['pre_checkout_query_id'] = pre_checkout_query_id
    payload['ok'] = ok
    if error_message is not None:
        payload['error_message'] = error_message

    result = requests.get(
        API_URL.format(
            token=token,
            method=answerPreCheckoutQuery),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def setPassportDataErrors() -> bool:
    """Informs a user that some of the Telegram Passport elements they provided contains errors. The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change). Returns True on success."""
    payload = {}

    result = requests.get(
        API_URL.format(
            token=token,
            method=setPassportDataErrors),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def sendGame(
        chat_id: int,
        game_short_name: str,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup = None) -> Message:
    """Use this method to send a game. On success, the sent Message is returned."""
    payload = {}
    payload['chat_id'] = chat_id
    payload['game_short_name'] = game_short_name
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if protect_content is not None:
        payload['protect_content'] = protect_content
    if reply_to_message_id is not None:
        payload['reply_to_message_id'] = reply_to_message_id
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup

    result = requests.get(
        API_URL.format(
            token=token,
            method=sendGame),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def setGameScore(
        user_id: int,
        score: int,
        force: bool = None,
        disable_edit_message: bool = None,
        chat_id: int = None,
        message_id: int = None,
        inline_message_id: str = None) -> Message | bool:
    """Use this method to set the score of the specified user in a game message. On success, if the message is not an inline message, the Message is returned, otherwise True is returned. Returns an error, if the new score is not greater than the user's current score in the chat and force is False."""
    payload = {}
    payload['user_id'] = user_id
    payload['score'] = score
    if force is not None:
        payload['force'] = force
    if disable_edit_message is not None:
        payload['disable_edit_message'] = disable_edit_message
    if chat_id is not None:
        payload['chat_id'] = chat_id
    if message_id is not None:
        payload['message_id'] = message_id
    if inline_message_id is not None:
        payload['inline_message_id'] = inline_message_id

    result = requests.get(
        API_URL.format(
            token=token,
            method=setGameScore),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result


def getGameHighScores() -> list[GameHighScore]:
    """Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. On success, returns an Array of GameHighScore objects."""
    payload = {}

    result = requests.get(
        API_URL.format(
            token=token,
            method=getGameHighScores),
        params=payload).json()
    if not result['ok']:
        raise Exception(
            'Error {errno}: {error}'.format(
                errno=result['error_code'],
                error=result['description']))
    return result
