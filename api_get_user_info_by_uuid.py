import os
import proto.user_proto_pb2 as user_proto_pb2
import proto.user_proto_pb2_grpc as user_proto_pb2_grpc
import time
import grpc

"""
    rpc get_user_info_by_uuid(GetUserInfoRequest) returns (GetUserInfoResponse){}

    message GetUserInfoRequest{
    string uuid = 1;
    }

    message GetUserInfoResponse{
        string uuid = 1;
        string first_name = 2;
        string family_name = 3;
        string email = 4;
        int32 user_id = 5;
        bool email_is_valid = 6;
    }
"""


def run(send_port):

    # Expected Response Data
    response_uuid = "string"
    response_email = "string"
    response_user_id = 32

    # Setting API Request Content
    print("[Mary]: Please enter your uuid . ")
    print("Example: '3442a288-b100-445e-b4dc-ae6b06d3ee28'")
    print("Example: '242a486e-5924-11ea-935d-7c04d0d98744'")
    req_uuid = input()
   
    print("\n---------------------------")
    print(req_uuid)
    print("----------------------------\n")

    # Origin Code:
    #  "localhost:5001"
    with grpc.insecure_channel("localhost:%s" % send_port) as channel:

        # Initial stub
        stub = user_proto_pb2_grpc.UserServiceStub(channel)

        #try:

        # Note: use ms unit
        # millis = int(round(time.time() * 1000))
        start_ms = int(round(time.time() * 1000))
        response = stub.get_user_info_by_uuid(user_proto_pb2.GetUserInfoRequest(uuid=req_uuid))
        end_ms = int(round(time.time() * 1000))
        #Received Response to Client Data
        response_uuid            = response.uuid
        response_first_name      = response.first_name 
        response_family_name     = response.family_name
        response_email           = response.email
        response_user_id         = response.user_id
        response_email_is_valid  = response.email_is_valid

        print("[System]: Recieved following info:")
        print("uuid             =           %s    "%response_uuid)
        print("first_name       =           %s    "%response_first_name)         
        print("family_name      =           %s    "%response_family_name)        
        print("email            =           %s    "%response_email)        
        print("user_id          =           %d    "%response_user_id)        
        print("email_is_valid   =           %s    "%response_email_is_valid)        
        print("Time Spent(ms)   =           %d ms" % (end_ms-start_ms))
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
