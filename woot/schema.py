"""Schema for the action request body. Woot, woot."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, List


@dataclass
class RequestError:
    field: str | None = None
    message: str | None = None
    code: str | None = None


@dataclass
class GenericId:
    id: float | None = None


@dataclass
class CannedResponse:
    id: int | None = None
    content: str | None = None
    short_code: str | None = None
    account_id: int | None = None


@dataclass
class CustomAttribute:
    id: int | None = None
    attribute_display_name: str | None = None
    attribute_display_type: str | None = None
    attribute_description: str | None = None
    attribute_key: str | None = None
    attribute_values: str | None = None
    default_value: str | None = None
    attribute_model: str | None = None
    account_id: int | None = None


class EventName(Enum):
    conversation_created = "conversation_created"
    conversation_updated = "conversation_updated"
    message_created = "message_created"


@dataclass
class AutomationRule:
    event_name: EventName | None = None
    name: str | None = None
    description: str | None = None
    active: bool | None = None
    actions: list[dict[str, Any]] | None = None
    conditions: list[dict[str, Any]] | None = None
    account_id: int | None = None


class Status(Enum):
    open = "open"
    resolved = "resolved"
    pending = "pending"


class ContentType(Enum):
    text = "text"
    input_select = "input_select"
    cards = "cards"
    form = "form"


class MessageType(Enum):
    incoming = "incoming"
    outgoing = "outgoing"
    activity = "activity"
    template = "template"


@dataclass
class Message:
    content: str | None = None
    content_type: ContentType | None = None
    content_attributes: dict[str, Any] | None = None
    message_type: MessageType | None = None
    created_at: int | None = None
    private: bool | None = None
    attachment: dict[str, Any] | None = None
    sender: dict[str, Any] | None = None
    conversation_id: float | None = None


class Role(Enum):
    agent = "agent"
    administrator = "administrator"


class AvailabilityStatus(Enum):
    available = "available"
    busy = "busy"
    offline = "offline"


@dataclass
class Agent:
    id: int | None = None
    uid: str | None = None
    name: str | None = None
    available_name: str | None = None
    display_name: str | None = None
    email: str | None = None
    account_id: int | None = None
    role: Role | None = None
    confirmed: bool | None = None
    availability_status: AvailabilityStatus | None = None
    auto_offline: bool | None = None
    custom_attributes: dict[str, Any] | None = None


@dataclass
class Inbox:
    id: float | None = None
    name: str | None = None
    website_url: str | None = None
    channel_type: str | None = None
    avatar_url: str | None = None
    widget_color: str | None = None
    website_token: str | None = None
    enable_auto_assignment: bool | None = None
    web_widget_script: str | None = None
    welcome_title: str | None = None
    welcome_tagline: str | None = None
    greeting_enabled: bool | None = None
    greeting_message: str | None = None


@dataclass
class AgentBot:
    id: float | None = None
    name: str | None = None
    description: str | None = None
    account_id: float | None = None
    outgoing_url: str | None = None


@dataclass
class ContactInboxes:
    source_id: str | None = None
    inbox: Inbox | None = None


@dataclass
class ContactableInboxes:
    source_id: str | None = None
    inbox: Inbox | None = None


class Type(Enum):
    conversation = "conversation"
    contact = "contact"
    report = "report"


@dataclass
class CustomFilter:
    id: float | None = None
    name: str | None = None
    type: Type | None = None
    query: dict[str, Any] | None = None
    created_at: str | None = None
    updated_at: str | None = None


class Subscription(Enum):
    conversation_created = "conversation_created"
    conversation_status_changed = "conversation_status_changed"
    conversation_updated = "conversation_updated"
    message_created = "message_created"
    message_updated = "message_updated"
    webwidget_triggered = "webwidget_triggered"


@dataclass
class Webhook:
    id: float | None = None
    url: str | None = None
    subscriptions: list[Subscription] | None = None
    account_id: float | None = None


class Role2(Enum):
    administrator = "administrator"
    agent = "agent"


@dataclass
class Account:
    id: float | None = None
    name: str | None = None
    role: Role2 | None = None


@dataclass
class PlatformAccount:
    id: float | None = None
    name: str | None = None


@dataclass
class Team:
    id: float | None = None
    name: str | None = None
    description: str | None = None
    allow_auto_assign: bool | None = None
    account_id: float | None = None
    is_member: bool | None = None


@dataclass
class IntegrationsApp:
    id: str | None = None
    name: str | None = None
    description: str | None = None
    hook_type: str | None = None
    enabled: bool | None = None
    allow_multiple_hooks: bool | None = None
    hooks: list[dict[str, Any]] | None = None


@dataclass
class IntegrationsHook:
    id: str | None = None
    app_id: str | None = None
    inbox_id: str | None = None
    account_id: str | None = None
    status: bool | None = None
    hook_type: bool | None = None
    settings: dict[str, Any] | None = None


@dataclass
class PublicContact:
    id: int | None = None
    source_id: str | None = None
    name: str | None = None
    email: str | None = None
    pubsub_token: str | None = None


@dataclass
class PublicConversation:
    id: int | None = None
    inbox_id: str | None = None
    messages: list[Message] | None = None
    contact: dict[str, Any] | None = None


@dataclass
class PublicMessage:
    id: str | None = None
    content: str | None = None
    message_type: str | None = None
    content_type: str | None = None
    content_attributes: str | None = None
    created_at: str | None = None
    conversation_id: str | None = None
    attachments: list[dict[str, Any]] | None = None
    sender: dict[str, Any] | None = None


@dataclass
class AccountCreateUpdatePayload:
    name: str | None = None


@dataclass
class AgentBotCreateUpdatePayload:
    name: str | None = None
    description: str | None = None
    outgoing_url: str | None = None


@dataclass
class UserCreateUpdatePayload:
    name: str | None = None
    email: str | None = None
    password: str | None = None
    custom_attributes: dict[str, Any] | None = None


@dataclass
class CannedResponseCreateUpdatePayload:
    content: str | None = None
    short_code: str | None = None


@dataclass
class CustomAttributeCreateUpdatePayload:
    attribute_display_name: str | None = None
    attribute_display_type: int | None = None
    attribute_description: str | None = None
    attribute_key: str | None = None
    attribute_values: list[str] | None = None
    attribute_model: int | None = None


@dataclass
class ContactCreate:
    inbox_id: float
    name: str | None = None
    email: str | None = None
    phone_number: str | None = None
    avatar: bytes | None = None
    avatar_url: str | None = None
    identifier: str | None = None
    custom_attributes: dict[str, Any] | None = None


@dataclass
class ContactUpdate:
    name: str | None = None
    email: str | None = None
    phone_number: str | None = None
    avatar: bytes | None = None
    avatar_url: str | None = None
    identifier: str | None = None
    custom_attributes: dict[str, Any] | None = None


class MessageType1(Enum):
    outgoing = "outgoing"
    incoming = "incoming"


class ContentType1(Enum):
    input_email = "input_email"
    cards = "cards"
    input_select = "input_select"
    form = "form"
    article = "article"


@dataclass
class ConversationMessageCreate:
    content: str
    message_type: MessageType1 | None = None
    private: bool | None = None
    content_type: ContentType1 | None = None
    content_attributes: dict[str, Any] | None = None


@dataclass
class ConversationMessageAttachmentCreate:
    content: str
    files: dict[str, str | Any] | None = None
    message_type: MessageType1 | None = None
    file_type: str | None = None


@dataclass
class TeamCreateUpdatePayload:
    name: str | None = None
    description: str | None = None
    allow_auto_assign: bool | None = None


@dataclass
class CustomFilterCreateUpdatePayload:
    name: str | None = None
    type: Type | None = None
    query: dict[str, Any] | None = None


@dataclass
class WebhookCreateUpdatePayload:
    url: str | None = None
    subscriptions: list[Subscription] | None = None


@dataclass
class IntegrationsHookCreatePayload:
    app_id: str | None = None
    inbox_id: str | None = None
    settings: dict[str, Any] | None = None


@dataclass
class IntegrationsHookUpdatePayload:
    settings: dict[str, Any] | None = None


@dataclass
class AutomationRuleCreateUpdatePayload:
    name: str | None = None
    description: str | None = None
    event_name: EventName | None = None
    active: bool | None = None
    actions: list[dict[str, Any]] | None = None
    conditions: list[dict[str, Any]] | None = None


@dataclass
class PublicContactCreateUpdatePayload:
    identifier: str | None = None
    identifier_hash: str | None = None
    email: str | None = None
    name: str | None = None
    phone_number: str | None = None
    avatar_url: str | None = None
    custom_attributes: dict[str, Any] | None = None


@dataclass
class PublicMessageCreatePayload:
    content: str | None = None
    echo_id: str | None = None
    files: list[tuple[str, Any]] | None = None


@dataclass
class PublicMessageUpdatePayload:
    submitted_values: dict[str, Any] | None = None


class AvailabilityStatus1(Enum):
    online = "online"
    offline = "offline"


@dataclass
class Sender:
    id: float | None = None
    name: str | None = None
    thumbnail: str | None = None
    channel: str | None = None


@dataclass
class Meta1:
    mine_count: float | None = None
    unassigned_count: float | None = None
    assigned_count: float | None = None
    all_count: float | None = None


class CurrentStatus(Enum):
    open = "open"
    resolved = "resolved"


@dataclass
class Payload:
    success: bool | None = None
    current_status: CurrentStatus | None = None
    conversation_id: float | None = None


@dataclass
class ConversationStatusToggle:
    meta: dict[str, Any] | None = None
    payload: Payload | None = None


@dataclass
class ConversationLabels:
    payload: list[str] | None = None


@dataclass
class ExtendedMessage(GenericId, Message):
    source_id: float | None = None
    sender: dict[str, Any] | None = None


@dataclass
class Previous:
    avg_first_response_time: str | None = None
    avg_resolution_time: str | None = None
    conversations_count: float | None = None
    incoming_messages_count: float | None = None
    outgoing_messages_count: float | None = None
    resolutions_count: float | None = None


@dataclass
class AccountSummary:
    avg_first_response_time: str | None = None
    avg_resolution_time: str | None = None
    conversations_count: float | None = None
    incoming_messages_count: float | None = None
    outgoing_messages_count: float | None = None
    resolutions_count: float | None = None
    previous: Previous | None = None


@dataclass
class Metric:
    open: float | None = None
    unattended: float | None = None


@dataclass
class AgentConversationMetrics:
    id: float | None = None
    name: str | None = None
    email: str | None = None
    thumbnail: str | None = None
    availability: str | None = None
    metric: Metric | None = None


@dataclass
class PlatformApiV1AccountsAccountIdAccountUsersGetResponse:
    account_id: int | None = None
    user_id: int | None = None
    role: str | None = None


@dataclass
class PlatformApiV1AccountsAccountIdAccountUsersPostRequest:
    user_id: int
    role: str


@dataclass
class PlatformApiV1AccountsAccountIdAccountUsersPostResponse:
    account_id: int | None = None
    user_id: int | None = None
    role: str | None = None


@dataclass
class PlatformApiV1AccountsAccountIdAccountUsersDeleteRequest:
    user_id: int


@dataclass
class PlatformApiV1UsersIdLoginGetResponse:
    url: str | None = None


class Role3(Enum):
    agent = "agent"
    administrator = "administrator"


class AvailabilityStatus2(Enum):
    available = "available"
    busy = "busy"
    offline = "offline"


@dataclass
class ApiV1AccountsAccountIdAgentsPostRequest:
    name: str
    email: str
    role: Role3
    availability_status: AvailabilityStatus2 | None = None
    auto_offline: bool | None = None


class Availability(Enum):
    available = "available"
    busy = "busy"
    offline = "offline"


@dataclass
class ApiV1AccountsAccountIdAgentsIdPatchRequest:
    role: Role3
    availability: Availability | None = None
    auto_offline: bool | None = None


class AttributeModel(Enum):
    field_0 = "0"
    field_1 = "1"


@dataclass
class ApiV1AccountsAccountIdCustomAttributeDefinitionsGetParametersQuery:
    attribute_model: AttributeModel


class Sort(Enum):
    name = "name"
    email = "email"
    phone_number = "phone_number"
    last_activity_at = "last_activity_at"
    field_name = "-name"
    field_email = "-email"
    field_phone_number = "-phone_number"
    field_last_activity_at = "-last_activity_at"


@dataclass
class ApiV1AccountsAccountIdContactsGetParametersQuery:
    sort: Sort | None = None
    page: int | None = 1


@dataclass
class ApiV1AccountsAccountIdContactsSearchGetParametersQuery:
    q: str | None = None
    sort: Sort | None = None
    page: int | None = 1


@dataclass
class ApiV1AccountsAccountIdContactsFilterPostParametersQuery:
    page: int | None = None


class FilterOperator(Enum):
    equal_to = "equal_to"
    not_equal_to = "not_equal_to"
    contains = "contains"
    does_not_contain = "does_not_contain"


class QueryOperator(Enum):
    AND = "AND"
    OR = "OR"


@dataclass
class ApiV1AccountsAccountIdContactsFilterPostRequest:
    attribute_key: str | None = None
    filter_operator: FilterOperator | None = None
    values: list[str] | None = None
    query_operator: QueryOperator | None = None


@dataclass
class ApiV1AccountsAccountIdContactsIdContactInboxesPostRequest:
    inbox_id: float
    source_id: str | None = None


@dataclass
class ApiV1AccountsAccountIdAutomationRulesGetParametersQuery:
    page: int | None = 1


class Status1(Enum):
    open = "open"
    resolved = "resolved"
    pending = "pending"
    snoozed = "snoozed"


@dataclass
class ApiV1AccountsAccountIdConversationsMetaGetParametersQuery:
    q: str | None = None
    inbox_id: int | None = None
    team_id: int | None = None
    labels: list[str] | None = None
    status: Status1 | None = "open"


@dataclass
class ApiV1AccountsAccountIdConversationsMetaGetResponse:
    meta: Meta1 | None = None


class AssigneeType(Enum):
    me = "me"
    unassigned = "unassigned"
    all = "all"
    assigned = "assigned"


@dataclass
class ApiV1AccountsAccountIdConversationsGetParametersQuery:
    q: str | None = None
    inbox_id: int | None = None
    team_id: int | None = None
    labels: list[str] | None = None
    assignee_type: AssigneeType | None = "all"
    status: Status1 | None = "open"
    page: int | None = 1


class Status3(Enum):
    open = "open"
    resolved = "resolved"
    pending = "pending"


@dataclass
class ApiV1AccountsAccountIdConversationsPostRequest:
    source_id: str | None = None
    inbox_id: str | None = None
    contact_id: str | None = None
    additional_attributes: dict[str, Any] | None = None
    custom_attributes: dict[str, Any] | None = None
    status: Status3 | None = None
    assignee_id: str | None = None
    team_id: str | None = None


@dataclass
class ApiV1AccountsAccountIdConversationsPostResponse:
    id: float | None = None
    account_id: float | None = None
    inbox_id: float | None = None


@dataclass
class ApiV1AccountsAccountIdConversationsFilterPostParametersQuery:
    page: int | None = None


@dataclass
class ApiV1AccountsAccountIdConversationsFilterPostRequest:
    attribute_key: str | None = None
    filter_operator: FilterOperator | None = None
    values: list[str] | None = None
    query_operator: QueryOperator | None = None


@dataclass
class ApiV1AccountsAccountIdConversationsConversationIdToggleStatusPostRequest:
    status: Status3


@dataclass
class ApiV1AccountsAccountIdConversationsConversationIdAssignmentsPostRequest:
    assignee_id: float | None = None
    team_id: float | None = None


@dataclass
class ApiV1AccountsAccountIdConversationsConversationIdLabelsPostRequest:
    labels: list[str] | None = None


class Type2(Enum):
    web_widget = "web_widget"


@dataclass
class Channel:
    type: Type2 | None = None
    website_url: str | None = None
    welcome_title: str | None = None
    welcome_tagline: str | None = None
    agent_away_message: str | None = None
    widget_color: str | None = None


@dataclass
class ApiV1AccountsAccountIdInboxesPostRequest:
    name: str | None = None
    avatar: bytes | None = None
    channel: Channel | None = None


@dataclass
class Channel1:
    website_url: str | None = None
    welcome_title: str | None = None
    welcome_tagline: str | None = None
    agent_away_message: str | None = None
    widget_color: str | None = None


@dataclass
class ApiV1AccountsAccountIdInboxesIdPatchRequest:
    enable_auto_assignment: bool
    name: str | None = None
    avatar: bytes | None = None
    channel: Channel1 | None = None


@dataclass
class ApiV1AccountsAccountIdInboxesIdSetAgentBotPostRequest:
    agent_bot: float


@dataclass
class ApiV1AccountsAccountIdInboxMembersInboxIdDeleteRequest:
    user_ids: list[int]
    inbox_id: str = field(alias="inbox_id_")


@dataclass
class ApiV1AccountsAccountIdInboxMembersPostRequest:
    inbox_id: str
    user_ids: list[int]


@dataclass
class ApiV1AccountsAccountIdInboxMembersPatchRequest:
    inbox_id: str
    user_ids: list[int]


@dataclass
class ApiV1AccountsAccountIdConversationsConversationIdMessagesGetResponse(
    GenericId,
    Message,
):
    pass


@dataclass
class ApiV1AccountsAccountIdConversationsConversationIdMessagesPostResponse(
    GenericId,
    Message,
):
    pass


@dataclass
class AccountsAccountIdTeamsTeamIdTeamMembersPostRequest:
    user_ids: list[int]


@dataclass
class AccountsAccountIdTeamsTeamIdTeamMembersPatchRequest:
    user_ids: list[int]


@dataclass
class AccountsAccountIdTeamsTeamIdTeamMembersDeleteRequest:
    user_ids: list[int]


class FilterType(Enum):
    conversation = "conversation"
    contact = "contact"
    report = "report"


@dataclass
class ApiV1AccountsAccountIdCustomFiltersGetParametersQuery:
    filter_type: FilterType | None = None


@dataclass
class ApiV1AccountsAccountIdCustomFiltersPostParametersQuery:
    filter_type: FilterType | None = None


class Metric1(Enum):
    conversations_count = "conversations_count"
    incoming_messages_count = "incoming_messages_count"
    outgoing_messages_count = "outgoing_messages_count"
    avg_first_response_time = "avg_first_response_time"
    avg_resolution_time = "avg_resolution_time"
    resolutions_count = "resolutions_count"


class Type3(Enum):
    account = "account"
    agent = "agent"
    inbox = "inbox"
    label = "label"
    team = "team"


@dataclass
class ApiV2AccountsAccountIdReportsGetParametersQuery:
    metric: Metric1
    type: Type3
    id: str | None = None
    since: str | None = None
    until: str | None = None


@dataclass
class ApiV2AccountsAccountIdReportsGetResponse:
    value: str | None = None
    timestamp: float | None = None


@dataclass
class ApiV2AccountsAccountIdReportsSummaryGetParametersQuery:
    type: Type3
    id: str | None = None
    since: str | None = None
    until: str | None = None


class Type5(Enum):
    account = "account"


@dataclass
class ApiV2AccountsAccountIdReportsConversationsGetParametersQuery:
    type: Type5


@dataclass
class ApiV2AccountsAccountIdReportsConversationsGetResponse:
    open: float | None = None
    unattended: float | None = None
    unassigned: float | None = None


class Type6(Enum):
    agent = "agent"


@dataclass
class ApiV2AccountsAccountIdReportsConversationsGetParametersQuery1:
    type: Type6
    user_id: str | None = None


@dataclass
class BadRequestError:
    description: str | None = None
    errors: list[RequestError] | None = None


@dataclass
class Contact:
    email: str | None = None
    name: str | None = None
    phone_number: str | None = None
    thumbnail: str | None = None
    additional_attributes: dict[str, Any] | None = None
    custom_attributes: dict[str, Any] | None = None
    contact_inboxes: list[ContactInboxes] | None = None


@dataclass
class Conversation:
    id: float | None = None
    messages: list[Message] | None = None
    account_id: float | None = None
    inbox_id: float | None = None
    status: Status | None = None
    timestamp: str | None = None
    contact_last_seen_at: str | None = None
    agent_last_seen_at: str | None = None
    unread_count: float | None = None
    additional_attributes: dict[str, Any] | None = None
    custom_attributes: dict[str, Any] | None = None


@dataclass
class User:
    id: float | None = None
    uid: str | None = None
    name: str | None = None
    available_name: str | None = None
    display_name: str | None = None
    email: str | None = None
    account_id: float | None = None
    role: Role | None = None
    confirmed: bool | None = None
    custom_attributes: dict[str, Any] | None = None
    accounts: list[Account] | None = None


@dataclass
class ExtendedContact(Contact):
    id: float | None = None
    availability_status: AvailabilityStatus1 | None = None


@dataclass
class ContactBase(GenericId, Contact):
    pass


@dataclass
class ContactListItem(GenericId, Contact):
    pass


ContactList = List[ContactListItem]


@dataclass
class Meta:
    sender: Sender | None = None
    assignee: User | None = None


@dataclass
class ContactConversation(Conversation):
    meta: Meta | None = None
    display_id: float | None = None


ContactConversations = List[ContactConversation]


@dataclass
class Meta2:
    sender: Sender | None = None
    assignee: User | None = None


@dataclass
class PayloadItem(GenericId, Conversation):
    meta: Meta2 | None = None


@dataclass
class Data:
    meta: Meta1 | None = None
    payload: list[PayloadItem] | None = None


@dataclass
class ConversationList:
    data: Data | None = None


@dataclass
class Meta3:
    sender: Sender | None = None
    assignee: User | None = None


@dataclass
class ConversationShow(GenericId, Conversation):
    meta: Meta3 | None = None


@dataclass
class ApiV1AccountsAccountIdContactsSearchGetResponse:
    payload: ContactList | None = None
