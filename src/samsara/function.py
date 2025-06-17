import json
import os
from typing import Dict, Any, Optional, Protocol


class SSMClientProtocol(Protocol):
    """Protocol defining the SSM client interface we need."""

    def get_parameter(self, Name: str, WithDecryption: bool) -> Dict[str, Any]:
        """Get parameter from SSM."""
        ...


class Secrets:
    """
    Handles loading secrets from either local environment or AWS Parameter Store.
    """

    def __init__(self, client: Optional[SSMClientProtocol]) -> None:
        """
        Initialize the Secrets handler.

        Args:
            client: SSM client for accessing AWS Parameter Store, or None for local development
        """
        self.__client = client

    def load(self) -> Dict[str, Any]:
        """
        Load secrets from the appropriate source based on environment.

        When running locally, secrets are loaded from the
        'SamsaraFunctionLocalSecretsJson' environment variable.

        Returns:
            Dict containing the parsed secrets
        """
        if self.__client is None:
            return json.loads(os.environ.get("SamsaraFunctionLocalSecretsJson", "{}"))

        res = self.__client.get_parameter(
            Name=os.environ["SamsaraFunctionSecretsPath"], WithDecryption=True
        )

        value = res["Parameter"]["Value"]
        if value == "null":
            return {}

        return json.loads(value)


class Function:
    """
    Handles environment detection and secrets management.
    """

    def __init__(
        self, is_local: bool = os.environ.get("AWS_EXECUTION_ENV", "") == ""
    ) -> None:
        """
        Initialize the function with appropriate configuration based on environment.

        Args:
            is_local: Flag indicating if running in local development environment

        Note:
            The is_local parameter doesn't need to be set explicitly as it defaults to
            checking if AWS_EXECUTION_ENV is empty. This environment variable is automatically
            set by AWS Lambda when running in the cloud, but will be empty during local
            development, making the detection automatic in most cases.
        """
        if is_local:
            self.__secrets = Secrets(None)
        else:
            # boto3 is always available in the execution enviroment and not required in development.
            import boto3  # type: ignore

            sts = boto3.client("sts")
            res = sts.assume_role(
                RoleArn=os.environ["SamsaraFunctionExecRoleArn"],
                RoleSessionName=os.environ["SamsaraFunctionName"],
            )

            credentials = {
                "aws_access_key_id": res["Credentials"]["AccessKeyId"],
                "aws_secret_access_key": res["Credentials"]["SecretAccessKey"],
                "aws_session_token": res["Credentials"]["SessionToken"],
            }

            self.__secrets = Secrets(boto3.client("ssm", **credentials))

    def secrets(self) -> Secrets:
        """
        Get the secrets handler.

        Returns:
            The configured Secrets instance
        """
        return self.__secrets