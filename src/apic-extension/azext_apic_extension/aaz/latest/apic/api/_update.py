# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "apic api update",
)
class Update(AAZCommand):
    """Update existing API.

    :example: Update API
        az apic api update -g contoso-resources -n contoso --api-id echo-api --summary "Basic REST API service"

    :example: Update custom properties
        az apic api update -g contoso-resources -n contoso --api-id echo-api --custom-properties '{\"public-facing\":true}'

    :example: Update custom properties using json file
        az apic api update -g contoso-resources -n contoso --api-id echo-api --custom-properties '@customProperities.json'

    :example: Update single custom metadata
        az apic api update -g contoso-resources -n contoso --api-id echo-api --set customProperties.internal=false
    """

    _aaz_info = {
        "version": "2024-03-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.apicenter/services/{}/workspaces/{}/apis/{}", "2024-03-01"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.api_id = AAZStrArg(
            options=["--api-id"],
            help="The id of the API.",
            required=True,
            id_part="child_name_2",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,90}$",
                max_length=90,
                min_length=1,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.service_name = AAZStrArg(
            options=["-n", "--service-name"],
            help="The name of Azure API Center service.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,90}$",
                max_length=90,
                min_length=1,
            ),
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["-w", "--workspace", "--workspace-name"],
            help="The name of the workspace.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,90}$",
                max_length=90,
                min_length=1,
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.contacts = AAZListArg(
            options=["--contacts"],
            arg_group="Properties",
            help="The contact information for the API.",
            nullable=True,
        )
        _args_schema.custom_properties = AAZFreeFormDictArg(
            options=["--custom-properties"],
            arg_group="Properties",
            help="The custom metadata defined for API catalog entities.",
            nullable=True,
            blank={},
        )
        _args_schema.description = AAZStrArg(
            options=["--description"],
            arg_group="Properties",
            help="Description of the API.",
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=1000,
            ),
        )
        _args_schema.external_documentation = AAZListArg(
            options=["--external-documentation"],
            arg_group="Properties",
            help="Additional, external documentation for the API.",
            nullable=True,
        )
        _args_schema.type = AAZStrArg(
            options=["--type"],
            arg_group="Properties",
            help="Type of API.",
            enum={"graphql": "graphql", "grpc": "grpc", "rest": "rest", "soap": "soap", "webhook": "webhook", "websocket": "websocket"},
        )
        _args_schema.license = AAZObjectArg(
            options=["--license"],
            arg_group="Properties",
            help="The license information for the API.",
            nullable=True,
        )
        _args_schema.summary = AAZStrArg(
            options=["--summary"],
            arg_group="Properties",
            help="Short description of the API.",
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=200,
            ),
        )
        _args_schema.title = AAZStrArg(
            options=["--title"],
            arg_group="Properties",
            help="API title.",
            fmt=AAZStrArgFormat(
                max_length=50,
                min_length=1,
            ),
        )

        contacts = cls._args_schema.contacts
        contacts.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.contacts.Element
        _element.email = AAZStrArg(
            options=["email"],
            help="Email address of the contact.",
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=100,
            ),
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="Name of the contact.",
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=100,
            ),
        )
        _element.url = AAZStrArg(
            options=["url"],
            help="URL for the contact.",
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=200,
            ),
        )

        external_documentation = cls._args_schema.external_documentation
        external_documentation.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.external_documentation.Element
        _element.description = AAZStrArg(
            options=["description"],
            help="Description of the documentation.",
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=500,
            ),
        )
        _element.title = AAZStrArg(
            options=["title"],
            help="Title of the documentation.",
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=50,
            ),
        )
        _element.url = AAZStrArg(
            options=["url"],
            help="URL pointing to the documentation.",
            fmt=AAZStrArgFormat(
                max_length=200,
            ),
        )

        license = cls._args_schema.license
        license.identifier = AAZStrArg(
            options=["identifier"],
            help="SPDX license information for the API. The identifier field is mutually exclusive of the URL field.",
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=50,
            ),
        )
        license.name = AAZStrArg(
            options=["name"],
            help="Name of the license.",
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=100,
            ),
        )
        license.url = AAZStrArg(
            options=["url"],
            help="URL pointing to the license details. The URL field is mutually exclusive of the identifier field.",
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=200,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ApisGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.ApisCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ApisGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiCenter/services/{serviceName}/workspaces/{workspaceName}/apis/{apiName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "apiName", self.ctx.args.api_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "serviceName", self.ctx.args.service_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-03-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_api_read(cls._schema_on_200)

            return cls._schema_on_200

    class ApisCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiCenter/services/{serviceName}/workspaces/{workspaceName}/apis/{apiName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "apiName", self.ctx.args.api_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "serviceName", self.ctx.args.service_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-03-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_api_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("contacts", AAZListType, ".contacts")
                properties.set_prop("customProperties", AAZFreeFormDictType, ".custom_properties")
                properties.set_prop("description", AAZStrType, ".description")
                properties.set_prop("externalDocumentation", AAZListType, ".external_documentation")
                properties.set_prop("kind", AAZStrType, ".type", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("license", AAZObjectType, ".license")
                properties.set_prop("summary", AAZStrType, ".summary")
                properties.set_prop("title", AAZStrType, ".title", typ_kwargs={"flags": {"required": True}})

            contacts = _builder.get(".properties.contacts")
            if contacts is not None:
                contacts.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.contacts[]")
            if _elements is not None:
                _elements.set_prop("email", AAZStrType, ".email")
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("url", AAZStrType, ".url")

            custom_properties = _builder.get(".properties.customProperties")
            if custom_properties is not None:
                custom_properties.set_anytype_elements(".")

            external_documentation = _builder.get(".properties.externalDocumentation")
            if external_documentation is not None:
                external_documentation.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.externalDocumentation[]")
            if _elements is not None:
                _elements.set_prop("description", AAZStrType, ".description")
                _elements.set_prop("title", AAZStrType, ".title")
                _elements.set_prop("url", AAZStrType, ".url", typ_kwargs={"flags": {"required": True}})

            license = _builder.get(".properties.license")
            if license is not None:
                license.set_prop("identifier", AAZStrType, ".identifier")
                license.set_prop("name", AAZStrType, ".name")
                license.set_prop("url", AAZStrType, ".url")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_api_read = None

    @classmethod
    def _build_schema_api_read(cls, _schema):
        if cls._schema_api_read is not None:
            _schema.id = cls._schema_api_read.id
            _schema.name = cls._schema_api_read.name
            _schema.properties = cls._schema_api_read.properties
            _schema.system_data = cls._schema_api_read.system_data
            _schema.type = cls._schema_api_read.type
            return

        cls._schema_api_read = _schema_api_read = AAZObjectType()

        api_read = _schema_api_read
        api_read.id = AAZStrType(
            flags={"read_only": True},
        )
        api_read.name = AAZStrType(
            flags={"read_only": True},
        )
        api_read.properties = AAZObjectType(
            flags={"required": True, "client_flatten": True},
        )
        api_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        api_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_api_read.properties
        properties.contacts = AAZListType()
        properties.custom_properties = AAZFreeFormDictType(
            serialized_name="customProperties",
        )
        properties.description = AAZStrType()
        properties.external_documentation = AAZListType(
            serialized_name="externalDocumentation",
        )
        properties.kind = AAZStrType(
            flags={"required": True},
        )
        properties.license = AAZObjectType()
        properties.lifecycle_stage = AAZStrType(
            serialized_name="lifecycleStage",
            flags={"read_only": True},
        )
        properties.summary = AAZStrType()
        properties.terms_of_service = AAZObjectType(
            serialized_name="termsOfService",
        )
        properties.title = AAZStrType(
            flags={"required": True},
        )

        contacts = _schema_api_read.properties.contacts
        contacts.Element = AAZObjectType()

        _element = _schema_api_read.properties.contacts.Element
        _element.email = AAZStrType()
        _element.name = AAZStrType()
        _element.url = AAZStrType()

        external_documentation = _schema_api_read.properties.external_documentation
        external_documentation.Element = AAZObjectType()

        _element = _schema_api_read.properties.external_documentation.Element
        _element.description = AAZStrType()
        _element.title = AAZStrType()
        _element.url = AAZStrType(
            flags={"required": True},
        )

        license = _schema_api_read.properties.license
        license.identifier = AAZStrType()
        license.name = AAZStrType()
        license.url = AAZStrType()

        terms_of_service = _schema_api_read.properties.terms_of_service
        terms_of_service.url = AAZStrType(
            flags={"required": True},
        )

        system_data = _schema_api_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.id = cls._schema_api_read.id
        _schema.name = cls._schema_api_read.name
        _schema.properties = cls._schema_api_read.properties
        _schema.system_data = cls._schema_api_read.system_data
        _schema.type = cls._schema_api_read.type


__all__ = ["Update"]
