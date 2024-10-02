from flask import Blueprint, jsonify, request

# Create a Blueprint for the items controller
items_bp = Blueprint('items_bp', __name__)

# Sample data
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

# GET all items
@items_bp.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# POST a new item
@items_bp.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    items.append(new_item)
    return jsonify({"message": "Item added successfully!"}), 201

#PUT item
@items_bp.route('/items/<int:item_id>', methods =['PUT'])
def update_item(item_id):
	item = next((item for item in items if item["id"] == item_id), None)
	
	if item is None:
		return jsonify({"message" : "Item not found" }),404
		
	updated_data = request.json
	
	item['name'] = updated_data.get('name',item['name'])
	item['description'] = updated_data.get('description', item['description'])
	
	return jsonify({"message" : "Item updated successfully!" }), 200
	
