from flask import Flask, jsonify, request
import json

# for POST, PUT
# data should be like {"first_name": <first_name>, "last_name": <last_name>, "pay": <pay>}}

app = Flask(__name__)

employees_info_file = "/Users/smantina/files/learning/practice/python/practice/rest/employees.json"

@app.route('/', methods=['GET'])
@app.route('/employees', methods=['GET'])
def get_employees_info():
    return read_employee_info_file()

@app.route('/employee/<filter_param>/<filter_value>', methods=['GET'])
def get_employee_data(filter_param, filter_value):
    default_result = {
        "result": "employee details not found"
    }
    employees_info = read_employee_info_file()
    for info in employees_info["employees"]:
        if info[filter_param] == filter_value:
            return info, 200
    return default_result, 404

@app.route('/employee/new', methods=['POST'])
def add_new_employee():
    employees_info = read_employee_info_file()
    input_data = json.loads(request.data)
    first_name = input_data['first_name']
    last_name = input_data['last_name']
    pay = input_data['pay']
    new_employee_info = generate_employee_data(first_name, last_name, pay)
    response = get_employee_data("user_id", new_employee_info["user_id"])
    if response[1] == 200:
        for info in employees_info["employees"]:
            if info["user_id"] == new_employee_info["user_id"]:
                if (info["first_name"] == first_name) and (info["last_name"] == last_name):
                    return "{} is already in employee list".format(new_employee_info["full_name"]), 409
                else:
                    user_id = first_name[0:1]+last_name
                    new_employee_info["user_id"] = user_id.lower()
    employees_info["employees"].append(new_employee_info)
    update_employee_info_file(employees_info)
    return new_employee_info, 201

@app.route('/employee/update', methods=['PUT'])
def update_employee():
    employees_info = read_employee_info_file()
    input_data = json.loads(request.data)
    first_name = input_data['first_name']
    last_name = input_data['last_name']
    pay = input_data['pay']
    updated_employee_info = generate_employee_data(first_name, last_name, pay)
    response = get_employee_data("user_id", updated_employee_info["user_id"])
    print(response[1])
    if response[1] == 200:
        for index, info in enumerate(employees_info["employees"]):
            if info["user_id"] == updated_employee_info["user_id"]:
                employees_info["employees"][index] = updated_employee_info
                update_employee_info_file(employees_info)
                return "updated {}'s details".format(updated_employee_info["full_name"]), 200
    else:
        return "couldn't find {}'s details".format(updated_employee_info["full_name"]), 404

@app.route('/employee/partial_update', methods=['PATCH'])
def partial_update_employee():
    match_index = 0
    employees_info = read_employee_info_file()
    input_data = json.loads(request.data)
    keys = input_data.keys()
    for index, info in enumerate(employees_info["employees"]):
        for key in keys:
            if info[key] == input_data[key]:
                match_index = index
                break
    for key in keys:
        employees_info["employees"][match_index][key] = input_data[key]
    update_employee_info_file(employees_info)
    return info

@app.route('/employee/remove/<filter_param>/<filter_value>', methods=['DELETE'])
def remove_employee(filter_param, filter_value):
    default_result = {
        "result": "couldn't delete employee details"
    }
    employees_info = get_employees_info()
    employee_info = get_employee_data(filter_param, filter_value)
    if employee_info[1] == 404:
        return default_result, 404
    elif employee_info[1] == 200:
        employees_info["employees"].remove(employee_info[0])
        update_employee_info_file(employees_info)
        return employees_info, 200


def update_employee_info_file(employees_info):
    with open(employees_info_file, mode='w') as info_file:
        json.dump(employees_info, info_file, indent=4)

def read_employee_info_file():
    with open(employees_info_file) as info_file:
        return json.load(info_file)

def generate_employee_data(first_name, last_name, pay):
    user_id = first_name[0]+last_name
    user_id = user_id.lower()
    email_address = f"{first_name}.{last_name}@email.com"
    employee_info = {
            "user_id": user_id,
            "first_name": first_name,
            "last_name": last_name,
            "full_name": f"{first_name} {last_name}",
            "email_address": email_address.lower(),
            "pay": pay
        }
    return employee_info




    


if __name__ == "__main__":
    app.run(debug=True)