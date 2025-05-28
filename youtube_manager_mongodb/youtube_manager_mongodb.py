from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("< mongodb url >", tlsAllowInvalidCertificates=True)

db = client["ytmanager"]

video_collection = db["videos"]

print(video_collection)

def lsit_videos():
    print("\n")
    print('*' * 25)
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")
    print("\n")
    print('*' * 25)
    
def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(id, name, time):
    video_collection.update_one(
        {'_id': ObjectId(id)},
        {"$set": {"name": name, "time": time}}
    )

def delete_video(id):
    video_collection.delete_one({'_id': ObjectId(id)})

def main():
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit")
        choice = input("Enter your choose: ")
        
        if choice == '1':
            lsit_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            id = input("Enter the video id: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(id, name, time)
        elif choice == '4':
            id = input("Enter the video id: ")
            delete_video(id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()