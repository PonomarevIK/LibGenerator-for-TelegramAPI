# This code in it's entirety was automatically generated and formated

class Update:
	"""This object represents an incoming update.At most one of the optional parameters can be present in any given update."""
	def __init__(self, json):
		pass


class WebhookInfo:
	"""Contains information about the current status of a webhook."""
	def __init__(self, json):
		pass


class User:
	"""This object represents a Telegram user or bot."""
	def __init__(self, json):
		pass


class Chat:
	"""This object represents a chat."""
	def __init__(self, json):
		pass


class Message:
	"""This object represents a message."""
	def __init__(self, json):
		pass


class MessageId:
	"""This object represents a unique message identifier."""
	def __init__(self, json):
		pass


class MessageEntity:
	"""This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc."""
	def __init__(self, json):
		pass


class PhotoSize:
	"""This object represents one size of a photo or a file / sticker thumbnail."""
	def __init__(self, json):
		pass


class Animation:
	"""This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound)."""
	def __init__(self, json):
		pass


class Audio:
	"""This object represents an audio file to be treated as music by the Telegram clients."""
	def __init__(self, json):
		pass


class Document:
	"""This object represents a general file (as opposed to photos, voice messages and audio files)."""
	def __init__(self, json):
		pass


class Video:
	"""This object represents a video file."""
	def __init__(self, json):
		pass


class VideoNote:
	"""This object represents a video message (available in Telegram apps as of v.4.0)."""
	def __init__(self, json):
		pass


class Voice:
	"""This object represents a voice note."""
	def __init__(self, json):
		pass


class Contact:
	"""This object represents a phone contact."""
	def __init__(self, json):
		pass


class Dice:
	"""This object represents an animated emoji that displays a random value."""
	def __init__(self, json):
		pass


class PollOption:
	"""This object contains information about one answer option in a poll."""
	def __init__(self, json):
		pass


class PollAnswer:
	"""This object represents an answer of a user in a non-anonymous poll."""
	def __init__(self, json):
		pass


class Poll:
	"""This object contains information about a poll."""
	def __init__(self, json):
		pass


class Location:
	"""This object represents a point on the map."""
	def __init__(self, json):
		pass


class Venue:
	"""This object represents a venue."""
	def __init__(self, json):
		pass


class WebAppData:
	"""Contains data sent from a Web App to the bot."""
	def __init__(self, json):
		pass


class ProximityAlertTriggered:
	"""This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user."""
	def __init__(self, json):
		pass


class MessageAutoDeleteTimerChanged:
	"""This object represents a service message about a change in auto-delete timer settings."""
	def __init__(self, json):
		pass


class VideoChatScheduled:
	"""This object represents a service message about a video chat scheduled in the chat."""
	def __init__(self, json):
		pass


class VideoChatStarted:
	"""This object represents a service message about a video chat started in the chat. Currently holds no information."""
	def __init__(self, json):
		pass


class VideoChatEnded:
	"""This object represents a service message about a video chat ended in the chat."""
	def __init__(self, json):
		pass


class VideoChatParticipantsInvited:
	"""This object represents a service message about new members invited to a video chat."""
	def __init__(self, json):
		pass


class UserProfilePhotos:
	"""This object represent a user's profile pictures."""
	def __init__(self, json):
		pass


class File:
	"""This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile."""
	def __init__(self, json):
		pass


class WebAppInfo:
	"""Contains information about a Web App."""
	def __init__(self, json):
		pass


class ReplyKeyboardMarkup:
	"""This object represents a custom keyboard with reply options (see Introduction to bots for details and examples)."""
	def __init__(self, json):
		pass


class KeyboardButton:
	"""This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields web_app, request_contact, request_location, and request_poll are mutually exclusive."""
	def __init__(self, json):
		pass


class KeyboardButtonPollType:
	"""This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed."""
	def __init__(self, json):
		pass


class ReplyKeyboardRemove:
	"""Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup)."""
	def __init__(self, json):
		pass


class InlineKeyboardMarkup:
	"""This object represents an inline keyboard that appears right next to the message it belongs to."""
	def __init__(self, json):
		pass


class InlineKeyboardButton:
	"""This object represents one button of an inline keyboard. You must use exactly one of the optional fields."""
	def __init__(self, json):
		pass


class LoginUrl:
	"""This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:"""
	def __init__(self, json):
		pass


class CallbackQuery:
	"""This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present."""
	def __init__(self, json):
		pass


class ForceReply:
	"""Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode."""
	def __init__(self, json):
		pass


class ChatPhoto:
	"""This object represents a chat photo."""
	def __init__(self, json):
		pass


class ChatInviteLink:
	"""Represents an invite link for a chat."""
	def __init__(self, json):
		pass


class ChatAdministratorRights:
	"""Represents the rights of an administrator in a chat."""
	def __init__(self, json):
		pass


class ChatMember:
	"""This object contains information about one member of a chat. Currently, the following 6 types of chat members are supported:"""
	def __init__(self, json):
		pass


class ChatMemberOwner:
	"""Represents a chat member that owns the chat and has all administrator privileges."""
	def __init__(self, json):
		pass


class ChatMemberAdministrator:
	"""Represents a chat member that has some additional privileges."""
	def __init__(self, json):
		pass


class ChatMemberMember:
	"""Represents a chat member that has no additional privileges or restrictions."""
	def __init__(self, json):
		pass


class ChatMemberRestricted:
	"""Represents a chat member that is under certain restrictions in the chat. Supergroups only."""
	def __init__(self, json):
		pass


class ChatMemberLeft:
	"""Represents a chat member that isn't currently a member of the chat, but may join it themselves."""
	def __init__(self, json):
		pass


class ChatMemberBanned:
	"""Represents a chat member that was banned in the chat and can't return to the chat or view chat messages."""
	def __init__(self, json):
		pass


class ChatMemberUpdated:
	"""This object represents changes in the status of a chat member."""
	def __init__(self, json):
		pass


class ChatJoinRequest:
	"""Represents a join request sent to a chat."""
	def __init__(self, json):
		pass


class ChatPermissions:
	"""Describes actions that a non-administrator user is allowed to take in a chat."""
	def __init__(self, json):
		pass


class ChatLocation:
	"""Represents a location to which a chat is connected."""
	def __init__(self, json):
		pass


class BotCommand:
	"""This object represents a bot command."""
	def __init__(self, json):
		pass


class BotCommandScope:
	"""This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:"""
	def __init__(self, json):
		pass


class BotCommandScopeDefault:
	"""Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user."""
	def __init__(self, json):
		pass


class BotCommandScopeAllPrivateChats:
	"""Represents the scope of bot commands, covering all private chats."""
	def __init__(self, json):
		pass


class BotCommandScopeAllGroupChats:
	"""Represents the scope of bot commands, covering all group and supergroup chats."""
	def __init__(self, json):
		pass


class BotCommandScopeAllChatAdministrators:
	"""Represents the scope of bot commands, covering all group and supergroup chat administrators."""
	def __init__(self, json):
		pass


class BotCommandScopeChat:
	"""Represents the scope of bot commands, covering a specific chat."""
	def __init__(self, json):
		pass


class BotCommandScopeChatAdministrators:
	"""Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat."""
	def __init__(self, json):
		pass


class BotCommandScopeChatMember:
	"""Represents the scope of bot commands, covering a specific member of a group or supergroup chat."""
	def __init__(self, json):
		pass


class MenuButton:
	"""This object describes the bot's menu button in a private chat. It should be one of"""
	def __init__(self, json):
		pass


class MenuButtonCommands:
	"""Represents a menu button, which opens the bot's list of commands."""
	def __init__(self, json):
		pass


class MenuButtonWebApp:
	"""Represents a menu button, which launches a Web App."""
	def __init__(self, json):
		pass


class MenuButtonDefault:
	"""Describes that no specific value for the menu button was set."""
	def __init__(self, json):
		pass


class ResponseParameters:
	"""Contains information about why a request was unsuccessful."""
	def __init__(self, json):
		pass


class InputMedia:
	"""This object represents the content of a media message to be sent. It should be one of"""
	def __init__(self, json):
		pass


class InputMediaPhoto:
	"""Represents a photo to be sent."""
	def __init__(self, json):
		pass


class InputMediaVideo:
	"""Represents a video to be sent."""
	def __init__(self, json):
		pass


class InputMediaAnimation:
	"""Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent."""
	def __init__(self, json):
		pass


class InputMediaAudio:
	"""Represents an audio file to be treated as music to be sent."""
	def __init__(self, json):
		pass


class InputMediaDocument:
	"""Represents a general file to be sent."""
	def __init__(self, json):
		pass


class InputFile:
	"""This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser."""
	def __init__(self, json):
		pass


class Sticker:
	"""This object represents a sticker."""
	def __init__(self, json):
		pass


class StickerSet:
	"""This object represents a sticker set."""
	def __init__(self, json):
		pass


class MaskPosition:
	"""This object describes the position on faces where a mask should be placed by default."""
	def __init__(self, json):
		pass


class InlineQuery:
	"""This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results."""
	def __init__(self, json):
		pass


class InlineQueryResult:
	"""This object represents one result of an inline query. Telegram clients currently support results of the following 20 types:"""
	def __init__(self, json):
		pass


class InlineQueryResultArticle:
	"""Represents a link to an article or web page."""
	def __init__(self, json):
		pass


class InlineQueryResultPhoto:
	"""Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo."""
	def __init__(self, json):
		pass


class InlineQueryResultGif:
	"""Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation."""
	def __init__(self, json):
		pass


class InlineQueryResultMpeg4Gif:
	"""Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation."""
	def __init__(self, json):
		pass


class InlineQueryResultVideo:
	"""Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video."""
	def __init__(self, json):
		pass


class InlineQueryResultAudio:
	"""Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio."""
	def __init__(self, json):
		pass


class InlineQueryResultVoice:
	"""Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message."""
	def __init__(self, json):
		pass


class InlineQueryResultDocument:
	"""Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method."""
	def __init__(self, json):
		pass


class InlineQueryResultLocation:
	"""Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location."""
	def __init__(self, json):
		pass


class InlineQueryResultVenue:
	"""Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue."""
	def __init__(self, json):
		pass


class InlineQueryResultContact:
	"""Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact."""
	def __init__(self, json):
		pass


class InlineQueryResultGame:
	"""Represents a Game."""
	def __init__(self, json):
		pass


class InlineQueryResultCachedPhoto:
	"""Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo."""
	def __init__(self, json):
		pass


class InlineQueryResultCachedGif:
	"""Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation."""
	def __init__(self, json):
		pass


class InlineQueryResultCachedMpeg4Gif:
	"""Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation."""
	def __init__(self, json):
		pass


class InlineQueryResultCachedSticker:
	"""Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker."""
	def __init__(self, json):
		pass


class InlineQueryResultCachedDocument:
	"""Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file."""
	def __init__(self, json):
		pass


class InlineQueryResultCachedVideo:
	"""Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video."""
	def __init__(self, json):
		pass


class InlineQueryResultCachedVoice:
	"""Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message."""
	def __init__(self, json):
		pass


class InlineQueryResultCachedAudio:
	"""Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio."""
	def __init__(self, json):
		pass


class InputMessageContent:
	"""This object represents the content of a message to be sent as a result of an inline query. Telegram clients currently support the following 5 types:"""
	def __init__(self, json):
		pass


class InputTextMessageContent:
	"""Represents the content of a text message to be sent as the result of an inline query."""
	def __init__(self, json):
		pass


class InputLocationMessageContent:
	"""Represents the content of a location message to be sent as the result of an inline query."""
	def __init__(self, json):
		pass


class InputVenueMessageContent:
	"""Represents the content of a venue message to be sent as the result of an inline query."""
	def __init__(self, json):
		pass


class InputContactMessageContent:
	"""Represents the content of a contact message to be sent as the result of an inline query."""
	def __init__(self, json):
		pass


class InputInvoiceMessageContent:
	"""Represents the content of an invoice message to be sent as the result of an inline query."""
	def __init__(self, json):
		pass


class ChosenInlineResult:
	"""Represents a result of an inline query that was chosen by the user and sent to their chat partner."""
	def __init__(self, json):
		pass


class SentWebAppMessage:
	"""Contains information about an inline message sent by a Web App on behalf of a user."""
	def __init__(self, json):
		pass


class LabeledPrice:
	"""This object represents a portion of the price for goods or services."""
	def __init__(self, json):
		pass


class Invoice:
	"""This object contains basic information about an invoice."""
	def __init__(self, json):
		pass


class ShippingAddress:
	"""This object represents a shipping address."""
	def __init__(self, json):
		pass


class OrderInfo:
	"""This object represents information about an order."""
	def __init__(self, json):
		pass


class ShippingOption:
	"""This object represents one shipping option."""
	def __init__(self, json):
		pass


class SuccessfulPayment:
	"""This object contains basic information about a successful payment."""
	def __init__(self, json):
		pass


class ShippingQuery:
	"""This object contains information about an incoming shipping query."""
	def __init__(self, json):
		pass


class PreCheckoutQuery:
	"""This object contains information about an incoming pre-checkout query."""
	def __init__(self, json):
		pass


class PassportData:
	"""Contains information about Telegram Passport data shared with the bot by the user."""
	def __init__(self, json):
		pass


class PassportFile:
	"""This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB."""
	def __init__(self, json):
		pass


class EncryptedPassportElement:
	"""Contains information about documents or other Telegram Passport elements shared with the bot by the user."""
	def __init__(self, json):
		pass


class EncryptedCredentials:
	"""Contains data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes."""
	def __init__(self, json):
		pass


class PassportElementError:
	"""This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user. It should be one of:"""
	def __init__(self, json):
		pass


class PassportElementErrorDataField:
	"""Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes."""
	def __init__(self, json):
		pass


class PassportElementErrorFrontSide:
	"""Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes."""
	def __init__(self, json):
		pass


class PassportElementErrorReverseSide:
	"""Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes."""
	def __init__(self, json):
		pass


class PassportElementErrorSelfie:
	"""Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes."""
	def __init__(self, json):
		pass


class PassportElementErrorFile:
	"""Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes."""
	def __init__(self, json):
		pass


class PassportElementErrorFiles:
	"""Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes."""
	def __init__(self, json):
		pass


class PassportElementErrorTranslationFile:
	"""Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes."""
	def __init__(self, json):
		pass


class PassportElementErrorTranslationFiles:
	"""Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change."""
	def __init__(self, json):
		pass


class PassportElementErrorUnspecified:
	"""Represents an issue in an unspecified place. The error is considered resolved when new data is added."""
	def __init__(self, json):
		pass


class Game:
	"""This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers."""
	def __init__(self, json):
		pass


class CallbackGame:
	"""A placeholder, currently holds no information. Use BotFather to set up your game."""
	def __init__(self, json):
		pass


class GameHighScore:
	"""This object represents one row of the high scores table for a game."""
	def __init__(self, json):
		pass


