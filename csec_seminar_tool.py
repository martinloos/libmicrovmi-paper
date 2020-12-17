import os
from datetime import datetime, timedelta
import time
from timeit import default_timer as timer


def main():
    # step 0 create needed files (if not already present) and starts the loop
    libvmi_md_statistics = "libvmi-dump-memory-statistics"
    libmicrovmi_md_statistics = "libmicrovmi-dump-memory-statistics"
    libvmi_dump_memory_file = "dump-memory-libvmi-file"
    empty_string = ""

    # create output file for libvmi's memory dump
    cd("~/libvmtrace21/libvmi/build/examples")
    create_output_file_if_not_existing(libvmi_dump_memory_file)

    # create output filex for mem-dump time statictics
    cd("~")
    create_output_file_if_not_existing(libvmi_md_statistics)
    create_output_file_if_not_existing(libmicrovmi_md_statistics)

    x = 1

    while x <= 10:
        print('Started {}th out of 10 loops'.format(x))
        # step 1 performs mem dump with libvmi and appends measured time to the given file
        print('Started memory dump for libvmi')
        execute_libvmi_mem_dump(libvmi_md_statistics)
        print('Memory dump performed successfully with libvmi.')
        # step 2 performs mem dump with libmicrovmi and appends measured time to the given file
        print('Started memory dump for libmicrovmi')
        execute_libmicrovmi_mem_dump(libmicrovmi_md_statistics)
        print('Memory dump performed successfully with libmicrovmi.')

        # step 3 increase the counter by 1 and pause the execution for 60 seconds
        x += 1
        time.sleep(60)

    # add empty line to file after performing all measurements of this run
    append_to_file(libvmi_md_statistics, empty_string)
    append_to_file(libvmi_dump_memory_file, empty_string)

    print('program ran for {} times. terminated successfully!'.format(x))


def execute_libvmi_mem_dump(file):
    # changes directory to where the command should be executed
    cd("~/libvmtrace21/libvmi/build/examples")
    # executes the command and measures the time taken
    start_libvmi_dump_memory = timer()
    os.system("./vmi-dump-memory one-48026 dump-memory-libvmi-file")
    end_libvmi_dump_memory = timer()
    dump_memory_execution_time_libvmi = timedelta(seconds=end_libvmi_dump_memory - start_libvmi_dump_memory)
    dump_memory_execution_time_libvmi_string = str(dump_memory_execution_time_libvmi)
    append_to_file(file, dump_memory_execution_time_libvmi_string)


def execute_libmicrovmi_mem_dump(file):
    # changes directory to where the command should be executed
    cd("~/libvmtrace21/libmicrovmi/target/debug/examples")
    # executes the command and measures the time taken
    start_libmicrovmi_dump_memory = timer()
    os.system("./mem-dump one-48026")
    end_libmicrovmi_dump_memory = timer()
    dump_memory_execution_time_libmicrovmi = \
        timedelta(seconds=end_libmicrovmi_dump_memory - start_libmicrovmi_dump_memory)
    dump_memory_execution_time_libmicrovmi_string = str(dump_memory_execution_time_libmicrovmi)
    append_to_file(file, dump_memory_execution_time_libmicrovmi_string)


def cd(path):
    os.chdir(os.path.expanduser(path))


def create_output_file_if_not_existing(filename):
    save_path = os.getcwd()

    name_of_file = filename

    complete_name = os.path.join(save_path, name_of_file + ".txt")

    if os.path.isfile(complete_name):
        print("File already exists")
    else:
        file1 = open(complete_name, "a")
        file1.close()


def append_to_file(filename, text):
    cd("~")

    save_path = os.getcwd()

    name_of_file = filename

    complete_name = os.path.join(save_path, name_of_file + ".txt")

    time_now = datetime.now()
    time_string = str(time_now)

    with open(complete_name, "a") as my_file:
        my_file.write(text + " " + time_string + "\n")


if __name__ == "__main__":
    main()
