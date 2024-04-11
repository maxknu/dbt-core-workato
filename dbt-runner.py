import subprocess
import sys
import os

def execute_dbt_command(folder_path, profiles_dir, dbt_command):
    # Check if the folder path exists
    if not os.path.isdir(folder_path):
        return f"Error: The folder '{folder_path}' does not exist."

    # Check if the profiles directory exists
    if not os.path.isdir(profiles_dir):
        return f"Error: The profiles directory '{profiles_dir}' does not exist."

    # Split the dbt command into main command and subcommand
    command_parts = dbt_command.split()
    if len(command_parts) != 2:
        return "Error: The dbt command is invalid. Please provide a command in the form 'dbt <subcommand>'."

    main_command, subcommand = command_parts

    # Change the current working directory to the specified folder
    os.chdir(folder_path)

    # Prepare the dbt command
    command = [main_command, subcommand, "--profiles-dir", profiles_dir]

    # Execute the dbt command and specify the profiles directory
    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT)
        return f"Success: '{dbt_command}' completed without errors."
    except subprocess.CalledProcessError as e:
        # Return the error output if the command fails
        return f"Failure: '{dbt_command}' encountered an error.\n" + e.output.decode()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python dbt_script.py <folder_path> <profiles_dir> <'dbt_command'>")
        sys.exit(1)

    folder_path = sys.argv[1]
    profiles_dir = sys.argv[2]
    dbt_command = sys.argv[3]  # This is expected to be in the form 'dbt <subcommand>'
    result_message = execute_dbt_command(folder_path, profiles_dir, dbt_command)
    print(result_message)
