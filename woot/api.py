"""Chatwoot API wrapper is here."""

from typing import TYPE_CHECKING

import woot.resources as wr
from woot.simple_rest_client.api import API
from woot.utils import get_account_name

if TYPE_CHECKING:
    from typing import Awaitable, Callable, Literal

    from woot.simple_rest_client.models import Response

    all_resource = Literal[
        "account",
        "account_users",
        "agent_bots",
        "users",
        "account_agent_bot",
        "agents",
        "canned_responses",
        "contacts",
        "conversation_assignment",
        "conversation_labels",
        "conversations",
        "custom_attributes",
        "custom_filters",
        "inbox",
        "integrations",
        "messages",
        "profile",
        "reports",
        "teams",
        "webhooks",
        "automation_rule",
        "client_contacts",
        "client_conversations",
        "client_messages",
    ]

    all_action = Literal[
        "create",
        "get",
        "update",
        "delete",
        "get_sso_link",
        "get_conversations",
        "search",
        "filter",
        "assign",
        "get_meta",
        "toggle_status",
        "get_associated_agent_bot",
        "set_agent_bot",
        "list_agents",
        "delete_agent",
        "add_agent",
        "update_agent",
        "create_attachment",
        "get_accounts_report",
        "get_account_report_summary",
        "get_conversation_metrics_for_account",
        "get_conversation_metrics_for_agent",
    ]

    class AllAction:
        def __getattr__(self, _prop: all_action) -> Callable[..., Response]:
            ...

    class AsyncAllAction:
        def __getattr__(self, _prop: all_action) -> Callable[..., Awaitable[Response]]:
            ...


class _BaseChatwoot:
    def __init__(self, chatwoot_url, access_key, **kwargs) -> None:
        self._chatwoot_url = chatwoot_url
        self._access_key = access_key
        self._timeout = kwargs.get("timeout", 60)
        self._json_encode_body = kwargs.get("json_encode_body", True)

        self._api = API(
            api_root_url=self._chatwoot_url,
            params={},
            headers={"api_access_token": f"{self._access_key}"},
            timeout=self._timeout,
            json_encode_body=self._json_encode_body,
        )
        self._add_resources()

    def _add_resources(self) -> None:
        for resource in self.resources:
            resource = getattr(wr, resource)
            self._api.add_resource(
                resource_name=get_account_name(resource.__name__),
                resource_class=resource,
            )
            setattr(
                self,
                get_account_name(resource.__name__),
                getattr(self._api, get_account_name(resource.__name__)),
            )  # because I want resources to be attributes of Chatwoot and AsyncChatwoot

    def __repr__(self) -> str:
        resource_names = [get_account_name(resource) for resource in self.resources]
        max_len = max([len(name) for name in resource_names]) + 2
        header = f"Available actions:\n{'-' * max_len}\n"
        actions = ""
        for name in resource_names:
            actions += f"{name:<{max_len}}"
            actions += f"\n{' ' * (max_len + 1)}"
            for action, details in getattr(getattr(self, name), "actions").items():
                actions += (
                    f"{action}: {details.method} {details.url}\n{' ' * (max_len + 1)}"
                )
            actions += "\n"  # Add blank line after actions for each resource
        return header + actions


class Chatwoot(_BaseChatwoot):
    @property
    def resources(self):
        return wr._ALL_RESOURCES

    if TYPE_CHECKING:

        def __getattr__(self, _prop: all_resource) -> "AllAction":
            ...


class AsyncChatwoot(_BaseChatwoot):
    @property
    def resources(self):
        return wr._ALL_ASYNC_RESOURCES

    if TYPE_CHECKING:

        def __getattr__(self, _prop: all_resource) -> "AsyncAllAction":
            ...
