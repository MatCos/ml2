# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ml2.tools.protos import ltl_pb2 as ml2_dot_tools_dot_protos_dot_ltl__pb2


class SpotStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CheckSat = channel.unary_unary(
            "/Spot/CheckSat",
            request_serializer=ml2_dot_tools_dot_protos_dot_ltl__pb2.LTLSatProblem.SerializeToString,
            response_deserializer=ml2_dot_tools_dot_protos_dot_ltl__pb2.LTLSatSolution.FromString,
        )
        self.MCTrace = channel.unary_unary(
            "/Spot/MCTrace",
            request_serializer=ml2_dot_tools_dot_protos_dot_ltl__pb2.LTLTraceMCProblem.SerializeToString,
            response_deserializer=ml2_dot_tools_dot_protos_dot_ltl__pb2.TraceMCSolution.FromString,
        )


class SpotServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CheckSat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def MCTrace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SpotServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CheckSat": grpc.unary_unary_rpc_method_handler(
            servicer.CheckSat,
            request_deserializer=ml2_dot_tools_dot_protos_dot_ltl__pb2.LTLSatProblem.FromString,
            response_serializer=ml2_dot_tools_dot_protos_dot_ltl__pb2.LTLSatSolution.SerializeToString,
        ),
        "MCTrace": grpc.unary_unary_rpc_method_handler(
            servicer.MCTrace,
            request_deserializer=ml2_dot_tools_dot_protos_dot_ltl__pb2.LTLTraceMCProblem.FromString,
            response_serializer=ml2_dot_tools_dot_protos_dot_ltl__pb2.TraceMCSolution.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("Spot", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Spot(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CheckSat(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Spot/CheckSat",
            ml2_dot_tools_dot_protos_dot_ltl__pb2.LTLSatProblem.SerializeToString,
            ml2_dot_tools_dot_protos_dot_ltl__pb2.LTLSatSolution.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def MCTrace(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Spot/MCTrace",
            ml2_dot_tools_dot_protos_dot_ltl__pb2.LTLTraceMCProblem.SerializeToString,
            ml2_dot_tools_dot_protos_dot_ltl__pb2.TraceMCSolution.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
