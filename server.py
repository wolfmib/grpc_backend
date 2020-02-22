import os
from concurrent import futures
import grpc
import proto.user_proto_pb2 as user_proto_pb2
import proto.user_proto_pb2_grpc as user_proto_pb2_grpc
import time
import threading


# Key: __grpc -> __Servicer
class Listener(user_proto_pb2_grpc.UserServiceServicer):
    def __init__(self,*args,**kwargs):
        self.counter = 0
        self.lastPrintTime = time.time()

    def register_api(self,request,context):
        self.counter += 1

        if self.counter % 1000 ==0:
            print("Servicer process cnts = ",self.counter)


        db_uuid= "da00fcb1-2869-4f47-b7ed-956b9afdf7f1"
        db_email = "hello@gmail.com"
        db_user_id = 31

        return user_proto_pb2.RegisterResponse(uuid=db_uuid,email=db_email,user_id=db_user_id)


def serve(input_port):

    # Inial Server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))

    # Add Servicer
    user_proto_pb2_grpc.add_UserServiceServicer_to_server(Listener(),server)


    # Setting port
    checking_cmd="netstat -a -n -v -p tcp  | grep %d"%my_port
    os.system(checking_cmd)

    print("[Jason]: are you sure to proceed the server !")
    read_nothing = input()

    # example:    
        #  [::]:5001
    server.add_insecure_port("[::]:%d"%my_port)
    server.start()
    try:
        while True:
            print("Server on: threads %i" % (threading.active_count()))
            time.sleep(10)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)

if __name__ == "__main__":

    print("[Jason]: Please set the port")
    print("For example 5001")
    my_port = int(input())
    serve(my_port)
    

