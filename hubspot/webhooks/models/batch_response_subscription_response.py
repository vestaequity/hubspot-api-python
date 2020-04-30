# coding: utf-8

"""
    Webhooks API

    Provides a way for apps to subscribe to certain change events in HubSpot. Once configured, apps will receive event payloads containing details about the changes at a specified target URL. There can only be one target URL for receiving event notifications per app.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.webhooks.configuration import Configuration


class BatchResponseSubscriptionResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'status': 'str',
        'results': 'list[SubscriptionResponse]',
        'num_errors': 'int',
        'errors': 'list[Error]',
        'requested_at': 'datetime',
        'started_at': 'datetime',
        'completed_at': 'datetime',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'status': 'status',
        'results': 'results',
        'num_errors': 'numErrors',
        'errors': 'errors',
        'requested_at': 'requestedAt',
        'started_at': 'startedAt',
        'completed_at': 'completedAt',
        'links': 'links'
    }

    def __init__(self, status=None, results=None, num_errors=None, errors=None, requested_at=None, started_at=None, completed_at=None, links=None, local_vars_configuration=None):  # noqa: E501
        """BatchResponseSubscriptionResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._results = None
        self._num_errors = None
        self._errors = None
        self._requested_at = None
        self._started_at = None
        self._completed_at = None
        self._links = None
        self.discriminator = None

        self.status = status
        self.results = results
        if num_errors is not None:
            self.num_errors = num_errors
        if errors is not None:
            self.errors = errors
        if requested_at is not None:
            self.requested_at = requested_at
        self.started_at = started_at
        self.completed_at = completed_at
        if links is not None:
            self.links = links

    @property
    def status(self):
        """Gets the status of this BatchResponseSubscriptionResponse.  # noqa: E501


        :return: The status of this BatchResponseSubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchResponseSubscriptionResponse.


        :param status: The status of this BatchResponseSubscriptionResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["PENDING", "PROCESSING", "CANCELED", "COMPLETE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def results(self):
        """Gets the results of this BatchResponseSubscriptionResponse.  # noqa: E501


        :return: The results of this BatchResponseSubscriptionResponse.  # noqa: E501
        :rtype: list[SubscriptionResponse]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this BatchResponseSubscriptionResponse.


        :param results: The results of this BatchResponseSubscriptionResponse.  # noqa: E501
        :type: list[SubscriptionResponse]
        """
        if self.local_vars_configuration.client_side_validation and results is None:  # noqa: E501
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

    @property
    def num_errors(self):
        """Gets the num_errors of this BatchResponseSubscriptionResponse.  # noqa: E501


        :return: The num_errors of this BatchResponseSubscriptionResponse.  # noqa: E501
        :rtype: int
        """
        return self._num_errors

    @num_errors.setter
    def num_errors(self, num_errors):
        """Sets the num_errors of this BatchResponseSubscriptionResponse.


        :param num_errors: The num_errors of this BatchResponseSubscriptionResponse.  # noqa: E501
        :type: int
        """

        self._num_errors = num_errors

    @property
    def errors(self):
        """Gets the errors of this BatchResponseSubscriptionResponse.  # noqa: E501


        :return: The errors of this BatchResponseSubscriptionResponse.  # noqa: E501
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this BatchResponseSubscriptionResponse.


        :param errors: The errors of this BatchResponseSubscriptionResponse.  # noqa: E501
        :type: list[Error]
        """

        self._errors = errors

    @property
    def requested_at(self):
        """Gets the requested_at of this BatchResponseSubscriptionResponse.  # noqa: E501


        :return: The requested_at of this BatchResponseSubscriptionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._requested_at

    @requested_at.setter
    def requested_at(self, requested_at):
        """Sets the requested_at of this BatchResponseSubscriptionResponse.


        :param requested_at: The requested_at of this BatchResponseSubscriptionResponse.  # noqa: E501
        :type: datetime
        """

        self._requested_at = requested_at

    @property
    def started_at(self):
        """Gets the started_at of this BatchResponseSubscriptionResponse.  # noqa: E501


        :return: The started_at of this BatchResponseSubscriptionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this BatchResponseSubscriptionResponse.


        :param started_at: The started_at of this BatchResponseSubscriptionResponse.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and started_at is None:  # noqa: E501
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def completed_at(self):
        """Gets the completed_at of this BatchResponseSubscriptionResponse.  # noqa: E501


        :return: The completed_at of this BatchResponseSubscriptionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """Sets the completed_at of this BatchResponseSubscriptionResponse.


        :param completed_at: The completed_at of this BatchResponseSubscriptionResponse.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and completed_at is None:  # noqa: E501
            raise ValueError("Invalid value for `completed_at`, must not be `None`")  # noqa: E501

        self._completed_at = completed_at

    @property
    def links(self):
        """Gets the links of this BatchResponseSubscriptionResponse.  # noqa: E501


        :return: The links of this BatchResponseSubscriptionResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this BatchResponseSubscriptionResponse.


        :param links: The links of this BatchResponseSubscriptionResponse.  # noqa: E501
        :type: dict(str, str)
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchResponseSubscriptionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchResponseSubscriptionResponse):
            return True

        return self.to_dict() != other.to_dict()
