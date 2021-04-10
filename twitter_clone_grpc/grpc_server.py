from proto import twitter_clone_pb2_grpc
from server.server import TweetServicer
import logging
from concurrent import futures
import grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    twitter_clone_pb2_grpc.add_TweetServiceServicer_to_server(TweetServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("GRPC Server Online")
    serve()
