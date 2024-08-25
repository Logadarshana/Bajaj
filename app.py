from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to extract numbers and alphabets from the input data
def process_data(data):
    numbers = []
    alphabets = []
    highest_lowercase = []
    
    for item in data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
            if item.islower():
                highest_lowercase.append(item)
    
    highest_lowercase.sort(reverse=True)  # Sort to find the highest
    return numbers, alphabets, highest_lowercase[:1]  # Only the highest

# POST endpoint
@app.route('/bfhl', methods=['POST'])
def process_request():
    try:
        content = request.json
        data = content['data']
        
        numbers, alphabets, highest_lowercase = process_data(data)
        
        response = {
            "is_success": True,
            "user_id": "your_fullname_yourdob",  # Replace with your actual format
            "email": "your_college_email@example.com",  # Replace with your actual email
            "roll_number": "your_roll_number",  # Replace with your actual roll number
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase
        }
        
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

# GET endpoint
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
