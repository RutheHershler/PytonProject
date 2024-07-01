from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)

# התחברות למסד נתונים של MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/gooood'
mongo = PyMongo(app)

# CREATE - יצירת ארגון חדש
@app.route('/organizations', methods=['POST'])
def create_organization():
    new_org = request.json
    result = mongo.db.organizations.insert_one(new_org)
    return jsonify({'message': 'Organization created successfully', 'id': str(result.inserted_id)})

# READ - קריאת ארגון על פי ID
@app.route('/organizations/<id>', methods=['GET'])
def get_organization_by_id(id):
    organization = mongo.db.organizations.find_one_or_404({'id': id}, {'_id': False})
    return jsonify(organization)


# READ - קריאת כל הארגונים
@app.route('/organizations', methods=['GET'])
def get_all_organizations():
    organizations = mongo.db.organizations.find({}, {'_id': False})
    output = []
    for org in organizations:
        output.append(org)
    return jsonify({'organizations': output})


# UPDATE - עדכון ארגון קיים על פי ID
@app.route('/organizations/<id>', methods=['PUT'])
def update_organization(id):
    updated_org = request.json
    result = mongo.db.organizations.update_one({'id': id}, {'$set': updated_org})
    if result.modified_count > 0:
        return jsonify({'message': 'Organization updated successfully'})
    else:
        return jsonify({'message': 'No organization found for updating'}), 404


# DELETE - מחיקת ארגון על פי ID
@app.route('/organizations/<id>', methods=['DELETE'])
def delete_organization(id):
    result = mongo.db.organizations.delete_one({'id': id})
    if result.deleted_count > 0:
        return jsonify({'message': 'Organization deleted successfully'})
    else:
        return jsonify({'message': 'No organization found for deletion'}), 404


if __name__ == '__main__':
    app.run(debug=True)
