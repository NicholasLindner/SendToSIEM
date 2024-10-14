# Send Data to SEIM System
This is a python program that tackles sending JSON data to a **SEIM** system, with Splunk being the SIEM of choice. 

## Usage Instructions
### Step 1: Clone the Repository
In your terminal or command prompt, run the following command:
```bash
git clone https://github.com/NicholasLindner/SendToSEIM.git
cd SendToSEIM
```

### Step 2: Install the requests Library
```bash
pip install requests
```

### Step 3: Run Program
For Windows, run the program using the following command:
```bash
python send_data_to_seim_system.py
```
For Mac or Linux, run:
```bash
python3 send_data_to_seim_system.py
```

### Step 4: Provide Your Input
1. Enter your JSON Data
2. Enter your SEIM URL


    Example for Splunk:
```bash
    https://prd-p-abcde.splunkcloud.com:8088/services/collector/event
```
3. Enter SEIM Token

### Output
Either "Success" or "Failure" will be displayed depending on the result of the request.
