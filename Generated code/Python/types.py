# This code in its entirety was generated and formatted automatically


class Update:
    """This object represents an incoming update.At most one of the optional parameters can be present in any given update.
    attribute update_id: The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you're using webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.
    attribute message: New incoming message of any kind - text, photo, sticker, etc.
    attribute edited_message: New version of a message that is known to the bot and was edited
    attribute channel_post: New incoming channel post of any kind - text, photo, sticker, etc.
    attribute edited_channel_post: New version of a channel post that is known to the bot and was edited
    attribute inline_query: New incoming inline query
    attribute chosen_inline_result: The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot.
    attribute callback_query: New incoming callback query
    attribute shipping_query: New incoming shipping query. Only for invoices with flexible price
    attribute pre_checkout_query: New incoming pre-checkout query. Contains full information about checkout
    attribute poll: New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot
    attribute poll_answer: A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.
    attribute my_chat_member: The bot's chat member status was updated in a chat. For private chats, this update is received only when the bot is blocked or unblocked by the user.
    attribute chat_member: A chat member's status was updated in a chat. The bot must be an administrator in the chat and must explicitly specify “chat_member” in the list of allowed_updates to receive these updates.
    attribute chat_join_request: A request to join the chat has been sent. The bot must have the can_invite_users administrator right in the chat to receive these updates."""

    def __init__(self, json):
        self.json = json
        self.update_id = int(json["update_id"])
        if "message" in json:
            self.message = Message(json["message"])
        if "edited_message" in json:
            self.edited_message = Message(json["edited_message"])
        if "channel_post" in json:
            self.channel_post = Message(json["channel_post"])
        if "edited_channel_post" in json:
            self.edited_channel_post = Message(json["edited_channel_post"])
        if "inline_query" in json:
            self.inline_query = InlineQuery(json["inline_query"])
        if "chosen_inline_result" in json:
            self.chosen_inline_result = ChosenInlineResult(json["chosen_inline_result"])
        if "callback_query" in json:
            self.callback_query = CallbackQuery(json["callback_query"])
        if "shipping_query" in json:
            self.shipping_query = ShippingQuery(json["shipping_query"])
        if "pre_checkout_query" in json:
            self.pre_checkout_query = PreCheckoutQuery(json["pre_checkout_query"])
        if "poll" in json:
            self.poll = Poll(json["poll"])
        if "poll_answer" in json:
            self.poll_answer = PollAnswer(json["poll_answer"])
        if "my_chat_member" in json:
            self.my_chat_member = ChatMemberUpdated(json["my_chat_member"])
        if "chat_member" in json:
            self.chat_member = ChatMemberUpdated(json["chat_member"])
        if "chat_join_request" in json:
            self.chat_join_request = ChatJoinRequest(json["chat_join_request"])


class WebhookInfo:
    """Describes the current status of a webhook.
    attribute url: Webhook URL, may be empty if webhook is not set up
    attribute has_custom_certificate: True, if a custom certificate was provided for webhook certificate checks
    attribute pending_update_count: Number of updates awaiting delivery
    attribute ip_address: Currently used webhook IP address
    attribute last_error_date: Unix time for the most recent error that happened when trying to deliver an update via webhook
    attribute last_error_message: Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook
    attribute last_synchronization_error_date: Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters
    attribute max_connections: The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery
    attribute allowed_updates: A list of update types the bot is subscribed to. Defaults to all update types except chat_member"""

    def __init__(self, json):
        self.json = json
        self.url = str(json["url"])
        self.has_custom_certificate = bool(json["has_custom_certificate"])
        self.pending_update_count = int(json["pending_update_count"])
        if "ip_address" in json:
            self.ip_address = str(json["ip_address"])
        if "last_error_date" in json:
            self.last_error_date = int(json["last_error_date"])
        if "last_error_message" in json:
            self.last_error_message = str(json["last_error_message"])
        if "last_synchronization_error_date" in json:
            self.last_synchronization_error_date = int(
                json["last_synchronization_error_date"]
            )
        if "max_connections" in json:
            self.max_connections = int(json["max_connections"])
        if "allowed_updates" in json:
            self.allowed_updates = [list[str](item) for item in json["allowed_updates"]]


class User:
    """This object represents a Telegram user or bot.
    attribute id: Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
    attribute is_bot: True, if this user is a bot
    attribute first_name: User's or bot's first name
    attribute last_name: User's or bot's last name
    attribute username: User's or bot's username
    attribute language_code: IETF language tag of the user's language
    attribute can_join_groups: True, if the bot can be invited to groups. Returned only in getMe.
    attribute can_read_all_group_messages: True, if privacy mode is disabled for the bot. Returned only in getMe.
    attribute supports_inline_queries: True, if the bot supports inline queries. Returned only in getMe."""

    def __init__(self, json):
        self.json = json
        self.id = int(json["id"])
        self.is_bot = bool(json["is_bot"])
        self.first_name = str(json["first_name"])
        if "last_name" in json:
            self.last_name = str(json["last_name"])
        if "username" in json:
            self.username = str(json["username"])
        if "language_code" in json:
            self.language_code = str(json["language_code"])
        if "can_join_groups" in json:
            self.can_join_groups = bool(json["can_join_groups"])
        if "can_read_all_group_messages" in json:
            self.can_read_all_group_messages = bool(json["can_read_all_group_messages"])
        if "supports_inline_queries" in json:
            self.supports_inline_queries = bool(json["supports_inline_queries"])


class Chat:
    """This object represents a chat.
    attribute id: Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    attribute type: Type of chat, can be either “private”, “group”, “supergroup” or “channel”
    attribute title: Title, for supergroups, channels and group chats
    attribute username: Username, for private chats, supergroups and channels if available
    attribute first_name: First name of the other party in a private chat
    attribute last_name: Last name of the other party in a private chat
    attribute photo: Chat photo. Returned only in getChat.
    attribute bio: Bio of the other party in a private chat. Returned only in getChat.
    attribute has_private_forwards: True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user. Returned only in getChat.
    attribute description: Description, for groups, supergroups and channel chats. Returned only in getChat.
    attribute invite_link: Primary invite link, for groups, supergroups and channel chats. Returned only in getChat.
    attribute pinned_message: The most recent pinned message (by sending date). Returned only in getChat.
    attribute permissions: Default chat member permissions, for groups and supergroups. Returned only in getChat.
    attribute slow_mode_delay: For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user; in seconds. Returned only in getChat.
    attribute message_auto_delete_time: The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in getChat.
    attribute has_protected_content: True, if messages from the chat can't be forwarded to other chats. Returned only in getChat.
    attribute sticker_set_name: For supergroups, name of group sticker set. Returned only in getChat.
    attribute can_set_sticker_set: True, if the bot can change the group sticker set. Returned only in getChat.
    attribute linked_chat_id: Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in getChat.
    attribute location: For supergroups, the location to which the supergroup is connected. Returned only in getChat."""

    def __init__(self, json):
        self.json = json
        self.id = int(json["id"])
        self.type = str(json["type"])
        if "title" in json:
            self.title = str(json["title"])
        if "username" in json:
            self.username = str(json["username"])
        if "first_name" in json:
            self.first_name = str(json["first_name"])
        if "last_name" in json:
            self.last_name = str(json["last_name"])
        if "photo" in json:
            self.photo = ChatPhoto(json["photo"])
        if "bio" in json:
            self.bio = str(json["bio"])
        if "has_private_forwards" in json:
            self.has_private_forwards = bool(json["has_private_forwards"])
        if "description" in json:
            self.description = str(json["description"])
        if "invite_link" in json:
            self.invite_link = str(json["invite_link"])
        if "pinned_message" in json:
            self.pinned_message = Message(json["pinned_message"])
        if "permissions" in json:
            self.permissions = ChatPermissions(json["permissions"])
        if "slow_mode_delay" in json:
            self.slow_mode_delay = int(json["slow_mode_delay"])
        if "message_auto_delete_time" in json:
            self.message_auto_delete_time = int(json["message_auto_delete_time"])
        if "has_protected_content" in json:
            self.has_protected_content = bool(json["has_protected_content"])
        if "sticker_set_name" in json:
            self.sticker_set_name = str(json["sticker_set_name"])
        if "can_set_sticker_set" in json:
            self.can_set_sticker_set = bool(json["can_set_sticker_set"])
        if "linked_chat_id" in json:
            self.linked_chat_id = int(json["linked_chat_id"])
        if "location" in json:
            self.location = ChatLocation(json["location"])


class Message:
    """This object represents a message.
    attribute message_id: Unique message identifier inside this chat
    attribute from_: Sender of the message; empty for messages sent to channels. For backward compatibility, the field contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.
    attribute sender_chat: Sender of the message, sent on behalf of a chat. For example, the channel itself for channel posts, the supergroup itself for messages from anonymous group administrators, the linked channel for messages automatically forwarded to the discussion group. For backward compatibility, the field from contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.
    attribute date: Date the message was sent in Unix time
    attribute chat: Conversation the message belongs to
    attribute forward_from: For forwarded messages, sender of the original message
    attribute forward_from_chat: For messages forwarded from channels or from anonymous administrators, information about the original sender chat
    attribute forward_from_message_id: For messages forwarded from channels, identifier of the original message in the channel
    attribute forward_signature: For forwarded messages that were originally sent in channels or by an anonymous chat administrator, signature of the message sender if present
    attribute forward_sender_name: Sender's name for messages forwarded from users who disallow adding a link to their account in forwarded messages
    attribute forward_date: For forwarded messages, date the original message was sent in Unix time
    attribute is_automatic_forward: True, if the message is a channel post that was automatically forwarded to the connected discussion group
    attribute reply_to_message: For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
    attribute via_bot: Bot through which the message was sent
    attribute edit_date: Date the message was last edited in Unix time
    attribute has_protected_content: True, if the message can't be forwarded
    attribute media_group_id: The unique identifier of a media message group this message belongs to
    attribute author_signature: Signature of the post author for messages in channels, or the custom title of an anonymous group administrator
    attribute text: For text messages, the actual UTF-8 text of the message, 0-4096 characters
    attribute entities: For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
    attribute animation: Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set
    attribute audio: Message is an audio file, information about the file
    attribute document: Message is a general file, information about the file
    attribute photo: Message is a photo, available sizes of the photo
    attribute sticker: Message is a sticker, information about the sticker
    attribute video: Message is a video, information about the video
    attribute video_note: Message is a video note, information about the video message
    attribute voice: Message is a voice message, information about the file
    attribute caption: Caption for the animation, audio, document, photo, video or voice, 0-1024 characters
    attribute caption_entities: For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption
    attribute contact: Message is a shared contact, information about the contact
    attribute dice: Message is a dice with random value
    attribute game: Message is a game, information about the game. More about games »
    attribute poll: Message is a native poll, information about the poll
    attribute venue: Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set
    attribute location: Message is a shared location, information about the location
    attribute new_chat_members: New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)
    attribute left_chat_member: A member was removed from the group, information about them (this member may be the bot itself)
    attribute new_chat_title: A chat title was changed to this value
    attribute new_chat_photo: A chat photo was change to this value
    attribute delete_chat_photo: Service message: the chat photo was deleted
    attribute group_chat_created: Service message: the group has been created
    attribute supergroup_chat_created: Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
    attribute channel_chat_created: Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.
    attribute message_auto_delete_timer_changed: Service message: auto-delete timer settings changed in the chat
    attribute migrate_to_chat_id: The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    attribute migrate_from_chat_id: The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    attribute pinned_message: Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it is itself a reply.
    attribute invoice: Message is an invoice for a payment, information about the invoice. More about payments »
    attribute successful_payment: Message is a service message about a successful payment, information about the payment. More about payments »
    attribute connected_website: The domain name of the website on which the user has logged in. More about Telegram Login »
    attribute passport_data: Telegram Passport data
    attribute proximity_alert_triggered: Service message. A user in the chat triggered another user's proximity alert while sharing Live Location.
    attribute video_chat_scheduled: Service message: video chat scheduled
    attribute video_chat_started: Service message: video chat started
    attribute video_chat_ended: Service message: video chat ended
    attribute video_chat_participants_invited: Service message: new participants invited to a video chat
    attribute web_app_data: Service message: data sent by a Web App
    attribute reply_markup: Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons."""

    def __init__(self, json):
        self.json = json
        self.message_id = int(json["message_id"])
        if "from" in json:
            self.from_ = User(json["from"])
        if "sender_chat" in json:
            self.sender_chat = Chat(json["sender_chat"])
        self.date = int(json["date"])
        self.chat = Chat(json["chat"])
        if "forward_from" in json:
            self.forward_from = User(json["forward_from"])
        if "forward_from_chat" in json:
            self.forward_from_chat = Chat(json["forward_from_chat"])
        if "forward_from_message_id" in json:
            self.forward_from_message_id = int(json["forward_from_message_id"])
        if "forward_signature" in json:
            self.forward_signature = str(json["forward_signature"])
        if "forward_sender_name" in json:
            self.forward_sender_name = str(json["forward_sender_name"])
        if "forward_date" in json:
            self.forward_date = int(json["forward_date"])
        if "is_automatic_forward" in json:
            self.is_automatic_forward = bool(json["is_automatic_forward"])
        if "reply_to_message" in json:
            self.reply_to_message = Message(json["reply_to_message"])
        if "via_bot" in json:
            self.via_bot = User(json["via_bot"])
        if "edit_date" in json:
            self.edit_date = int(json["edit_date"])
        if "has_protected_content" in json:
            self.has_protected_content = bool(json["has_protected_content"])
        if "media_group_id" in json:
            self.media_group_id = str(json["media_group_id"])
        if "author_signature" in json:
            self.author_signature = str(json["author_signature"])
        if "text" in json:
            self.text = str(json["text"])
        if "entities" in json:
            self.entities = [list[MessageEntity](item) for item in json["entities"]]
        if "animation" in json:
            self.animation = Animation(json["animation"])
        if "audio" in json:
            self.audio = Audio(json["audio"])
        if "document" in json:
            self.document = Document(json["document"])
        if "photo" in json:
            self.photo = [list[PhotoSize](item) for item in json["photo"]]
        if "sticker" in json:
            self.sticker = Sticker(json["sticker"])
        if "video" in json:
            self.video = Video(json["video"])
        if "video_note" in json:
            self.video_note = VideoNote(json["video_note"])
        if "voice" in json:
            self.voice = Voice(json["voice"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]
        if "contact" in json:
            self.contact = Contact(json["contact"])
        if "dice" in json:
            self.dice = Dice(json["dice"])
        if "game" in json:
            self.game = Game(json["game"])
        if "poll" in json:
            self.poll = Poll(json["poll"])
        if "venue" in json:
            self.venue = Venue(json["venue"])
        if "location" in json:
            self.location = Location(json["location"])
        if "new_chat_members" in json:
            self.new_chat_members = [
                list[User](item) for item in json["new_chat_members"]
            ]
        if "left_chat_member" in json:
            self.left_chat_member = User(json["left_chat_member"])
        if "new_chat_title" in json:
            self.new_chat_title = str(json["new_chat_title"])
        if "new_chat_photo" in json:
            self.new_chat_photo = [
                list[PhotoSize](item) for item in json["new_chat_photo"]
            ]
        if "delete_chat_photo" in json:
            self.delete_chat_photo = bool(json["delete_chat_photo"])
        if "group_chat_created" in json:
            self.group_chat_created = bool(json["group_chat_created"])
        if "supergroup_chat_created" in json:
            self.supergroup_chat_created = bool(json["supergroup_chat_created"])
        if "channel_chat_created" in json:
            self.channel_chat_created = bool(json["channel_chat_created"])
        if "message_auto_delete_timer_changed" in json:
            self.message_auto_delete_timer_changed = MessageAutoDeleteTimerChanged(
                json["message_auto_delete_timer_changed"]
            )
        if "migrate_to_chat_id" in json:
            self.migrate_to_chat_id = int(json["migrate_to_chat_id"])
        if "migrate_from_chat_id" in json:
            self.migrate_from_chat_id = int(json["migrate_from_chat_id"])
        if "pinned_message" in json:
            self.pinned_message = Message(json["pinned_message"])
        if "invoice" in json:
            self.invoice = Invoice(json["invoice"])
        if "successful_payment" in json:
            self.successful_payment = SuccessfulPayment(json["successful_payment"])
        if "connected_website" in json:
            self.connected_website = str(json["connected_website"])
        if "passport_data" in json:
            self.passport_data = PassportData(json["passport_data"])
        if "proximity_alert_triggered" in json:
            self.proximity_alert_triggered = ProximityAlertTriggered(
                json["proximity_alert_triggered"]
            )
        if "video_chat_scheduled" in json:
            self.video_chat_scheduled = VideoChatScheduled(json["video_chat_scheduled"])
        if "video_chat_started" in json:
            self.video_chat_started = VideoChatStarted(json["video_chat_started"])
        if "video_chat_ended" in json:
            self.video_chat_ended = VideoChatEnded(json["video_chat_ended"])
        if "video_chat_participants_invited" in json:
            self.video_chat_participants_invited = VideoChatParticipantsInvited(
                json["video_chat_participants_invited"]
            )
        if "web_app_data" in json:
            self.web_app_data = WebAppData(json["web_app_data"])
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])


class MessageId:
    """This object represents a unique message identifier.
    attribute message_id: Unique message identifier"""

    def __init__(self, json):
        self.json = json
        self.message_id = int(json["message_id"])


class MessageEntity:
    """This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.
    attribute type: Type of the entity. Currently, can be “mention” (@username), “hashtag” (#hashtag), “cashtag” ($USD), “bot_command” (/start@jobs_bot), “url” (https://telegram.org), “email” (do-not-reply@telegram.org), “phone_number” (+1-212-555-0123), “bold” (bold text), “italic” (italic text), “underline” (underlined text), “strikethrough” (strikethrough text), “spoiler” (spoiler message), “code” (monowidth string), “pre” (monowidth block), “text_link” (for clickable text URLs), “text_mention” (for users without usernames)
    attribute offset: Offset in UTF-16 code units to the start of the entity
    attribute length: Length of the entity in UTF-16 code units
    attribute url: For “text_link” only, URL that will be opened after user taps on the text
    attribute user: For “text_mention” only, the mentioned user
    attribute language: For “pre” only, the programming language of the entity text"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.offset = int(json["offset"])
        self.length = int(json["length"])
        if "url" in json:
            self.url = str(json["url"])
        if "user" in json:
            self.user = User(json["user"])
        if "language" in json:
            self.language = str(json["language"])


class PhotoSize:
    """This object represents one size of a photo or a file / sticker thumbnail.
    attribute file_id: Identifier for this file, which can be used to download or reuse the file
    attribute file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    attribute width: Photo width
    attribute height: Photo height
    attribute file_size: File size in bytes"""

    def __init__(self, json):
        self.json = json
        self.file_id = str(json["file_id"])
        self.file_unique_id = str(json["file_unique_id"])
        self.width = int(json["width"])
        self.height = int(json["height"])
        if "file_size" in json:
            self.file_size = int(json["file_size"])


class Animation:
    """This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).
    attribute file_id: Identifier for this file, which can be used to download or reuse the file
    attribute file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    attribute width: Video width as defined by sender
    attribute height: Video height as defined by sender
    attribute duration: Duration of the video in seconds as defined by sender
    attribute thumb: Animation thumbnail as defined by sender
    attribute file_name: Original animation filename as defined by sender
    attribute mime_type: MIME type of the file as defined by sender
    attribute file_size: File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value."""

    def __init__(self, json):
        self.json = json
        self.file_id = str(json["file_id"])
        self.file_unique_id = str(json["file_unique_id"])
        self.width = int(json["width"])
        self.height = int(json["height"])
        self.duration = int(json["duration"])
        if "thumb" in json:
            self.thumb = PhotoSize(json["thumb"])
        if "file_name" in json:
            self.file_name = str(json["file_name"])
        if "mime_type" in json:
            self.mime_type = str(json["mime_type"])
        if "file_size" in json:
            self.file_size = int(json["file_size"])


class Audio:
    """This object represents an audio file to be treated as music by the Telegram clients.
    attribute file_id: Identifier for this file, which can be used to download or reuse the file
    attribute file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    attribute duration: Duration of the audio in seconds as defined by sender
    attribute performer: Performer of the audio as defined by sender or by audio tags
    attribute title: Title of the audio as defined by sender or by audio tags
    attribute file_name: Original filename as defined by sender
    attribute mime_type: MIME type of the file as defined by sender
    attribute file_size: File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
    attribute thumb: Thumbnail of the album cover to which the music file belongs"""

    def __init__(self, json):
        self.json = json
        self.file_id = str(json["file_id"])
        self.file_unique_id = str(json["file_unique_id"])
        self.duration = int(json["duration"])
        if "performer" in json:
            self.performer = str(json["performer"])
        if "title" in json:
            self.title = str(json["title"])
        if "file_name" in json:
            self.file_name = str(json["file_name"])
        if "mime_type" in json:
            self.mime_type = str(json["mime_type"])
        if "file_size" in json:
            self.file_size = int(json["file_size"])
        if "thumb" in json:
            self.thumb = PhotoSize(json["thumb"])


class Document:
    """This object represents a general file (as opposed to photos, voice messages and audio files).
    attribute file_id: Identifier for this file, which can be used to download or reuse the file
    attribute file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    attribute thumb: Document thumbnail as defined by sender
    attribute file_name: Original filename as defined by sender
    attribute mime_type: MIME type of the file as defined by sender
    attribute file_size: File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value."""

    def __init__(self, json):
        self.json = json
        self.file_id = str(json["file_id"])
        self.file_unique_id = str(json["file_unique_id"])
        if "thumb" in json:
            self.thumb = PhotoSize(json["thumb"])
        if "file_name" in json:
            self.file_name = str(json["file_name"])
        if "mime_type" in json:
            self.mime_type = str(json["mime_type"])
        if "file_size" in json:
            self.file_size = int(json["file_size"])


class Video:
    """This object represents a video file.
    attribute file_id: Identifier for this file, which can be used to download or reuse the file
    attribute file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    attribute width: Video width as defined by sender
    attribute height: Video height as defined by sender
    attribute duration: Duration of the video in seconds as defined by sender
    attribute thumb: Video thumbnail
    attribute file_name: Original filename as defined by sender
    attribute mime_type: MIME type of the file as defined by sender
    attribute file_size: File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value."""

    def __init__(self, json):
        self.json = json
        self.file_id = str(json["file_id"])
        self.file_unique_id = str(json["file_unique_id"])
        self.width = int(json["width"])
        self.height = int(json["height"])
        self.duration = int(json["duration"])
        if "thumb" in json:
            self.thumb = PhotoSize(json["thumb"])
        if "file_name" in json:
            self.file_name = str(json["file_name"])
        if "mime_type" in json:
            self.mime_type = str(json["mime_type"])
        if "file_size" in json:
            self.file_size = int(json["file_size"])


class VideoNote:
    """This object represents a video message (available in Telegram apps as of v.4.0).
    attribute file_id: Identifier for this file, which can be used to download or reuse the file
    attribute file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    attribute length: Video width and height (diameter of the video message) as defined by sender
    attribute duration: Duration of the video in seconds as defined by sender
    attribute thumb: Video thumbnail
    attribute file_size: File size in bytes"""

    def __init__(self, json):
        self.json = json
        self.file_id = str(json["file_id"])
        self.file_unique_id = str(json["file_unique_id"])
        self.length = int(json["length"])
        self.duration = int(json["duration"])
        if "thumb" in json:
            self.thumb = PhotoSize(json["thumb"])
        if "file_size" in json:
            self.file_size = int(json["file_size"])


class Voice:
    """This object represents a voice note.
    attribute file_id: Identifier for this file, which can be used to download or reuse the file
    attribute file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    attribute duration: Duration of the audio in seconds as defined by sender
    attribute mime_type: MIME type of the file as defined by sender
    attribute file_size: File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value."""

    def __init__(self, json):
        self.json = json
        self.file_id = str(json["file_id"])
        self.file_unique_id = str(json["file_unique_id"])
        self.duration = int(json["duration"])
        if "mime_type" in json:
            self.mime_type = str(json["mime_type"])
        if "file_size" in json:
            self.file_size = int(json["file_size"])


class Contact:
    """This object represents a phone contact.
    attribute phone_number: Contact's phone number
    attribute first_name: Contact's first name
    attribute last_name: Contact's last name
    attribute user_id: Contact's user identifier in Telegram. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
    attribute vcard: Additional data about the contact in the form of a vCard"""

    def __init__(self, json):
        self.json = json
        self.phone_number = str(json["phone_number"])
        self.first_name = str(json["first_name"])
        if "last_name" in json:
            self.last_name = str(json["last_name"])
        if "user_id" in json:
            self.user_id = int(json["user_id"])
        if "vcard" in json:
            self.vcard = str(json["vcard"])


class Dice:
    """This object represents an animated emoji that displays a random value.
    attribute emoji: Emoji on which the dice throw animation is based
    attribute value: Value of the dice, 1-6 for “”, “” and “” base emoji, 1-5 for “” and “” base emoji, 1-64 for “” base emoji"""

    def __init__(self, json):
        self.json = json
        self.emoji = str(json["emoji"])
        self.value = int(json["value"])


class PollOption:
    """This object contains information about one answer option in a poll.
    attribute text: Option text, 1-100 characters
    attribute voter_count: Number of users that voted for this option"""

    def __init__(self, json):
        self.json = json
        self.text = str(json["text"])
        self.voter_count = int(json["voter_count"])


class PollAnswer:
    """This object represents an answer of a user in a non-anonymous poll.
    attribute poll_id: Unique poll identifier
    attribute user: The user, who changed the answer to the poll
    attribute option_ids: 0-based identifiers of answer options, chosen by the user. May be empty if the user retracted their vote."""

    def __init__(self, json):
        self.json = json
        self.poll_id = str(json["poll_id"])
        self.user = User(json["user"])
        self.option_ids = [list[int](item) for item in json["option_ids"]]


class Poll:
    """This object contains information about a poll.
    attribute id: Unique poll identifier
    attribute question: Poll question, 1-300 characters
    attribute options: List of poll options
    attribute total_voter_count: Total number of users that voted in the poll
    attribute is_closed: True, if the poll is closed
    attribute is_anonymous: True, if the poll is anonymous
    attribute type: Poll type, currently can be “regular” or “quiz”
    attribute allows_multiple_answers: True, if the poll allows multiple answers
    attribute correct_option_id: 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
    attribute explanation: Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters
    attribute explanation_entities: Special entities like usernames, URLs, bot commands, etc. that appear in the explanation
    attribute open_period: Amount of time in seconds the poll will be active after creation
    attribute close_date: Point in time (Unix timestamp) when the poll will be automatically closed"""

    def __init__(self, json):
        self.json = json
        self.id = str(json["id"])
        self.question = str(json["question"])
        self.options = [list[PollOption](item) for item in json["options"]]
        self.total_voter_count = int(json["total_voter_count"])
        self.is_closed = bool(json["is_closed"])
        self.is_anonymous = bool(json["is_anonymous"])
        self.type = str(json["type"])
        self.allows_multiple_answers = bool(json["allows_multiple_answers"])
        if "correct_option_id" in json:
            self.correct_option_id = int(json["correct_option_id"])
        if "explanation" in json:
            self.explanation = str(json["explanation"])
        if "explanation_entities" in json:
            self.explanation_entities = [
                list[MessageEntity](item) for item in json["explanation_entities"]
            ]
        if "open_period" in json:
            self.open_period = int(json["open_period"])
        if "close_date" in json:
            self.close_date = int(json["close_date"])


class Location:
    """This object represents a point on the map.
    attribute longitude: Longitude as defined by sender
    attribute latitude: Latitude as defined by sender
    attribute horizontal_accuracy: The radius of uncertainty for the location, measured in meters; 0-1500
    attribute live_period: Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only.
    attribute heading: The direction in which user is moving, in degrees; 1-360. For active live locations only.
    attribute proximity_alert_radius: The maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only."""

    def __init__(self, json):
        self.json = json
        self.longitude = float(json["longitude"])
        self.latitude = float(json["latitude"])
        if "horizontal_accuracy" in json:
            self.horizontal_accuracy = float(json["horizontal_accuracy"])
        if "live_period" in json:
            self.live_period = int(json["live_period"])
        if "heading" in json:
            self.heading = int(json["heading"])
        if "proximity_alert_radius" in json:
            self.proximity_alert_radius = int(json["proximity_alert_radius"])


class Venue:
    """This object represents a venue.
    attribute location: Venue location. Can't be a live location
    attribute title: Name of the venue
    attribute address: Address of the venue
    attribute foursquare_id: Foursquare identifier of the venue
    attribute foursquare_type: Foursquare type of the venue. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    attribute google_place_id: Google Places identifier of the venue
    attribute google_place_type: Google Places type of the venue. (See supported types.)"""

    def __init__(self, json):
        self.json = json
        self.location = Location(json["location"])
        self.title = str(json["title"])
        self.address = str(json["address"])
        if "foursquare_id" in json:
            self.foursquare_id = str(json["foursquare_id"])
        if "foursquare_type" in json:
            self.foursquare_type = str(json["foursquare_type"])
        if "google_place_id" in json:
            self.google_place_id = str(json["google_place_id"])
        if "google_place_type" in json:
            self.google_place_type = str(json["google_place_type"])


class WebAppData:
    """Describes data sent from a Web App to the bot.
    attribute data: The data. Be aware that a bad client can send arbitrary data in this field.
    attribute button_text: Text of the web_app keyboard button from which the Web App was opened. Be aware that a bad client can send arbitrary data in this field."""

    def __init__(self, json):
        self.json = json
        self.data = str(json["data"])
        self.button_text = str(json["button_text"])


class ProximityAlertTriggered:
    """This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.
    attribute traveler: User that triggered the alert
    attribute watcher: User that set the alert
    attribute distance: The distance between the users"""

    def __init__(self, json):
        self.json = json
        self.traveler = User(json["traveler"])
        self.watcher = User(json["watcher"])
        self.distance = int(json["distance"])


class MessageAutoDeleteTimerChanged:
    """This object represents a service message about a change in auto-delete timer settings.
    attribute message_auto_delete_time: New auto-delete time for messages in the chat; in seconds"""

    def __init__(self, json):
        self.json = json
        self.message_auto_delete_time = int(json["message_auto_delete_time"])


class VideoChatScheduled:
    """This object represents a service message about a video chat scheduled in the chat.
    attribute start_date: Point in time (Unix timestamp) when the video chat is supposed to be started by a chat administrator"""

    def __init__(self, json):
        self.json = json
        self.start_date = int(json["start_date"])


class VideoChatStarted:
    """This object represents a service message about a video chat started in the chat. Currently holds no information."""

    def __init__(self, json):
        self.json = json


class VideoChatEnded:
    """This object represents a service message about a video chat ended in the chat.
    attribute duration: Video chat duration in seconds"""

    def __init__(self, json):
        self.json = json
        self.duration = int(json["duration"])


class VideoChatParticipantsInvited:
    """This object represents a service message about new members invited to a video chat.
    attribute users: New members that were invited to the video chat"""

    def __init__(self, json):
        self.json = json
        self.users = [list[User](item) for item in json["users"]]


class UserProfilePhotos:
    """This object represent a user's profile pictures.
    attribute total_count: Total number of profile pictures the target user has
    attribute photos: Requested profile pictures (in up to 4 sizes each)"""

    def __init__(self, json):
        self.json = json
        self.total_count = int(json["total_count"])
        self.photos = [
            [list[list[PhotoSize]](item) for item in arr] for arr in json["photos"]
        ]


class File:
    """This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile."""

    def __init__(self, json):
        self.json = json


class WebAppInfo:
    """Describes a Web App.
    attribute url: An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps"""

    def __init__(self, json):
        self.json = json
        self.url = str(json["url"])


class ReplyKeyboardMarkup:
    """This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).
    attribute keyboard: Array of button rows, each represented by an Array of KeyboardButton objects
    attribute resize_keyboard: Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is always of the same height as the app's standard keyboard.
    attribute one_time_keyboard: Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat - the user can press a special button in the input field to see the custom keyboard again. Defaults to false.
    attribute input_field_placeholder: The placeholder to be shown in the input field when the keyboard is active; 1-64 characters
    attribute selective: Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.Example: A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard."""

    def __init__(self, json):
        self.json = json
        self.keyboard = [
            [list[list[KeyboardButton]](item) for item in arr]
            for arr in json["keyboard"]
        ]
        if "resize_keyboard" in json:
            self.resize_keyboard = bool(json["resize_keyboard"])
        if "one_time_keyboard" in json:
            self.one_time_keyboard = bool(json["one_time_keyboard"])
        if "input_field_placeholder" in json:
            self.input_field_placeholder = str(json["input_field_placeholder"])
        if "selective" in json:
            self.selective = bool(json["selective"])


class KeyboardButton:
    """This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields web_app, request_contact, request_location, and request_poll are mutually exclusive.
    attribute text: Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed
    attribute request_contact: If True, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only.
    attribute request_location: If True, the user's current location will be sent when the button is pressed. Available in private chats only.
    attribute request_poll: If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only.
    attribute web_app: If specified, the described Web App will be launched when the button is pressed. The Web App will be able to send a “web_app_data” service message. Available in private chats only."""

    def __init__(self, json):
        self.json = json
        self.text = str(json["text"])
        if "request_contact" in json:
            self.request_contact = bool(json["request_contact"])
        if "request_location" in json:
            self.request_location = bool(json["request_location"])
        if "request_poll" in json:
            self.request_poll = KeyboardButtonPollType(json["request_poll"])
        if "web_app" in json:
            self.web_app = WebAppInfo(json["web_app"])


class KeyboardButtonPollType:
    """This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.
    attribute type: If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type."""

    def __init__(self, json):
        self.json = json
        if "type" in json:
            self.type = str(json["type"])


class ReplyKeyboardRemove:
    """Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).
    attribute remove_keyboard: Requests clients to remove the custom keyboard (user will not be able to summon this keyboard; if you want to hide the keyboard from sight but keep it accessible, use one_time_keyboard in ReplyKeyboardMarkup)
    attribute selective: Use this parameter if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet."""

    def __init__(self, json):
        self.json = json
        self.remove_keyboard = bool(json["remove_keyboard"])
        if "selective" in json:
            self.selective = bool(json["selective"])


class InlineKeyboardMarkup:
    """This object represents an inline keyboard that appears right next to the message it belongs to.
    attribute inline_keyboard: Array of button rows, each represented by an Array of InlineKeyboardButton objects"""

    def __init__(self, json):
        self.json = json
        self.inline_keyboard = [
            [list[list[InlineKeyboardButton]](item) for item in arr]
            for arr in json["inline_keyboard"]
        ]


class InlineKeyboardButton:
    """This object represents one button of an inline keyboard. You must use exactly one of the optional fields.
    attribute text: Label text on the button
    attribute url: HTTP or tg:// URL to be opened when the button is pressed. Links tg://user?id=<user_id> can be used to mention a user by their ID without using a username, if this is allowed by their privacy settings.
    attribute callback_data: Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes
    attribute web_app: Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery. Available only in private chats between a user and the bot.
    attribute login_url: An HTTP URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget.
    attribute switch_inline_query: If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which case just the bot's username will be inserted.Note: This offers an easy way for users to start using your bot in inline mode when they are currently in a private chat with it. Especially useful when combined with switch_pm… actions - in this case the user will be automatically returned to the chat they switched from, skipping the chat selection screen.
    attribute switch_inline_query_current_chat: If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. May be empty, in which case only the bot's username will be inserted.This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options.
    attribute callback_game: Description of the game that will be launched when the user presses the button.NOTE: This type of button must always be the first button in the first row.
    attribute pay: Specify True, to send a Pay button.NOTE: This type of button must always be the first button in the first row and can only be used in invoice messages."""

    def __init__(self, json):
        self.json = json
        self.text = str(json["text"])
        if "url" in json:
            self.url = str(json["url"])
        if "callback_data" in json:
            self.callback_data = str(json["callback_data"])
        if "web_app" in json:
            self.web_app = WebAppInfo(json["web_app"])
        if "login_url" in json:
            self.login_url = LoginUrl(json["login_url"])
        if "switch_inline_query" in json:
            self.switch_inline_query = str(json["switch_inline_query"])
        if "switch_inline_query_current_chat" in json:
            self.switch_inline_query_current_chat = str(
                json["switch_inline_query_current_chat"]
            )
        if "callback_game" in json:
            self.callback_game = CallbackGame(json["callback_game"])
        if "pay" in json:
            self.pay = bool(json["pay"])


class LoginUrl:
    """This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:"""

    def __init__(self, json):
        self.json = json


class CallbackQuery:
    """This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.
    attribute id: Unique identifier for this query
    attribute from_: Sender
    attribute message: Message with the callback button that originated the query. Note that message content and message date will not be available if the message is too old
    attribute inline_message_id: Identifier of the message sent via the bot in inline mode, that originated the query.
    attribute chat_instance: Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.
    attribute data: Data associated with the callback button. Be aware that the message originated the query can contain no callback buttons with this data.
    attribute game_short_name: Short name of a Game to be returned, serves as the unique identifier for the game"""

    def __init__(self, json):
        self.json = json
        self.id = str(json["id"])
        self.from_ = User(json["from"])
        if "message" in json:
            self.message = Message(json["message"])
        if "inline_message_id" in json:
            self.inline_message_id = str(json["inline_message_id"])
        self.chat_instance = str(json["chat_instance"])
        if "data" in json:
            self.data = str(json["data"])
        if "game_short_name" in json:
            self.game_short_name = str(json["game_short_name"])


class ForceReply:
    """Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.
    attribute force_reply: Shows reply interface to the user, as if they manually selected the bot's message and tapped 'Reply'
    attribute input_field_placeholder: The placeholder to be shown in the input field when the reply is active; 1-64 characters
    attribute selective: Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message."""

    def __init__(self, json):
        self.json = json
        self.force_reply = bool(json["force_reply"])
        if "input_field_placeholder" in json:
            self.input_field_placeholder = str(json["input_field_placeholder"])
        if "selective" in json:
            self.selective = bool(json["selective"])


class ChatPhoto:
    """This object represents a chat photo.
    attribute small_file_id: File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
    attribute small_file_unique_id: Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    attribute big_file_id: File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
    attribute big_file_unique_id: Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file."""

    def __init__(self, json):
        self.json = json
        self.small_file_id = str(json["small_file_id"])
        self.small_file_unique_id = str(json["small_file_unique_id"])
        self.big_file_id = str(json["big_file_id"])
        self.big_file_unique_id = str(json["big_file_unique_id"])


class ChatInviteLink:
    """Represents an invite link for a chat.
    attribute invite_link: The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with “…”.
    attribute creator: Creator of the link
    attribute creates_join_request: True, if users joining the chat via the link need to be approved by chat administrators
    attribute is_primary: True, if the link is primary
    attribute is_revoked: True, if the link is revoked
    attribute name: Invite link name
    attribute expire_date: Point in time (Unix timestamp) when the link will expire or has been expired
    attribute member_limit: The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
    attribute pending_join_request_count: Number of pending join requests created using this link"""

    def __init__(self, json):
        self.json = json
        self.invite_link = str(json["invite_link"])
        self.creator = User(json["creator"])
        self.creates_join_request = bool(json["creates_join_request"])
        self.is_primary = bool(json["is_primary"])
        self.is_revoked = bool(json["is_revoked"])
        if "name" in json:
            self.name = str(json["name"])
        if "expire_date" in json:
            self.expire_date = int(json["expire_date"])
        if "member_limit" in json:
            self.member_limit = int(json["member_limit"])
        if "pending_join_request_count" in json:
            self.pending_join_request_count = int(json["pending_join_request_count"])


class ChatAdministratorRights:
    """Represents the rights of an administrator in a chat.
    attribute is_anonymous: True, if the user's presence in the chat is hidden
    attribute can_manage_chat: True, if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege
    attribute can_delete_messages: True, if the administrator can delete messages of other users
    attribute can_manage_video_chats: True, if the administrator can manage video chats
    attribute can_restrict_members: True, if the administrator can restrict, ban or unban chat members
    attribute can_promote_members: True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
    attribute can_change_info: True, if the user is allowed to change the chat title, photo and other settings
    attribute can_invite_users: True, if the user is allowed to invite new users to the chat
    attribute can_post_messages: True, if the administrator can post in the channel; channels only
    attribute can_edit_messages: True, if the administrator can edit messages of other users and can pin messages; channels only
    attribute can_pin_messages: True, if the user is allowed to pin messages; groups and supergroups only"""

    def __init__(self, json):
        self.json = json
        self.is_anonymous = bool(json["is_anonymous"])
        self.can_manage_chat = bool(json["can_manage_chat"])
        self.can_delete_messages = bool(json["can_delete_messages"])
        self.can_manage_video_chats = bool(json["can_manage_video_chats"])
        self.can_restrict_members = bool(json["can_restrict_members"])
        self.can_promote_members = bool(json["can_promote_members"])
        self.can_change_info = bool(json["can_change_info"])
        self.can_invite_users = bool(json["can_invite_users"])
        if "can_post_messages" in json:
            self.can_post_messages = bool(json["can_post_messages"])
        if "can_edit_messages" in json:
            self.can_edit_messages = bool(json["can_edit_messages"])
        if "can_pin_messages" in json:
            self.can_pin_messages = bool(json["can_pin_messages"])


class ChatMember:
    """This object contains information about one member of a chat. Currently, the following 6 types of chat members are supported:"""

    def __init__(self, json):
        self.json = json


class ChatMemberOwner:
    """Represents a chat member that owns the chat and has all administrator privileges.
    attribute status: The member's status in the chat, always “creator”
    attribute user: Information about the user
    attribute is_anonymous: True, if the user's presence in the chat is hidden
    attribute custom_title: Custom title for this user"""

    def __init__(self, json):
        self.json = json
        self.status = str(json["status"])
        self.user = User(json["user"])
        self.is_anonymous = bool(json["is_anonymous"])
        if "custom_title" in json:
            self.custom_title = str(json["custom_title"])


class ChatMemberAdministrator:
    """Represents a chat member that has some additional privileges.
    attribute status: The member's status in the chat, always “administrator”
    attribute user: Information about the user
    attribute can_be_edited: True, if the bot is allowed to edit administrator privileges of that user
    attribute is_anonymous: True, if the user's presence in the chat is hidden
    attribute can_manage_chat: True, if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege
    attribute can_delete_messages: True, if the administrator can delete messages of other users
    attribute can_manage_video_chats: True, if the administrator can manage video chats
    attribute can_restrict_members: True, if the administrator can restrict, ban or unban chat members
    attribute can_promote_members: True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
    attribute can_change_info: True, if the user is allowed to change the chat title, photo and other settings
    attribute can_invite_users: True, if the user is allowed to invite new users to the chat
    attribute can_post_messages: True, if the administrator can post in the channel; channels only
    attribute can_edit_messages: True, if the administrator can edit messages of other users and can pin messages; channels only
    attribute can_pin_messages: True, if the user is allowed to pin messages; groups and supergroups only
    attribute custom_title: Custom title for this user"""

    def __init__(self, json):
        self.json = json
        self.status = str(json["status"])
        self.user = User(json["user"])
        self.can_be_edited = bool(json["can_be_edited"])
        self.is_anonymous = bool(json["is_anonymous"])
        self.can_manage_chat = bool(json["can_manage_chat"])
        self.can_delete_messages = bool(json["can_delete_messages"])
        self.can_manage_video_chats = bool(json["can_manage_video_chats"])
        self.can_restrict_members = bool(json["can_restrict_members"])
        self.can_promote_members = bool(json["can_promote_members"])
        self.can_change_info = bool(json["can_change_info"])
        self.can_invite_users = bool(json["can_invite_users"])
        if "can_post_messages" in json:
            self.can_post_messages = bool(json["can_post_messages"])
        if "can_edit_messages" in json:
            self.can_edit_messages = bool(json["can_edit_messages"])
        if "can_pin_messages" in json:
            self.can_pin_messages = bool(json["can_pin_messages"])
        if "custom_title" in json:
            self.custom_title = str(json["custom_title"])


class ChatMemberMember:
    """Represents a chat member that has no additional privileges or restrictions.
    attribute status: The member's status in the chat, always “member”
    attribute user: Information about the user"""

    def __init__(self, json):
        self.json = json
        self.status = str(json["status"])
        self.user = User(json["user"])


class ChatMemberRestricted:
    """Represents a chat member that is under certain restrictions in the chat. Supergroups only.
    attribute status: The member's status in the chat, always “restricted”
    attribute user: Information about the user
    attribute is_member: True, if the user is a member of the chat at the moment of the request
    attribute can_change_info: True, if the user is allowed to change the chat title, photo and other settings
    attribute can_invite_users: True, if the user is allowed to invite new users to the chat
    attribute can_pin_messages: True, if the user is allowed to pin messages
    attribute can_send_messages: True, if the user is allowed to send text messages, contacts, locations and venues
    attribute can_send_media_messages: True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes
    attribute can_send_polls: True, if the user is allowed to send polls
    attribute can_send_other_messages: True, if the user is allowed to send animations, games, stickers and use inline bots
    attribute can_add_web_page_previews: True, if the user is allowed to add web page previews to their messages
    attribute until_date: Date when restrictions will be lifted for this user; unix time. If 0, then the user is restricted forever"""

    def __init__(self, json):
        self.json = json
        self.status = str(json["status"])
        self.user = User(json["user"])
        self.is_member = bool(json["is_member"])
        self.can_change_info = bool(json["can_change_info"])
        self.can_invite_users = bool(json["can_invite_users"])
        self.can_pin_messages = bool(json["can_pin_messages"])
        self.can_send_messages = bool(json["can_send_messages"])
        self.can_send_media_messages = bool(json["can_send_media_messages"])
        self.can_send_polls = bool(json["can_send_polls"])
        self.can_send_other_messages = bool(json["can_send_other_messages"])
        self.can_add_web_page_previews = bool(json["can_add_web_page_previews"])
        self.until_date = int(json["until_date"])


class ChatMemberLeft:
    """Represents a chat member that isn't currently a member of the chat, but may join it themselves.
    attribute status: The member's status in the chat, always “left”
    attribute user: Information about the user"""

    def __init__(self, json):
        self.json = json
        self.status = str(json["status"])
        self.user = User(json["user"])


class ChatMemberBanned:
    """Represents a chat member that was banned in the chat and can't return to the chat or view chat messages.
    attribute status: The member's status in the chat, always “kicked”
    attribute user: Information about the user
    attribute until_date: Date when restrictions will be lifted for this user; unix time. If 0, then the user is banned forever"""

    def __init__(self, json):
        self.json = json
        self.status = str(json["status"])
        self.user = User(json["user"])
        self.until_date = int(json["until_date"])


class ChatMemberUpdated:
    """This object represents changes in the status of a chat member.
    attribute chat: Chat the user belongs to
    attribute from_: Performer of the action, which resulted in the change
    attribute date: Date the change was done in Unix time
    attribute old_chat_member: Previous information about the chat member
    attribute new_chat_member: New information about the chat member
    attribute invite_link: Chat invite link, which was used by the user to join the chat; for joining by invite link events only."""

    def __init__(self, json):
        self.json = json
        self.chat = Chat(json["chat"])
        self.from_ = User(json["from"])
        self.date = int(json["date"])
        self.old_chat_member = ChatMember(json["old_chat_member"])
        self.new_chat_member = ChatMember(json["new_chat_member"])
        if "invite_link" in json:
            self.invite_link = ChatInviteLink(json["invite_link"])


class ChatJoinRequest:
    """Represents a join request sent to a chat.
    attribute chat: Chat to which the request was sent
    attribute from_: User that sent the join request
    attribute date: Date the request was sent in Unix time
    attribute bio: Bio of the user.
    attribute invite_link: Chat invite link that was used by the user to send the join request"""

    def __init__(self, json):
        self.json = json
        self.chat = Chat(json["chat"])
        self.from_ = User(json["from"])
        self.date = int(json["date"])
        if "bio" in json:
            self.bio = str(json["bio"])
        if "invite_link" in json:
            self.invite_link = ChatInviteLink(json["invite_link"])


class ChatPermissions:
    """Describes actions that a non-administrator user is allowed to take in a chat.
    attribute can_send_messages: True, if the user is allowed to send text messages, contacts, locations and venues
    attribute can_send_media_messages: True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes, implies can_send_messages
    attribute can_send_polls: True, if the user is allowed to send polls, implies can_send_messages
    attribute can_send_other_messages: True, if the user is allowed to send animations, games, stickers and use inline bots, implies can_send_media_messages
    attribute can_add_web_page_previews: True, if the user is allowed to add web page previews to their messages, implies can_send_media_messages
    attribute can_change_info: True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups
    attribute can_invite_users: True, if the user is allowed to invite new users to the chat
    attribute can_pin_messages: True, if the user is allowed to pin messages. Ignored in public supergroups"""

    def __init__(self, json):
        self.json = json
        if "can_send_messages" in json:
            self.can_send_messages = bool(json["can_send_messages"])
        if "can_send_media_messages" in json:
            self.can_send_media_messages = bool(json["can_send_media_messages"])
        if "can_send_polls" in json:
            self.can_send_polls = bool(json["can_send_polls"])
        if "can_send_other_messages" in json:
            self.can_send_other_messages = bool(json["can_send_other_messages"])
        if "can_add_web_page_previews" in json:
            self.can_add_web_page_previews = bool(json["can_add_web_page_previews"])
        if "can_change_info" in json:
            self.can_change_info = bool(json["can_change_info"])
        if "can_invite_users" in json:
            self.can_invite_users = bool(json["can_invite_users"])
        if "can_pin_messages" in json:
            self.can_pin_messages = bool(json["can_pin_messages"])


class ChatLocation:
    """Represents a location to which a chat is connected.
    attribute location: The location to which the supergroup is connected. Can't be a live location.
    attribute address: Location address; 1-64 characters, as defined by the chat owner"""

    def __init__(self, json):
        self.json = json
        self.location = Location(json["location"])
        self.address = str(json["address"])


class BotCommand:
    """This object represents a bot command.
    attribute command: Text of the command; 1-32 characters. Can contain only lowercase English letters, digits and underscores.
    attribute description: Description of the command; 1-256 characters."""

    def __init__(self, json):
        self.json = json
        self.command = str(json["command"])
        self.description = str(json["description"])


class BotCommandScope:
    """This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:"""

    def __init__(self, json):
        self.json = json


class BotCommandScopeDefault:
    """Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user.
    attribute type: Scope type, must be default"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])


class BotCommandScopeAllPrivateChats:
    """Represents the scope of bot commands, covering all private chats.
    attribute type: Scope type, must be all_private_chats"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])


class BotCommandScopeAllGroupChats:
    """Represents the scope of bot commands, covering all group and supergroup chats.
    attribute type: Scope type, must be all_group_chats"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])


class BotCommandScopeAllChatAdministrators:
    """Represents the scope of bot commands, covering all group and supergroup chat administrators.
    attribute type: Scope type, must be all_chat_administrators"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])


class BotCommandScopeChat:
    """Represents the scope of bot commands, covering a specific chat.
    attribute type: Scope type, must be chat
    attribute chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.chat_id = int | str(json["chat_id"])


class BotCommandScopeChatAdministrators:
    """Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.
    attribute type: Scope type, must be chat_administrators
    attribute chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.chat_id = int | str(json["chat_id"])


class BotCommandScopeChatMember:
    """Represents the scope of bot commands, covering a specific member of a group or supergroup chat.
    attribute type: Scope type, must be chat_member
    attribute chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    attribute user_id: Unique identifier of the target user"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.chat_id = int | str(json["chat_id"])
        self.user_id = int(json["user_id"])


class MenuButton:
    """This object describes the bot's menu button in a private chat. It should be one of"""

    def __init__(self, json):
        self.json = json


class MenuButtonCommands:
    """Represents a menu button, which opens the bot's list of commands.
    attribute type: Type of the button, must be commands"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])


class MenuButtonWebApp:
    """Represents a menu button, which launches a Web App.
    attribute type: Type of the button, must be web_app
    attribute text: Text on the button
    attribute web_app: Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery."""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.text = str(json["text"])
        self.web_app = WebAppInfo(json["web_app"])


class MenuButtonDefault:
    """Describes that no specific value for the menu button was set.
    attribute type: Type of the button, must be default"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])


class ResponseParameters:
    """Describes why a request was unsuccessful.
    attribute migrate_to_chat_id: The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    attribute retry_after: In case of exceeding flood control, the number of seconds left to wait before the request can be repeated"""

    def __init__(self, json):
        self.json = json
        if "migrate_to_chat_id" in json:
            self.migrate_to_chat_id = int(json["migrate_to_chat_id"])
        if "retry_after" in json:
            self.retry_after = int(json["retry_after"])


class InputMedia:
    """This object represents the content of a media message to be sent. It should be one of"""

    def __init__(self, json):
        self.json = json


class InputMediaPhoto:
    """Represents a photo to be sent.
    attribute type: Type of the result, must be photo
    attribute media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »
    attribute caption: Caption of the photo to be sent, 0-1024 characters after entities parsing
    attribute parse_mode: Mode for parsing entities in the photo caption. See formatting options for more details.
    attribute caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.media = str(json["media"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]


class InputMediaVideo:
    """Represents a video to be sent.
    attribute type: Type of the result, must be video
    attribute media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »
    attribute thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »
    attribute caption: Caption of the video to be sent, 0-1024 characters after entities parsing
    attribute parse_mode: Mode for parsing entities in the video caption. See formatting options for more details.
    attribute caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
    attribute width: Video width
    attribute height: Video height
    attribute duration: Video duration in seconds
    attribute supports_streaming: Pass True, if the uploaded video is suitable for streaming"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.media = str(json["media"])
        if "thumb" in json:
            self.thumb = InputFile | str(json["thumb"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]
        if "width" in json:
            self.width = int(json["width"])
        if "height" in json:
            self.height = int(json["height"])
        if "duration" in json:
            self.duration = int(json["duration"])
        if "supports_streaming" in json:
            self.supports_streaming = bool(json["supports_streaming"])


class InputMediaAnimation:
    """Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.
    attribute type: Type of the result, must be animation
    attribute media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »
    attribute thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »
    attribute caption: Caption of the animation to be sent, 0-1024 characters after entities parsing
    attribute parse_mode: Mode for parsing entities in the animation caption. See formatting options for more details.
    attribute caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
    attribute width: Animation width
    attribute height: Animation height
    attribute duration: Animation duration in seconds"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.media = str(json["media"])
        if "thumb" in json:
            self.thumb = InputFile | str(json["thumb"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]
        if "width" in json:
            self.width = int(json["width"])
        if "height" in json:
            self.height = int(json["height"])
        if "duration" in json:
            self.duration = int(json["duration"])


class InputMediaAudio:
    """Represents an audio file to be treated as music to be sent.
    attribute type: Type of the result, must be audio
    attribute media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »
    attribute thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »
    attribute caption: Caption of the audio to be sent, 0-1024 characters after entities parsing
    attribute parse_mode: Mode for parsing entities in the audio caption. See formatting options for more details.
    attribute caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
    attribute duration: Duration of the audio in seconds
    attribute performer: Performer of the audio
    attribute title: Title of the audio"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.media = str(json["media"])
        if "thumb" in json:
            self.thumb = InputFile | str(json["thumb"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]
        if "duration" in json:
            self.duration = int(json["duration"])
        if "performer" in json:
            self.performer = str(json["performer"])
        if "title" in json:
            self.title = str(json["title"])


class InputMediaDocument:
    """Represents a general file to be sent.
    attribute type: Type of the result, must be document
    attribute media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »
    attribute thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »
    attribute caption: Caption of the document to be sent, 0-1024 characters after entities parsing
    attribute parse_mode: Mode for parsing entities in the document caption. See formatting options for more details.
    attribute caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
    attribute disable_content_type_detection: Disables automatic server-side content type detection for files uploaded using multipart/form-data. Always True, if the document is sent as part of an album."""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.media = str(json["media"])
        if "thumb" in json:
            self.thumb = InputFile | str(json["thumb"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]
        if "disable_content_type_detection" in json:
            self.disable_content_type_detection = bool(
                json["disable_content_type_detection"]
            )


class InputFile:
    """This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser."""

    def __init__(self, json):
        self.json = json


class Sticker:
    """This object represents a sticker.
    attribute file_id: Identifier for this file, which can be used to download or reuse the file
    attribute file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    attribute width: Sticker width
    attribute height: Sticker height
    attribute is_animated: True, if the sticker is animated
    attribute is_video: True, if the sticker is a video sticker
    attribute thumb: Sticker thumbnail in the .WEBP or .JPG format
    attribute emoji: Emoji associated with the sticker
    attribute set_name: Name of the sticker set to which the sticker belongs
    attribute mask_position: For mask stickers, the position where the mask should be placed
    attribute file_size: File size in bytes"""

    def __init__(self, json):
        self.json = json
        self.file_id = str(json["file_id"])
        self.file_unique_id = str(json["file_unique_id"])
        self.width = int(json["width"])
        self.height = int(json["height"])
        self.is_animated = bool(json["is_animated"])
        self.is_video = bool(json["is_video"])
        if "thumb" in json:
            self.thumb = PhotoSize(json["thumb"])
        if "emoji" in json:
            self.emoji = str(json["emoji"])
        if "set_name" in json:
            self.set_name = str(json["set_name"])
        if "mask_position" in json:
            self.mask_position = MaskPosition(json["mask_position"])
        if "file_size" in json:
            self.file_size = int(json["file_size"])


class StickerSet:
    """This object represents a sticker set.
    attribute name: Sticker set name
    attribute title: Sticker set title
    attribute is_animated: True, if the sticker set contains animated stickers
    attribute is_video: True, if the sticker set contains video stickers
    attribute contains_masks: True, if the sticker set contains masks
    attribute stickers: List of all set stickers
    attribute thumb: Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format"""

    def __init__(self, json):
        self.json = json
        self.name = str(json["name"])
        self.title = str(json["title"])
        self.is_animated = bool(json["is_animated"])
        self.is_video = bool(json["is_video"])
        self.contains_masks = bool(json["contains_masks"])
        self.stickers = [list[Sticker](item) for item in json["stickers"]]
        if "thumb" in json:
            self.thumb = PhotoSize(json["thumb"])


class MaskPosition:
    """This object describes the position on faces where a mask should be placed by default.
    attribute point: The part of the face relative to which the mask should be placed. One of “forehead”, “eyes”, “mouth”, or “chin”.
    attribute x_shift: Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position.
    attribute y_shift: Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position.
    attribute scale: Mask scaling coefficient. For example, 2.0 means double size."""

    def __init__(self, json):
        self.json = json
        self.point = str(json["point"])
        self.x_shift = float(json["x_shift"])
        self.y_shift = float(json["y_shift"])
        self.scale = float(json["scale"])


class InlineQuery:
    """This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.
    attribute id: Unique identifier for this query
    attribute from_: Sender
    attribute query: Text of the query (up to 256 characters)
    attribute offset: Offset of the results to be returned, can be controlled by the bot
    attribute chat_type: Type of the chat from which the inline query was sent. Can be either “sender” for a private chat with the inline query sender, “private”, “group”, “supergroup”, or “channel”. The chat type should be always known for requests sent from official clients and most third-party clients, unless the request was sent from a secret chat
    attribute location: Sender location, only for bots that request user location"""

    def __init__(self, json):
        self.json = json
        self.id = str(json["id"])
        self.from_ = User(json["from"])
        self.query = str(json["query"])
        self.offset = str(json["offset"])
        if "chat_type" in json:
            self.chat_type = str(json["chat_type"])
        if "location" in json:
            self.location = Location(json["location"])


class InlineQueryResult:
    """This object represents one result of an inline query. Telegram clients currently support results of the following 20 types:"""

    def __init__(self, json):
        self.json = json


class InlineQueryResultArticle:
    """Represents a link to an article or web page.
    attribute type: Type of the result, must be article
    attribute id: Unique identifier for this result, 1-64 Bytes
    attribute title: Title of the result
    attribute input_message_content: Content of the message to be sent
    attribute reply_markup: Inline keyboard attached to the message
    attribute url: URL of the result
    attribute hide_url: Pass True, if you don't want the URL to be shown in the message
    attribute description: Short description of the result
    attribute thumb_url: Url of the thumbnail for the result
    attribute thumb_width: Thumbnail width
    attribute thumb_height: Thumbnail height"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.title = str(json["title"])
        self.input_message_content = InputMessageContent(json["input_message_content"])
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])
        if "url" in json:
            self.url = str(json["url"])
        if "hide_url" in json:
            self.hide_url = bool(json["hide_url"])
        if "description" in json:
            self.description = str(json["description"])
        if "thumb_url" in json:
            self.thumb_url = str(json["thumb_url"])
        if "thumb_width" in json:
            self.thumb_width = int(json["thumb_width"])
        if "thumb_height" in json:
            self.thumb_height = int(json["thumb_height"])


class InlineQueryResultPhoto:
    """Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.
    attribute type: Type of the result, must be photo
    attribute id: Unique identifier for this result, 1-64 bytes
    attribute photo_url: A valid URL of the photo. Photo must be in JPEG format. Photo size must not exceed 5MB
    attribute thumb_url: URL of the thumbnail for the photo
    attribute photo_width: Width of the photo
    attribute photo_height: Height of the photo
    attribute title: Title for the result
    attribute description: Short description of the result
    attribute caption: Caption of the photo to be sent, 0-1024 characters after entities parsing
    attribute parse_mode: Mode for parsing entities in the photo caption. See formatting options for more details.
    attribute caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
    attribute reply_markup: Inline keyboard attached to the message
    attribute input_message_content: Content of the message to be sent instead of the photo"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.photo_url = str(json["photo_url"])
        self.thumb_url = str(json["thumb_url"])
        if "photo_width" in json:
            self.photo_width = int(json["photo_width"])
        if "photo_height" in json:
            self.photo_height = int(json["photo_height"])
        if "title" in json:
            self.title = str(json["title"])
        if "description" in json:
            self.description = str(json["description"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])
        if "input_message_content" in json:
            self.input_message_content = InputMessageContent(
                json["input_message_content"]
            )


class InlineQueryResultGif:
    """Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
    attribute type: Type of the result, must be gif
    attribute id: Unique identifier for this result, 1-64 bytes
    attribute gif_url: A valid URL for the GIF file. File size must not exceed 1MB
    attribute gif_width: Width of the GIF
    attribute gif_height: Height of the GIF
    attribute gif_duration: Duration of the GIF in seconds
    attribute thumb_url: URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    attribute thumb_mime_type: MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg”
    attribute title: Title for the result
    attribute caption: Caption of the GIF file to be sent, 0-1024 characters after entities parsing
    attribute parse_mode: Mode for parsing entities in the caption. See formatting options for more details.
    attribute caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
    attribute reply_markup: Inline keyboard attached to the message
    attribute input_message_content: Content of the message to be sent instead of the GIF animation"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.gif_url = str(json["gif_url"])
        if "gif_width" in json:
            self.gif_width = int(json["gif_width"])
        if "gif_height" in json:
            self.gif_height = int(json["gif_height"])
        if "gif_duration" in json:
            self.gif_duration = int(json["gif_duration"])
        self.thumb_url = str(json["thumb_url"])
        if "thumb_mime_type" in json:
            self.thumb_mime_type = str(json["thumb_mime_type"])
        if "title" in json:
            self.title = str(json["title"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])
        if "input_message_content" in json:
            self.input_message_content = InputMessageContent(
                json["input_message_content"]
            )


class InlineQueryResultMpeg4Gif:
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
    attribute type: Type of the result, must be mpeg4_gif
    attribute id: Unique identifier for this result, 1-64 bytes
    attribute mpeg4_url: A valid URL for the MPEG4 file. File size must not exceed 1MB
    attribute mpeg4_width: Video width
    attribute mpeg4_height: Video height
    attribute mpeg4_duration: Video duration in seconds
    attribute thumb_url: URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    attribute thumb_mime_type: MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg”
    attribute title: Title for the result
    attribute caption: Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
    attribute parse_mode: Mode for parsing entities in the caption. See formatting options for more details.
    attribute caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
    attribute reply_markup: Inline keyboard attached to the message
    attribute input_message_content: Content of the message to be sent instead of the video animation"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.mpeg4_url = str(json["mpeg4_url"])
        if "mpeg4_width" in json:
            self.mpeg4_width = int(json["mpeg4_width"])
        if "mpeg4_height" in json:
            self.mpeg4_height = int(json["mpeg4_height"])
        if "mpeg4_duration" in json:
            self.mpeg4_duration = int(json["mpeg4_duration"])
        self.thumb_url = str(json["thumb_url"])
        if "thumb_mime_type" in json:
            self.thumb_mime_type = str(json["thumb_mime_type"])
        if "title" in json:
            self.title = str(json["title"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])
        if "input_message_content" in json:
            self.input_message_content = InputMessageContent(
                json["input_message_content"]
            )


class InlineQueryResultVideo:
    """Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video."""

    def __init__(self, json):
        self.json = json


class InlineQueryResultAudio:
    """Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    attribute type: Type of the result, must be audio
    attribute id: Unique identifier for this result, 1-64 bytes
    attribute audio_url: A valid URL for the audio file
    attribute title: Title
    attribute caption: Caption, 0-1024 characters after entities parsing
    attribute parse_mode: Mode for parsing entities in the audio caption. See formatting options for more details.
    attribute caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
    attribute performer: Performer
    attribute audio_duration: Audio duration in seconds
    attribute reply_markup: Inline keyboard attached to the message
    attribute input_message_content: Content of the message to be sent instead of the audio"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.audio_url = str(json["audio_url"])
        self.title = str(json["title"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]
        if "performer" in json:
            self.performer = str(json["performer"])
        if "audio_duration" in json:
            self.audio_duration = int(json["audio_duration"])
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])
        if "input_message_content" in json:
            self.input_message_content = InputMessageContent(
                json["input_message_content"]
            )


class InlineQueryResultVoice:
    """Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
    attribute type: Type of the result, must be voice
    attribute id: Unique identifier for this result, 1-64 bytes
    attribute voice_url: A valid URL for the voice recording
    attribute title: Recording title
    attribute caption: Caption, 0-1024 characters after entities parsing
    attribute parse_mode: Mode for parsing entities in the voice message caption. See formatting options for more details.
    attribute caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
    attribute voice_duration: Recording duration in seconds
    attribute reply_markup: Inline keyboard attached to the message
    attribute input_message_content: Content of the message to be sent instead of the voice recording"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.voice_url = str(json["voice_url"])
        self.title = str(json["title"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]
        if "voice_duration" in json:
            self.voice_duration = int(json["voice_duration"])
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])
        if "input_message_content" in json:
            self.input_message_content = InputMessageContent(
                json["input_message_content"]
            )


class InlineQueryResultDocument:
    """Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
    attribute type: Type of the result, must be document
    attribute id: Unique identifier for this result, 1-64 bytes
    attribute title: Title for the result
    attribute caption: Caption of the document to be sent, 0-1024 characters after entities parsing
    attribute parse_mode: Mode for parsing entities in the document caption. See formatting options for more details.
    attribute caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
    attribute document_url: A valid URL for the file
    attribute mime_type: MIME type of the content of the file, either “application/pdf” or “application/zip”
    attribute description: Short description of the result
    attribute reply_markup: Inline keyboard attached to the message
    attribute input_message_content: Content of the message to be sent instead of the file
    attribute thumb_url: URL of the thumbnail (JPEG only) for the file
    attribute thumb_width: Thumbnail width
    attribute thumb_height: Thumbnail height"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.title = str(json["title"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]
        self.document_url = str(json["document_url"])
        self.mime_type = str(json["mime_type"])
        if "description" in json:
            self.description = str(json["description"])
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])
        if "input_message_content" in json:
            self.input_message_content = InputMessageContent(
                json["input_message_content"]
            )
        if "thumb_url" in json:
            self.thumb_url = str(json["thumb_url"])
        if "thumb_width" in json:
            self.thumb_width = int(json["thumb_width"])
        if "thumb_height" in json:
            self.thumb_height = int(json["thumb_height"])


class InlineQueryResultLocation:
    """Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
    attribute type: Type of the result, must be location
    attribute id: Unique identifier for this result, 1-64 Bytes
    attribute latitude: Location latitude in degrees
    attribute longitude: Location longitude in degrees
    attribute title: Location title
    attribute horizontal_accuracy: The radius of uncertainty for the location, measured in meters; 0-1500
    attribute live_period: Period in seconds for which the location can be updated, should be between 60 and 86400.
    attribute heading: For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    attribute proximity_alert_radius: For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
    attribute reply_markup: Inline keyboard attached to the message
    attribute input_message_content: Content of the message to be sent instead of the location
    attribute thumb_url: Url of the thumbnail for the result
    attribute thumb_width: Thumbnail width
    attribute thumb_height: Thumbnail height"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.latitude = float(json["latitude"])
        self.longitude = float(json["longitude"])
        self.title = str(json["title"])
        if "horizontal_accuracy" in json:
            self.horizontal_accuracy = float(json["horizontal_accuracy"])
        if "live_period" in json:
            self.live_period = int(json["live_period"])
        if "heading" in json:
            self.heading = int(json["heading"])
        if "proximity_alert_radius" in json:
            self.proximity_alert_radius = int(json["proximity_alert_radius"])
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])
        if "input_message_content" in json:
            self.input_message_content = InputMessageContent(
                json["input_message_content"]
            )
        if "thumb_url" in json:
            self.thumb_url = str(json["thumb_url"])
        if "thumb_width" in json:
            self.thumb_width = int(json["thumb_width"])
        if "thumb_height" in json:
            self.thumb_height = int(json["thumb_height"])


class InlineQueryResultVenue:
    """Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
    attribute type: Type of the result, must be venue
    attribute id: Unique identifier for this result, 1-64 Bytes
    attribute latitude: Latitude of the venue location in degrees
    attribute longitude: Longitude of the venue location in degrees
    attribute title: Title of the venue
    attribute address: Address of the venue
    attribute foursquare_id: Foursquare identifier of the venue if known
    attribute foursquare_type: Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    attribute google_place_id: Google Places identifier of the venue
    attribute google_place_type: Google Places type of the venue. (See supported types.)
    attribute reply_markup: Inline keyboard attached to the message
    attribute input_message_content: Content of the message to be sent instead of the venue
    attribute thumb_url: Url of the thumbnail for the result
    attribute thumb_width: Thumbnail width
    attribute thumb_height: Thumbnail height"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.latitude = float(json["latitude"])
        self.longitude = float(json["longitude"])
        self.title = str(json["title"])
        self.address = str(json["address"])
        if "foursquare_id" in json:
            self.foursquare_id = str(json["foursquare_id"])
        if "foursquare_type" in json:
            self.foursquare_type = str(json["foursquare_type"])
        if "google_place_id" in json:
            self.google_place_id = str(json["google_place_id"])
        if "google_place_type" in json:
            self.google_place_type = str(json["google_place_type"])
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])
        if "input_message_content" in json:
            self.input_message_content = InputMessageContent(
                json["input_message_content"]
            )
        if "thumb_url" in json:
            self.thumb_url = str(json["thumb_url"])
        if "thumb_width" in json:
            self.thumb_width = int(json["thumb_width"])
        if "thumb_height" in json:
            self.thumb_height = int(json["thumb_height"])


class InlineQueryResultContact:
    """Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
    attribute type: Type of the result, must be contact
    attribute id: Unique identifier for this result, 1-64 Bytes
    attribute phone_number: Contact's phone number
    attribute first_name: Contact's first name
    attribute last_name: Contact's last name
    attribute vcard: Additional data about the contact in the form of a vCard, 0-2048 bytes
    attribute reply_markup: Inline keyboard attached to the message
    attribute input_message_content: Content of the message to be sent instead of the contact
    attribute thumb_url: Url of the thumbnail for the result
    attribute thumb_width: Thumbnail width
    attribute thumb_height: Thumbnail height"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.phone_number = str(json["phone_number"])
        self.first_name = str(json["first_name"])
        if "last_name" in json:
            self.last_name = str(json["last_name"])
        if "vcard" in json:
            self.vcard = str(json["vcard"])
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])
        if "input_message_content" in json:
            self.input_message_content = InputMessageContent(
                json["input_message_content"]
            )
        if "thumb_url" in json:
            self.thumb_url = str(json["thumb_url"])
        if "thumb_width" in json:
            self.thumb_width = int(json["thumb_width"])
        if "thumb_height" in json:
            self.thumb_height = int(json["thumb_height"])


class InlineQueryResultGame:
    """Represents a Game.
    attribute type: Type of the result, must be game
    attribute id: Unique identifier for this result, 1-64 bytes
    attribute game_short_name: Short name of the game
    attribute reply_markup: Inline keyboard attached to the message"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.game_short_name = str(json["game_short_name"])
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])


class InlineQueryResultCachedPhoto:
    """Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.
    attribute type: Type of the result, must be photo
    attribute id: Unique identifier for this result, 1-64 bytes
    attribute photo_file_id: A valid file identifier of the photo
    attribute title: Title for the result
    attribute description: Short description of the result
    attribute caption: Caption of the photo to be sent, 0-1024 characters after entities parsing
    attribute parse_mode: Mode for parsing entities in the photo caption. See formatting options for more details.
    attribute caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
    attribute reply_markup: Inline keyboard attached to the message
    attribute input_message_content: Content of the message to be sent instead of the photo"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.photo_file_id = str(json["photo_file_id"])
        if "title" in json:
            self.title = str(json["title"])
        if "description" in json:
            self.description = str(json["description"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])
        if "input_message_content" in json:
            self.input_message_content = InputMessageContent(
                json["input_message_content"]
            )


class InlineQueryResultCachedGif:
    """Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.
    attribute type: Type of the result, must be gif
    attribute id: Unique identifier for this result, 1-64 bytes
    attribute gif_file_id: A valid file identifier for the GIF file
    attribute title: Title for the result
    attribute caption: Caption of the GIF file to be sent, 0-1024 characters after entities parsing
    attribute parse_mode: Mode for parsing entities in the caption. See formatting options for more details.
    attribute caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
    attribute reply_markup: Inline keyboard attached to the message
    attribute input_message_content: Content of the message to be sent instead of the GIF animation"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.gif_file_id = str(json["gif_file_id"])
        if "title" in json:
            self.title = str(json["title"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])
        if "input_message_content" in json:
            self.input_message_content = InputMessageContent(
                json["input_message_content"]
            )


class InlineQueryResultCachedMpeg4Gif:
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
    attribute type: Type of the result, must be mpeg4_gif
    attribute id: Unique identifier for this result, 1-64 bytes
    attribute mpeg4_file_id: A valid file identifier for the MPEG4 file
    attribute title: Title for the result
    attribute caption: Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
    attribute parse_mode: Mode for parsing entities in the caption. See formatting options for more details.
    attribute caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
    attribute reply_markup: Inline keyboard attached to the message
    attribute input_message_content: Content of the message to be sent instead of the video animation"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.mpeg4_file_id = str(json["mpeg4_file_id"])
        if "title" in json:
            self.title = str(json["title"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])
        if "input_message_content" in json:
            self.input_message_content = InputMessageContent(
                json["input_message_content"]
            )


class InlineQueryResultCachedSticker:
    """Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
    attribute type: Type of the result, must be sticker
    attribute id: Unique identifier for this result, 1-64 bytes
    attribute sticker_file_id: A valid file identifier of the sticker
    attribute reply_markup: Inline keyboard attached to the message
    attribute input_message_content: Content of the message to be sent instead of the sticker"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.sticker_file_id = str(json["sticker_file_id"])
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])
        if "input_message_content" in json:
            self.input_message_content = InputMessageContent(
                json["input_message_content"]
            )


class InlineQueryResultCachedDocument:
    """Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file.
    attribute type: Type of the result, must be document
    attribute id: Unique identifier for this result, 1-64 bytes
    attribute title: Title for the result
    attribute document_file_id: A valid file identifier for the file
    attribute description: Short description of the result
    attribute caption: Caption of the document to be sent, 0-1024 characters after entities parsing
    attribute parse_mode: Mode for parsing entities in the document caption. See formatting options for more details.
    attribute caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
    attribute reply_markup: Inline keyboard attached to the message
    attribute input_message_content: Content of the message to be sent instead of the file"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.title = str(json["title"])
        self.document_file_id = str(json["document_file_id"])
        if "description" in json:
            self.description = str(json["description"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])
        if "input_message_content" in json:
            self.input_message_content = InputMessageContent(
                json["input_message_content"]
            )


class InlineQueryResultCachedVideo:
    """Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.
    attribute type: Type of the result, must be video
    attribute id: Unique identifier for this result, 1-64 bytes
    attribute video_file_id: A valid file identifier for the video file
    attribute title: Title for the result
    attribute description: Short description of the result
    attribute caption: Caption of the video to be sent, 0-1024 characters after entities parsing
    attribute parse_mode: Mode for parsing entities in the video caption. See formatting options for more details.
    attribute caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
    attribute reply_markup: Inline keyboard attached to the message
    attribute input_message_content: Content of the message to be sent instead of the video"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.video_file_id = str(json["video_file_id"])
        self.title = str(json["title"])
        if "description" in json:
            self.description = str(json["description"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])
        if "input_message_content" in json:
            self.input_message_content = InputMessageContent(
                json["input_message_content"]
            )


class InlineQueryResultCachedVoice:
    """Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.
    attribute type: Type of the result, must be voice
    attribute id: Unique identifier for this result, 1-64 bytes
    attribute voice_file_id: A valid file identifier for the voice message
    attribute title: Voice message title
    attribute caption: Caption, 0-1024 characters after entities parsing
    attribute parse_mode: Mode for parsing entities in the voice message caption. See formatting options for more details.
    attribute caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
    attribute reply_markup: Inline keyboard attached to the message
    attribute input_message_content: Content of the message to be sent instead of the voice message"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.voice_file_id = str(json["voice_file_id"])
        self.title = str(json["title"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])
        if "input_message_content" in json:
            self.input_message_content = InputMessageContent(
                json["input_message_content"]
            )


class InlineQueryResultCachedAudio:
    """Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    attribute type: Type of the result, must be audio
    attribute id: Unique identifier for this result, 1-64 bytes
    attribute audio_file_id: A valid file identifier for the audio file
    attribute caption: Caption, 0-1024 characters after entities parsing
    attribute parse_mode: Mode for parsing entities in the audio caption. See formatting options for more details.
    attribute caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
    attribute reply_markup: Inline keyboard attached to the message
    attribute input_message_content: Content of the message to be sent instead of the audio"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        self.id = str(json["id"])
        self.audio_file_id = str(json["audio_file_id"])
        if "caption" in json:
            self.caption = str(json["caption"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "caption_entities" in json:
            self.caption_entities = [
                list[MessageEntity](item) for item in json["caption_entities"]
            ]
        if "reply_markup" in json:
            self.reply_markup = InlineKeyboardMarkup(json["reply_markup"])
        if "input_message_content" in json:
            self.input_message_content = InputMessageContent(
                json["input_message_content"]
            )


class InputMessageContent:
    """This object represents the content of a message to be sent as a result of an inline query. Telegram clients currently support the following 5 types:"""

    def __init__(self, json):
        self.json = json


class InputTextMessageContent:
    """Represents the content of a text message to be sent as the result of an inline query.
    attribute message_text: Text of the message to be sent, 1-4096 characters
    attribute parse_mode: Mode for parsing entities in the message text. See formatting options for more details.
    attribute entities: List of special entities that appear in message text, which can be specified instead of parse_mode
    attribute disable_web_page_preview: Disables link previews for links in the sent message"""

    def __init__(self, json):
        self.json = json
        self.message_text = str(json["message_text"])
        if "parse_mode" in json:
            self.parse_mode = str(json["parse_mode"])
        if "entities" in json:
            self.entities = [list[MessageEntity](item) for item in json["entities"]]
        if "disable_web_page_preview" in json:
            self.disable_web_page_preview = bool(json["disable_web_page_preview"])


class InputLocationMessageContent:
    """Represents the content of a location message to be sent as the result of an inline query.
    attribute latitude: Latitude of the location in degrees
    attribute longitude: Longitude of the location in degrees
    attribute horizontal_accuracy: The radius of uncertainty for the location, measured in meters; 0-1500
    attribute live_period: Period in seconds for which the location can be updated, should be between 60 and 86400.
    attribute heading: For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    attribute proximity_alert_radius: For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified."""

    def __init__(self, json):
        self.json = json
        self.latitude = float(json["latitude"])
        self.longitude = float(json["longitude"])
        if "horizontal_accuracy" in json:
            self.horizontal_accuracy = float(json["horizontal_accuracy"])
        if "live_period" in json:
            self.live_period = int(json["live_period"])
        if "heading" in json:
            self.heading = int(json["heading"])
        if "proximity_alert_radius" in json:
            self.proximity_alert_radius = int(json["proximity_alert_radius"])


class InputVenueMessageContent:
    """Represents the content of a venue message to be sent as the result of an inline query.
    attribute latitude: Latitude of the venue in degrees
    attribute longitude: Longitude of the venue in degrees
    attribute title: Name of the venue
    attribute address: Address of the venue
    attribute foursquare_id: Foursquare identifier of the venue, if known
    attribute foursquare_type: Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    attribute google_place_id: Google Places identifier of the venue
    attribute google_place_type: Google Places type of the venue. (See supported types.)"""

    def __init__(self, json):
        self.json = json
        self.latitude = float(json["latitude"])
        self.longitude = float(json["longitude"])
        self.title = str(json["title"])
        self.address = str(json["address"])
        if "foursquare_id" in json:
            self.foursquare_id = str(json["foursquare_id"])
        if "foursquare_type" in json:
            self.foursquare_type = str(json["foursquare_type"])
        if "google_place_id" in json:
            self.google_place_id = str(json["google_place_id"])
        if "google_place_type" in json:
            self.google_place_type = str(json["google_place_type"])


class InputContactMessageContent:
    """Represents the content of a contact message to be sent as the result of an inline query.
    attribute phone_number: Contact's phone number
    attribute first_name: Contact's first name
    attribute last_name: Contact's last name
    attribute vcard: Additional data about the contact in the form of a vCard, 0-2048 bytes"""

    def __init__(self, json):
        self.json = json
        self.phone_number = str(json["phone_number"])
        self.first_name = str(json["first_name"])
        if "last_name" in json:
            self.last_name = str(json["last_name"])
        if "vcard" in json:
            self.vcard = str(json["vcard"])


class InputInvoiceMessageContent:
    """Represents the content of an invoice message to be sent as the result of an inline query.
    attribute title: Product name, 1-32 characters
    attribute description: Product description, 1-255 characters
    attribute payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
    attribute provider_token: Payment provider token, obtained via @BotFather
    attribute currency: Three-letter ISO 4217 currency code, see more on currencies
    attribute prices: Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
    attribute max_tip_amount: The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0
    attribute suggested_tip_amounts: A JSON-serialized array of suggested amounts of tip in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
    attribute provider_data: A JSON-serialized object for data about the invoice, which will be shared with the payment provider. A detailed description of the required fields should be provided by the payment provider.
    attribute photo_url: URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service.
    attribute photo_size: Photo size in bytes
    attribute photo_width: Photo width
    attribute photo_height: Photo height
    attribute need_name: Pass True, if you require the user's full name to complete the order
    attribute need_phone_number: Pass True, if you require the user's phone number to complete the order
    attribute need_email: Pass True, if you require the user's email address to complete the order
    attribute need_shipping_address: Pass True, if you require the user's shipping address to complete the order
    attribute send_phone_number_to_provider: Pass True, if the user's phone number should be sent to provider
    attribute send_email_to_provider: Pass True, if the user's email address should be sent to provider
    attribute is_flexible: Pass True, if the final price depends on the shipping method"""

    def __init__(self, json):
        self.json = json
        self.title = str(json["title"])
        self.description = str(json["description"])
        self.payload = str(json["payload"])
        self.provider_token = str(json["provider_token"])
        self.currency = str(json["currency"])
        self.prices = [list[LabeledPrice](item) for item in json["prices"]]
        if "max_tip_amount" in json:
            self.max_tip_amount = int(json["max_tip_amount"])
        if "suggested_tip_amounts" in json:
            self.suggested_tip_amounts = [
                list[int](item) for item in json["suggested_tip_amounts"]
            ]
        if "provider_data" in json:
            self.provider_data = str(json["provider_data"])
        if "photo_url" in json:
            self.photo_url = str(json["photo_url"])
        if "photo_size" in json:
            self.photo_size = int(json["photo_size"])
        if "photo_width" in json:
            self.photo_width = int(json["photo_width"])
        if "photo_height" in json:
            self.photo_height = int(json["photo_height"])
        if "need_name" in json:
            self.need_name = bool(json["need_name"])
        if "need_phone_number" in json:
            self.need_phone_number = bool(json["need_phone_number"])
        if "need_email" in json:
            self.need_email = bool(json["need_email"])
        if "need_shipping_address" in json:
            self.need_shipping_address = bool(json["need_shipping_address"])
        if "send_phone_number_to_provider" in json:
            self.send_phone_number_to_provider = bool(
                json["send_phone_number_to_provider"]
            )
        if "send_email_to_provider" in json:
            self.send_email_to_provider = bool(json["send_email_to_provider"])
        if "is_flexible" in json:
            self.is_flexible = bool(json["is_flexible"])


class ChosenInlineResult:
    """Represents a result of an inline query that was chosen by the user and sent to their chat partner.
    attribute result_id: The unique identifier for the result that was chosen
    attribute from_: The user that chose the result
    attribute location: Sender location, only for bots that require user location
    attribute inline_message_id: Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.
    attribute query: The query that was used to obtain the result"""

    def __init__(self, json):
        self.json = json
        self.result_id = str(json["result_id"])
        self.from_ = User(json["from"])
        if "location" in json:
            self.location = Location(json["location"])
        if "inline_message_id" in json:
            self.inline_message_id = str(json["inline_message_id"])
        self.query = str(json["query"])


class SentWebAppMessage:
    """Describes an inline message sent by a Web App on behalf of a user.
    attribute inline_message_id: Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message."""

    def __init__(self, json):
        self.json = json
        if "inline_message_id" in json:
            self.inline_message_id = str(json["inline_message_id"])


class LabeledPrice:
    """This object represents a portion of the price for goods or services.
    attribute label: Portion label
    attribute amount: Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies)."""

    def __init__(self, json):
        self.json = json
        self.label = str(json["label"])
        self.amount = int(json["amount"])


class Invoice:
    """This object contains basic information about an invoice.
    attribute title: Product name
    attribute description: Product description
    attribute start_parameter: Unique bot deep-linking parameter that can be used to generate this invoice
    attribute currency: Three-letter ISO 4217 currency code
    attribute total_amount: Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies)."""

    def __init__(self, json):
        self.json = json
        self.title = str(json["title"])
        self.description = str(json["description"])
        self.start_parameter = str(json["start_parameter"])
        self.currency = str(json["currency"])
        self.total_amount = int(json["total_amount"])


class ShippingAddress:
    """This object represents a shipping address.
    attribute country_code: Two-letter ISO 3166-1 alpha-2 country code
    attribute state: State, if applicable
    attribute city: City
    attribute street_line1: First line for the address
    attribute street_line2: Second line for the address
    attribute post_code: Address post code"""

    def __init__(self, json):
        self.json = json
        self.country_code = str(json["country_code"])
        self.state = str(json["state"])
        self.city = str(json["city"])
        self.street_line1 = str(json["street_line1"])
        self.street_line2 = str(json["street_line2"])
        self.post_code = str(json["post_code"])


class OrderInfo:
    """This object represents information about an order.
    attribute name: User name
    attribute phone_number: User's phone number
    attribute email: User email
    attribute shipping_address: User shipping address"""

    def __init__(self, json):
        self.json = json
        if "name" in json:
            self.name = str(json["name"])
        if "phone_number" in json:
            self.phone_number = str(json["phone_number"])
        if "email" in json:
            self.email = str(json["email"])
        if "shipping_address" in json:
            self.shipping_address = ShippingAddress(json["shipping_address"])


class ShippingOption:
    """This object represents one shipping option.
    attribute id: Shipping option identifier
    attribute title: Option title
    attribute prices: List of price portions"""

    def __init__(self, json):
        self.json = json
        self.id = str(json["id"])
        self.title = str(json["title"])
        self.prices = [list[LabeledPrice](item) for item in json["prices"]]


class SuccessfulPayment:
    """This object contains basic information about a successful payment.
    attribute currency: Three-letter ISO 4217 currency code
    attribute total_amount: Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    attribute invoice_payload: Bot specified invoice payload
    attribute shipping_option_id: Identifier of the shipping option chosen by the user
    attribute order_info: Order information provided by the user
    attribute telegram_payment_charge_id: Telegram payment identifier
    attribute provider_payment_charge_id: Provider payment identifier"""

    def __init__(self, json):
        self.json = json
        self.currency = str(json["currency"])
        self.total_amount = int(json["total_amount"])
        self.invoice_payload = str(json["invoice_payload"])
        if "shipping_option_id" in json:
            self.shipping_option_id = str(json["shipping_option_id"])
        if "order_info" in json:
            self.order_info = OrderInfo(json["order_info"])
        self.telegram_payment_charge_id = str(json["telegram_payment_charge_id"])
        self.provider_payment_charge_id = str(json["provider_payment_charge_id"])


class ShippingQuery:
    """This object contains information about an incoming shipping query.
    attribute id: Unique query identifier
    attribute from_: User who sent the query
    attribute invoice_payload: Bot specified invoice payload
    attribute shipping_address: User specified shipping address"""

    def __init__(self, json):
        self.json = json
        self.id = str(json["id"])
        self.from_ = User(json["from"])
        self.invoice_payload = str(json["invoice_payload"])
        self.shipping_address = ShippingAddress(json["shipping_address"])


class PreCheckoutQuery:
    """This object contains information about an incoming pre-checkout query.
    attribute id: Unique query identifier
    attribute from_: User who sent the query
    attribute currency: Three-letter ISO 4217 currency code
    attribute total_amount: Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    attribute invoice_payload: Bot specified invoice payload
    attribute shipping_option_id: Identifier of the shipping option chosen by the user
    attribute order_info: Order information provided by the user"""

    def __init__(self, json):
        self.json = json
        self.id = str(json["id"])
        self.from_ = User(json["from"])
        self.currency = str(json["currency"])
        self.total_amount = int(json["total_amount"])
        self.invoice_payload = str(json["invoice_payload"])
        if "shipping_option_id" in json:
            self.shipping_option_id = str(json["shipping_option_id"])
        if "order_info" in json:
            self.order_info = OrderInfo(json["order_info"])


class PassportData:
    """Describes Telegram Passport data shared with the bot by the user.
    attribute data: Array with information about documents and other Telegram Passport elements that was shared with the bot
    attribute credentials: Encrypted credentials required to decrypt the data"""

    def __init__(self, json):
        self.json = json
        self.data = [list[EncryptedPassportElement](item) for item in json["data"]]
        self.credentials = EncryptedCredentials(json["credentials"])


class PassportFile:
    """This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.
    attribute file_id: Identifier for this file, which can be used to download or reuse the file
    attribute file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    attribute file_size: File size in bytes
    attribute file_date: Unix time when the file was uploaded"""

    def __init__(self, json):
        self.json = json
        self.file_id = str(json["file_id"])
        self.file_unique_id = str(json["file_unique_id"])
        self.file_size = int(json["file_size"])
        self.file_date = int(json["file_date"])


class EncryptedPassportElement:
    """Describes documents or other Telegram Passport elements shared with the bot by the user.
    attribute type: Element type. One of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”, “phone_number”, “email”.
    attribute data: Base64-encoded encrypted Telegram Passport element data provided by the user, available for “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport” and “address” types. Can be decrypted and verified using the accompanying EncryptedCredentials.
    attribute phone_number: User's verified phone number, available only for “phone_number” type
    attribute email: User's verified email address, available only for “email” type
    attribute files: Array of encrypted files with documents provided by the user, available for “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
    attribute front_side: Encrypted file with the front side of the document, provided by the user. Available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
    attribute reverse_side: Encrypted file with the reverse side of the document, provided by the user. Available for “driver_license” and “identity_card”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
    attribute selfie: Encrypted file with the selfie of the user holding a document, provided by the user; available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
    attribute translation: Array of encrypted files with translated versions of documents provided by the user. Available if requested for “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
    attribute hash: Base64-encoded element hash for using in PassportElementErrorUnspecified"""

    def __init__(self, json):
        self.json = json
        self.type = str(json["type"])
        if "data" in json:
            self.data = str(json["data"])
        if "phone_number" in json:
            self.phone_number = str(json["phone_number"])
        if "email" in json:
            self.email = str(json["email"])
        if "files" in json:
            self.files = [list[PassportFile](item) for item in json["files"]]
        if "front_side" in json:
            self.front_side = PassportFile(json["front_side"])
        if "reverse_side" in json:
            self.reverse_side = PassportFile(json["reverse_side"])
        if "selfie" in json:
            self.selfie = PassportFile(json["selfie"])
        if "translation" in json:
            self.translation = [
                list[PassportFile](item) for item in json["translation"]
            ]
        self.hash = str(json["hash"])


class EncryptedCredentials:
    """Describes data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes.
    attribute data: Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication
    attribute hash: Base64-encoded data hash for data authentication
    attribute secret: Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption"""

    def __init__(self, json):
        self.json = json
        self.data = str(json["data"])
        self.hash = str(json["hash"])
        self.secret = str(json["secret"])


class PassportElementError:
    """This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user. It should be one of:"""

    def __init__(self, json):
        self.json = json


class PassportElementErrorDataField:
    """Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.
    attribute source: Error source, must be data
    attribute type: The section of the user's Telegram Passport which has the error, one of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”
    attribute field_name: Name of the data field which has the error
    attribute data_hash: Base64-encoded data hash
    attribute message: Error message"""

    def __init__(self, json):
        self.json = json
        self.source = str(json["source"])
        self.type = str(json["type"])
        self.field_name = str(json["field_name"])
        self.data_hash = str(json["data_hash"])
        self.message = str(json["message"])


class PassportElementErrorFrontSide:
    """Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.
    attribute source: Error source, must be front_side
    attribute type: The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”
    attribute file_hash: Base64-encoded hash of the file with the front side of the document
    attribute message: Error message"""

    def __init__(self, json):
        self.json = json
        self.source = str(json["source"])
        self.type = str(json["type"])
        self.file_hash = str(json["file_hash"])
        self.message = str(json["message"])


class PassportElementErrorReverseSide:
    """Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.
    attribute source: Error source, must be reverse_side
    attribute type: The section of the user's Telegram Passport which has the issue, one of “driver_license”, “identity_card”
    attribute file_hash: Base64-encoded hash of the file with the reverse side of the document
    attribute message: Error message"""

    def __init__(self, json):
        self.json = json
        self.source = str(json["source"])
        self.type = str(json["type"])
        self.file_hash = str(json["file_hash"])
        self.message = str(json["message"])


class PassportElementErrorSelfie:
    """Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.
    attribute source: Error source, must be selfie
    attribute type: The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”
    attribute file_hash: Base64-encoded hash of the file with the selfie
    attribute message: Error message"""

    def __init__(self, json):
        self.json = json
        self.source = str(json["source"])
        self.type = str(json["type"])
        self.file_hash = str(json["file_hash"])
        self.message = str(json["message"])


class PassportElementErrorFile:
    """Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.
    attribute source: Error source, must be file
    attribute type: The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
    attribute file_hash: Base64-encoded file hash
    attribute message: Error message"""

    def __init__(self, json):
        self.json = json
        self.source = str(json["source"])
        self.type = str(json["type"])
        self.file_hash = str(json["file_hash"])
        self.message = str(json["message"])


class PassportElementErrorFiles:
    """Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.
    attribute source: Error source, must be files
    attribute type: The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
    attribute file_hashes: List of base64-encoded file hashes
    attribute message: Error message"""

    def __init__(self, json):
        self.json = json
        self.source = str(json["source"])
        self.type = str(json["type"])
        self.file_hashes = [list[str](item) for item in json["file_hashes"]]
        self.message = str(json["message"])


class PassportElementErrorTranslationFile:
    """Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.
    attribute source: Error source, must be translation_file
    attribute type: Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
    attribute file_hash: Base64-encoded file hash
    attribute message: Error message"""

    def __init__(self, json):
        self.json = json
        self.source = str(json["source"])
        self.type = str(json["type"])
        self.file_hash = str(json["file_hash"])
        self.message = str(json["message"])


class PassportElementErrorTranslationFiles:
    """Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.
    attribute source: Error source, must be translation_files
    attribute type: Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
    attribute file_hashes: List of base64-encoded file hashes
    attribute message: Error message"""

    def __init__(self, json):
        self.json = json
        self.source = str(json["source"])
        self.type = str(json["type"])
        self.file_hashes = [list[str](item) for item in json["file_hashes"]]
        self.message = str(json["message"])


class PassportElementErrorUnspecified:
    """Represents an issue in an unspecified place. The error is considered resolved when new data is added.
    attribute source: Error source, must be unspecified
    attribute type: Type of element of the user's Telegram Passport which has the issue
    attribute element_hash: Base64-encoded element hash
    attribute message: Error message"""

    def __init__(self, json):
        self.json = json
        self.source = str(json["source"])
        self.type = str(json["type"])
        self.element_hash = str(json["element_hash"])
        self.message = str(json["message"])


class Game:
    """This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.
    attribute title: Title of the game
    attribute description: Description of the game
    attribute photo: Photo that will be displayed in the game message in chats.
    attribute text: Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText. 0-4096 characters.
    attribute text_entities: Special entities that appear in text, such as usernames, URLs, bot commands, etc.
    attribute animation: Animation that will be displayed in the game message in chats. Upload via BotFather"""

    def __init__(self, json):
        self.json = json
        self.title = str(json["title"])
        self.description = str(json["description"])
        self.photo = [list[PhotoSize](item) for item in json["photo"]]
        if "text" in json:
            self.text = str(json["text"])
        if "text_entities" in json:
            self.text_entities = [
                list[MessageEntity](item) for item in json["text_entities"]
            ]
        if "animation" in json:
            self.animation = Animation(json["animation"])


class CallbackGame:
    """A placeholder, currently holds no information. Use BotFather to set up your game."""

    def __init__(self, json):
        self.json = json


class GameHighScore:
    """This object represents one row of the high scores table for a game.
    attribute position: Position in high score table for the game
    attribute user: User
    attribute score: Score"""

    def __init__(self, json):
        self.json = json
        self.position = int(json["position"])
        self.user = User(json["user"])
        self.score = int(json["score"])
