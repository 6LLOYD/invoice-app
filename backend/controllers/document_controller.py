# In your controllers/document_controller.py or similar file
from flask import Blueprint, jsonify, request # Make sure to import request as well
from actions.post_document_action import PostDocumentAction
from commands.post_document_command import PostDocumentCommand
from commands.get_document_command import GetDocumentCommand
from actions.get_document_action import GetDocumentAction

# Create the Blueprint instance
document_bp = Blueprint('documents', __name__)

@document_bp.route('/documents', methods=['POST'])
def post_document():
    from actions.post_document_action import PostDocumentAction
    from commands.post_document_command import PostDocumentCommand

    data = request.get_json()

    command = PostDocumentCommand(
        numero=data['numero'],
        date=data['date'],
        total_ht=data['total_ht'],
        tva_taux=data.get('tva_taux', 5.5),
        tva_montant=data.get('tva_montant'),
        total_ttc=data.get('total_ttc'),
        type_document=data['type_document'],
        client_id=data['client_id'],
        profile_id=data.get('profile_id'),
        statut=data.get('statut', 'Brouillon'),
        adresse_chantier=data.get('adresse_chantier'),
        nom_client=data.get('nom_client'),
        email_client=data.get('email_client'),
        telephone_client=data.get('telephone_client'),
        adresse_client=data.get('adresse_client'),
        document_source_id=data.get('document_source_id')
    )

    try:
        document = PostDocumentAction.execute(command)
        return jsonify(document.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@document_bp.route('/documents/<string:id>', methods=['GET'])
def get_document(id):
    command = GetDocumentCommand(id)
    document = GetDocumentAction.execute(command)

    if document:
        return jsonify(document.to_dict()), 200
    else:
        return jsonify({'error': 'Document non trouvé'}), 404