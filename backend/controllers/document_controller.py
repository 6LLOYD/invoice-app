from flask import Blueprint, request, jsonify

document_bp = Blueprint('document', __name__)

@document_bp.route('/documents', methods=['POST'])
def post_document():
    from actions.post_document_action import PostDocumentAction
    from commands.post_document_command import PostDocumentCommand
    data = request.get_json()
    command = PostDocumentCommand(
        numero=data['numero'],
        date=data['date'],
        total=data['total'],
        type_document=data['type_document'],
        client_id=data['client_id'],
        profile_id=data.get('profile_id')
    )
    try:
        document = PostDocumentAction.execute(command)
        return jsonify(document.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400