import os
from concurrent import futures
import grpc
import proto.user_proto_pb2 as user_proto_pb2
import proto.user_proto_pb2_grpc as user_proto_pb2_grpc
import time
import threading


######################### logger_handler() ######################################
import sys
import logging
from logrusformatter import LogrusFormatter   #!pip3 install logrusformatter 
#################################################################################

######################### mongodb_handler () ##############
from pymongo import MongoClient
import uuid
import pprint
import bson # fix uid.UUID() class issue
###########################################################

###### random password #####
import random
import string
###########################




def logger_handler():
    # Use the package:  https://github.com/velp/logrus-formatter
    # Init formatter
    fmt_string = "%(levelname)s %(message)-20s %(filename)s %(lineno)s %(datetime)s"
    fmtr = LogrusFormatter(colorize=True, fmt=fmt_string)
    # Create logger
    logger = logging.getLogger('example')
    logger.setLevel(logging.DEBUG)
    # Add handler
    hdlr = logging.StreamHandler(sys.stdout)
    hdlr.setFormatter(fmtr)
    logger.addHandler(hdlr)
    # Example logging
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    return logger

def mongodb_handler():
    db_address = "mongodb://localhost:27017/"
    client = MongoClient(db_address)

    print("-----------------------------------------")
    print("[MongoDB]: Set the uuid-format for the db [%s] !!" % db_address)
    print("-----------------------------------------")
        # db = client.user_db
    
    db = client.get_database('user_db', bson.codec_options.CodecOptions(
        uuid_representation=bson.binary.UUID_SUBTYPE),)

    result_cursor = db.user_collection.find()
        #print(list(result_cursor))
    pprint.pprint(result_cursor)


    # collection = user_collection
    return db.user_collection

def random_password(string_lens = 10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_lens))


# Key: __grpc -> __Servicer
class Listener(user_proto_pb2_grpc.UserServiceServicer):
    def __init__(self,*args,**kwargs):
        self.counter = 0
        self.lastPrintTime = time.time()
        self.logger = logger_handler()
        # How to use--- logger-------------------
            # logger.debug("debug message")
            # logger.info("info message")
            # logger.warning("warning message")
            # logger.error("error message")
            # logger.critical("critical message")
        #----------------------------------------
        self.db     = mongodb_handler() # db <-  db.user_collection


    # client list:
        # python3 api_register.py
    def register_api(self,request,context):
        self.counter += 1

        if self.counter % 1000 ==0:
            print("Servicer process cnts = ",self.counter)

        # password random:
        db_generated_password = random_password(10)

        # uuid
            # db_generated_uuid = "da00fcb1-2869-4f47-b7ed-956b9afdf7f1"
        db_generated_uuid = uuid.uuid1()

        # user_id
            # 1. Check max_user_id
        check_cur   = self.db.find().sort([('user_id', -1)]).limit(1)
        _tem_data   = check_cur.next()
        max_user_id = _tem_data['user_id']
        self.logger.debug("the max user_id in db  = %d"%max_user_id)
            # 2. Faire user_id += 1
        db_generated_user_id = int(max_user_id + 1)

        # email_is_valud
        db_generated_email_is_valid = False

        self.logger.info("first_name       =  %s"%request.first_name)
        self.logger.info("family_name      =  %s"%request.family_name)
        self.logger.info("email            =  %s"%request.email)
        self.logger.info("password         =  %s"%db_generated_password)
        self.logger.info("uuid             =  %s"%db_generated_uuid)
        self.logger.info("user_id          =  %d"%db_generated_user_id)
        self.logger.info("email_is_valud   =  %s"%db_generated_email_is_valid)


        tem_row = {
            "uuid": db_generated_uuid,
            "first_name": request.first_name,
            "family_name": request.family_name,
            "email": request.email,
            "password": db_generated_password,
            "user_id": db_generated_user_id,
            "email_is_valid": db_generated_email_is_valid
        }

        # Insert
        result = self.db.insert_one(tem_row)
        self.logger.debug(result)

        # Check DB
        check_all  = self.db.find()
        _tem_data = check_all.next()
        while _tem_data:
            self.logger.info(_tem_data)
            try:
                _tem_data = check_all.next()
            except:
                _tem_data = []

        return user_proto_pb2.RegisterResponse(uuid=str(db_generated_uuid),email=request.email,user_id=db_generated_user_id)

    def get_user_info_by_uuid(self,request,context):
        self.counter += 1


       

        self.logger.info("Get Request = ")
        self.logger.info(request.uuid)

        tem_arg = {
            "uuid": uuid.UUID(request.uuid)
        }
       
        # Insert
        result = self.db.find(tem_arg)
        # result = self.db.find({'uuid': uuid.UUID('3442a288-b100-445e-b4dc-ae6b06d3ee28')})
        my_data = result.next()
        self.logger.info("Get the querry !")
        self.logger.debug(pprint.pprint(my_data))

        print("###################################")
        print(my_data['uuid'])
        print(my_data['first_name'])
        print("##################################")

        # Check DB
        # check_all  = self.db.find()
        # _tem_data = check_all.next()
        # while _tem_data:
        #     self.logger.info(pprint.pprint(_tem_data))
        #     try:
        #         _tem_data = check_all.next()
        #     except:
        #         _tem_data = []

        return user_proto_pb2.GetUserInfoResponse(uuid=str(my_data['uuid']),first_name=my_data['first_name'],family_name=my_data['family_name'],email=my_data['email'],user_id=int(my_data['user_id']),email_is_valid=my_data['email_is_valid'])






def serve(input_port):

    # Inial Server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))

    # Add Servicer
    user_proto_pb2_grpc.add_UserServiceServicer_to_server(Listener(),server)


    # Setting port
    print("[Jason]: Checking: Currently any thread running port: [%5d] or not"%my_port)
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
    

