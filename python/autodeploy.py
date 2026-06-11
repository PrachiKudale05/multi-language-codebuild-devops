import paramiko

# EC2 Details
hostname = "65.0.105.172"
username = "lunchgithub"  # Amazon Linux
key_file = "gitdevlopa.pem"  # Path to your .pem file

# Connect to EC2
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname=hostname,
    username=username,
    key_filename=key_file
)

print("Connected to EC2")

# Create a new Python file on EC2
python_code = """
print("Hello from the new Python file!")
numbers = [10,20,30,40,50,60,70,80,90,100]
print("Highest:", max(numbers))
print("Lowest:", min(numbers))
print("Average:", sum(numbers)/len(numbers))
"""

command = f"cat > autodeploy.py << 'EOF'\n{python_code}\nEOF"

stdin, stdout, stderr = ssh.exec_command(command)

print("File created successfully.")

# Run the new Python file
stdin, stdout, stderr = ssh.exec_command("python autodeploy.py")

print("Output:")
print(stdout.read().decode())

error = stderr.read().decode()
if error:
    print("Errors:")
    print(error)

ssh.close()
