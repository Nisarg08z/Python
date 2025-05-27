import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)
        return True
    
def list_all_videos(videos):
    print("\n")
    print('*' * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} , Duration: {video['time']}")
    print("\n")
    print('*' * 50)

def add_video(videos):
    name = input("Enter video Name: ")
    time = input("enter video Time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to upsate: "))
    if 1 <= index <= len(videos):
        name = input("Enter new video Name: ")
        time = input("Enter new video Time: ")
        videos[index - 1] = {'name': name, 'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid index")

def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit")
        choice = input("Enter your choose: ")
        
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice. Please choose a valid option")
                
if __name__ == "__main__":  
    main()