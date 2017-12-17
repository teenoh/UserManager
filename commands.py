import os
import argparse

def build_containers():
    '''
        This function builds the mongo and app containers
    '''
    print("+++"*7,"Building containers", "+++"*7)
    
    build_command = "docker build -t mongo_db ./mongo_db " \
                    + " && docker build -t user_manager ."
    os.system(build_command)

    print('='*3, "Containers Built", '='*3)
    print('\n\n')

def start_containers():
    '''
        This function starts the containers
    '''
    print("+++"*7,"Starting containers", "+++"*7)

    start_mongo = "docker run --name mongo_container -d -p 27017:27017 mongo_db"
    print(("="*3), "starting mongodb", ("="*3))
    os.system(start_mongo)
    print("="*3, "MongoDB started, running on port 27017", "="*3)

    start_app = "docker run --name user_manager_container -d --network='host' user_manager"
    print("="*3, "starting userManager app", "="*3)
    os.system(start_app)
    print("="*3,"userManager app started running on port 3000", "="*3)
    print('\n\n\n')
    
def stop_containers():
    '''
        stop the containers    
    '''
    print("+++"*7,"Stopping containers", "+++"*7)

    #stops and removes the container to prevent issues when reusing the name
    stop_mongo = "docker container stop mongo_container && docker container rm mongo_container"
    
    print("="*3, "stopping mongo container", "="*3)
    os.system(stop_mongo)
    print("="*3, "Mongodb container stopped", "="*3)

    stop_user_manager = "docker container stop user_manager_container && docker container rm user_manager_container"
    print("="*3,"stopping user_manager container", "="*3,)
    os.system(stop_user_manager)
    print("="*3,"user_manager container stopped", "="*3)
    print('\n\n\n')




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="commands for controlling docker containers")
    parser.add_argument('-b', '--build',  action="store_true", help='builds the containers')
    parser.add_argument('--start', action="store_true", help="start the docker containers")
    parser.add_argument('--stop', action="store_true", help="stop docker containers")
    args = parser.parse_args()

    if args.build:
        build_containers()

    if args.start:
        start_containers()
    
    if args.stop:
        stop_containers()
