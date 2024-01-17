import psutil


def services_scanner():
    # Get a list of all running processes
    running_processes = psutil.process_iter(attrs=['pid', 'name'])

    print("List of running services/processes:")
    for process in running_processes:
        try:
            process_info = process.info
            print(
                f"Process ID: {process_info['pid']}, Name: {process_info['name']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
