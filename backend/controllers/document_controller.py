from flask import Blueprint, jsonify, request 
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
    try:
        command = GetDocumentCommand(id)
        document = GetDocumentAction.execute(command)
        return jsonify(document.to_dict()), 200
    except Exception :
        return jsonify({'error': 'Document non trouvé'}), 400
    
@document_bp.route('/documents/<string:document_id>', methods=['PATCH'])
def patch_document(document_id):
    from commands.patch_document_command import PatchDocumentCommand
    from actions.patch_document_action import PatchDocumentAction

    data = request.get_json()
    command = PatchDocumentCommand(document_id=document_id, fields_to_update=data)
    try:
        document = PatchDocumentAction.execute(command)
        return jsonify(document.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception:
        return jsonify({'error': 'Document non trouvé'}), 404

@document_bp.route('/documents/<string:document_id>', methods=['DELETE'])
def delete_document(document_id):
    from commands.delete_document_command import DeleteDocumentCommand
    from actions.delete_document_action import DeleteDocumentAction
    
    try:
        command = DeleteDocumentCommand(document_id=document_id)
        DeleteDocumentAction.execute(command)
        return jsonify({'message' : 'Document supprimé avec succès'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404