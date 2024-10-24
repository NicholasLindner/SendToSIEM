# Manual Testing
## Functionality Test
Ensure JSON Data is Successfully Sent

### 1. Run Program:
```bash
python send_data_to_siem_system.py
```
### 2. Provide Valid Input
* Choose "Splunk" or "Other" (Only Splunk is supported currently)
* JSON Data
* URL
* Token

### 3. Verify Event Sent Successfully Using Spunk Cloud
* Use the seach functionality and search for '*'
* If event was sent to Splunk successfully, data will appear


## Invalid URL
Ensure program responds correctly to invalid URl.

### 1. Input an invalid URL when prompted
Example: https://test.com 

### 2. Expected:
Network error

## Invalid JSON Data
Ensure program responds correctly to invalid JSON data.

### 1. Input invalid JSON data when prompted
Example: {"event": "test", "status": 

### 2. Expected Output:
Failure status: 401 - {"text":"Invalid authorization","code":3}

## Invalid Token
Ensure program responds correctly to invalid token.

### 1. Input invalid token when prompted
Example: invalid-token 

### 2. Expected Output:
Failure status: 403

## Disconnection

### 1. Stop program from running using Crtl + C

### 2. Expected Output:
 Interuption occurred.
 
# Unit Testing

## Run Unit Tests
These tests ensure that the Splunk class correctly builds the headers and the payload so that the data sending works successfully.

### Run Tests Using:
```bash
python -m unittest siem_tests.py
```
