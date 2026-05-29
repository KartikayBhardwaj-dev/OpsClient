from enum import Enum

class IntegrationProvider(str, Enum):
    GMAIL = "gmail"
    SLACK = "slack"
    NOTION = "notion"