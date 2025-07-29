from flask import Blueprint, jsonify, request 

client_bp = Blueprint('clients', __name__)

@client_bp.route('/clients', methods=['POST'])
def post_client():
    from commands.client.post_client_command import PostClientCommand
    from actions.client.post_client_action import PostClientAction
    
    data = request.get_json()
    
    command = PostClientCommand(
        nom = data['nom'],
        prenom = data['prenom'],
        email = data.get('email'),
        telephone = data.get('telephone'),
        adresse_id = data.get('adresse_id')
    )
    
    try:
        client = PostClientAction.execute(command)
        return jsonify(client.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400