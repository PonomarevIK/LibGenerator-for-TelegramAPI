# This code in its entirety was generated and formatted automatically

import requests
import logging
from types import *

API_URL = 'https://api.telegram.org/bot{token}/{method}'
token = 'your_bot_token_here'
logger = None


def getUpdates(offset: int = None, limit: int = None, timeout: int = None, allowed_updates: list[str] = None) -> list[Update]:
    """Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned."""
    request_params = {}
    request_params['offset'] = offset
    request_params['limit'] = limit
    request_params['timeout'] = timeout
    request_params['allowed_updates'] = allowed_updates

    response = requests.get(API_URL.format(token=token, method=getUpdates), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return [Update(item) for item in result]


def setWebhook() -> bool:
    """Use this method to specify a url and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified url, containing a JSON-serialized Update. In case of an unsuccessful request, we will give up after a reasonable amount of attempts. Returns True on success."""
    request_params = None

    response = requests.get(API_URL.format(token=token, method=setWebhook), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def deleteWebhook(drop_pending_updates: bool = None) -> bool:
    """Use this method to remove webhook integration if you decide to switch back to getUpdates. Returns True on success."""
    request_params = {}
    request_params['drop_pending_updates'] = drop_pending_updates

    response = requests.get(API_URL.format(token=token, method=deleteWebhook), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def getWebhookInfo() -> WebhookInfo:
    """Use this method to get current webhook status. Requires no parameters. On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty."""
    request_params = None

    response = requests.get(API_URL.format(token=token, method=getWebhookInfo), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return WebhookInfo(result)


def getMe() -> User:
    """A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a User object."""
    request_params = None

    response = requests.get(API_URL.format(token=token, method=getMe), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return User(result)


def logOut() -> bool:
    """Use this method to log out from the cloud Bot API server before launching the bot locally. You must log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns True on success. Requires no parameters."""
    request_params = None

    response = requests.get(API_URL.format(token=token, method=logOut), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def close() -> bool:
    """Use this method to close the bot instance before moving it from one local server to another. You need to delete the webhook before calling this method to ensure that the bot isn't launched again after server restart. The method will return error 429 in the first 10 minutes after the bot is launched. Returns True on success. Requires no parameters."""
    request_params = None

    response = requests.get(API_URL.format(token=token, method=close), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def sendMessage(chat_id: int | str, text: str, parse_mode: str = None, entities: list[MessageEntity] = None, disable_web_page_preview: bool = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send text messages. On success, the sent Message is returned."""
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

    response = requests.get(API_URL.format(token=token, method=sendMessage), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def forwardMessage(chat_id: int | str, from_chat_id: int | str, message_id: int, disable_notification: bool = None, protect_content: bool = None) -> Message:
    """Use this method to forward messages of any kind. Service messages can't be forwarded. On success, the sent Message is returned."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['from_chat_id'] = from_chat_id
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['message_id'] = message_id

    response = requests.get(API_URL.format(token=token, method=forwardMessage), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def copyMessage(chat_id: int | str, from_chat_id: int | str, message_id: int, caption: str = None, parse_mode: str = None, caption_entities: list[MessageEntity] = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> MessageId:
    """Use this method to copy messages of any kind. Service messages and invoice messages can't be copied. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['from_chat_id'] = from_chat_id
    request_params['message_id'] = message_id
    request_params['caption'] = caption
    request_params['parse_mode'] = parse_mode
    request_params['caption_entities'] = [item.json for item in caption_entities]
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(API_URL.format(token=token, method=copyMessage), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return MessageId(result)


def sendPhoto(chat_id: int | str, photo: InputFile | str, caption: str = None, parse_mode: str = None, caption_entities: list[MessageEntity] = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send photos. On success, the sent Message is returned."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['photo'] = photo.json
    request_params['caption'] = caption
    request_params['parse_mode'] = parse_mode
    request_params['caption_entities'] = [item.json for item in caption_entities]
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(API_URL.format(token=token, method=sendPhoto), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def sendAudio() -> Message:
    """Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future."""
    request_params = None

    response = requests.get(API_URL.format(token=token, method=sendAudio), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def sendDocument(chat_id: int | str, document: InputFile | str, thumb: InputFile | str = None, caption: str = None, parse_mode: str = None, caption_entities: list[MessageEntity] = None, disable_content_type_detection: bool = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send general files. On success, the sent Message is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['document'] = document.json
    request_params['thumb'] = thumb.json
    request_params['caption'] = caption
    request_params['parse_mode'] = parse_mode
    request_params['caption_entities'] = [item.json for item in caption_entities]
    request_params['disable_content_type_detection'] = disable_content_type_detection
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(API_URL.format(token=token, method=sendDocument), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def sendVideo(chat_id: int | str, video: InputFile | str, duration: int = None, width: int = None, height: int = None, thumb: InputFile | str = None, caption: str = None, parse_mode: str = None, caption_entities: list[MessageEntity] = None, supports_streaming: bool = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['video'] = video.json
    request_params['duration'] = duration
    request_params['width'] = width
    request_params['height'] = height
    request_params['thumb'] = thumb.json
    request_params['caption'] = caption
    request_params['parse_mode'] = parse_mode
    request_params['caption_entities'] = [item.json for item in caption_entities]
    request_params['supports_streaming'] = supports_streaming
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(API_URL.format(token=token, method=sendVideo), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def sendAnimation(chat_id: int | str, animation: InputFile | str, duration: int = None, width: int = None, height: int = None, thumb: InputFile | str = None, caption: str = None, parse_mode: str = None, caption_entities: list[MessageEntity] = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent Message is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['animation'] = animation.json
    request_params['duration'] = duration
    request_params['width'] = width
    request_params['height'] = height
    request_params['thumb'] = thumb.json
    request_params['caption'] = caption
    request_params['parse_mode'] = parse_mode
    request_params['caption_entities'] = [item.json for item in caption_entities]
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(API_URL.format(token=token, method=sendAnimation), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def sendVoice(chat_id: int | str, voice: InputFile | str, caption: str = None, parse_mode: str = None, caption_entities: list[MessageEntity] = None, duration: int = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['voice'] = voice.json
    request_params['caption'] = caption
    request_params['parse_mode'] = parse_mode
    request_params['caption_entities'] = [item.json for item in caption_entities]
    request_params['duration'] = duration
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(API_URL.format(token=token, method=sendVoice), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def sendVideoNote(chat_id: int | str, video_note: InputFile | str, duration: int = None, length: int = None, thumb: InputFile | str = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """As of v.4.0, Telegram clients support rounded square mp4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent Message is returned."""
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

    response = requests.get(API_URL.format(token=token, method=sendVideoNote), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def sendMediaGroup(chat_id: int | str, media: list[InputMediaAudio | InputMediaDocument | InputMediaPhoto | InputMediaVideo], disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None) -> list[Message]:
    """Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an array of Messages that were sent is returned."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['media'] = [item.json for item in media]
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply

    response = requests.get(API_URL.format(token=token, method=sendMediaGroup), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return [Message(item) for item in result]


def sendLocation(chat_id: int | str, latitude: float, longitude: float, horizontal_accuracy: float = None, live_period: int = None, heading: int = None, proximity_alert_radius: int = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send point on the map. On success, the sent Message is returned."""
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

    response = requests.get(API_URL.format(token=token, method=sendLocation), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def editMessageLiveLocation(latitude: float, longitude: float, chat_id: int | str = None, message_id: int = None, inline_message_id: str = None, horizontal_accuracy: float = None, heading: int = None, proximity_alert_radius: int = None, reply_markup: InlineKeyboardMarkup = None) -> Message:
    """Use this method to edit live location messages. A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""
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

    response = requests.get(API_URL.format(token=token, method=editMessageLiveLocation), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def stopMessageLiveLocation(chat_id: int | str = None, message_id: int = None, inline_message_id: str = None, reply_markup: InlineKeyboardMarkup = None) -> Message:
    """Use this method to stop updating a live location message before live_period expires. On success, if the message is not an inline message, the edited Message is returned, otherwise True is returned."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id
    request_params['inline_message_id'] = inline_message_id
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(API_URL.format(token=token, method=stopMessageLiveLocation), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def sendVenue(chat_id: int | str, latitude: float, longitude: float, title: str, address: str, foursquare_id: str = None, foursquare_type: str = None, google_place_id: str = None, google_place_type: str = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send information about a venue. On success, the sent Message is returned."""
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

    response = requests.get(API_URL.format(token=token, method=sendVenue), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def sendContact(chat_id: int | str, phone_number: str, first_name: str, last_name: str = None, vcard: str = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send phone contacts. On success, the sent Message is returned."""
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

    response = requests.get(API_URL.format(token=token, method=sendContact), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def sendPoll(chat_id: int | str, question: str, options: list[str], is_anonymous: bool = None, type: str = None, allows_multiple_answers: bool = None, correct_option_id: int = None, explanation: str = None, explanation_parse_mode: str = None, explanation_entities: list[MessageEntity] = None, open_period: int = None, close_date: int = None, is_closed: bool = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send a native poll. On success, the sent Message is returned."""
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
    request_params['explanation_entities'] = [item.json for item in explanation_entities]
    request_params['open_period'] = open_period
    request_params['close_date'] = close_date
    request_params['is_closed'] = is_closed
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(API_URL.format(token=token, method=sendPoll), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def sendDice(chat_id: int | str, emoji: str = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send an animated emoji that will display a random value. On success, the sent Message is returned."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['emoji'] = emoji
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(API_URL.format(token=token, method=sendDice), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def sendChatAction() -> bool:
    """Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns True on success."""
    request_params = None

    response = requests.get(API_URL.format(token=token, method=sendChatAction), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def getUserProfilePhotos(user_id: int, offset: int = None, limit: int = None) -> UserProfilePhotos:
    """Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object."""
    request_params = {}
    request_params['user_id'] = user_id
    request_params['offset'] = offset
    request_params['limit'] = limit

    response = requests.get(API_URL.format(token=token, method=getUserProfilePhotos), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return UserProfilePhotos(result)


def getFile(file_id: str) -> File:
    """Use this method to get basic info about a file and prepare it for downloading. For the moment, bots can download files of up to 20MB in size. On success, a File object is returned. The file can then be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>, where <file_path> is taken from the response. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile again."""
    request_params = {}
    request_params['file_id'] = file_id

    response = requests.get(API_URL.format(token=token, method=getFile), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return File(result)


def banChatMember(chat_id: int | str, user_id: int, until_date: int = None, revoke_messages: bool = None) -> bool:
    """Use this method to ban a user in a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless unbanned first. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['user_id'] = user_id
    request_params['until_date'] = until_date
    request_params['revoke_messages'] = revoke_messages

    response = requests.get(API_URL.format(token=token, method=banChatMember), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def unbanChatMember(chat_id: int | str, user_id: int, only_if_banned: bool = None) -> bool:
    """Use this method to unban a previously banned user in a supergroup or channel. The user will not return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be removed from the chat. If you don't want this, use the parameter only_if_banned. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['user_id'] = user_id
    request_params['only_if_banned'] = only_if_banned

    response = requests.get(API_URL.format(token=token, method=unbanChatMember), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def restrictChatMember(chat_id: int | str, user_id: int, permissions: ChatPermissions, until_date: int = None) -> bool:
    """Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass True for all permissions to lift restrictions from a user. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['user_id'] = user_id
    request_params['permissions'] = permissions.json
    request_params['until_date'] = until_date

    response = requests.get(API_URL.format(token=token, method=restrictChatMember), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def promoteChatMember(chat_id: int | str, user_id: int, is_anonymous: bool = None, can_manage_chat: bool = None, can_post_messages: bool = None, can_edit_messages: bool = None, can_delete_messages: bool = None, can_manage_video_chats: bool = None, can_restrict_members: bool = None, can_promote_members: bool = None, can_change_info: bool = None, can_invite_users: bool = None, can_pin_messages: bool = None) -> bool:
    """Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass False for all boolean parameters to demote a user. Returns True on success."""
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

    response = requests.get(API_URL.format(token=token, method=promoteChatMember), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def setChatAdministratorCustomTitle(chat_id: int | str, user_id: int, custom_title: str) -> bool:
    """Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['user_id'] = user_id
    request_params['custom_title'] = custom_title

    response = requests.get(API_URL.format(token=token, method=setChatAdministratorCustomTitle), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def banChatSenderChat(chat_id: int | str, sender_chat_id: int) -> bool:
    """Use this method to ban a channel chat in a supergroup or a channel. Until the chat is unbanned, the owner of the banned chat won't be able to send messages on behalf of any of their channels. The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['sender_chat_id'] = sender_chat_id

    response = requests.get(API_URL.format(token=token, method=banChatSenderChat), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def unbanChatSenderChat(chat_id: int | str, sender_chat_id: int) -> bool:
    """Use this method to unban a previously banned channel chat in a supergroup or channel. The bot must be an administrator for this to work and must have the appropriate administrator rights. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['sender_chat_id'] = sender_chat_id

    response = requests.get(API_URL.format(token=token, method=unbanChatSenderChat), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def setChatPermissions(chat_id: int | str, permissions: ChatPermissions) -> bool:
    """Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the can_restrict_members administrator rights. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['permissions'] = permissions.json

    response = requests.get(API_URL.format(token=token, method=setChatPermissions), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def exportChatInviteLink(chat_id: int | str) -> str:
    """Use this method to generate a new primary invite link for a chat; any previously generated primary link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the new invite link as String on success."""
    request_params = {}
    request_params['chat_id'] = chat_id

    response = requests.get(API_URL.format(token=token, method=exportChatInviteLink), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return str(result)


def createChatInviteLink(chat_id: int | str, name: str = None, expire_date: int = None, member_limit: int = None, creates_join_request: bool = None) -> ChatInviteLink:
    """Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. The link can be revoked using the method revokeChatInviteLink. Returns the new invite link as ChatInviteLink object."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['name'] = name
    request_params['expire_date'] = expire_date
    request_params['member_limit'] = member_limit
    request_params['creates_join_request'] = creates_join_request

    response = requests.get(API_URL.format(token=token, method=createChatInviteLink), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return ChatInviteLink(result)


def editChatInviteLink(chat_id: int | str, invite_link: str, name: str = None, expire_date: int = None, member_limit: int = None, creates_join_request: bool = None) -> ChatInviteLink:
    """Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a ChatInviteLink object."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['invite_link'] = invite_link
    request_params['name'] = name
    request_params['expire_date'] = expire_date
    request_params['member_limit'] = member_limit
    request_params['creates_join_request'] = creates_join_request

    response = requests.get(API_URL.format(token=token, method=editChatInviteLink), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return ChatInviteLink(result)


def revokeChatInviteLink(chat_id: int | str, invite_link: str) -> ChatInviteLink:
    """Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the revoked invite link as ChatInviteLink object."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['invite_link'] = invite_link

    response = requests.get(API_URL.format(token=token, method=revokeChatInviteLink), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return ChatInviteLink(result)


def approveChatJoinRequest(chat_id: int | str, user_id: int) -> bool:
    """Use this method to approve a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['user_id'] = user_id

    response = requests.get(API_URL.format(token=token, method=approveChatJoinRequest), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def declineChatJoinRequest(chat_id: int | str, user_id: int) -> bool:
    """Use this method to decline a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['user_id'] = user_id

    response = requests.get(API_URL.format(token=token, method=declineChatJoinRequest), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def setChatPhoto(chat_id: int | str, photo: InputFile) -> bool:
    """Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['photo'] = photo.json

    response = requests.get(API_URL.format(token=token, method=setChatPhoto), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def deleteChatPhoto(chat_id: int | str) -> bool:
    """Use this method to delete a chat photo. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id

    response = requests.get(API_URL.format(token=token, method=deleteChatPhoto), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def setChatTitle(chat_id: int | str, title: str) -> bool:
    """Use this method to change the title of a chat. Titles can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['title'] = title

    response = requests.get(API_URL.format(token=token, method=setChatTitle), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def setChatDescription(chat_id: int | str, description: str = None) -> bool:
    """Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['description'] = description

    response = requests.get(API_URL.format(token=token, method=setChatDescription), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def pinChatMessage(chat_id: int | str, message_id: int, disable_notification: bool = None) -> bool:
    """Use this method to add a message to the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id
    request_params['disable_notification'] = disable_notification

    response = requests.get(API_URL.format(token=token, method=pinChatMessage), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def unpinChatMessage(chat_id: int | str, message_id: int = None) -> bool:
    """Use this method to remove a message from the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id

    response = requests.get(API_URL.format(token=token, method=unpinChatMessage), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def unpinAllChatMessages(chat_id: int | str) -> bool:
    """Use this method to clear the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id

    response = requests.get(API_URL.format(token=token, method=unpinAllChatMessages), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def leaveChat(chat_id: int | str) -> bool:
    """Use this method for your bot to leave a group, supergroup or channel. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id

    response = requests.get(API_URL.format(token=token, method=leaveChat), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def getChat(chat_id: int | str) -> Chat:
    """Use this method to get up to date information about the chat (current name of the user for one-on-one conversations, current username of a user, group or channel, etc.). Returns a Chat object on success."""
    request_params = {}
    request_params['chat_id'] = chat_id

    response = requests.get(API_URL.format(token=token, method=getChat), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Chat(result)


def getChatAdministrators(chat_id: int | str) -> list[ChatMember]:
    """Use this method to get a list of administrators in a chat. On success, returns an Array of ChatMember objects that contains information about all chat administrators except other bots. If the chat is a group or a supergroup and no administrators were appointed, only the creator will be returned."""
    request_params = {}
    request_params['chat_id'] = chat_id

    response = requests.get(API_URL.format(token=token, method=getChatAdministrators), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return [ChatMember(item) for item in result]


def getChatMemberCount(chat_id: int | str) -> int:
    """Use this method to get the number of members in a chat. Returns Int on success."""
    request_params = {}
    request_params['chat_id'] = chat_id

    response = requests.get(API_URL.format(token=token, method=getChatMemberCount), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return int(result)


def getChatMember(chat_id: int | str, user_id: int) -> ChatMember:
    """Use this method to get information about a member of a chat. Returns a ChatMember object on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['user_id'] = user_id

    response = requests.get(API_URL.format(token=token, method=getChatMember), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return ChatMember(result)


def setChatStickerSet(chat_id: int | str, sticker_set_name: str) -> bool:
    """Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['sticker_set_name'] = sticker_set_name

    response = requests.get(API_URL.format(token=token, method=setChatStickerSet), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def deleteChatStickerSet(chat_id: int | str) -> bool:
    """Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id

    response = requests.get(API_URL.format(token=token, method=deleteChatStickerSet), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def answerCallbackQuery() -> bool:
    """Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned."""
    request_params = None

    response = requests.get(API_URL.format(token=token, method=answerCallbackQuery), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def setMyCommands(commands: list[BotCommand], scope: BotCommandScope = None, language_code: str = None) -> bool:
    """Use this method to change the list of the bot's commands. See https://core.telegram.org/bots#commands for more details about bot commands. Returns True on success."""
    request_params = {}
    request_params['commands'] = [item.json for item in commands]
    request_params['scope'] = scope.json
    request_params['language_code'] = language_code

    response = requests.get(API_URL.format(token=token, method=setMyCommands), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def deleteMyCommands(scope: BotCommandScope = None, language_code: str = None) -> bool:
    """Use this method to delete the list of the bot's commands for the given scope and user language. After deletion, higher level commands will be shown to affected users. Returns True on success."""
    request_params = {}
    request_params['scope'] = scope.json
    request_params['language_code'] = language_code

    response = requests.get(API_URL.format(token=token, method=deleteMyCommands), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def getMyCommands(scope: BotCommandScope = None, language_code: str = None) -> list[BotCommand]:
    """Use this method to get the current list of the bot's commands for the given scope and user language. Returns Array of BotCommand on success. If commands aren't set, an empty list is returned."""
    request_params = {}
    request_params['scope'] = scope.json
    request_params['language_code'] = language_code

    response = requests.get(API_URL.format(token=token, method=getMyCommands), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return [BotCommand(item) for item in result]


def setChatMenuButton(chat_id: int = None, menu_button: MenuButton = None) -> bool:
    """Use this method to change the bot's menu button in a private chat, or the default menu button. Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['menu_button'] = menu_button.json

    response = requests.get(API_URL.format(token=token, method=setChatMenuButton), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def getChatMenuButton(chat_id: int = None) -> MenuButton:
    """Use this method to get the current value of the bot's menu button in a private chat, or the default menu button. Returns MenuButton on success."""
    request_params = {}
    request_params['chat_id'] = chat_id

    response = requests.get(API_URL.format(token=token, method=getChatMenuButton), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return MenuButton(result)


def setMyDefaultAdministratorRights(rights: ChatAdministratorRights = None, for_channels: bool = None) -> bool:
    """Use this method to change the default administrator rights requested by the bot when it's added as an administrator to groups or channels. These rights will be suggested to users, but they are are free to modify the list before adding the bot. Returns True on success."""
    request_params = {}
    request_params['rights'] = rights.json
    request_params['for_channels'] = for_channels

    response = requests.get(API_URL.format(token=token, method=setMyDefaultAdministratorRights), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def getMyDefaultAdministratorRights(for_channels: bool = None) -> ChatAdministratorRights:
    """Use this method to get the current default administrator rights of the bot. Returns ChatAdministratorRights on success."""
    request_params = {}
    request_params['for_channels'] = for_channels

    response = requests.get(API_URL.format(token=token, method=getMyDefaultAdministratorRights), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return ChatAdministratorRights(result)


def editMessageText(text: str, chat_id: int | str = None, message_id: int = None, inline_message_id: str = None, parse_mode: str = None, entities: list[MessageEntity] = None, disable_web_page_preview: bool = None, reply_markup: InlineKeyboardMarkup = None) -> Message:
    """Use this method to edit text and game messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id
    request_params['inline_message_id'] = inline_message_id
    request_params['text'] = text
    request_params['parse_mode'] = parse_mode
    request_params['entities'] = [item.json for item in entities]
    request_params['disable_web_page_preview'] = disable_web_page_preview
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(API_URL.format(token=token, method=editMessageText), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def editMessageCaption(chat_id: int | str = None, message_id: int = None, inline_message_id: str = None, caption: str = None, parse_mode: str = None, caption_entities: list[MessageEntity] = None, reply_markup: InlineKeyboardMarkup = None) -> Message:
    """Use this method to edit captions of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id
    request_params['inline_message_id'] = inline_message_id
    request_params['caption'] = caption
    request_params['parse_mode'] = parse_mode
    request_params['caption_entities'] = [item.json for item in caption_entities]
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(API_URL.format(token=token, method=editMessageCaption), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def editMessageMedia(media: InputMedia, chat_id: int | str = None, message_id: int = None, inline_message_id: str = None, reply_markup: InlineKeyboardMarkup = None) -> Message:
    """Use this method to edit animation, audio, document, photo, or video messages. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo or a video otherwise. When an inline message is edited, a new file can't be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id
    request_params['inline_message_id'] = inline_message_id
    request_params['media'] = media.json
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(API_URL.format(token=token, method=editMessageMedia), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def editMessageReplyMarkup(chat_id: int | str = None, message_id: int = None, inline_message_id: str = None, reply_markup: InlineKeyboardMarkup = None) -> Message:
    """Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id
    request_params['inline_message_id'] = inline_message_id
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(API_URL.format(token=token, method=editMessageReplyMarkup), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def stopPoll(chat_id: int | str, message_id: int, reply_markup: InlineKeyboardMarkup = None) -> Poll:
    """Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(API_URL.format(token=token, method=stopPoll), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Poll(result)


def deleteMessage(chat_id: int | str, message_id: int) -> bool:
    """Use this method to delete a message, including service messages, with the following limitations:- A message can only be deleted if it was sent less than 48 hours ago.- A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.- Bots can delete outgoing messages in private chats, groups, and supergroups.- Bots can delete incoming messages in private chats.- Bots granted can_post_messages permissions can delete outgoing messages in channels.- If the bot is an administrator of a group, it can delete any message there.- If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.Returns True on success."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id

    response = requests.get(API_URL.format(token=token, method=deleteMessage), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def sendSticker(chat_id: int | str, sticker: InputFile | str, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None) -> Message:
    """Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers. On success, the sent Message is returned."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['sticker'] = sticker.json
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(API_URL.format(token=token, method=sendSticker), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def getStickerSet(name: str) -> StickerSet:
    """Use this method to get a sticker set. On success, a StickerSet object is returned."""
    request_params = {}
    request_params['name'] = name

    response = requests.get(API_URL.format(token=token, method=getStickerSet), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return StickerSet(result)


def uploadStickerFile(user_id: int, png_sticker: InputFile) -> File:
    """Use this method to upload a .PNG file with a sticker for later use in createNewStickerSet and addStickerToSet methods (can be used multiple times). Returns the uploaded File on success."""
    request_params = {}
    request_params['user_id'] = user_id
    request_params['png_sticker'] = png_sticker.json

    response = requests.get(API_URL.format(token=token, method=uploadStickerFile), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return File(result)


def createNewStickerSet(user_id: int, name: str, title: str, emojis: str, png_sticker: InputFile | str = None, tgs_sticker: InputFile = None, webm_sticker: InputFile = None, contains_masks: bool = None, mask_position: MaskPosition = None) -> bool:
    """Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. You must use exactly one of the fields png_sticker, tgs_sticker, or webm_sticker. Returns True on success."""
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

    response = requests.get(API_URL.format(token=token, method=createNewStickerSet), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def addStickerToSet(user_id: int, name: str, emojis: str, png_sticker: InputFile | str = None, tgs_sticker: InputFile = None, webm_sticker: InputFile = None, mask_position: MaskPosition = None) -> bool:
    """Use this method to add a new sticker to a set created by the bot. You must use exactly one of the fields png_sticker, tgs_sticker, or webm_sticker. Animated stickers can be added to animated sticker sets and only to them. Animated sticker sets can have up to 50 stickers. Static sticker sets can have up to 120 stickers. Returns True on success."""
    request_params = {}
    request_params['user_id'] = user_id
    request_params['name'] = name
    request_params['png_sticker'] = png_sticker.json
    request_params['tgs_sticker'] = tgs_sticker.json
    request_params['webm_sticker'] = webm_sticker.json
    request_params['emojis'] = emojis
    request_params['mask_position'] = mask_position.json

    response = requests.get(API_URL.format(token=token, method=addStickerToSet), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def setStickerPositionInSet(sticker: str, position: int) -> bool:
    """Use this method to move a sticker in a set created by the bot to a specific position. Returns True on success."""
    request_params = {}
    request_params['sticker'] = sticker
    request_params['position'] = position

    response = requests.get(API_URL.format(token=token, method=setStickerPositionInSet), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def deleteStickerFromSet(sticker: str) -> bool:
    """Use this method to delete a sticker from a set created by the bot. Returns True on success."""
    request_params = {}
    request_params['sticker'] = sticker

    response = requests.get(API_URL.format(token=token, method=deleteStickerFromSet), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def setStickerSetThumb(name: str, user_id: int, thumb: InputFile | str = None) -> bool:
    """Use this method to set the thumbnail of a sticker set. Animated thumbnails can be set for animated sticker sets only. Video thumbnails can be set only for video sticker sets only. Returns True on success."""
    request_params = {}
    request_params['name'] = name
    request_params['user_id'] = user_id
    request_params['thumb'] = thumb.json

    response = requests.get(API_URL.format(token=token, method=setStickerSetThumb), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def answerInlineQuery(inline_query_id: str, results: list[InlineQueryResult], cache_time: int = None, is_personal: bool = None, next_offset: str = None, switch_pm_text: str = None, switch_pm_parameter: str = None) -> bool:
    """Use this method to send answers to an inline query. On success, True is returned.No more than 50 results per query are allowed."""
    request_params = {}
    request_params['inline_query_id'] = inline_query_id
    request_params['results'] = [item.json for item in results]
    request_params['cache_time'] = cache_time
    request_params['is_personal'] = is_personal
    request_params['next_offset'] = next_offset
    request_params['switch_pm_text'] = switch_pm_text
    request_params['switch_pm_parameter'] = switch_pm_parameter

    response = requests.get(API_URL.format(token=token, method=answerInlineQuery), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def answerWebAppQuery(web_app_query_id: str, result: InlineQueryResult) -> SentWebAppMessage:
    """Use this method to set the result of an interaction with a Web App and send a corresponding message on behalf of the user to the chat from which the query originated. On success, a SentWebAppMessage object is returned."""
    request_params = {}
    request_params['web_app_query_id'] = web_app_query_id
    request_params['result'] = result.json

    response = requests.get(API_URL.format(token=token, method=answerWebAppQuery), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return SentWebAppMessage(result)


def sendInvoice(chat_id: int | str, title: str, description: str, payload: str, provider_token: str, currency: str, prices: list[LabeledPrice], max_tip_amount: int = None, suggested_tip_amounts: list[int] = None, start_parameter: str = None, provider_data: str = None, photo_url: str = None, photo_size: int = None, photo_width: int = None, photo_height: int = None, need_name: bool = None, need_phone_number: bool = None, need_email: bool = None, need_shipping_address: bool = None, send_phone_number_to_provider: bool = None, send_email_to_provider: bool = None, is_flexible: bool = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: InlineKeyboardMarkup = None) -> Message:
    """Use this method to send invoices. On success, the sent Message is returned."""
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

    response = requests.get(API_URL.format(token=token, method=sendInvoice), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def answerShippingQuery(shipping_query_id: str, ok: bool, shipping_options: list[ShippingOption] = None, error_message: str = None) -> bool:
    """If you sent an invoice requesting a shipping address and the parameter is_flexible was specified, the Bot API will send an Update with a shipping_query field to the bot. Use this method to reply to shipping queries. On success, True is returned."""
    request_params = {}
    request_params['shipping_query_id'] = shipping_query_id
    request_params['ok'] = ok
    request_params['shipping_options'] = [item.json for item in shipping_options]
    request_params['error_message'] = error_message

    response = requests.get(API_URL.format(token=token, method=answerShippingQuery), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def answerPreCheckoutQuery(pre_checkout_query_id: str, ok: bool, error_message: str = None) -> bool:
    """Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an Update with the field pre_checkout_query. Use this method to respond to such pre-checkout queries. On success, True is returned. Note: The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent."""
    request_params = {}
    request_params['pre_checkout_query_id'] = pre_checkout_query_id
    request_params['ok'] = ok
    request_params['error_message'] = error_message

    response = requests.get(API_URL.format(token=token, method=answerPreCheckoutQuery), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def setPassportDataErrors() -> bool:
    """Informs a user that some of the Telegram Passport elements they provided contains errors. The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change). Returns True on success."""
    request_params = None

    response = requests.get(API_URL.format(token=token, method=setPassportDataErrors), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return bool(result)


def sendGame(chat_id: int, game_short_name: str, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: InlineKeyboardMarkup = None) -> Message:
    """Use this method to send a game. On success, the sent Message is returned."""
    request_params = {}
    request_params['chat_id'] = chat_id
    request_params['game_short_name'] = game_short_name
    request_params['disable_notification'] = disable_notification
    request_params['protect_content'] = protect_content
    request_params['reply_to_message_id'] = reply_to_message_id
    request_params['allow_sending_without_reply'] = allow_sending_without_reply
    request_params['reply_markup'] = reply_markup.json

    response = requests.get(API_URL.format(token=token, method=sendGame), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def setGameScore(user_id: int, score: int, force: bool = None, disable_edit_message: bool = None, chat_id: int = None, message_id: int = None, inline_message_id: str = None) -> Message:
    """Use this method to set the score of the specified user in a game message. On success, if the message is not an inline message, the Message is returned, otherwise True is returned. Returns an error, if the new score is not greater than the user's current score in the chat and force is False."""
    request_params = {}
    request_params['user_id'] = user_id
    request_params['score'] = score
    request_params['force'] = force
    request_params['disable_edit_message'] = disable_edit_message
    request_params['chat_id'] = chat_id
    request_params['message_id'] = message_id
    request_params['inline_message_id'] = inline_message_id

    response = requests.get(API_URL.format(token=token, method=setGameScore), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return Message(result)


def getGameHighScores() -> list[GameHighScore]:
    """Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. On success, returns an Array of GameHighScore objects."""
    request_params = None

    response = requests.get(API_URL.format(token=token, method=getGameHighScores), params=request_params).json()
    if not response['ok']:
        raise requests.exceptions.RequestException('Error {errno}: {error}'.format(errno=response['error_code'], error=response['description']))
    result = response['result']

    return [GameHighScore(item) for item in result]


