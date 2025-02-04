import os
import shutil
import threading
import time

class PrimeCenter:
    def __init__(self, source_directory, destination_directory):
        self.source_directory = source_directory
        self.destination_directory = destination_directory

    def transfer_files(self):
        for filename in os.listdir(self.source_directory):
            source_file = os.path.join(self.source_directory, filename)
            destination_file = os.path.join(self.destination_directory, filename)
            if os.path.isfile(source_file):
                shutil.copy2(source_file, destination_file)
                print(f"Transferred: {filename}")

    def optimize_disk_space(self):
        for filename in os.listdir(self.source_directory):
            file_path = os.path.join(self.source_directory, filename)
            if os.path.isfile(file_path):
                file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
                if file_size_mb > 100:  # Example threshold
                    os.remove(file_path)
                    print(f"Deleted large file: {filename}")

    def run(self):
        transfer_thread = threading.Thread(target=self.transfer_files)
        optimize_thread = threading.Thread(target=self.optimize_disk_space)

        transfer_thread.start()
        optimize_thread.start()

        transfer_thread.join()
        optimize_thread.join()

        print("File transfer and disk optimization completed.")

if __name__ == "__main__":
    source_dir = r"C:\path\to\source"
    destination_dir = r"C:\path\to\destination"

    prime_center = PrimeCenter(source_dir, destination_dir)
    start_time = time.time()
    prime_center.run()
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")