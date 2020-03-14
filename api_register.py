import os
import proto.user_proto_pb2 as user_proto_pb2
import proto.user_proto_pb2_grpc as user_proto_pb2_grpc
import time
import grpc


"""
        message RegisterResponse{
            string uuid = 1;
            string email = 2;
            int32 user_id = 3;
        }
"""




def run(send_port):

    # Expected Response Data
    response_uuid =    "string"
    response_email =   "string"
    response_user_id = 32


    # Setting API Request Content
    print("[Mary]: Please enter your first name. Example: johnny")
    req_first_name  = input()
    print("[Mary]: Please enter your family name. Example: hung")
    req_family_name = input()
    print("[Mary]: Please enter your email")
    req_email       = input()

    print("\n---------------------------")
    print(req_first_name)
    print(req_family_name)
    print(req_email)
    print("----------------------------\n")

    # Origin Code:  
        #  "localhost:5001" 
    with grpc.insecure_channel("localhost:%s"%send_port) as channel:

        # Initial stub
        stub = user_proto_pb2_grpc.UserServiceStub(channel)


        #try:

        # Note: use ms unit
        # millis = int(round(time.time() * 1000))
        start_ms = int(round(time.time() * 1000) )
        response = stub.register_api(user_proto_pb2.RegisterRequest(first_name=req_first_name,family_name=req_family_name,email=req_email))
        end_ms   = int(round(time.time() * 1000) )
        #Received Response to Client Data
        response_uuid    = response.uuid
        response_email   = response.email
        response_user_id = response.user_id
        print("[System]: Recieved following info:")
        print("uuid            =           %s   "%response_uuid)
        print("email           =           %s   "%response_email)
        print("user_id         =           %d   "%response_user_id)
        print("Time Spent(ms)  =           %d ms"%(end_ms-start_ms))
        # Close Channel
        channel.unsubscribe(close)
        exit()

        #except:
        #    print("Call Server Error")
        #    channel.unsubscribe(close)
        #    exit()


# Addintion close
def close(channel):
    channel.close()


if __name__ == "__main__":
    print("[System]: Set your sending port ")
    print("For example: 5001")
    send_port = input()
    run(send_port)

