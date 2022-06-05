# This code in its entirety was generated and formatted automatically



class Update:
    """This object represents an incoming update.At most one of the optional parameters can be present in any given update."""
    def __init__(self, json):
        self.json = json
        self.update_id = int(json['update_id'])
        self.message = Message(json['message']) if ('message' in json) else None
        self.edited_message = Message(json['edited_message']) if ('edited_message' in json) else None
        self.channel_post = Message(json['channel_post']) if ('channel_post' in json) else None
        self.edited_channel_post = Message(json['edited_channel_post']) if ('edited_channel_post' in json) else None
        self.inline_query = InlineQuery(json['inline_query']) if ('inline_query' in json) else None
        self.chosen_inline_result = ChosenInlineResult(json['chosen_inline_result']) if ('chosen_inline_result' in json) else None
        self.callback_query = CallbackQuery(json['callback_query']) if ('callback_query' in json) else None
        self.shipping_query = ShippingQuery(json['shipping_query']) if ('shipping_query' in json) else None
        self.pre_checkout_query = PreCheckoutQuery(json['pre_checkout_query']) if ('pre_checkout_query' in json) else None
        self.poll = Poll(json['poll']) if ('poll' in json) else None
        self.poll_answer = PollAnswer(json['poll_answer']) if ('poll_answer' in json) else None
        self.my_chat_member = ChatMemberUpdated(json['my_chat_member']) if ('my_chat_member' in json) else None
        self.chat_member = ChatMemberUpdated(json['chat_member']) if ('chat_member' in json) else None
        self.chat_join_request = ChatJoinRequest(json['chat_join_request']) if ('chat_join_request' in json) else None


class WebhookInfo:
    """Contains information about the current status of a webhook."""
    def __init__(self, json):
        self.json = json
        self.url = str(json['url'])
        self.has_custom_certificate = bool(json['has_custom_certificate'])
        self.pending_update_count = int(json['pending_update_count'])
        self.ip_address = str(json['ip_address']) if ('ip_address' in json) else None
        self.last_error_date = int(json['last_error_date']) if ('last_error_date' in json) else None
        self.last_error_message = str(json['last_error_message']) if ('last_error_message' in json) else None
        self.last_synchronization_error_date = int(json['last_synchronization_error_date']) if ('last_synchronization_error_date' in json) else None
        self.max_connections = int(json['max_connections']) if ('max_connections' in json) else None
        self.allowed_updates = [list[str](item) for item in json['allowed_updates']] if ('allowed_updates' in json) else None


class User:
    """This object represents a Telegram user or bot."""
    def __init__(self, json):
        self.json = json
        self.id = int(json['id'])
        self.is_bot = bool(json['is_bot'])
        self.first_name = str(json['first_name'])
        self.last_name = str(json['last_name']) if ('last_name' in json) else None
        self.username = str(json['username']) if ('username' in json) else None
        self.language_code = str(json['language_code']) if ('language_code' in json) else None
        self.can_join_groups = bool(json['can_join_groups']) if ('can_join_groups' in json) else None
        self.can_read_all_group_messages = bool(json['can_read_all_group_messages']) if ('can_read_all_group_messages' in json) else None
        self.supports_inline_queries = bool(json['supports_inline_queries']) if ('supports_inline_queries' in json) else None


class Chat:
    """This object represents a chat."""
    def __init__(self, json):
        self.json = json
        self.id = int(json['id'])
        self.type = str(json['type'])
        self.title = str(json['title']) if ('title' in json) else None
        self.username = str(json['username']) if ('username' in json) else None
        self.first_name = str(json['first_name']) if ('first_name' in json) else None
        self.last_name = str(json['last_name']) if ('last_name' in json) else None
        self.photo = ChatPhoto(json['photo']) if ('photo' in json) else None
        self.bio = str(json['bio']) if ('bio' in json) else None
        self.has_private_forwards = bool(json['has_private_forwards']) if ('has_private_forwards' in json) else None
        self.description = str(json['description']) if ('description' in json) else None
        self.invite_link = str(json['invite_link']) if ('invite_link' in json) else None
        self.pinned_message = Message(json['pinned_message']) if ('pinned_message' in json) else None
        self.permissions = ChatPermissions(json['permissions']) if ('permissions' in json) else None
        self.slow_mode_delay = int(json['slow_mode_delay']) if ('slow_mode_delay' in json) else None
        self.message_auto_delete_time = int(json['message_auto_delete_time']) if ('message_auto_delete_time' in json) else None
        self.has_protected_content = bool(json['has_protected_content']) if ('has_protected_content' in json) else None
        self.sticker_set_name = str(json['sticker_set_name']) if ('sticker_set_name' in json) else None
        self.can_set_sticker_set = bool(json['can_set_sticker_set']) if ('can_set_sticker_set' in json) else None
        self.linked_chat_id = int(json['linked_chat_id']) if ('linked_chat_id' in json) else None
        self.location = ChatLocation(json['location']) if ('location' in json) else None


class Message:
    """This object represents a message."""
    def __init__(self, json):
        self.json = json
        self.message_id = int(json['message_id'])
        self.from_ = User(json['from_']) if ('from_' in json) else None
        self.sender_chat = Chat(json['sender_chat']) if ('sender_chat' in json) else None
        self.date = int(json['date'])
        self.chat = Chat(json['chat'])
        self.forward_from = User(json['forward_from']) if ('forward_from' in json) else None
        self.forward_from_chat = Chat(json['forward_from_chat']) if ('forward_from_chat' in json) else None
        self.forward_from_message_id = int(json['forward_from_message_id']) if ('forward_from_message_id' in json) else None
        self.forward_signature = str(json['forward_signature']) if ('forward_signature' in json) else None
        self.forward_sender_name = str(json['forward_sender_name']) if ('forward_sender_name' in json) else None
        self.forward_date = int(json['forward_date']) if ('forward_date' in json) else None
        self.is_automatic_forward = bool(json['is_automatic_forward']) if ('is_automatic_forward' in json) else None
        self.reply_to_message = Message(json['reply_to_message']) if ('reply_to_message' in json) else None
        self.via_bot = User(json['via_bot']) if ('via_bot' in json) else None
        self.edit_date = int(json['edit_date']) if ('edit_date' in json) else None
        self.has_protected_content = bool(json['has_protected_content']) if ('has_protected_content' in json) else None
        self.media_group_id = str(json['media_group_id']) if ('media_group_id' in json) else None
        self.author_signature = str(json['author_signature']) if ('author_signature' in json) else None
        self.text = str(json['text']) if ('text' in json) else None
        self.entities = [list[MessageEntity](item) for item in json['entities']] if ('entities' in json) else None
        self.animation = Animation(json['animation']) if ('animation' in json) else None
        self.audio = Audio(json['audio']) if ('audio' in json) else None
        self.document = Document(json['document']) if ('document' in json) else None
        self.photo = [list[PhotoSize](item) for item in json['photo']] if ('photo' in json) else None
        self.sticker = Sticker(json['sticker']) if ('sticker' in json) else None
        self.video = Video(json['video']) if ('video' in json) else None
        self.video_note = VideoNote(json['video_note']) if ('video_note' in json) else None
        self.voice = Voice(json['voice']) if ('voice' in json) else None
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None
        self.contact = Contact(json['contact']) if ('contact' in json) else None
        self.dice = Dice(json['dice']) if ('dice' in json) else None
        self.game = Game(json['game']) if ('game' in json) else None
        self.poll = Poll(json['poll']) if ('poll' in json) else None
        self.venue = Venue(json['venue']) if ('venue' in json) else None
        self.location = Location(json['location']) if ('location' in json) else None
        self.new_chat_members = [list[User](item) for item in json['new_chat_members']] if ('new_chat_members' in json) else None
        self.left_chat_member = User(json['left_chat_member']) if ('left_chat_member' in json) else None
        self.new_chat_title = str(json['new_chat_title']) if ('new_chat_title' in json) else None
        self.new_chat_photo = [list[PhotoSize](item) for item in json['new_chat_photo']] if ('new_chat_photo' in json) else None
        self.delete_chat_photo = bool(json['delete_chat_photo']) if ('delete_chat_photo' in json) else None
        self.group_chat_created = bool(json['group_chat_created']) if ('group_chat_created' in json) else None
        self.supergroup_chat_created = bool(json['supergroup_chat_created']) if ('supergroup_chat_created' in json) else None
        self.channel_chat_created = bool(json['channel_chat_created']) if ('channel_chat_created' in json) else None
        self.message_auto_delete_timer_changed = MessageAutoDeleteTimerChanged(json['message_auto_delete_timer_changed']) if ('message_auto_delete_timer_changed' in json) else None
        self.migrate_to_chat_id = int(json['migrate_to_chat_id']) if ('migrate_to_chat_id' in json) else None
        self.migrate_from_chat_id = int(json['migrate_from_chat_id']) if ('migrate_from_chat_id' in json) else None
        self.pinned_message = Message(json['pinned_message']) if ('pinned_message' in json) else None
        self.invoice = Invoice(json['invoice']) if ('invoice' in json) else None
        self.successful_payment = SuccessfulPayment(json['successful_payment']) if ('successful_payment' in json) else None
        self.connected_website = str(json['connected_website']) if ('connected_website' in json) else None
        self.passport_data = PassportData(json['passport_data']) if ('passport_data' in json) else None
        self.proximity_alert_triggered = ProximityAlertTriggered(json['proximity_alert_triggered']) if ('proximity_alert_triggered' in json) else None
        self.video_chat_scheduled = VideoChatScheduled(json['video_chat_scheduled']) if ('video_chat_scheduled' in json) else None
        self.video_chat_started = VideoChatStarted(json['video_chat_started']) if ('video_chat_started' in json) else None
        self.video_chat_ended = VideoChatEnded(json['video_chat_ended']) if ('video_chat_ended' in json) else None
        self.video_chat_participants_invited = VideoChatParticipantsInvited(json['video_chat_participants_invited']) if ('video_chat_participants_invited' in json) else None
        self.web_app_data = WebAppData(json['web_app_data']) if ('web_app_data' in json) else None
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None


class MessageId:
    """This object represents a unique message identifier."""
    def __init__(self, json):
        self.json = json
        self.message_id = int(json['message_id'])


class MessageEntity:
    """This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.offset = int(json['offset'])
        self.length = int(json['length'])
        self.url = str(json['url']) if ('url' in json) else None
        self.user = User(json['user']) if ('user' in json) else None
        self.language = str(json['language']) if ('language' in json) else None


class PhotoSize:
    """This object represents one size of a photo or a file / sticker thumbnail."""
    def __init__(self, json):
        self.json = json
        self.file_id = str(json['file_id'])
        self.file_unique_id = str(json['file_unique_id'])
        self.width = int(json['width'])
        self.height = int(json['height'])
        self.file_size = int(json['file_size']) if ('file_size' in json) else None


class Animation:
    """This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound)."""
    def __init__(self, json):
        self.json = json
        self.file_id = str(json['file_id'])
        self.file_unique_id = str(json['file_unique_id'])
        self.width = int(json['width'])
        self.height = int(json['height'])
        self.duration = int(json['duration'])
        self.thumb = PhotoSize(json['thumb']) if ('thumb' in json) else None
        self.file_name = str(json['file_name']) if ('file_name' in json) else None
        self.mime_type = str(json['mime_type']) if ('mime_type' in json) else None
        self.file_size = int(json['file_size']) if ('file_size' in json) else None


class Audio:
    """This object represents an audio file to be treated as music by the Telegram clients."""
    def __init__(self, json):
        self.json = json
        self.file_id = str(json['file_id'])
        self.file_unique_id = str(json['file_unique_id'])
        self.duration = int(json['duration'])
        self.performer = str(json['performer']) if ('performer' in json) else None
        self.title = str(json['title']) if ('title' in json) else None
        self.file_name = str(json['file_name']) if ('file_name' in json) else None
        self.mime_type = str(json['mime_type']) if ('mime_type' in json) else None
        self.file_size = int(json['file_size']) if ('file_size' in json) else None
        self.thumb = PhotoSize(json['thumb']) if ('thumb' in json) else None


class Document:
    """This object represents a general file (as opposed to photos, voice messages and audio files)."""
    def __init__(self, json):
        self.json = json
        self.file_id = str(json['file_id'])
        self.file_unique_id = str(json['file_unique_id'])
        self.thumb = PhotoSize(json['thumb']) if ('thumb' in json) else None
        self.file_name = str(json['file_name']) if ('file_name' in json) else None
        self.mime_type = str(json['mime_type']) if ('mime_type' in json) else None
        self.file_size = int(json['file_size']) if ('file_size' in json) else None


class Video:
    """This object represents a video file."""
    def __init__(self, json):
        self.json = json
        self.file_id = str(json['file_id'])
        self.file_unique_id = str(json['file_unique_id'])
        self.width = int(json['width'])
        self.height = int(json['height'])
        self.duration = int(json['duration'])
        self.thumb = PhotoSize(json['thumb']) if ('thumb' in json) else None
        self.file_name = str(json['file_name']) if ('file_name' in json) else None
        self.mime_type = str(json['mime_type']) if ('mime_type' in json) else None
        self.file_size = int(json['file_size']) if ('file_size' in json) else None


class VideoNote:
    """This object represents a video message (available in Telegram apps as of v.4.0)."""
    def __init__(self, json):
        self.json = json
        self.file_id = str(json['file_id'])
        self.file_unique_id = str(json['file_unique_id'])
        self.length = int(json['length'])
        self.duration = int(json['duration'])
        self.thumb = PhotoSize(json['thumb']) if ('thumb' in json) else None
        self.file_size = int(json['file_size']) if ('file_size' in json) else None


class Voice:
    """This object represents a voice note."""
    def __init__(self, json):
        self.json = json
        self.file_id = str(json['file_id'])
        self.file_unique_id = str(json['file_unique_id'])
        self.duration = int(json['duration'])
        self.mime_type = str(json['mime_type']) if ('mime_type' in json) else None
        self.file_size = int(json['file_size']) if ('file_size' in json) else None


class Contact:
    """This object represents a phone contact."""
    def __init__(self, json):
        self.json = json
        self.phone_number = str(json['phone_number'])
        self.first_name = str(json['first_name'])
        self.last_name = str(json['last_name']) if ('last_name' in json) else None
        self.user_id = int(json['user_id']) if ('user_id' in json) else None
        self.vcard = str(json['vcard']) if ('vcard' in json) else None


class Dice:
    """This object represents an animated emoji that displays a random value."""
    def __init__(self, json):
        self.json = json
        self.emoji = str(json['emoji'])
        self.value = int(json['value'])


class PollOption:
    """This object contains information about one answer option in a poll."""
    def __init__(self, json):
        self.json = json
        self.text = str(json['text'])
        self.voter_count = int(json['voter_count'])


class PollAnswer:
    """This object represents an answer of a user in a non-anonymous poll."""
    def __init__(self, json):
        self.json = json
        self.poll_id = str(json['poll_id'])
        self.user = User(json['user'])
        self.option_ids = [list[int](item) for item in json['option_ids']]


class Poll:
    """This object contains information about a poll."""
    def __init__(self, json):
        self.json = json
        self.id = str(json['id'])
        self.question = str(json['question'])
        self.options = [list[PollOption](item) for item in json['options']]
        self.total_voter_count = int(json['total_voter_count'])
        self.is_closed = bool(json['is_closed'])
        self.is_anonymous = bool(json['is_anonymous'])
        self.type = str(json['type'])
        self.allows_multiple_answers = bool(json['allows_multiple_answers'])
        self.correct_option_id = int(json['correct_option_id']) if ('correct_option_id' in json) else None
        self.explanation = str(json['explanation']) if ('explanation' in json) else None
        self.explanation_entities = [list[MessageEntity](item) for item in json['explanation_entities']] if ('explanation_entities' in json) else None
        self.open_period = int(json['open_period']) if ('open_period' in json) else None
        self.close_date = int(json['close_date']) if ('close_date' in json) else None


class Location:
    """This object represents a point on the map."""
    def __init__(self, json):
        self.json = json
        self.longitude = float(json['longitude'])
        self.latitude = float(json['latitude'])
        self.horizontal_accuracy = float(json['horizontal_accuracy']) if ('horizontal_accuracy' in json) else None
        self.live_period = int(json['live_period']) if ('live_period' in json) else None
        self.heading = int(json['heading']) if ('heading' in json) else None
        self.proximity_alert_radius = int(json['proximity_alert_radius']) if ('proximity_alert_radius' in json) else None


class Venue:
    """This object represents a venue."""
    def __init__(self, json):
        self.json = json
        self.location = Location(json['location'])
        self.title = str(json['title'])
        self.address = str(json['address'])
        self.foursquare_id = str(json['foursquare_id']) if ('foursquare_id' in json) else None
        self.foursquare_type = str(json['foursquare_type']) if ('foursquare_type' in json) else None
        self.google_place_id = str(json['google_place_id']) if ('google_place_id' in json) else None
        self.google_place_type = str(json['google_place_type']) if ('google_place_type' in json) else None


class WebAppData:
    """Contains data sent from a Web App to the bot."""
    def __init__(self, json):
        self.json = json
        self.data = str(json['data'])
        self.button_text = str(json['button_text'])


class ProximityAlertTriggered:
    """This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user."""
    def __init__(self, json):
        self.json = json
        self.traveler = User(json['traveler'])
        self.watcher = User(json['watcher'])
        self.distance = int(json['distance'])


class MessageAutoDeleteTimerChanged:
    """This object represents a service message about a change in auto-delete timer settings."""
    def __init__(self, json):
        self.json = json
        self.message_auto_delete_time = int(json['message_auto_delete_time'])


class VideoChatScheduled:
    """This object represents a service message about a video chat scheduled in the chat."""
    def __init__(self, json):
        self.json = json
        self.start_date = int(json['start_date'])


class VideoChatStarted:
    """This object represents a service message about a video chat started in the chat. Currently holds no information."""
    def __init__(self, json):
        self.json = json
        


class VideoChatEnded:
    """This object represents a service message about a video chat ended in the chat."""
    def __init__(self, json):
        self.json = json
        self.duration = int(json['duration'])


class VideoChatParticipantsInvited:
    """This object represents a service message about new members invited to a video chat."""
    def __init__(self, json):
        self.json = json
        self.users = [list[User](item) for item in json['users']]


class UserProfilePhotos:
    """This object represent a user's profile pictures."""
    def __init__(self, json):
        self.json = json
        self.total_count = int(json['total_count'])
        self.photos = [[list[list[PhotoSize]](item) for item in arr] for arr in json['photos']]


class File:
    """This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile."""
    def __init__(self, json):
        self.json = json
        


class WebAppInfo:
    """Contains information about a Web App."""
    def __init__(self, json):
        self.json = json
        self.url = str(json['url'])


class ReplyKeyboardMarkup:
    """This object represents a custom keyboard with reply options (see Introduction to bots for details and examples)."""
    def __init__(self, json):
        self.json = json
        self.keyboard = [[list[list[KeyboardButton]](item) for item in arr] for arr in json['keyboard']]
        self.resize_keyboard = bool(json['resize_keyboard']) if ('resize_keyboard' in json) else None
        self.one_time_keyboard = bool(json['one_time_keyboard']) if ('one_time_keyboard' in json) else None
        self.input_field_placeholder = str(json['input_field_placeholder']) if ('input_field_placeholder' in json) else None
        self.selective = bool(json['selective']) if ('selective' in json) else None


class KeyboardButton:
    """This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields web_app, request_contact, request_location, and request_poll are mutually exclusive."""
    def __init__(self, json):
        self.json = json
        self.text = str(json['text'])
        self.request_contact = bool(json['request_contact']) if ('request_contact' in json) else None
        self.request_location = bool(json['request_location']) if ('request_location' in json) else None
        self.request_poll = KeyboardButtonPollType(json['request_poll']) if ('request_poll' in json) else None
        self.web_app = WebAppInfo(json['web_app']) if ('web_app' in json) else None


class KeyboardButtonPollType:
    """This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type']) if ('type' in json) else None


class ReplyKeyboardRemove:
    """Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup)."""
    def __init__(self, json):
        self.json = json
        self.remove_keyboard = bool(json['remove_keyboard'])
        self.selective = bool(json['selective']) if ('selective' in json) else None


class InlineKeyboardMarkup:
    """This object represents an inline keyboard that appears right next to the message it belongs to."""
    def __init__(self, json):
        self.json = json
        self.inline_keyboard = [[list[list[InlineKeyboardButton]](item) for item in arr] for arr in json['inline_keyboard']]


class InlineKeyboardButton:
    """This object represents one button of an inline keyboard. You must use exactly one of the optional fields."""
    def __init__(self, json):
        self.json = json
        self.text = str(json['text'])
        self.url = str(json['url']) if ('url' in json) else None
        self.callback_data = str(json['callback_data']) if ('callback_data' in json) else None
        self.web_app = WebAppInfo(json['web_app']) if ('web_app' in json) else None
        self.login_url = LoginUrl(json['login_url']) if ('login_url' in json) else None
        self.switch_inline_query = str(json['switch_inline_query']) if ('switch_inline_query' in json) else None
        self.switch_inline_query_current_chat = str(json['switch_inline_query_current_chat']) if ('switch_inline_query_current_chat' in json) else None
        self.callback_game = CallbackGame(json['callback_game']) if ('callback_game' in json) else None
        self.pay = bool(json['pay']) if ('pay' in json) else None


class LoginUrl:
    """This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:"""
    def __init__(self, json):
        self.json = json
        


class CallbackQuery:
    """This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present."""
    def __init__(self, json):
        self.json = json
        self.id = str(json['id'])
        self.from_ = User(json['from_'])
        self.message = Message(json['message']) if ('message' in json) else None
        self.inline_message_id = str(json['inline_message_id']) if ('inline_message_id' in json) else None
        self.chat_instance = str(json['chat_instance'])
        self.data = str(json['data']) if ('data' in json) else None
        self.game_short_name = str(json['game_short_name']) if ('game_short_name' in json) else None


class ForceReply:
    """Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode."""
    def __init__(self, json):
        self.json = json
        self.force_reply = bool(json['force_reply'])
        self.input_field_placeholder = str(json['input_field_placeholder']) if ('input_field_placeholder' in json) else None
        self.selective = bool(json['selective']) if ('selective' in json) else None


class ChatPhoto:
    """This object represents a chat photo."""
    def __init__(self, json):
        self.json = json
        self.small_file_id = str(json['small_file_id'])
        self.small_file_unique_id = str(json['small_file_unique_id'])
        self.big_file_id = str(json['big_file_id'])
        self.big_file_unique_id = str(json['big_file_unique_id'])


class ChatInviteLink:
    """Represents an invite link for a chat."""
    def __init__(self, json):
        self.json = json
        self.invite_link = str(json['invite_link'])
        self.creator = User(json['creator'])
        self.creates_join_request = bool(json['creates_join_request'])
        self.is_primary = bool(json['is_primary'])
        self.is_revoked = bool(json['is_revoked'])
        self.name = str(json['name']) if ('name' in json) else None
        self.expire_date = int(json['expire_date']) if ('expire_date' in json) else None
        self.member_limit = int(json['member_limit']) if ('member_limit' in json) else None
        self.pending_join_request_count = int(json['pending_join_request_count']) if ('pending_join_request_count' in json) else None


class ChatAdministratorRights:
    """Represents the rights of an administrator in a chat."""
    def __init__(self, json):
        self.json = json
        self.is_anonymous = bool(json['is_anonymous'])
        self.can_manage_chat = bool(json['can_manage_chat'])
        self.can_delete_messages = bool(json['can_delete_messages'])
        self.can_manage_video_chats = bool(json['can_manage_video_chats'])
        self.can_restrict_members = bool(json['can_restrict_members'])
        self.can_promote_members = bool(json['can_promote_members'])
        self.can_change_info = bool(json['can_change_info'])
        self.can_invite_users = bool(json['can_invite_users'])
        self.can_post_messages = bool(json['can_post_messages']) if ('can_post_messages' in json) else None
        self.can_edit_messages = bool(json['can_edit_messages']) if ('can_edit_messages' in json) else None
        self.can_pin_messages = bool(json['can_pin_messages']) if ('can_pin_messages' in json) else None


class ChatMember:
    """This object contains information about one member of a chat. Currently, the following 6 types of chat members are supported:"""
    def __init__(self, json):
        self.json = json
        


class ChatMemberOwner:
    """Represents a chat member that owns the chat and has all administrator privileges."""
    def __init__(self, json):
        self.json = json
        self.status = str(json['status'])
        self.user = User(json['user'])
        self.is_anonymous = bool(json['is_anonymous'])
        self.custom_title = str(json['custom_title']) if ('custom_title' in json) else None


class ChatMemberAdministrator:
    """Represents a chat member that has some additional privileges."""
    def __init__(self, json):
        self.json = json
        self.status = str(json['status'])
        self.user = User(json['user'])
        self.can_be_edited = bool(json['can_be_edited'])
        self.is_anonymous = bool(json['is_anonymous'])
        self.can_manage_chat = bool(json['can_manage_chat'])
        self.can_delete_messages = bool(json['can_delete_messages'])
        self.can_manage_video_chats = bool(json['can_manage_video_chats'])
        self.can_restrict_members = bool(json['can_restrict_members'])
        self.can_promote_members = bool(json['can_promote_members'])
        self.can_change_info = bool(json['can_change_info'])
        self.can_invite_users = bool(json['can_invite_users'])
        self.can_post_messages = bool(json['can_post_messages']) if ('can_post_messages' in json) else None
        self.can_edit_messages = bool(json['can_edit_messages']) if ('can_edit_messages' in json) else None
        self.can_pin_messages = bool(json['can_pin_messages']) if ('can_pin_messages' in json) else None
        self.custom_title = str(json['custom_title']) if ('custom_title' in json) else None


class ChatMemberMember:
    """Represents a chat member that has no additional privileges or restrictions."""
    def __init__(self, json):
        self.json = json
        self.status = str(json['status'])
        self.user = User(json['user'])


class ChatMemberRestricted:
    """Represents a chat member that is under certain restrictions in the chat. Supergroups only."""
    def __init__(self, json):
        self.json = json
        self.status = str(json['status'])
        self.user = User(json['user'])
        self.is_member = bool(json['is_member'])
        self.can_change_info = bool(json['can_change_info'])
        self.can_invite_users = bool(json['can_invite_users'])
        self.can_pin_messages = bool(json['can_pin_messages'])
        self.can_send_messages = bool(json['can_send_messages'])
        self.can_send_media_messages = bool(json['can_send_media_messages'])
        self.can_send_polls = bool(json['can_send_polls'])
        self.can_send_other_messages = bool(json['can_send_other_messages'])
        self.can_add_web_page_previews = bool(json['can_add_web_page_previews'])
        self.until_date = int(json['until_date'])


class ChatMemberLeft:
    """Represents a chat member that isn't currently a member of the chat, but may join it themselves."""
    def __init__(self, json):
        self.json = json
        self.status = str(json['status'])
        self.user = User(json['user'])


class ChatMemberBanned:
    """Represents a chat member that was banned in the chat and can't return to the chat or view chat messages."""
    def __init__(self, json):
        self.json = json
        self.status = str(json['status'])
        self.user = User(json['user'])
        self.until_date = int(json['until_date'])


class ChatMemberUpdated:
    """This object represents changes in the status of a chat member."""
    def __init__(self, json):
        self.json = json
        self.chat = Chat(json['chat'])
        self.from_ = User(json['from_'])
        self.date = int(json['date'])
        self.old_chat_member = ChatMember(json['old_chat_member'])
        self.new_chat_member = ChatMember(json['new_chat_member'])
        self.invite_link = ChatInviteLink(json['invite_link']) if ('invite_link' in json) else None


class ChatJoinRequest:
    """Represents a join request sent to a chat."""
    def __init__(self, json):
        self.json = json
        self.chat = Chat(json['chat'])
        self.from_ = User(json['from_'])
        self.date = int(json['date'])
        self.bio = str(json['bio']) if ('bio' in json) else None
        self.invite_link = ChatInviteLink(json['invite_link']) if ('invite_link' in json) else None


class ChatPermissions:
    """Describes actions that a non-administrator user is allowed to take in a chat."""
    def __init__(self, json):
        self.json = json
        self.can_send_messages = bool(json['can_send_messages']) if ('can_send_messages' in json) else None
        self.can_send_media_messages = bool(json['can_send_media_messages']) if ('can_send_media_messages' in json) else None
        self.can_send_polls = bool(json['can_send_polls']) if ('can_send_polls' in json) else None
        self.can_send_other_messages = bool(json['can_send_other_messages']) if ('can_send_other_messages' in json) else None
        self.can_add_web_page_previews = bool(json['can_add_web_page_previews']) if ('can_add_web_page_previews' in json) else None
        self.can_change_info = bool(json['can_change_info']) if ('can_change_info' in json) else None
        self.can_invite_users = bool(json['can_invite_users']) if ('can_invite_users' in json) else None
        self.can_pin_messages = bool(json['can_pin_messages']) if ('can_pin_messages' in json) else None


class ChatLocation:
    """Represents a location to which a chat is connected."""
    def __init__(self, json):
        self.json = json
        self.location = Location(json['location'])
        self.address = str(json['address'])


class BotCommand:
    """This object represents a bot command."""
    def __init__(self, json):
        self.json = json
        self.command = str(json['command'])
        self.description = str(json['description'])


class BotCommandScope:
    """This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:"""
    def __init__(self, json):
        self.json = json
        


class BotCommandScopeDefault:
    """Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])


class BotCommandScopeAllPrivateChats:
    """Represents the scope of bot commands, covering all private chats."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])


class BotCommandScopeAllGroupChats:
    """Represents the scope of bot commands, covering all group and supergroup chats."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])


class BotCommandScopeAllChatAdministrators:
    """Represents the scope of bot commands, covering all group and supergroup chat administrators."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])


class BotCommandScopeChat:
    """Represents the scope of bot commands, covering a specific chat."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.chat_id = int | str(json['chat_id'])


class BotCommandScopeChatAdministrators:
    """Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.chat_id = int | str(json['chat_id'])


class BotCommandScopeChatMember:
    """Represents the scope of bot commands, covering a specific member of a group or supergroup chat."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.chat_id = int | str(json['chat_id'])
        self.user_id = int(json['user_id'])


class MenuButton:
    """This object describes the bot's menu button in a private chat. It should be one of"""
    def __init__(self, json):
        self.json = json
        


class MenuButtonCommands:
    """Represents a menu button, which opens the bot's list of commands."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])


class MenuButtonWebApp:
    """Represents a menu button, which launches a Web App."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.text = str(json['text'])
        self.web_app = WebAppInfo(json['web_app'])


class MenuButtonDefault:
    """Describes that no specific value for the menu button was set."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])


class ResponseParameters:
    """Contains information about why a request was unsuccessful."""
    def __init__(self, json):
        self.json = json
        self.migrate_to_chat_id = int(json['migrate_to_chat_id']) if ('migrate_to_chat_id' in json) else None
        self.retry_after = int(json['retry_after']) if ('retry_after' in json) else None


class InputMedia:
    """This object represents the content of a media message to be sent. It should be one of"""
    def __init__(self, json):
        self.json = json
        


class InputMediaPhoto:
    """Represents a photo to be sent."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.media = str(json['media'])
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None


class InputMediaVideo:
    """Represents a video to be sent."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.media = str(json['media'])
        self.thumb = InputFile | str(json['thumb']) if ('thumb' in json) else None
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None
        self.width = int(json['width']) if ('width' in json) else None
        self.height = int(json['height']) if ('height' in json) else None
        self.duration = int(json['duration']) if ('duration' in json) else None
        self.supports_streaming = bool(json['supports_streaming']) if ('supports_streaming' in json) else None


class InputMediaAnimation:
    """Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.media = str(json['media'])
        self.thumb = InputFile | str(json['thumb']) if ('thumb' in json) else None
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None
        self.width = int(json['width']) if ('width' in json) else None
        self.height = int(json['height']) if ('height' in json) else None
        self.duration = int(json['duration']) if ('duration' in json) else None


class InputMediaAudio:
    """Represents an audio file to be treated as music to be sent."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.media = str(json['media'])
        self.thumb = InputFile | str(json['thumb']) if ('thumb' in json) else None
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None
        self.duration = int(json['duration']) if ('duration' in json) else None
        self.performer = str(json['performer']) if ('performer' in json) else None
        self.title = str(json['title']) if ('title' in json) else None


class InputMediaDocument:
    """Represents a general file to be sent."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.media = str(json['media'])
        self.thumb = InputFile | str(json['thumb']) if ('thumb' in json) else None
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None
        self.disable_content_type_detection = bool(json['disable_content_type_detection']) if ('disable_content_type_detection' in json) else None


class InputFile:
    """This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser."""
    def __init__(self, json):
        self.json = json
        


class Sticker:
    """This object represents a sticker."""
    def __init__(self, json):
        self.json = json
        self.file_id = str(json['file_id'])
        self.file_unique_id = str(json['file_unique_id'])
        self.width = int(json['width'])
        self.height = int(json['height'])
        self.is_animated = bool(json['is_animated'])
        self.is_video = bool(json['is_video'])
        self.thumb = PhotoSize(json['thumb']) if ('thumb' in json) else None
        self.emoji = str(json['emoji']) if ('emoji' in json) else None
        self.set_name = str(json['set_name']) if ('set_name' in json) else None
        self.mask_position = MaskPosition(json['mask_position']) if ('mask_position' in json) else None
        self.file_size = int(json['file_size']) if ('file_size' in json) else None


class StickerSet:
    """This object represents a sticker set."""
    def __init__(self, json):
        self.json = json
        self.name = str(json['name'])
        self.title = str(json['title'])
        self.is_animated = bool(json['is_animated'])
        self.is_video = bool(json['is_video'])
        self.contains_masks = bool(json['contains_masks'])
        self.stickers = [list[Sticker](item) for item in json['stickers']]
        self.thumb = PhotoSize(json['thumb']) if ('thumb' in json) else None


class MaskPosition:
    """This object describes the position on faces where a mask should be placed by default."""
    def __init__(self, json):
        self.json = json
        self.point = str(json['point'])
        self.x_shift = float(json['x_shift'])
        self.y_shift = float(json['y_shift'])
        self.scale = float(json['scale'])


class InlineQuery:
    """This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results."""
    def __init__(self, json):
        self.json = json
        self.id = str(json['id'])
        self.from_ = User(json['from_'])
        self.query = str(json['query'])
        self.offset = str(json['offset'])
        self.chat_type = str(json['chat_type']) if ('chat_type' in json) else None
        self.location = Location(json['location']) if ('location' in json) else None


class InlineQueryResult:
    """This object represents one result of an inline query. Telegram clients currently support results of the following 20 types:"""
    def __init__(self, json):
        self.json = json
        


class InlineQueryResultArticle:
    """Represents a link to an article or web page."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.title = str(json['title'])
        self.input_message_content = InputMessageContent(json['input_message_content'])
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None
        self.url = str(json['url']) if ('url' in json) else None
        self.hide_url = bool(json['hide_url']) if ('hide_url' in json) else None
        self.description = str(json['description']) if ('description' in json) else None
        self.thumb_url = str(json['thumb_url']) if ('thumb_url' in json) else None
        self.thumb_width = int(json['thumb_width']) if ('thumb_width' in json) else None
        self.thumb_height = int(json['thumb_height']) if ('thumb_height' in json) else None


class InlineQueryResultPhoto:
    """Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.photo_url = str(json['photo_url'])
        self.thumb_url = str(json['thumb_url'])
        self.photo_width = int(json['photo_width']) if ('photo_width' in json) else None
        self.photo_height = int(json['photo_height']) if ('photo_height' in json) else None
        self.title = str(json['title']) if ('title' in json) else None
        self.description = str(json['description']) if ('description' in json) else None
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None
        self.input_message_content = InputMessageContent(json['input_message_content']) if ('input_message_content' in json) else None


class InlineQueryResultGif:
    """Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.gif_url = str(json['gif_url'])
        self.gif_width = int(json['gif_width']) if ('gif_width' in json) else None
        self.gif_height = int(json['gif_height']) if ('gif_height' in json) else None
        self.gif_duration = int(json['gif_duration']) if ('gif_duration' in json) else None
        self.thumb_url = str(json['thumb_url'])
        self.thumb_mime_type = str(json['thumb_mime_type']) if ('thumb_mime_type' in json) else None
        self.title = str(json['title']) if ('title' in json) else None
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None
        self.input_message_content = InputMessageContent(json['input_message_content']) if ('input_message_content' in json) else None


class InlineQueryResultMpeg4Gif:
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.mpeg4_url = str(json['mpeg4_url'])
        self.mpeg4_width = int(json['mpeg4_width']) if ('mpeg4_width' in json) else None
        self.mpeg4_height = int(json['mpeg4_height']) if ('mpeg4_height' in json) else None
        self.mpeg4_duration = int(json['mpeg4_duration']) if ('mpeg4_duration' in json) else None
        self.thumb_url = str(json['thumb_url'])
        self.thumb_mime_type = str(json['thumb_mime_type']) if ('thumb_mime_type' in json) else None
        self.title = str(json['title']) if ('title' in json) else None
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None
        self.input_message_content = InputMessageContent(json['input_message_content']) if ('input_message_content' in json) else None


class InlineQueryResultVideo:
    """Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video."""
    def __init__(self, json):
        self.json = json
        


class InlineQueryResultAudio:
    """Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.audio_url = str(json['audio_url'])
        self.title = str(json['title'])
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None
        self.performer = str(json['performer']) if ('performer' in json) else None
        self.audio_duration = int(json['audio_duration']) if ('audio_duration' in json) else None
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None
        self.input_message_content = InputMessageContent(json['input_message_content']) if ('input_message_content' in json) else None


class InlineQueryResultVoice:
    """Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.voice_url = str(json['voice_url'])
        self.title = str(json['title'])
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None
        self.voice_duration = int(json['voice_duration']) if ('voice_duration' in json) else None
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None
        self.input_message_content = InputMessageContent(json['input_message_content']) if ('input_message_content' in json) else None


class InlineQueryResultDocument:
    """Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.title = str(json['title'])
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None
        self.document_url = str(json['document_url'])
        self.mime_type = str(json['mime_type'])
        self.description = str(json['description']) if ('description' in json) else None
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None
        self.input_message_content = InputMessageContent(json['input_message_content']) if ('input_message_content' in json) else None
        self.thumb_url = str(json['thumb_url']) if ('thumb_url' in json) else None
        self.thumb_width = int(json['thumb_width']) if ('thumb_width' in json) else None
        self.thumb_height = int(json['thumb_height']) if ('thumb_height' in json) else None


class InlineQueryResultLocation:
    """Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.latitude = float(json['latitude'])
        self.longitude = float(json['longitude'])
        self.title = str(json['title'])
        self.horizontal_accuracy = float(json['horizontal_accuracy']) if ('horizontal_accuracy' in json) else None
        self.live_period = int(json['live_period']) if ('live_period' in json) else None
        self.heading = int(json['heading']) if ('heading' in json) else None
        self.proximity_alert_radius = int(json['proximity_alert_radius']) if ('proximity_alert_radius' in json) else None
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None
        self.input_message_content = InputMessageContent(json['input_message_content']) if ('input_message_content' in json) else None
        self.thumb_url = str(json['thumb_url']) if ('thumb_url' in json) else None
        self.thumb_width = int(json['thumb_width']) if ('thumb_width' in json) else None
        self.thumb_height = int(json['thumb_height']) if ('thumb_height' in json) else None


class InlineQueryResultVenue:
    """Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.latitude = float(json['latitude'])
        self.longitude = float(json['longitude'])
        self.title = str(json['title'])
        self.address = str(json['address'])
        self.foursquare_id = str(json['foursquare_id']) if ('foursquare_id' in json) else None
        self.foursquare_type = str(json['foursquare_type']) if ('foursquare_type' in json) else None
        self.google_place_id = str(json['google_place_id']) if ('google_place_id' in json) else None
        self.google_place_type = str(json['google_place_type']) if ('google_place_type' in json) else None
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None
        self.input_message_content = InputMessageContent(json['input_message_content']) if ('input_message_content' in json) else None
        self.thumb_url = str(json['thumb_url']) if ('thumb_url' in json) else None
        self.thumb_width = int(json['thumb_width']) if ('thumb_width' in json) else None
        self.thumb_height = int(json['thumb_height']) if ('thumb_height' in json) else None


class InlineQueryResultContact:
    """Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.phone_number = str(json['phone_number'])
        self.first_name = str(json['first_name'])
        self.last_name = str(json['last_name']) if ('last_name' in json) else None
        self.vcard = str(json['vcard']) if ('vcard' in json) else None
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None
        self.input_message_content = InputMessageContent(json['input_message_content']) if ('input_message_content' in json) else None
        self.thumb_url = str(json['thumb_url']) if ('thumb_url' in json) else None
        self.thumb_width = int(json['thumb_width']) if ('thumb_width' in json) else None
        self.thumb_height = int(json['thumb_height']) if ('thumb_height' in json) else None


class InlineQueryResultGame:
    """Represents a Game."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.game_short_name = str(json['game_short_name'])
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None


class InlineQueryResultCachedPhoto:
    """Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.photo_file_id = str(json['photo_file_id'])
        self.title = str(json['title']) if ('title' in json) else None
        self.description = str(json['description']) if ('description' in json) else None
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None
        self.input_message_content = InputMessageContent(json['input_message_content']) if ('input_message_content' in json) else None


class InlineQueryResultCachedGif:
    """Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.gif_file_id = str(json['gif_file_id'])
        self.title = str(json['title']) if ('title' in json) else None
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None
        self.input_message_content = InputMessageContent(json['input_message_content']) if ('input_message_content' in json) else None


class InlineQueryResultCachedMpeg4Gif:
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.mpeg4_file_id = str(json['mpeg4_file_id'])
        self.title = str(json['title']) if ('title' in json) else None
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None
        self.input_message_content = InputMessageContent(json['input_message_content']) if ('input_message_content' in json) else None


class InlineQueryResultCachedSticker:
    """Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.sticker_file_id = str(json['sticker_file_id'])
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None
        self.input_message_content = InputMessageContent(json['input_message_content']) if ('input_message_content' in json) else None


class InlineQueryResultCachedDocument:
    """Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.title = str(json['title'])
        self.document_file_id = str(json['document_file_id'])
        self.description = str(json['description']) if ('description' in json) else None
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None
        self.input_message_content = InputMessageContent(json['input_message_content']) if ('input_message_content' in json) else None


class InlineQueryResultCachedVideo:
    """Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.video_file_id = str(json['video_file_id'])
        self.title = str(json['title'])
        self.description = str(json['description']) if ('description' in json) else None
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None
        self.input_message_content = InputMessageContent(json['input_message_content']) if ('input_message_content' in json) else None


class InlineQueryResultCachedVoice:
    """Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.voice_file_id = str(json['voice_file_id'])
        self.title = str(json['title'])
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None
        self.input_message_content = InputMessageContent(json['input_message_content']) if ('input_message_content' in json) else None


class InlineQueryResultCachedAudio:
    """Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.id = str(json['id'])
        self.audio_file_id = str(json['audio_file_id'])
        self.caption = str(json['caption']) if ('caption' in json) else None
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.caption_entities = [list[MessageEntity](item) for item in json['caption_entities']] if ('caption_entities' in json) else None
        self.reply_markup = InlineKeyboardMarkup(json['reply_markup']) if ('reply_markup' in json) else None
        self.input_message_content = InputMessageContent(json['input_message_content']) if ('input_message_content' in json) else None


class InputMessageContent:
    """This object represents the content of a message to be sent as a result of an inline query. Telegram clients currently support the following 5 types:"""
    def __init__(self, json):
        self.json = json
        


class InputTextMessageContent:
    """Represents the content of a text message to be sent as the result of an inline query."""
    def __init__(self, json):
        self.json = json
        self.message_text = str(json['message_text'])
        self.parse_mode = str(json['parse_mode']) if ('parse_mode' in json) else None
        self.entities = [list[MessageEntity](item) for item in json['entities']] if ('entities' in json) else None
        self.disable_web_page_preview = bool(json['disable_web_page_preview']) if ('disable_web_page_preview' in json) else None


class InputLocationMessageContent:
    """Represents the content of a location message to be sent as the result of an inline query."""
    def __init__(self, json):
        self.json = json
        self.latitude = float(json['latitude'])
        self.longitude = float(json['longitude'])
        self.horizontal_accuracy = float(json['horizontal_accuracy']) if ('horizontal_accuracy' in json) else None
        self.live_period = int(json['live_period']) if ('live_period' in json) else None
        self.heading = int(json['heading']) if ('heading' in json) else None
        self.proximity_alert_radius = int(json['proximity_alert_radius']) if ('proximity_alert_radius' in json) else None


class InputVenueMessageContent:
    """Represents the content of a venue message to be sent as the result of an inline query."""
    def __init__(self, json):
        self.json = json
        self.latitude = float(json['latitude'])
        self.longitude = float(json['longitude'])
        self.title = str(json['title'])
        self.address = str(json['address'])
        self.foursquare_id = str(json['foursquare_id']) if ('foursquare_id' in json) else None
        self.foursquare_type = str(json['foursquare_type']) if ('foursquare_type' in json) else None
        self.google_place_id = str(json['google_place_id']) if ('google_place_id' in json) else None
        self.google_place_type = str(json['google_place_type']) if ('google_place_type' in json) else None


class InputContactMessageContent:
    """Represents the content of a contact message to be sent as the result of an inline query."""
    def __init__(self, json):
        self.json = json
        self.phone_number = str(json['phone_number'])
        self.first_name = str(json['first_name'])
        self.last_name = str(json['last_name']) if ('last_name' in json) else None
        self.vcard = str(json['vcard']) if ('vcard' in json) else None


class InputInvoiceMessageContent:
    """Represents the content of an invoice message to be sent as the result of an inline query."""
    def __init__(self, json):
        self.json = json
        self.title = str(json['title'])
        self.description = str(json['description'])
        self.payload = str(json['payload'])
        self.provider_token = str(json['provider_token'])
        self.currency = str(json['currency'])
        self.prices = [list[LabeledPrice](item) for item in json['prices']]
        self.max_tip_amount = int(json['max_tip_amount']) if ('max_tip_amount' in json) else None
        self.suggested_tip_amounts = [list[int](item) for item in json['suggested_tip_amounts']] if ('suggested_tip_amounts' in json) else None
        self.provider_data = str(json['provider_data']) if ('provider_data' in json) else None
        self.photo_url = str(json['photo_url']) if ('photo_url' in json) else None
        self.photo_size = int(json['photo_size']) if ('photo_size' in json) else None
        self.photo_width = int(json['photo_width']) if ('photo_width' in json) else None
        self.photo_height = int(json['photo_height']) if ('photo_height' in json) else None
        self.need_name = bool(json['need_name']) if ('need_name' in json) else None
        self.need_phone_number = bool(json['need_phone_number']) if ('need_phone_number' in json) else None
        self.need_email = bool(json['need_email']) if ('need_email' in json) else None
        self.need_shipping_address = bool(json['need_shipping_address']) if ('need_shipping_address' in json) else None
        self.send_phone_number_to_provider = bool(json['send_phone_number_to_provider']) if ('send_phone_number_to_provider' in json) else None
        self.send_email_to_provider = bool(json['send_email_to_provider']) if ('send_email_to_provider' in json) else None
        self.is_flexible = bool(json['is_flexible']) if ('is_flexible' in json) else None


class ChosenInlineResult:
    """Represents a result of an inline query that was chosen by the user and sent to their chat partner."""
    def __init__(self, json):
        self.json = json
        self.result_id = str(json['result_id'])
        self.from_ = User(json['from_'])
        self.location = Location(json['location']) if ('location' in json) else None
        self.inline_message_id = str(json['inline_message_id']) if ('inline_message_id' in json) else None
        self.query = str(json['query'])


class SentWebAppMessage:
    """Contains information about an inline message sent by a Web App on behalf of a user."""
    def __init__(self, json):
        self.json = json
        self.inline_message_id = str(json['inline_message_id']) if ('inline_message_id' in json) else None


class LabeledPrice:
    """This object represents a portion of the price for goods or services."""
    def __init__(self, json):
        self.json = json
        self.label = str(json['label'])
        self.amount = int(json['amount'])


class Invoice:
    """This object contains basic information about an invoice."""
    def __init__(self, json):
        self.json = json
        self.title = str(json['title'])
        self.description = str(json['description'])
        self.start_parameter = str(json['start_parameter'])
        self.currency = str(json['currency'])
        self.total_amount = int(json['total_amount'])


class ShippingAddress:
    """This object represents a shipping address."""
    def __init__(self, json):
        self.json = json
        self.country_code = str(json['country_code'])
        self.state = str(json['state'])
        self.city = str(json['city'])
        self.street_line1 = str(json['street_line1'])
        self.street_line2 = str(json['street_line2'])
        self.post_code = str(json['post_code'])


class OrderInfo:
    """This object represents information about an order."""
    def __init__(self, json):
        self.json = json
        self.name = str(json['name']) if ('name' in json) else None
        self.phone_number = str(json['phone_number']) if ('phone_number' in json) else None
        self.email = str(json['email']) if ('email' in json) else None
        self.shipping_address = ShippingAddress(json['shipping_address']) if ('shipping_address' in json) else None


class ShippingOption:
    """This object represents one shipping option."""
    def __init__(self, json):
        self.json = json
        self.id = str(json['id'])
        self.title = str(json['title'])
        self.prices = [list[LabeledPrice](item) for item in json['prices']]


class SuccessfulPayment:
    """This object contains basic information about a successful payment."""
    def __init__(self, json):
        self.json = json
        self.currency = str(json['currency'])
        self.total_amount = int(json['total_amount'])
        self.invoice_payload = str(json['invoice_payload'])
        self.shipping_option_id = str(json['shipping_option_id']) if ('shipping_option_id' in json) else None
        self.order_info = OrderInfo(json['order_info']) if ('order_info' in json) else None
        self.telegram_payment_charge_id = str(json['telegram_payment_charge_id'])
        self.provider_payment_charge_id = str(json['provider_payment_charge_id'])


class ShippingQuery:
    """This object contains information about an incoming shipping query."""
    def __init__(self, json):
        self.json = json
        self.id = str(json['id'])
        self.from_ = User(json['from_'])
        self.invoice_payload = str(json['invoice_payload'])
        self.shipping_address = ShippingAddress(json['shipping_address'])


class PreCheckoutQuery:
    """This object contains information about an incoming pre-checkout query."""
    def __init__(self, json):
        self.json = json
        self.id = str(json['id'])
        self.from_ = User(json['from_'])
        self.currency = str(json['currency'])
        self.total_amount = int(json['total_amount'])
        self.invoice_payload = str(json['invoice_payload'])
        self.shipping_option_id = str(json['shipping_option_id']) if ('shipping_option_id' in json) else None
        self.order_info = OrderInfo(json['order_info']) if ('order_info' in json) else None


class PassportData:
    """Contains information about Telegram Passport data shared with the bot by the user."""
    def __init__(self, json):
        self.json = json
        self.data = [list[EncryptedPassportElement](item) for item in json['data']]
        self.credentials = EncryptedCredentials(json['credentials'])


class PassportFile:
    """This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB."""
    def __init__(self, json):
        self.json = json
        self.file_id = str(json['file_id'])
        self.file_unique_id = str(json['file_unique_id'])
        self.file_size = int(json['file_size'])
        self.file_date = int(json['file_date'])


class EncryptedPassportElement:
    """Contains information about documents or other Telegram Passport elements shared with the bot by the user."""
    def __init__(self, json):
        self.json = json
        self.type = str(json['type'])
        self.data = str(json['data']) if ('data' in json) else None
        self.phone_number = str(json['phone_number']) if ('phone_number' in json) else None
        self.email = str(json['email']) if ('email' in json) else None
        self.files = [list[PassportFile](item) for item in json['files']] if ('files' in json) else None
        self.front_side = PassportFile(json['front_side']) if ('front_side' in json) else None
        self.reverse_side = PassportFile(json['reverse_side']) if ('reverse_side' in json) else None
        self.selfie = PassportFile(json['selfie']) if ('selfie' in json) else None
        self.translation = [list[PassportFile](item) for item in json['translation']] if ('translation' in json) else None
        self.hash = str(json['hash'])


class EncryptedCredentials:
    """Contains data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes."""
    def __init__(self, json):
        self.json = json
        self.data = str(json['data'])
        self.hash = str(json['hash'])
        self.secret = str(json['secret'])


class PassportElementError:
    """This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user. It should be one of:"""
    def __init__(self, json):
        self.json = json
        


class PassportElementErrorDataField:
    """Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes."""
    def __init__(self, json):
        self.json = json
        self.source = str(json['source'])
        self.type = str(json['type'])
        self.field_name = str(json['field_name'])
        self.data_hash = str(json['data_hash'])
        self.message = str(json['message'])


class PassportElementErrorFrontSide:
    """Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes."""
    def __init__(self, json):
        self.json = json
        self.source = str(json['source'])
        self.type = str(json['type'])
        self.file_hash = str(json['file_hash'])
        self.message = str(json['message'])


class PassportElementErrorReverseSide:
    """Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes."""
    def __init__(self, json):
        self.json = json
        self.source = str(json['source'])
        self.type = str(json['type'])
        self.file_hash = str(json['file_hash'])
        self.message = str(json['message'])


class PassportElementErrorSelfie:
    """Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes."""
    def __init__(self, json):
        self.json = json
        self.source = str(json['source'])
        self.type = str(json['type'])
        self.file_hash = str(json['file_hash'])
        self.message = str(json['message'])


class PassportElementErrorFile:
    """Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes."""
    def __init__(self, json):
        self.json = json
        self.source = str(json['source'])
        self.type = str(json['type'])
        self.file_hash = str(json['file_hash'])
        self.message = str(json['message'])


class PassportElementErrorFiles:
    """Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes."""
    def __init__(self, json):
        self.json = json
        self.source = str(json['source'])
        self.type = str(json['type'])
        self.file_hashes = [list[str](item) for item in json['file_hashes']]
        self.message = str(json['message'])


class PassportElementErrorTranslationFile:
    """Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes."""
    def __init__(self, json):
        self.json = json
        self.source = str(json['source'])
        self.type = str(json['type'])
        self.file_hash = str(json['file_hash'])
        self.message = str(json['message'])


class PassportElementErrorTranslationFiles:
    """Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change."""
    def __init__(self, json):
        self.json = json
        self.source = str(json['source'])
        self.type = str(json['type'])
        self.file_hashes = [list[str](item) for item in json['file_hashes']]
        self.message = str(json['message'])


class PassportElementErrorUnspecified:
    """Represents an issue in an unspecified place. The error is considered resolved when new data is added."""
    def __init__(self, json):
        self.json = json
        self.source = str(json['source'])
        self.type = str(json['type'])
        self.element_hash = str(json['element_hash'])
        self.message = str(json['message'])


class Game:
    """This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers."""
    def __init__(self, json):
        self.json = json
        self.title = str(json['title'])
        self.description = str(json['description'])
        self.photo = [list[PhotoSize](item) for item in json['photo']]
        self.text = str(json['text']) if ('text' in json) else None
        self.text_entities = [list[MessageEntity](item) for item in json['text_entities']] if ('text_entities' in json) else None
        self.animation = Animation(json['animation']) if ('animation' in json) else None


class CallbackGame:
    """A placeholder, currently holds no information. Use BotFather to set up your game."""
    def __init__(self, json):
        self.json = json
        


class GameHighScore:
    """This object represents one row of the high scores table for a game."""
    def __init__(self, json):
        self.json = json
        self.position = int(json['position'])
        self.user = User(json['user'])
        self.score = int(json['score'])


